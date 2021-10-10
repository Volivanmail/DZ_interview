
class Stack:

    def __init__(self, stack):
        self.stack = stack


    def isEmpty(self):
        """проверка стека на пустоту. Метод возвращает True или False."""
        if self.stack:
            return True
        else:
            return False


    def push(self):
        """добавляет новый элемент на вершину стека. Метод ничего не возвращает."""
        element = input('Ввидите элемент для добавления:')
        self.stack = self.stack + element


    def pop(self):
        """ удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека"""
        self.stack = self.stack[:-1]
        element = self.stack[-1]
        return element


    def peek(self):
        """возвращает верхний элемент стека, но не удаляет его. Стек не меняется."""
        if self.isEmpty():
            element = self.stack[-1]
            return print(element)

    def size(self):
        """возвращает количество элементов в стеке"""
        len_stack = len(self.stack)
        return print(len_stack)



if __name__ == "__main__":

    object_1 = Stack('(((([{}]))))')
    object_2 = Stack('')

    object_1.peek()
    object_2.peek()

    object_1.size()
    object_2.size()

