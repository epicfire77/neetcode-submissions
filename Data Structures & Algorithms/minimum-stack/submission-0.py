class MinStack:
    class Node:
        def __init__(self, val = None, next = None, min = None):
            self.val = val
            self.next = next
            self.min = min

    def __init__(self):
        self.sentinel = self.Node()

    def push(self, val: int) -> None:
        m = val
        if self.sentinel.next:
            m = min(val, self.sentinel.next.min)
        newNode = self.Node(val, self.sentinel.next, m)
        self.sentinel.next = newNode

    def pop(self) -> None:
        if self.sentinel.next:
            self.sentinel.next = self.sentinel.next.next
        

    def top(self) -> int:
        return self.sentinel.next.val

    def getMin(self) -> int:
        return self.sentinel.next.min
        
