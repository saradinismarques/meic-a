from nodes import * 
from Taint_Units import *
from copy import deepcopy

def flatten_list(lst):
    flat_list = []
    for element in lst:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

class Static_Analysis:
    def __init__(self, ast, pattern):
        self.ast = ast
        self.pattern = pattern
        self.sources = pattern['sources']
        self.sinks = pattern['sinks']
        self.sanitizers = pattern['sanitizers']

        self.decorated_ast = None
        # self.taint_table_list[self.current_index] = dict()
        # self.taint_table_list = [dict()]    # start wiht global taint_table
        self.flows = list()
        self.implicit_sources = []
        # current execution context is head of stack
        self.active_taint_table_stack = [dict()]    # start wiht global taint_table

        self.implicit_sources_stack = []

    def is_implicit_pattern(self):
        return self.pattern["implicit"] == "yes"
    
    def current_implicit_source_list(self):
        return self.implicit_sources_stack[0]

    def pop_active_implicit_source_list(self):
        return self.implicit_sources_stack.pop(0)
    
    def insert_implicit_source_list(self, list):
        self.implicit_sources_stack.insert(0, list)

    def current_taint_table(self):
        return self.active_taint_table_stack[0]

    def pop_active_taint_table_from_stack(self):
        return self.active_taint_table_stack.pop(0)
    
    def new_context_taint_table(self):
        new_taint_table = dict()
        # self.taint_table_list.append(new_taint_table)
        self.active_taint_table_stack.insert(0, new_taint_table)

    def append_taint_unit_current_table(self, unit):
        self.current_taint_table()[unit.name] = unit
    
    def get_taint_unit_current_table(self, name):
        return self.current_taint_table()[name]

    def in_any_taint_tables(self, name):
        for taint_table in self.active_taint_table_stack:
            if name in taint_table:
                return True

        return False

    def merge_taint_tables_with_current(self, tables):
        if not isinstance(tables, list):
            tables = [tables]

        # create single merged table
        res_table = dict()
        for table in tables:
            # Non exisiting values will be uninitialized vars in that context
            for current_unit in res_table.values():
                if current_unit.name not in table and not self.in_any_taint_tables(current_unit.name) and isinstance(current_unit, Variable):
                    table[current_unit.name] = Variable(current_unit.name, pattern_sources=self.sources, pattern_sinks=self.sinks)

            # Add or merge context existing taint units
            for unit in table.values():
                if unit.name not in res_table:
                    res_table[unit.name] = unit
                else:
                    existing_unit = res_table[unit.name]
                    existing_unit.merge(unit) 

        # merge with current        
        for unit in res_table.values():
            if unit.name not in self.current_taint_table():
                self.append_taint_unit_current_table(unit)
            else:
                existing_unit = self.get_taint_unit_current_table(unit.name)
                existing_unit.merge(unit) 

    def analyse(self):
        '''
        parse tree
        loop node visit
        '''
        # Decorate tree
        self.decorated_ast = self.parse_tree(self.ast) 

        self.decorated_ast.accept(self)
        # print("FLOWS: ", self.flows)

        return self.match_pattern()

    def parse_tree(self, ast):
        '''
        Loop tree and create nodes
        '''
        return Program_Node(ast)

    def match_pattern(self):
        '''
        loop through variables, match pattern in self.pattern
        return json
        '''
        vulnerabilities = []
        
        for flow in self.flows:
        
            vuln = None
            for vulnerability in vulnerabilities:
                if vulnerability['source'] == flow["sources"] and vulnerability['sink'] == flow['sink']:
                    vuln = vulnerability

            if vuln == None:
                new_vuln = {}
                new_vuln['vulnerability'] = self.pattern['vulnerability']

                new_vuln['source'] = flow["sources"]
                new_vuln['sink'] = flow['sink']

                new_vuln['sanitized flows'] = []
                new_vuln['unsanitized flows'] = "yes"

                if 'sanitizers' in flow:
                    new_vuln['sanitized flows'].append(flow['sanitizers'])
                    new_vuln['unsanitized flows'] = "no"

                vulnerabilities.append(new_vuln)

            else:
                if 'sanitizers' not in flow or len(flow['sanitizers']) == 0:
                    vuln['unsanitized flows'] = "yes"
                else:
                    if flow['sanitizers'] not in vuln['sanitized flows']:
                        vuln['sanitized flows'].append(flow['sanitizers'])
        return vulnerabilities


    ##   =========================================================
    ##                       Visitors
    ##   =========================================================

    def visit_Program_Node(self, node: Program_Node):
        for expr in node.body:
            expr.accept(self)

    def visit_Stmt_Nop_Node(self, node: Stmt_Nop_Node):
        pass

    def visit_Stmt_Expression_Node(self, node: Stmt_Expression_Node):
        # New expression clean tainted function register
        for key in self.current_taint_table().copy().keys():
            if isinstance(self.current_taint_table()[key], Function):
                self.current_taint_table().pop(key)
        
        # print(f"\n@{node.start_line} => \n\t#pre table(depth={len(self.active_taint_table_stack)}): {self.current_taint_table()}\n{'='*55}")

        result = node.expr.accept(self)
        
        # print(f"{'='*55}\n\t#taint table: {self.current_taint_table()}\n\t#flows: {self.flows}\n")

        return result

    #   =========================================================
    #                       Variables
    #   =========================================================

    def visit_Expr_Assign_Node(self, node: Expr_Assign_Node):
        var = node.var.accept(self)

        right_expr = None

        # Variable taint will result from expression        
        if isinstance(node.expr, Expr_FuncCall_Node):
            right_expr = node.expr.accept(self)
            function = right_expr
            
            if function.is_source():
                var.set_flows(function.get_flows())
                var.set_type(Taint_Unit.TAINTED)
            elif function.is_sanitizer() or function.is_sanitized():
                var.set_sanitizer_result(function)
                var.set_type(Taint_Unit.SANITIZED)
            elif function.is_tainted():
                var.set_tainted_result(function)
                var.set_type(Taint_Unit.TAINTED)
                
            else:
                var.set_type(Taint_Unit.PURE)
                var.set_source([])

        else:
            if isinstance(node.expr, Expr_Variable_Node):
                right_expr = node.expr.accept(self)
                var.assign(right_expr)
            
            else:
                var.clear_flows()   # initializing variable
                
                implicit_sources = []
                for implicit_source in self.implicit_sources:
                    for flow in implicit_source.flows:
                        implicit_sources.append(flow['sources'])
                
                var.set_source(implicit_sources)

                right_expr = node.expr.accept(self)
                
                # case: pass by each element and capture the existing flows
                if not isinstance(right_expr, list):
                    right_expr = [right_expr]

                taint_level = Taint_Unit.PURE
                for element in right_expr:
                    if isinstance(element, Taint_Unit):
                        if element.is_tainted() or element.is_sanitized():
                            var.extend_flows(element)
                        
                        if element.is_tainted():
                            taint_level = Taint_Unit.TAINTED
                        elif element.is_sanitized() and taint_level != Taint_Unit.TAINTED:
                            taint_level = Taint_Unit.SANITIZED

                var.set_type(taint_level)


        # implicit sources
        print("[VAR]: ", var.name)
        print("[IMPLICTI SOURCES]: ", self.implicit_sources_stack)
        if self.is_implicit_pattern() and self.implicit_sources_stack:
            for stack in self.implicit_sources_stack:
                for implicit_source in stack:
                    var.extend_flows(implicit_source)
                    var.set_type(Variable.TAINTED)  


        # case: own var is sink. sink = something
        if not isinstance(right_expr, list):
                right_expr = [right_expr]

        if var.name in self.sinks:
            for element in right_expr:
                if isinstance(element, Taint_Unit):
                    for flow in element.flow_info(self.active_taint_table_stack):
                        if 'sources' in flow or 'sanitizers' in flow:
                            self.flows += [{**flow, "sink": var.name}]

        return var.type

    def visit_Expr_Variable_Node(self, node: Expr_Variable_Node):
        # print(f"> Varible node {node.name}")
        
        var = Variable(node.name, pattern_sources=self.sources, pattern_sinks=self.sinks)
        if var.name not in self.current_taint_table():
            old_var = None
            for taint_table in self.active_taint_table_stack:
                if var.name in taint_table:
                    old_var = taint_table[var.name]
                    break
            
            #  if old found, add new version to current table
            if old_var:
                var = deepcopy(old_var)
          
            # add
            self.append_taint_unit_current_table(var)

        return self.get_taint_unit_current_table(var.name)

    
    def visit_Expr_ConstFetch_Node(self, node: Expr_ConstFetch_Node):
        return node.name.accept(self)

    #   =========================================================
    #                       Functions
    #   =========================================================


    def visit_Expr_FuncCall_Node(self, node: Expr_FuncCall_Node):
        name = node.name.accept(self)

        args = [arg.accept(self) for arg in node.args]
        args = flatten_list(args)

        if name not in self.current_taint_table():
            function = Function(name)
            self.current_taint_table()[name] = function

        function = self.current_taint_table()[name]
        
        if name in self.sources:
            for arg in args:
                if isinstance(arg, Taint_Unit) and arg.is_tainted():
                    function.append_arg(arg)
                    arg.set_type(Taint_Unit.SOURCE)
            function.set_type(Function.SOURCE)

        elif name in self.sanitizers:
            for arg in args:
                function.append_arg(arg)
                
            function.set_type(Taint_Unit.SANITIZER)
            

        elif name in self.sinks:

            for arg in args:
                if isinstance(arg, Taint_Unit) and (arg.is_tainted() or arg.is_sanitized()) \
                    or isinstance(arg, Function) and (arg.is_source() or arg.is_sanitizer()):
                    for flow in arg.flow_info(self.active_taint_table_stack):
                        if 'sources' in flow or 'sanitizers' in flow:
                            self.flows += [{**flow, "sink": name}]
                    
                function.append_arg(arg)

            function.set_type(Taint_Unit.TAINTED)     

        else:   # any other function
            taint_level = Taint_Unit.PURE
            for arg in args:
                function.append_arg(arg)

                if isinstance(arg, Taint_Unit):
                    if arg.is_tainted():
                        taint_level = Taint_Unit.TAINTED
                    elif arg.is_sanitized() and taint_level != Taint_Unit.TAINTED:
                        taint_level = Taint_Unit.SANITIZED
            function.set_type(taint_level) 
        
        # print(f"\nFuncCall=> \nFunction: {function} \n CallArgs: {args}\n")

        return function

    def visit_Arg_Node(self, node: Arg_Node):
        return node.value.accept(self)

    #   =========================================================
    #                       Conditions
    #   =========================================================


    def visit_Stmt_If_Node(self, node: Stmt_If_Node):

        if self.is_implicit_pattern():
            print(node.cond)
            self.insert_implicit_source_list(node.cond.accept(self))

        generated_tables = []
        # if direct statements
        self.new_context_taint_table()
        for stmt in node.stmts:
            stmt.accept(self)
        taint_table = self.pop_active_taint_table_from_stack()
        generated_tables.append(taint_table)

        # elif direct statements
        for elseif in node.elseifs:
            self.new_context_taint_table()
            elseif.accept(self)
            taint_table = self.pop_active_taint_table_from_stack()
            generated_tables.append(taint_table)

        # else statements, have context even if empty to consider case non enterance
        self.new_context_taint_table()
        if node._else:
            node._else.accept(self)
        taint_table = self.pop_active_taint_table_from_stack()
        generated_tables.append(taint_table)

        if self.is_implicit_pattern():
            self.pop_active_implicit_source_list()

        self.merge_taint_tables_with_current(generated_tables)

    def visit_Stmt_Else_Node(self, node: Stmt_Else_Node):
        for stmt in node.stmts:
            stmt.accept(self)


    #   =========================================================
    #                       Loops
    #   =========================================================


    def visit_Stmt_While_Node(self, node: Stmt_While_Node):
        if self.is_implicit_pattern():
            print(node.cond)
            self.insert_implicit_source_list(node.cond.accept(self))
        #print("[IMPLICTI SOURCES]: ", self.implicit_sources_stack)

        self.new_context_taint_table()

        old_snapshot_table = None
        while old_snapshot_table != self.current_taint_table():     # until no changes are registred
            old_snapshot_table = deepcopy(self.current_taint_table())
            for stmt in node.stmts:
                stmt.accept(self)

            print("Old table:", old_snapshot_table)
            print("Tt end of while ", self.current_taint_table() )
            # input()

        taint_table = self.pop_active_taint_table_from_stack()

        if self.is_implicit_pattern():
            self.pop_active_implicit_source_list()

        self.merge_taint_tables_with_current(taint_table)

    def visit_Stmt_Break_Node(self, node: Stmt_Break_Node):
        pass

    def visit_Stmt_For_Node(self, node: Stmt_For_Node):
        #initialize all elements at init 
        [init.accept(self) for init in node.init]

        if self.is_implicit_pattern():
            self.insert_implicit_source_list(node.cond.accept(self))

        self.new_context_taint_table()

        old_snapshot_table = None
        while old_snapshot_table != self.current_taint_table():     # until no changes are registred
            old_snapshot_table = deepcopy(self.current_taint_table())
            for stmt in node.stmts:
                stmt.accept(self)

        taint_table = self.pop_active_taint_table_from_stack()

        if self.is_implicit_pattern():
            self.pop_active_implicit_source_list()

        self.merge_taint_tables_with_current(taint_table)

    #   =========================================================
    #                       Ops
    #   =========================================================


    def visit_Expr_BinaryOp_Concat_Node(self, node: Expr_BinaryOp_Concat_Node):
        left = node.left.accept(self)
        right = node.right.accept(self)

        var_list = []
        if isinstance(left, Taint_Unit):
            var_list.append(left)
        if isinstance(right, Taint_Unit):
            var_list.append(right)
        if isinstance(left, list):
            var_list.extend(left)
        if isinstance(right, list):
            var_list.extend(right)

        return var_list

    def visit_Expr_BinaryOp_Greater_Node(self, node: Expr_BinaryOp_Greater_Node):
        left = node.left.accept(self)
        right = node.right.accept(self)

        implicit_sources = []
        if isinstance(left, Taint_Unit) and left.is_tainted():
            implicit_sources.append(left)
        if isinstance(right, Taint_Unit) and right.is_tainted():
            implicit_sources.append(right)
        
        return implicit_sources

    def visit_Expr_BinaryOp_Smaller_Node(self, node: Expr_BinaryOp_Smaller_Node):
        left = node.left.accept(self)
        right = node.right.accept(self)

        implicit_sources = []
        if isinstance(left, Taint_Unit) and left.is_tainted():
            implicit_sources.append(left)
        if isinstance(right, Taint_Unit) and right.is_tainted():
            implicit_sources.append(right)
        
        return implicit_sources

    def visit_Expr_BinaryOp_Equal_Node(self, node: Expr_BinaryOp_Equal_Node):
        print("EQ node")
        
        left = node.left.accept(self)
        right = node.right.accept(self)

        print(f"right: {right}, left: {left}")


        implicit_sources = []
        if isinstance(left, Taint_Unit) and left.is_tainted():
            implicit_sources.append(left)
        if isinstance(right, Taint_Unit) and right.is_tainted():
            print(f"TURE")
            implicit_sources.append(right)
        
        return implicit_sources

    def visit_Expr_BinaryOp_NotEqual(self, node: Expr_BinaryOp_Equal_Node):
        left = node.left.accept(self)
        right = node.right.accept(self)

             

        print(f"right: {right}, left: {left}")

        implicit_sources = []
        if isinstance(left, Taint_Unit) and left.is_tainted():
            implicit_sources.append(left)
        if isinstance(right, Taint_Unit) and right.is_tainted():
            print(f"TURE")
            implicit_sources.append(right)

        print("Final", implicit_sources)
        
        return implicit_sources

    def visit_Expr_BinaryOp_Plus_Node(self, node: Expr_BinaryOp_Plus_Node):
        left = node.left.accept(self)
        right = node.right.accept(self)

        var_list = []
        if isinstance(left, Taint_Unit):
            var_list.append(left)
        if isinstance(right, Taint_Unit):
            var_list.append(right)
        if isinstance(left, list):
            var_list.extend(left)
        if isinstance(right, list):
            var_list.extend(right)
        return var_list

    def visit_Expr_PreInc_Node(self, node: Expr_BinaryOp_Equal_Node):
        pass

    def visit_Expr_BinaryOp_SmallerOrEqual_Node(self, node: Expr_BinaryOp_SmallerOrEqual_Node):
        pass

    def visit_Expr_PostInc_Node(self, node: Expr_PostInc_Node):
        pass

    #   =========================================================
    #                       Scalar
    #   =========================================================

    def visit_Scalar_String_Node(self, node: Scalar_String_Node):
        return Taint_Unit.PURE


    def visit_Name_Node(self, node: Name_Node):
        return "".join(node.parts)

    def visit_Scalar_LNumber_Node(self, node: Scalar_LNumber_Node):
        return Taint_Unit.PURE

    
    