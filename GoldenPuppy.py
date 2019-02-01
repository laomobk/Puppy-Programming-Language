'''
This is Puppy Language 's virtual machine 
'''

byte_code_map = {
                 0:"LOAD_CONST",
                 1:"LOAD_FAST",
                 2:"STORE_FAST",
                 3:"STACK_ADD",
                 4:"STACK_SUB",
                 5:"STACK_DIV",
                 6:"STACK_MUIT",
                 7:"STACK_POW",
                 8:"PRINT_ITEM",
                 9:"PRINT_LINE",
                 10:"LOAD_NAME",
                 11:"STORE_NAME",
                 12:"LOAD_GLOBAL"
                }

class VirtualMachine(object):

    def __init__(self, consts, varnames, byte_code = []):
        
        self.call_stack = []
        self.frame = []

        self.byte_code = byte_code

        self.global_consts = []
        self.varnames = varnames
        self.global_name = {}
    
    def run_code(self,code,argv):
        pass

    def top_frame(self):
        return self.frame[-1]

    def LOAD_CONST(self, argv):

        self.top_frame().data_stack.append(self.global_consts[argv])

    def LOAD_NAME(self, argv):
        self.global_name[self.names[argv]] = self.top_frame().data_stack.pop()


class Frame(object):

    def __init__(self, global_name):

        self.data_stack = []
        self.names = {}
        
        #将全局变量放入帧变量中
        for each in global_name.items():
            self.names[each[0]] = each[1]

