def unabs(x):
    if not isinstance(x,(int,float)):
        raise TypeError ('wrong')
    else:
         if x <=0:
            return x
         else:
            return -x ##定义一个反绝对值的函数

def power(x, n =2):
    s = x
    while n > 1:
        n = n-1
        s = s * x
    return s ##次方工具

def imfor(name, age):
     print ("name:", name)
     print ("age:", age) ##信息收集

def get(f, g, h):
    b =(f, g, h)
    a =b[0]
    print (a) ##选取第一个元素

def jiecheng(i):
    if i ==1:
        return 1
    return i * jiecheng(i-1) ##阶乘好耶！


    

     