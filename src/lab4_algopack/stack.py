class Stack:

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):

        if not self._items:
            raise IndexError("Нельзя извлечь элемент из пустого стека")
        return self._items.pop()

    def peek(self):

        if not self._items:
            raise IndexError("В пустом стеке нет верхнего элемента")
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return len(self._items) > 0