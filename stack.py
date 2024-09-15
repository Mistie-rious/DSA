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

print(misty.pop(), misty.size(), misty.peek(), misty.isFull())


pythonList = []
pythonList.append(1)
pythonList.append("Cute")
pythonList.append(3)
pythonList.append(4.98)
pythonList.append('Orange')
print(pythonList.pop(), pythonList.pop(), pythonList.pop(), pythonList.pop())
print(pythonList)

from collections import deque

misty = deque()
misty.append(1)
misty.append(2)
misty.append('Great')
print(misty.pop(), misty.pop(), misty.pop())

from queue import LifoQueue

mistylifo = LifoQueue(maxsize=5)

print(mistylifo.full())

mistylifo.put(3)
mistylifo.put(6)
mistylifo.put('popop')
print(mistylifo.qsize())
mistylifo.put(9)
mistylifo.put(12)


print(mistylifo.full())
print(mistylifo.empty())
print(mistylifo.get(), mistylifo.get(), mistylifo.get(), mistylifo.get(), mistylifo.get())
print(mistylifo.empty())


