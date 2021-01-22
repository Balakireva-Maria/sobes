from main import Stack
class Stack2(Stack):
    open_symbol = ['[','{','(']
    close_symbol = [']','}',')']
stack = Stack2()

if stack.size() % 2 != 0 or stack.full_content[0] in stack.close_symbol or stack.peek() in stack.open_symbol or stack.full_content.count('(') != stack.full_content.count(')') or stack.full_content.count('[') != stack.full_content.count(']') or stack.full_content.count('{') != stack.full_content.count('}'):
    print('Несбалансированно')
else:
    print('Сбаласнированно')




