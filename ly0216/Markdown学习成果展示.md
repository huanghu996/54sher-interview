# Markdown学习成果==展示==

### 就拿原来的一道题展示吧（~~偷懒~~）

![1633349693752](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633349693752.png)

手玩 $k\le5$ 发现每个k可能对应的相对位置关系情况很少 并且能够计数.. 

$k=1$ 显然  $ ans = n \times m $

$k=2$  和 $k\ge6$ 显然只有位于一条线的情况

**同一竖线时**  $ans=m \times \dbinom{n}{k}$

**同一横线时** $ans = n \times \dbinom{m}{k} $

***在同一斜线的时候*** 需要固定一端点计数 不然会计重 向左斜和向右斜一样 可以直接 $\times 2$
$$
ans=2\times \sum_{i=1}^{n} \sum_{j=1}^{m} \binom{min(i,j)-1}{k-1}
$$
枚举端点后 对角线长度为最小正方形边长 $min(i,j)-1$ 选 $k-1$ 个 (固定一个点了..)

$k=3$

显然只会有两种情况

​	●	

●	●  

通过枚举正方形边长 $i$ 一个正方形里 通过旋转可以得到$4$个相同构造方法的
$$
ans=4\times\sum_{i=2}^{min(n,m)} (n-i+1)\times(m-i+1)
$$
为了不计重 在枚举正方形的时候只计$1$次 $i$ 从$2$ 枚举防止一个点..

●		●

​	●

你发现这种情况长和宽有关系 设宽是$x$ 长就是$2\times x-1$ 

所以数矩形就行了 你把矩形倒过来看又是一种相似构造
$$
ans=2\times \sum_{x=2}^{min(n,\frac{m+1}{2})} (n-x+1)\times(m-2\times x+2)
$$
竖过来同理

●

​	●

●
$$
ans=2\times \sum_{x=2}^{min(m,\frac{n+1}{2})} (m-x+1)\times(n-2\times x+2)
$$
$k=4$

共四种情况

​	●

●	●	●

这种类似$k=3$的第二种

●

​	●

●		●

同样数正方形 枚举边长 旋转可以得到4种相似构造
$$
\large{ans=4\times\sum_{i=2}^{\frac{min(n,m)+1}{2}} (n-2\times i+2)(m-2\times i+2)}
$$
​	●

●		●

​	●

同样是数正方形 枚举边长 和上式子一样

●	●

●	●

同样枚举正方形..
$$
\sum_{i=2}^{min(n,m)} (n-i+1)\times(m-i+1)
$$
$k=5$

两种情况

​	●				●		●

●	●	●				●

​	●				●		●

同样是正方形..
$$
\large{ans=2\times\sum_{i=2}^\frac{min(n,m)+1}{2} (n-2\times i+2)(m-2\times i+2)}
$$
这样$O(nm)$就有$80$分了.

然后毒瘤式子可以化简到$O(\log_{mod}n)$..

$k=1$ 依旧是$n*m$

$k=2$ 组合数$n$ $m$ 过大而 $p$ 很小的时候 需要用$Lucas$定理

> $Lucas$定理 对于 $p$ 为质数

$$
\binom{n}{m}\equiv \binom{n \mod \ p}{m \mod \ p}\times \binom{n / p}{m / p} \ (mod \ p)
$$

其实就是组合数多加一行 往下递归到$< p$ 就能计算了.

然后你还需要一些. **组合数学知识** 和 **和式化简的能力.**

> 提取/吸收恒等式

$$
\binom{n}{m}= \frac{n}{m} \times \binom{n-1}{m-1}
$$

> 上指标求和法 要求i相同

$$
\sum_{i}^{n}\binom{i}{k} = \binom{n+1}{k+1}
$$

化简这个式子
$$
ans=\sum_{i=1}^{n} \sum_{j=1}^{m} \binom{min(i,j)-1}{k-1}
$$
先把$min$去掉
$$
ans=\sum_{i=1}^{n}\sum_{j=1}^{i-1}\binom{j-1}{k-1}+\sum_{i=1}^{n}\sum_{j=i}^{m}\binom{i-1}{k-1}
$$
然后对第一个式子把下标$j$ 改变一下. 通常方式都是把里面的值域算出来 然后枚举值域

后面内层与$j$无关
$$
ans=\sum_{i=1}^{n}\sum_{j=0}^{i-2}\binom{j}{k-1}+\sum_{i=1}^{n}\binom{i-1}{k-1}\times (m-i+1)
$$
然后第一个式子内层上指标求和 第二个式子拆开式子 所以需要保证$n>m$ 不然$(m-i+1)<0$
$$
ans=\sum_{i=1}^{n}\binom{i-1}{k}+\sum_{i=1}^{n}m\times\binom{i-1}{k-1}-\sum_{i=1}^{n}i\times\binom{i-1}{k-1}+\sum_{i=1}^{n}\binom{i-1}{k-1}
$$
然后第一个式子再变化指标 第二个式子提出$m$并变化指标 第三个式子里面吸收恒等式 外面$\times k$

第四个式子变化指标
$$
ans=\sum_{i=0}^{n-1}\binom{i}{k}+m\times\sum_{i=0}^{n-1}\binom{i}{k-1}-k\times\sum_{i=1}^{n}\binom{i}{k}+\sum_{i=0}^{n-1}\binom{i}{k-1}
$$
然后上指标求和就$ok$了
$$
ans=\binom{n}{k+1}+m\times\binom{n}{k}-k\times\binom{n+1}{k+1}+\binom{n}{k}
$$
然后就解决了$k=2$  和 $k\ge6$  的了

