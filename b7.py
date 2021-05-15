import math
class circle(object):
    def __init__(self,r):
        self.radius = r
    def dt(self):
        return self.radius**2*3.14
    def cv(self):
        return self.radius*2*3.14
n=int(input('nhap gia tri: '))
acircle= circle(n)
print(acircle.dt())
print(acircle.cv())
