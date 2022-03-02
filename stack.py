class Stack:
    def __init__(self, SIZE = 6):
        self.stack = []
        self.top = -1
        self.MAX = SIZE
    
    def push(self, value):
        if(self.isFull()): raise Exception("Stack full")
        self.stack.append(value)
        self.top += 1
    
    def pop(self):
        if(self.isEmpty()): raise Exception("Stack empty")
        self.stack.pop()
        self.top -= 1
    
    def peek(self):
        if(self.isEmpty()): raise Exception("Stack empty")
        return self.stack[self.top]
    
    def isFull(self):
        if(self.top == self.MAX-1): return True
        return False
    
    def isEmpty(self):
        if(self.top == -1): return True
        return False
    
    def printStack(self):
        print(self.stack)