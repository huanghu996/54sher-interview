[Github]<https://github.com/huanghu996/54sher-interview>

# 第一部分 学习Git

对git bash这种单调的命令窗口，我一直怀有着比较深的刻板印象：感觉他和github这门高端的页面（尤其是还要开VPN）完全连不上关系。在我学习完一些基操后，震撼狗子100年！:+1:

##### 基本操作

1. git config --global user.name/email 设置

2. 创建文件夹，并初始化

3. 建立远程库

4. * touch 创建文件
   * vi +文件名 修改文件
   * git add +文件名 添加到暂存区
   * git commit -m"  " 添加描述
   * git push leadwolf3 master push到远程库中 
   * 惊奇的发现 github里竟然有我传的文件了
   * git clone +网址 下载到文件夹
   * git push 上传文件，提交任务一

   

5. ```
   另外
   git status 查看状态
   git checkout +branch 转换branch
   ```

   

##### 主要出现的问题 

* 远程库的建立花了我很多时间，主要是各个教程都不相同，把每个都试了一遍水，发现只有一个成功了
* 建完库后发现push时又报错了 然后又回去检查了一遍远程库

##### 感谢菜鸟教程！:+1:

# 第二部分 学习Markdown

> 技术的用途，是用出来的，Markdown也是如此



#### 1.过程

我是使用了《了不起的Markdown》这本书来对Markdown的语法进行学习的，该书的教学思路十分简明扼要，是我很快掌握了markdown的相关语法。

我是在新校区图书馆学习的所有这些，在整个学习过程中我也顺便学会了图书馆的预约规则与方法，在哪里也遇到了很多学长学姐也在一同学习。在学习markdown的过程中，我深刻感受到markdown的简洁方便，因为平常用WPS写文档时，对很多文字的格式、字体、表格插入等等都需要一个一个寻找、点按钮才能实现，有些许繁琐，而markdown中，你只需输入一些字符就可以实现这点，不再需要手脱离键盘去用鼠标点来点去，十分方便。   

#### 2.成果展示（基础语法）

1.  自我介绍（一）

我叫**赵传禹**，来自  *土木安全2129班*    (斜体)，是 个~~男生~~ 帅哥   :clap::clap::clap:;

2.  自我介绍（二）

| 姓名   | 班级           | 爱好         | 目标                 |
| ------ | -------------- | ------------ | -------------------- |
| 赵传禹 | 土木安全2129班 | 足球，打游戏 | 进入升华工作室程序部 |

3.  自我介绍（三）

我的QQ名称是  `旅人 `  ,qq号是`954636711`，[QQ空间](https://user.qzone.qq.com/954636711/main) :smile:，

下面的是我的QQ头像，来自《守望先锋》的**死神**

![QQ头像](http://m.qpic.cn/psc?/V11Z8VTJ0Ljmi1/bqQfVz5yrrGYSXMvKr.cqSG4*OZRNKSm0I5EGTU0L8n*kUPYPBduMyN.angZ828nSpP7282HQr3WNyJOh5Ko5Pf7k1lYfiWg2qWUWGeCBbM!/mnull&bo=gAKAAgAAAAABByA!&rf=photolist&t=5)

***



4.  总结 

- (一)中 我应用了**标题**、**加粗**、**斜体**、**删除线** 、**表情**的Markdown代码 ；

- (二)中 我应用了**表格**的Markdown代码；

- (三)中 我应用了**行内代码**对文字进行高亮处理 ，应用了**文字链接**与**图片引用**(来源网络)的Markdown代码 

  ***

  

5. 由于使用markdown时间较少，有些地方的语法排版不是那么的好，但我如果进入程序部后在多加使用联系，就会越来越熟练的！

   

#### 3.拓展语法

* 序列图(/``` sequence)

  ```sequence
  张三->李四:早上好呀！
  李四->张三:早上好！
  ```

* 流程图（/```flow）

  

  ```flow
  st=>start: 开始
  op=>operation: 我是帅哥
  cond=>condition: yes or no?
  e=>end: 结束
  
  st->op->cond
  cond(yes)->e
  cond(no)->op
  
  ```

* mermaid甘特图（/``` mermaid     gantt）

  ```mermaid
  gantt
  dateFormat YYYY-MM-DD
      title 学习周期
  section 学习
      
  学习    :2021-09-10,2022-02-06
  section 考试
  期中考试    :2021-11-20,2021-11-25
  期末考试    :2022-01-30,2022-02-05
  ```

  

# 第三部分 想要学习的内容

- 多种语法相关的各种知识(python,linux......)
- 认识大佬，认识新朋友，拓展自己的朋友圈
- 学习网页、微信小程序设计与制作和相关知识

