class Stack:
    def __init__(self, size):
       self.arr = [None] * size
       self.capacity = size
       self.top = -1

    def push(self, val):
        if self.isFull():
            print("Stack is full")
            return
        self.top += 1
        self.arr[self.top] = val

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        val = self.arr[self.top]
        self.top -= 1
        return val

    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.arr[self.top]

    def size(self):
        return self.top + 1

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
        


# Test
misty = Stack(5)
misty.push(1)
misty.push(2)
misty.push(3)
misty.push(4)
misty.push(5)
misty.push(6)
print(misty.pop(), misty.size(), misty.peek(), misty.isFull())
