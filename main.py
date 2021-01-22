class Stack:
    list_for_pop = []
    full_content = input('введите данные')
    full_content = full_content.split(' ')

    def isEmpty(self):
        if len(self.full_content) == 0:
            print ('False')
        else:
            return print ('True')

    def push(self, content = ''):
        self.full_content.append(content)

    def pop(self):
        self.list_for_pop.append(self.full_content[-1])
        del self.full_content[-1]
        return self.list_for_pop[0]

    def peek(self):
        return self.full_content[-1]

    def size(self):
        return len(self.full_content)




stack_1 = Stack()
print(stack_1.size())

