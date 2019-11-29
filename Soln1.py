class MyException(Exception):
    def _init_(self,v):
        self.v=v
    def _str_(self):
        return self.v
        
def xyz(a,b):
    c=a+b
    if c<150:
        raise TypeError('custom exception occured')
    else:
        return c
a=int(input())
b=int(input())
print(xyz(a,b))
