from pycparser import c_ast, c_parser, parse_file
from context import ot_context

class FunctionFinder(c_ast.NodeVisitor):
    def find_function(self, node, func_name):
        if(func_name == node.decl.name):
            print('%s at %s' % (node.decl.name, node.decl.coord))

def find_kernel(cur_context):
    if cur_context is not ot_context:
        return None

    kernel_name = cur_context.kernel_name
    file_name = cur_context.kernel_file



    return res