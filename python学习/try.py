## 这已经完全是粪山了……
from unabs import unabs
from unabs import power
from unabs import imfor
from unabs import get
from unabs import jiecheng
## 
print ("将分别测试unabs中的函数")

e =int(input())
a =unabs(e) ##unabs测试
print (a)

b =int(input())
c =int(input())
d =power(b, c) ##power测试
print (d)

print ("name and age")
f = input()
g = input()
imfor(f, g) ##imfor测试

h = abs(int(input()))
i = input()
j = input()
get (h, i, j) ##get测试

k = int(input())
l = jiecheng(k)
print (l) ##jiecheng测试

n = int(input())
while n > 0:
    n =n+1
    print (n) ##好玩的东西