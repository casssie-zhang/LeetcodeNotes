class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.push_stack = []
        self.pop_stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.push_stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None

        if not self.pop_stack:
            self.transfer()

        return self.pop_stack.pop()

    def transfer(self):
        for i in range(len(self.push_stack)):
            x = self.push_stack.pop()
            self.pop_stack.append(x)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None

        if not self.pop_stack:
            self.transfer()

        x = self.pop_stack.pop()
        self.pop_stack.append(x)
        return x

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.push_stack and not self.pop_stack:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()