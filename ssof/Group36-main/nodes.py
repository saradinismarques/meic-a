global taint_table

class Node:
    def accept(self, visitor):
        raise NotImplementedError()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}"

    def parse(self, ast_node):
        if "nodeType" not in ast_node:
            return None

        nodeType = ast_node["nodeType"]

        if nodeType == "Stmt_Expression":
            return Stmt_Expression_Node(ast_node)
        elif nodeType == "Expr_Assign":
            return Expr_Assign_Node(ast_node)
        elif nodeType == "Expr_Variable":
            return Expr_Variable_Node(ast_node)
        elif nodeType == "Scalar_String":
            return Scalar_String_Node(ast_node)
        elif nodeType == "Stmt_Nop":
            return Stmt_Nop_Node(ast_node)
        elif nodeType == "Expr_FuncCall":
            return Expr_FuncCall_Node(ast_node)
        elif nodeType == "Name":
            return Name_Node(ast_node)
        elif nodeType == "Arg":
            return Arg_Node(ast_node)
        elif nodeType == "Expr_BinaryOp_Concat":
            return Expr_BinaryOp_Concat_Node(ast_node)
        elif nodeType == "Stmt_If":
            return Stmt_If_Node(ast_node)
        elif nodeType == "Stmt_Else":
            return Stmt_Else_Node(ast_node)
        elif nodeType == "Expr_BinaryOp_Greater":
            return Expr_BinaryOp_Greater_Node(ast_node)
        elif nodeType == "Expr_BinaryOp_Smaller":
            return Expr_BinaryOp_Smaller_Node(ast_node)
        elif nodeType == "Scalar_LNumber":
            return Scalar_LNumber_Node(ast_node)
        elif nodeType == "Stmt_While":
            return Stmt_While_Node(ast_node)
        elif nodeType == "Expr_BinaryOp_Equal":
            return Expr_BinaryOp_Equal_Node(ast_node)
        elif nodeType == "Expr_BinaryOp_NotEqual":
            return Expr_BinaryOp_NotEqual(ast_node)
        elif nodeType == "Expr_BinaryOp_Plus":
            return Expr_BinaryOp_Plus_Node(ast_node)
        elif nodeType == "Expr_ConstFetch":
            return Expr_ConstFetch_Node(ast_node)
        elif nodeType == "Stmt_Break":
            return Stmt_Break_Node(ast_node)
        elif nodeType == "Expr_PreInc":
            return Expr_PreInc_Node(ast_node)
        elif nodeType == "Stmt_For":
            return Stmt_For_Node(ast_node)
        elif nodeType == "Expr_BinaryOp_SmallerOrEqual":
            return Expr_BinaryOp_SmallerOrEqual_Node(ast_node)
        elif nodeType == "Expr_PostInc":
            return Expr_PostInc_Node(ast_node)

class Program_Node(Node):
    def __init__(self, ast):
        self.body:list = []

        for expr in ast:
            self.body.append(self.parse(expr))

    def accept(self, visitor):
        return visitor.visit_Program_Node(self)

    def __str__(self) -> str:
        tree = ""
        for node in self.body:
            tree += str(node) + "\n"
        return tree
        

class Stmt_Expression_Node(Node):
    def __init__(self, ast_node):
        self.expr = self.parse(ast_node["expr"])
        self.start_line = ast_node["attributes"]["startLine"]

    def accept(self, visitor):
        return visitor.visit_Stmt_Expression_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.expr} }}"

class Expr_Assign_Node(Node):
    """ var = expr """
    def __init__(self, ast_node):
        self.var = self.parse(ast_node["var"])
        self.expr = self.parse(ast_node["expr"])

    def accept(self, visitor):
        return visitor.visit_Expr_Assign_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.var}, {self.expr} }}"   

class Expr_Variable_Node(Node):
    """ $name """
    def __init__(self, ast_node):
        self.name = ast_node["name"]

    def accept(self, visitor):
        return visitor.visit_Expr_Variable_Node(self)
    
    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.name} }}"   


class Scalar_String_Node(Node):
    """ \"string\" """
    def __init__(self, ast_node):
        self.value = ast_node["value"]

    def accept(self, visitor):
        return visitor.visit_Scalar_String_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.value} }}"   

