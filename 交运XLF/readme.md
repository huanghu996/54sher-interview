# 任务一

+ ## 题外话

  容我先扯些题外话，希望学长学姐不要介意：）

  再次介绍一下我自己。我来自交通运输类2101班，二面群里头像是这个：

  <img src="https://i.loli.net/2021/10/04/UagGeIy7hMlXpCr.jpg" alt="dawn.jpg.bmp" style="zoom:5%;" />	

  其实在CSU我最想进的专业是计算机，可惜分不太够。我知道，在大一下学期会有一次转专业的机会，我想去尝试一下。在此之前，我想，我不光应该把学业搞好，还应自主地学习一些计算机的技术。当我听说升华工作室的程序部招新时，我心想，这里正是我能够接触并学习技术的好地方啊。于是，我怀着一颗激动和好奇的心，来了。

+ ## 关于Git和Github

     我是在b站上学习的这两样东西，网址如下：

     <https://www.bilibili.com/video/BV1fK4y1b7XL?spm_id_from=333.999.0.0>

     首先，我了解了Git最初是Linux基于Bitkeeper开发出的一套属于自己的分布式版本管理系统。Git可以帮助我们轻松实现本地文件几个版本之间的来回切换。而在GitHub上面我们可以建立一个远程仓库，从而实现本地仓库与远程仓库的同步以及与其他开发者的文件共享。

     在学习过程中，我学会了Git的一些基本命令行的运用，如：

     | 目的         | 命令行   |
     | ------------ | -------- |
     | 建立本地仓库 | git init |
     |生成密钥对|ssh-keygen -t rsa|
     |添加远程仓库|git remote add origin ......|
     |从本地仓库把master分支推送到远程|git push -u origin master|
     |从远程仓库克隆到本地|git clone ......|
  
     更多地，我学会了用TortoiseGit这一Git的图形化软件进行除上述外其他的一些操作：如分支的建立以及切换、从GitHub的远程仓库pull到本地仓库等等等等（如图）。
  
     ​	![2021-10-05.png](https://i.loli.net/2021/10/05/mMAU1HqDgXoV7RL.png)
  
     ![2021-10-05 _1_.png](https://i.loli.net/2021/10/05/TLoVlwSk6abJBy1.png)
     
+ ## 关于Markdown

     我是通过[菜鸟教程](https://www.runoob.com/markdown/md-tutorial.html)学习的Markdown

     通过学习，我了解了Markdown是一种轻量级标记语言，以纯文本的格式编写，而能够以图片、PDF、网页等多种形式导出，非常地方便实用。

     我学会了通过控制”#“的数量调节标题的大小（如”任务一“用的是一号字体，而”题外话“用的是二号字体),通过控制”*“的数量打出：

     *斜体*、**粗体**以及***粗斜体***，用”~“打出~~删除线~~，学会了<u>划重点</u>, 会加脚注[^1],会添加代码区块：

     ```c
     #include<stdio.h>
     int C(unsigned int x,unsigned int y)
     {  
     	int t;
     	if(y<0||y>x)putchar('\a');
     	else
     	{
     		t=jc(x)/jc(y)/jc(x-y);
     		return(t);
     	}
     }
     int jc(unsigned int x)
     {
     	int t=1,i=1;
     	for(;i<=x;i++)t*=i;
     	return(t);
     
     }
     int main( )
     {
     	int a,b;
     	printf("组合数计算：\n形式：C(x,y)\t注意：其中0<=y<=x\n请输入x:");
     	scanf("%d",&a);
     	printf("请输入y:");
     	scanf("%d",&b);
     	printf("C(%d,%d)=%d!/%d!/(%d-%d)!=%d\n",a,b,a,b,a,b,C(a,b));
     	return 0;
     }
     ```

     以及链接、图片、表格等的添加（在此文档中都有展示）......

     [^1]:脚注，是汉语词汇，汉语拼音为jiǎo zhù，是可以附在文章页面的最底端的，对某些东西加以说明，印在书页下端的注文。脚注和尾注是对文本的补充说明。脚注一般位于页面的底部，可以作为文档某处内容的注释；尾注一般位于文档的末尾，列出引文的出处等。

+ ## 进入程序部后我想学习什么

想学习开发微信小程序。我有上网查过开发小程序需要什么技术，大概会涉及到Java、HTML、css、js什么的。这些我先前都没怎么接触过，所以我都想学23333.

