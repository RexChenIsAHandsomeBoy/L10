class leaf:
    def __init__(self,num=None):
        self.num=num
        self.left=None
        self.right=None
    def plant(self,num):
        if self.num:
            if num<self.num:
                if self.left is None:
                    self.left=leaf(num)
                else:
                    self.left.plant(num)
            if num>self.num:
                if self.right is None:
                    self.right=leaf(num)
                else:
                    self.right.plant(num)
        else:
            self.num=num
    def show(self):
        print(self.num,end="")
        if self.left:
            print(" ",end="")
            self.left.show()
        if self.right:
            print(" ",end="")
            self.right.show()
timed=0
while 1>0:
    if timed>0:
        print("")
    timed=timed+1
    total=int(input())
    data=[int(x) for x in input().split()]
    root=leaf()
    for i in range(len(data)):
        root.plant(data[i])
    root.show()