然后$k=3$ 的两个式子
$$
ans=4\times\sum_{i=2}^{min(n,m)} (n-i+1)\times(m-i+1)
$$
设$k=min(n,m)$ 先把内层的$i+1$ 看成整体 $i-1$ 然后变化一下指标
$$
ans=4\times\sum_{i=1}^{k}(n-i)\times(m-i)
$$
然后展开式子 遇到式子就展开
$$
ans=4\times\sum_{i=1}^{k}n\times m-(n+m)\times i + i^2
$$
然后第一项和$i$ 无关 第二项$(n+m)$提出来 里面等差数列求和 第三项自然数平方和
$$
ans=4\times(k\times n\times m-(n+m)\times\frac{(k+1)\times k}{2}+\frac{k\times (k+1)\times (2\times k+1)}{6})
$$
枚举宽的式子
$$
ans=2\times \sum_{x=2}^{min(n,\frac{m+1}{2})} (n-x+1)\times(m-2\times x+2)
$$
还是把上界特化 $k=min(n,\frac{m+1}{2})$ 然后把$2$乘进去 然后把$2\times x+2$ 变化指标呗 

<u>变化指标的时候不能有系数.. 不然值域的枚举会有问题..  第一次就变错了..</u>
$$
ans=\sum_{x=1}^{k-1}{(2n-2x)(m-2x)}
$$
然后拆开中间的式子
$$
ans=\sum_{x=2}^{k} (2n-2x)(m-2x)
$$
然后和上面式子方法一样
$$
ans=2\times (k-1)n\times m-(2n+m)\times k\times (k-1)+\frac{2\times k(k -1)(2k-1)}{3}
$$
类似式子也一样
$$
ans=2\times (k-1)n\times m-(2m+n)\times k\times (k-1)+\frac{2\times k(k -1)(2k-1)}{3}
$$
然后$k=4$的式子 又一个枚举正方形的 
$$
\sum_{i=2}^{min(n,m)} (n-i+1)\times(m-i+1)
$$
拆式子得到
$$
ans=k\times n\times m-(n+m)\times\frac{(k+1)\times k}{2}+\frac{k\times (k+1)\times (2\times k+1)}{6}
$$
另一个式子也是枚举正方形. 复读.
$$
\large{ans=\sum_{i=2}^{\frac{min(n,m)+1}{2}} (n-2\times i+2)(m-2\times i+2)}
$$
然后变指标 代替上界 但是$2\times i$需要把系数提出来 必须是线性才能变下标..
$$
ans=(k-1)\times n\times m-(n+m)\times k \times (k-1)+\frac{2\times k\times (k-1)\times (2k-1)}{3}
$$
$k=5$的式子 就是枚举正方形. 和上式一样
$$
ans=(k-1)\times n\times m-(n+m)\times k \times (k-1)+\frac{2\times k\times (k-1)\times (2k-1)}{3}
$$
然后你都可以算完了.. 你会发现最后一共就$4$个式子只不过是用的时候会有重叠的问题

然后这题还贼恶心.. 隔一个取一次模..

---

```c++
#include<bits/stdc++.h>
using namespace std;
const int N=1e3+10,mod=3e5+7;
int T,n,m,k,ans,tmp;
int fac[N],ifac[N],inv[N];
int C(int m,int n){if(m>n) return 0;return 1ll*fac[n]*(1ll*ifac[m]*ifac[n-m]%mod)%mod;}

int main()
{
	freopen("queen.in","r",stdin);
	freopen("queen.out","w",stdout);
//	freopen("in.txt","r",stdin);
	fac[0]=fac[1]=ifac[0]=ifac[1]=inv[1]=1;
	for(int i=2;i<=1000;i++){fac[i]=1ll*fac[i-1]*i%mod;inv[i]=1ll*(mod-mod/i)*inv[mod%i]%mod;ifac[i]=1ll*ifac[i-1]*inv[i]%mod;}
	scanf("%d",&T);
	while(T--)
	{
		ans=0;
		scanf("%d%d%d",&n,&m,&k);
		if(k==1){ans=1ll*n*m%mod;printf("%d\n",ans);continue;}
		
		ans=(1ll*n*C(k,m)%mod+1ll*m*C(k,n)%mod)%mod;
		tmp=0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=m;j++)
				tmp=(tmp+C(k-1,min(i,j)-1))%mod;
		ans=(ans+2*tmp%mod)%mod;
		
		if(k==3||k==4)
		{
			tmp=0;
			for(int x=2;x<=min(n,(m+1)/2);x++) tmp=(tmp+1ll*(n-x+1)*(m-2*x+2)%mod)%mod;
			ans=(ans+2*tmp%mod)%mod;
			tmp=0;
			for(int x=2;x<=min(m,(n+1)/2);x++) tmp=(tmp+1ll*(m-x+1)*(n-2*x+2)%mod)%mod;
			ans=(ans+2*tmp%mod)%mod;
		}
		if(k==3)
		{
			tmp=0;
			for(int i=2;i<=min(n,m);i++) tmp=(tmp+1ll*(n-i+1)*(m-i+1)%mod)%mod;
			ans=(ans+4*tmp%mod)%mod;
		}
		if(k==4)
		{
			tmp=0;
			for(int i=2;i<=((min(n,m)+1)/2);i++) tmp=(tmp+1ll*(n-2*i+2)*(m-2*i+2)%mod)%mod;
			ans=(ans+5*tmp%mod)%mod;
			for(int i=2;i<=min(n,m);i++) ans=(ans+1ll*(n-i+1)*(m-i+1)%mod)%mod;
		}
		if(k==5)
		{
			tmp=0;
			for(int i=2;i<=((min(n,m)+1)/2);i++) tmp=(tmp+1ll*(n-2*i+2)*(m-2*i+2)%mod)%mod;
			ans=(ans+2*tmp%mod)%mod;
		}
		printf("%d\n",ans);
	}
	return 0;
}
```

