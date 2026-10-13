class Solution:
    def calPoints(self, operations: List[str]) -> int:
        class stack:
            def __init__(self):
                self.values=[]
            def push(self,x):
                self.values.append(x)
            def pop(self):
                return self.values.pop()
        s=stack()
        for opr in operations:
            if opr not in ("+","D","C"):
                s.push(int(opr))
            elif opr=="+":
                s.push(s.values[-1]+s.values[-2])
            elif opr=="C":
                s.pop()
            else:
                s.push(2*s.values[-1])
        return sum(s.values)

    
        

        