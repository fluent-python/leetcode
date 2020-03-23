class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> None:
        """
        Removes the element on top of the stack.
        """
        self.data.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.data[-1]

    def getMin(self) -> int:
        """
        Retrieve the minimum element in the stack.
        """
        return min(self.data)


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    obj = MinStack()
    obj.push(x=3)
    obj.push(x=4)

    obj.push(x=1)

    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)