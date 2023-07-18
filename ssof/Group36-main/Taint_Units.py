from copy import deepcopy


def flatten_list(lst):
    flat_list = []
    for element in lst:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

def remove_duplicates(lst):
    res_list = []
    for i in range(len(lst)):
        if lst[i] not in lst[i + 1:]:
            res_list.append(lst[i])

    return res_list

class Taint_Unit:
        PURE = 0
        SANITIZED = 1
        TAINTED = 2
        SANITIZER = 10
        SOURCE = 11

        def __init__(self, name):
            self.name = name
            
        def __repr__(self) -> str:
            return f"name: {self.name}, type: {self.type}"

        def __eq__(self, __o: object) -> bool:
            return self.name == __o.name
            
        def set_type(self, type):
            self.type = type

        def is_tainted(self):
            return self.type == self.TAINTED or self.type == self.SOURCE
        
        def is_sanitized(self):
            return self.type == self.SANITIZED

        def is_source(self):
            return self.type == self.SOURCE

        def merge(self, unit):
            assert self.name == unit.name
            self.type = max(self.type, unit.type)
       

class Function(Taint_Unit):
    def __init__(self, name):
        super().__init__(name)
        self.type = self.PURE
        self.args = []

    def __repr__(self) -> str:
        return f"Function: {super().__repr__()}, args: {self.args}"
    
    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) and self.type == __o.type and self.args == __o.args

    def append_arg(self, arg):
        if isinstance(arg, Taint_Unit):
            self.args.append(arg)

    def is_sanitizer(self):
        return self.type == self.SANITIZER
    
    def get_flows(self):
        res_flows = []
        for arg in self.args:
            if isinstance(arg, Taint_Unit):
                flows = arg.get_flows()
                # print(f"Arg:{arg}, flows:{flows}")

                for flow in flows:
                    if self.is_sanitizer():
                        if "sanitizers" in flow and self.name not in flow["sanitizers"]:
                            flow["sanitizers"].append(self.name)
                        else:
                            flow["sanitizers"] = [self.name]
                    
                    res_flows.append(flow)

        # add function if source
        if self.is_source() and (not res_flows or {"sources": self.name} not in res_flows):
            flow = dict()
            flow["sources"] = self.name
            
            res_flows.append(flow)
        print("[RES FLOW]: ", res_flows)
        return deepcopy(res_flows)

    def flow_info(self, taint_table_list):
        list_of_flows = []
        for arg in self.args:
            if isinstance(arg, Taint_Unit):
                for taint_table in taint_table_list:
                    # print(f"\t>Arg{arg.name} taint_table: {taint_table}")
                    if arg.name in taint_table:
                        taint_table_arg = taint_table[arg.name]
                        flows = taint_table_arg.get_flows()
                        for flow in flows:
                            if flow not in list_of_flows:
                                list_of_flows.append(deepcopy(flow))

        # function is sanitizer
        if self.is_sanitizer():
            for flow in list_of_flows:
                if self.is_sanitizer():
                    if "sanitizers" in flow:
                        flow["sanitizers"].append(self.name)
                    else:
                        flow["sanitizers"] = [self.name]
        
        elif self.is_source():
            flow = dict()
            flow["sources"] = self.name
            list_of_flows.append(flow)

        
        # print(f">Function {self.name} list of flows: {list_of_flows}")
        return flatten_list(list_of_flows)

    def merge(self, unit):
        pass
        # no need to keep functions, will be deleted


class Variable(Taint_Unit):
    def __init__(self, name, pattern_sources, pattern_sinks):
        name = name.replace("$", "")    # clear of any $
        super().__init__(f"${name}")
        self.flows = [{"sources": self.name}] # own var is source
        
        # if var is defined as source in patters
        if self.name in pattern_sources:
            self.type = self.SOURCE
        else:
            # defualt uninitialized is tainted
            self.type = self.TAINTED
    
    def __repr__(self) -> str:
        return f"Variable: {super().__repr__()}, flows: {self.flows}"

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o) and self.flows == __o.flows

    def get_flows(self):
        return deepcopy(self.flows)
    
    def is_tainted(self):
            return self.type == self.TAINTED or self.is_source()

    def set_source(self, names):
        if isinstance(names, list):
            names = flatten_list(names)
        else:
            names = [names]

        if self.is_source():    # if source in pattern, always source
            names.append(self.name)

        self.flows = [{"sources": name} for name in names]

    def set_type(self, type):
        if self.is_source():
            type = self.SOURCE

        if type == self.SOURCE and not self.is_source():
            type = self.TAINTED

        super().set_type(type)

  
    def set_flows(self, flows):
        self.flows = remove_duplicates(flows)

        if self.is_source():    # if source in pattern, always source
            self.flows.append({"sources": self.name})

    def clear_flows(self):
        self.set_flows([])

    def extend_flows(self, unit):
        print("$$$ Extends flow")
        print("$$$ Current flow:", self.flows)
        for flow in unit.get_flows():
            if flow not in self.flows:
                print("$$$ add flow:", flow)
                self.flows.append(flow)

    def set_sanitizer_result(self, function):
        self.set_flows(function.get_flows())
    
    def set_tainted_result(self, function):
        self.set_flows(function.get_flows())


    def assign(self, var):
        self.set_type(var.type)
        self.set_flows(var.get_flows())

    def merge(self, unit):
        super().merge(unit)
        self.extend_flows(unit)

    def flow_info(self, taint_table_list):
        list_of_flows = []
        for taint_table in taint_table_list:
            if self.name in taint_table:
                var = taint_table[self.name]
                flow = var.get_flows()
                if flow not in list_of_flows:
                    list_of_flows.append(deepcopy(flow))

        # print(f"Variable {self.name} list of flows: {list_of_flows}")
        return flatten_list(list_of_flows)