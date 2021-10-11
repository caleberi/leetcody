class Stack:
    def __init__(self,max_size=4):
        self.max_size = max_size
        self.stk = [None]*max_size
        self.last_pos = -1

    def pop(self):
        if self.last_pos < 0:
            raise IndexError()
        temp = self.stk[self.last_pos]
        self.stk[self.last_pos]=None
        if self.last_pos >=0:
            self.last_pos-=1
        return temp

    def push(self,value):
        if self.last_pos > self.max_size:
            raise IndexError()
        if self.last_pos<0:
            self.last_pos+=1
            self.stk[self.last_pos]=value
            return
        self.last_pos+=1
        self.stk[self.last_pos]=value

    def top(self):
        return self.stk[self.last_pos]


def test_stack():
    stk = Stack()
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    # print("********************")
    # stk.push(5)
    print("********************")
    print(stk.pop())
    print(stk.top())
    print(stk.pop())
    print(stk.top())
    print(stk.pop())
    print(stk.top())
    print(stk.pop())
    print(stk.pop())

if __name__ == "__main__":
    test_stack()