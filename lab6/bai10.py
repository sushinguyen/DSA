from collections import deque

class StackUsingTwoQueues:
    def __init__(self):
        self.q1 = deque() 
        self.q2 = deque() 

    def push(self, value):       
        self.q1.append(value)

    def pop(self):               
        if self.isEmpty():
            print("Underflow")
            return None
        
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        val = self.q1.popleft()   
        self.q1, self.q2 = self.q2, self.q1 
        return val

    def top(self):                
        val = self.pop()
        if val is not None:
            self.q1.append(val) 
        return val

    def isEmpty(self):
        return len(self.q1) == 0


s = StackUsingTwoQueues()
s.push(1)
s.push(2)
s.push(3)
print(s.pop()) 
print(s.pop())
s.push(9)
print(s.pop())
print(s.pop()) 
print(s.pop())