class Expr_FuncCall_Node(Node):
    """ name() """
    def __init__(self, ast_node):
        self.name = self.parse(ast_node["name"])
        self.args = [self.parse(arg) for arg in ast_node["args"]]

    def accept(self, visitor):
        return visitor.visit_Expr_FuncCall_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.name}, args: {[str(arg) for arg in self.args]} }}"   

class Name_Node(Node):
    def __init__(self, ast_node):
        self.parts = ast_node["parts"]

    def accept(self, visitor):
        return visitor.visit_Name_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.parts} }}"   

class Arg_Node(Node):
    def __init__(self, ast_node):
        self.value = self.parse(ast_node["value"])

    def accept(self, visitor):
        return visitor.visit_Arg_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.value} }}"   

        
class Stmt_Nop_Node(Node):
    def __init__(self, ast_node):
        super().__init__()

    def accept(self, visitor):
        return visitor.visit_Stmt_Nop_Node(self)

class Expr_BinaryOp_Concat_Node(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_Concat_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"     

class Stmt_If_Node(Node):
    def __init__(self, ast_node):
        self.cond = self.parse(ast_node["cond"])
        self.stmts = [self.parse(stmt) for stmt in ast_node["stmts"]]
        self.elseifs = [self.parse(elseif) for elseif in ast_node["elseifs"]]
        self._else = None
        if ast_node["else"]: 
            self._else = self.parse(ast_node["else"])
        
    def accept(self, visitor):
        return visitor.visit_Stmt_If_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.cond}, {self.stmts}, {self.elseifs}, {self._else} }}"  

class Stmt_Else_Node(Node):
    def __init__(self, ast_node):
        self.stmts = [self.parse(stmt) for stmt in ast_node["stmts"]]

    def accept(self, visitor):
        return visitor.visit_Stmt_Else_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.stmts} }}"  

class Expr_BinaryOp_Greater_Node(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_Greater_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"  

class Expr_BinaryOp_Smaller_Node(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_Smaller_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"  

class Scalar_LNumber_Node(Node):
    def __init__(self, ast_node):
        self.value = ast_node["value"]

    def accept(self, visitor):
        return visitor.visit_Scalar_LNumber_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.value} }}"  

class Stmt_While_Node(Node):
    def __init__(self, ast_node):
        self.cond = self.parse(ast_node["cond"])
        self.stmts = [self.parse(stmt) for stmt in ast_node["stmts"]]

    def accept(self, visitor):
        return visitor.visit_Stmt_While_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.cond}, {self.stmts}}}"  

class Expr_BinaryOp_Equal_Node(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_Equal_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"  

class Expr_BinaryOp_NotEqual(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_NotEqual(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"  


class Expr_BinaryOp_Plus_Node(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_Plus_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"  

class Expr_ConstFetch_Node(Node):
    def __init__(self, ast_node):
        self.name = self.parse(ast_node["name"])

    def accept(self, visitor):
        return visitor.visit_Expr_ConstFetch_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.name}}}"  

class Stmt_Break_Node(Node):
    def __init__(self, ast_node):
        super().__init__()

    def accept(self, visitor):
        return visitor.visit_Stmt_Break_Node(self) 

class Expr_PreInc_Node(Node):
    def __init__(self, ast_node):
        self.var = self.parse(ast_node["var"])

    def accept(self, visitor):
        return visitor.visit_Expr_PreInc_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.var} }}"  

class Stmt_For_Node(Node):
    def __init__(self, ast_node):
        self.init = [self.parse(init) for init in ast_node["init"]]
        self.cond = [self.parse(cond) for cond in ast_node["cond"]]
        self.loop = [self.parse(loop) for loop in ast_node["loop"]]
        self.stmts = [self.parse(stmt) for stmt in ast_node["stmts"]]

    def accept(self, visitor):
        return visitor.visit_Stmt_For_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.init}, {self.cond}, {self.loop}, {self.stmts}}}" 

class Expr_BinaryOp_SmallerOrEqual_Node(Node):
    def __init__(self, ast_node):
        self.left = self.parse(ast_node["left"])
        self.right = self.parse(ast_node["right"])

    def accept(self, visitor):
        return visitor.visit_Expr_BinaryOp_SmallerOrEqual_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.left}, {self.right} }}"  

class Expr_PostInc_Node(Node):
    def __init__(self, ast_node):
        self.var = self.parse(ast_node["var"])

    def accept(self, visitor):
        return visitor.visit_Expr_PostInc_Node(self)

    def __str__(self) -> str:
        return f"{super().__str__()}{{ {self.var} }}"  