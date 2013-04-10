import ast
import os
import pprint


class TextNode:
    def __init__(self, value, parent=None):
        self.parent = parent
        self.val = value
        self.children = []
        if parent is not None:
            parent.children.append(self)

    def dump(self):
        return self.val + '\n' + '\n'.join('\n'.join('  ' + line for line in child_str.split('\n')) for child_str in (child.dump() for child in self.children))

    def __str__(self):
        return self.dump()
        

class ToStringConverter:

    def to_string_FunctionDef(self, function_def):
        return "\n".join(map(lambda n: self.to_string(n), function_def.body))

    def to_string_Expr(self, expr):
        return self.to_string(expr.value)

    def to_string_Call(self, call):
        if isinstance(call.func, ast.Attribute) and isinstance(call.func.value, ast.Name):
            func_name = call.func.attr if call.func.value.id == 'self' else ' '.join([call.func.value.id, call.func.attr] )
            return func_name + ' ' + ', '.join(map(self.to_string, call.args))


    def to_string_Num(self, num):
        return str(num.n)

    def to_string_BinOp(self, binop):
        op_symbol = {
                ast.Add: '+',
            }.get(type(binop.op))
        return ' '.join([self.to_string(binop.left), op_symbol, self.to_string(binop.right)])

    def to_string_Str(self, node):
        return node.s

    def to_string(self, node):
        return getattr(self, 'to_string_%s' % node.__class__.__name__)(node)


class ToTextConverterVisitor(ast.NodeVisitor):
    def __init__(self, *args, **kwargs):
        ast.NodeVisitor.__init__(self, *args, **kwargs)
        self.current_node = TextNode('root')

    def visit_ClassDef(self, node):
        self.current_node = TextNode(node.name, self.current_node)
        self.generic_visit(node)
        self.current_node = self.current_node.parent

    def visit_FunctionDef(self, node):
        if not node.name.startswith('test'):
            return
        self.current_node = TextNode(node.name, self.current_node)
        self.current_node.val += '\n' + '\n'.join('  ' + line for line in ToStringConverter().to_string(node).split('\n'))
        self.current_node = self.current_node.parent


#    def visit(self, node):
#        print '<visit>', node
#        ast.NodeVisitor.visit(self, node)


def to_text(python_file_content):
    root = ast.parse(python_file_content, 'somefile.py')
#    pprint.pprint(ast.dump(root))
    v = ToTextConverterVisitor()
    v.visit(root)
    return v.current_node

if __name__ == '__main__':
    sample_content = """
import unittest


class ExampleTest(unittest.TestCase):

    def test_add_two_numbers(self):
        self.assertEquals(2, 1 + 1, 'basic testcase')

    def some_helper_method(self):
        return 'xc'
"""
    print to_text(sample_content)



