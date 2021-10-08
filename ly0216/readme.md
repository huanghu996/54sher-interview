# 一、git相关知识学习笔记

## 一、一些基础概念

​	**1.版本控制系统（VCS-version control system）：**记录若干文件内容（只限于文本文件）变化，以便查阅特定版本修订情况的系统。

​	**2.RCS（一种本地版本控制）:**其工作原理为在硬盘上保存补丁集，通过应用补丁重新计算出各个版本的文件内容

​	**3.CVCS:**集中化的版本控制系统，即协同工作的人都可以操作，但历史记录保存在单一位置。问题在于有一个管理员掌握大权，其他合作的人只能申请更新、无法直接拥有全部历史版本。

​	**4.DVCS:**分布式版本控制系统，在CVCS的基础上保证每个人都能镜像克隆出完整的历史版本，相当于可以有多个完整的代码仓库。

​	**5.repository:**仓库，存储所有项目文件。

​	**6:branch:**分为main和feature，main为已确定的版本，feature是自己克隆出的main对其进行修改，feature可通过submit、discuss、pull request将其合并到main上。git上类似

​	**7:pull request:**拉取申请，即将feature合并到main上，可查看版本区别，红色表示subtraction，绿色表示addition。

​	**8.git:**一个分布式版本控制系统（目前世界上最先进的），基于c语言，由Linus写成。由工作区和版本库组成，版本库分为stage和master。

​	**9.远程仓库（origin）:**git的特别之处，每台机器都可以克隆相同的原始版本库，无主次之分。防止硬盘损坏导致文件丢失。

​	**10.SSH Key:**在本机向GitHub提交文件时，需要确定在账号上添加了SSH Key，只有这样GitHub才能确认是你推送的。

​	**11.fork:**将已有的开源项目中的仓库克隆到自己的仓库里。

​	**12.source tree:**一个可视化平台，将git仓库的内容展现的更直观，也可以进行一些git能实现的操作。

## 二、关于git的一些基本操作和常识 （~~过程，经历，实践~~）

​	**1.**使用了--global，该命令只需运行一次，之后对本机所有Git仓库都有用。

​	**2.**git config --list，查看配置，按q结束；进一步的 git config <key> 查看某一项配置

![1633323984194](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633323984194.png)

​	**3.**获取Git仓库（repository），本地目录转换or其他服务器克隆，前者只需在本地目录通过git init命令将其转化为Git可管理的repository，

​	**4.**mkdir <key> 创建一个名为<key>的目录

​	**5.**pwd 显示当前目录

![1633323908419](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633323908419.png)

​	**6.**add 将当前目录下的已存在的文件加入Git仓库(stage)，例如

```
$ git add readme.txt
```

​		若该文件被.gitignore忽略了，可加上 -f参数强制添加

```
$ git add -f app.class
```

​	**7.**commit 将文件提交到Git仓库（master），-m后的内容为本次提交的解释说明，便于以后的自己和别人看懂

```
$ git commit -m"explanation"
```

可以add多个文件后，一次commit提交多个文件

​	**8.**dir 或者 ls能查看当前目录的文件

![1633224110564](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633224110564.png)

​	**9.**cd /xxx/xxx/xxx 一次性到达指定位置；cd .. 返回上一级

​	**10.**diff查询文件的修改内容,-表示原先版本，+表示修改后的版本，默认比较的是工作区和缓存区的区别。

```
$ git diff
```

![1633224125743](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633224125743.png)

​		也可以选择工作区与上一次commit的区别。

```
$ git diff HEAD
```

​	**11.**log查看文件修改的历史记录，在此基础上加上--pretty oneline可以精简，HEAD（指针）表示当前版本，上一个版本是HEAD^，HEAD~99等等

![1633165019093](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633165019093.png)

![1633165578909](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633165578909.png)

​	**12.**cat <key> 用git bash窗口查看文件

![1633166593597](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633166593597.png)

​	**13.**reset可用于将当前版本退回到之前的版本，--hard之后加版本号即可，可以是HEAD^这种，也可以是--pretty=online中查到的版本号的前几位，例如ca594（十六进制编码）；reset还可用于将缓存区的文件退回到工作区

![1633167178207](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633167178207.png)

```
$ git reset HEAD readme.txt
```

![1633184547547](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633184547547.png)

​	**14.**reflog可以查看命令记录，加入忘记了版本号就可以通过这个查看，按q结束查看

![1633167017607](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633167017607.png)

​	**15.**git status可以查看文件状态，是否有modify，是否add，是否commit

![1633183489115](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633183489115.png)

​	**16.**git checkout  -- <file> 可以将工作区修改过的文件恢复到上个版本，将缓存区修改过的文件恢复到add时的版本

![1633183947725](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633183947725.png)

​	**17.**rm <file> 删除当前目录下的file，不记录删除操作；git rm删除文件，并将该文件纳入缓存区，然以后commit，如果误删了可通过**16**恢复最新的commit的版本

![1633184940500](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633184940500.png)

![1633185400276](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633185400276.png)

​	**18.**remote add将本地仓库和GitHub远程仓库关联，此处的origin是远程仓库的名字（可自定义），lewisyakon是你的id，learngit为远程仓库里repository的名字（可自定义）

```
$ git remote add origin git@github.com:lewisyakon/learngit.git
```

​		remote rm将本地仓库和远程仓库解绑

```
$ git remote rm origin
```

​		解绑前可通过git remote -v查看远程仓库信息，显示的分别是抓取和推送的地址

![1633226415857](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633226415857.png)

​	**19.**git push origin master将本地仓库的master推送到远程仓库origin中，如果首次推送需要加上-u参数（给git push -u origin master），本地文件通过add和commit后可通过该命令同步到origin上。

![1633226666152](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633226666152.png)

​	**20.**git clone将远程仓库克隆到本地仓库，克隆后只会得到master分支。

```
$ git clone git@github.com:lewisyakon/gitskills.git
```

![1633227752258](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633227752258.png)

​		如果想要得到其他分支，需要以下命令，以dev为例。（switch -c也可以）

```
$ git checkout -b dev origin/dev
```

​		同样，本地dev和远程origin/dev也需要关联。

```
$ git branch --set-upstream-to=origin/dev dev
```

​	**21.**git branch 用于查看当前分支（当前分支前会有*）；git branch dev 创建一个名为dev的分支；git swich dev 切换到dev分支上。类似命令 git switch -c dev 或 git checkout -b dev 创建一个名为dev的分支并切换到dev上,git checkout dev 也可以切换到dev分支上。git branch -d dev 删除一个名为dev的分支（该分支已merge过）；如果该分支没有merge，而且用不上了，直接用git branch -D dev强制删除。修复bug时也可用此方法，建立分支->在分支上修复->合并并删除分支。

![1633231908274](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633231908274.png)

​	**22.**git merge dev 将名为dev的分支合并到当前分支上，即将修改同步。现实的Fast-forward表示合并速度较快，当两个分支都进行了add和commit时，自动合并会出错（如图二），此时需要手动修改文件。Fast-forward合并时会丢弃dev的信息，可通过--no-ff禁用，此时的合并多一个commit操作，会将dev的信息记录下来（如图三,查看分支修改记录）

![1633232218084](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633232218084.png)

![1633247564679](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633247564679.png)

![1633248555825](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633248555825.png)

​	**23.**若当前分支的工作还没有完成，不能提交，但需要在别的分支工作。如果不将当前文件提交就无法switch（如图一），所以需要git stash，用来将当前现场储存下来不用提交。git stash list用于查看储存的列表，git stash apply用于恢复工作现场，恢复后不会删除，git stash drop删除；git stash pop在恢复的同时将其删除（以上操作对象均默认为list中的第一个，可通过stash@{number}准确操作对应对象）。

![1633251703426](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633251703426.png)

​	**24.**当我们在master分支上修复了bug，dev分支上却没有修复，可以在dev上开个分支修复，但git提供了更简单的复制操作的方法（当然不是直接把master merge到dev上）。git cherry-pick 修复时commit的操作序列号，相当于复制一个commit操作到当前分支。

![1633260744234](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633260744234.png)

![1633260753803](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633260753803.png)

​	**25.**git pull当提交失败时将最新的提交从origin/dev中抓取下来，然后在本地合并后，再push

​	**26.**git rebase将本地未push的分叉提交历史整理成直线，查看历史提交的变化时更容易。

​	**27.**当我们用十六进制编码代表commit时，较难记忆，可通过tag操作将其打上标签。首先要切换到对应分支上，下以v1.0为例，默认对象是最新的一次提交。

```
$ git tag v1.0
```

​		也可以指定对象打上tag。

```
$ git tag v1.0 df56a4
```

​		git tag可以查看当前的所有标签，排列方式按字典序。

​		以下命令可详细查看tag信息。

```
$ git show v1.0
```

​		打tag时还可以加以详细的描绘，-a指定标签名，-m指定说明文字

```
$ git tag -a v1.0 -m"version 1.0 released"
```

![1633271292873](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633271292873.png)

​		删除标签

```
$ git tag -d v1.0
```

​		将tag push到远程仓库

```
$ git push origin v1.0
```

​		push可以批量操作

```
$ git push origin --tags
```

​		远程删除tag

```
$ git push origin :refs/tags/v1.0
```

​	**28.**当命令一行写不下时，输入 \ + enter下一行接着写

![1633307043417](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633307043417.png)

​	**29.** .gitignore文件 用于处理一些需要用的但不能提交的文件，该文件放在根目录下，该目录下的所有仓库都能用。文件编辑时遵循相应的语法，每一行指定一个忽略规则（~~看起来十分繁琐，可以直接复制现成的~~）。

​	**30.**git bash中一些操作命令较长，可通过一些重定义简化命令。

```
$ git config --global alias.st status
```

​		该命令相当于用st代替status，以后就可以敲git st查看状态。（相当于#define 的宏定义）

## 三、学习感想（~~牢骚~~）

​	首先是对Git的发明的感慨吧，就从初始的版本控制系统，逐步改进到如今的Git，从中体会到科技的发展使人类生活变得更加便捷，不用担心一个本地库崩溃导致项目丢失、每个人都可以参与的开源项目、alias.简化命令等等。这就是程序开发的魅力吧，Linus发明Git使研发项目的人有了免费且高效的工具，这还不够激励一个人去学习程序开发吗？

​	其次是Git Bash使用过程的迷茫，虽然是学会了一些基本的命令，但是过程中也遇到了解决不了的问题（无法进行add和commit，错误提示也看不懂），还好现在只是自己写一些无关紧要的文件，用最简单粗暴的方法直接从零开始，但以后如果是项目开发过程中遇到问题就不行了，路漫漫其修远兮啊。

​	最后是意识到自己学习新知识方法上的缺陷吧，很少与别人交流，总是自己埋头瞎干，有的问题可能只需要问下别人就能解决，却自己琢磨浪费大量时间，与人交流在以后的工作中肯定是必不可少的，需要锻炼。

​	还有一点，感觉自己这么多年一直都是应试英语学习，使用GitHub和Git时才发现自己英语水平是真的不够....

## 四、文献参考及学习途径

​	**1.progit**

​    **2.知乎文章**

​    **3.一些dalao的博客**

​	**4.GitHub official guide**

---

# 二、Markdown相关知识学习笔记

## 一、基本语法

​	**1.标题：**n级标题格式为：n个#+空格+标题内容，共六级，快捷键为ctrl+n。

​	**2.字体：**斜体、粗体、加粗斜体分别是在文本前后加一、二、三个*或_，如下图。快捷键分别是ctrl+i，ctrl+b，ctrl+i+b。

​		*我是斜体*					 **我是粗体**				***我是加粗斜体***

​	**3.分割线：**一行中有三个以上的*、-或_，都可以把该行变成分割线，如下图。

***

​	**4.删除线：**文本内容前后各两个波浪线~~，如下图。快捷键为alt+shift+5。

​	~~我被删除了~~

​	**5.下划线：**<u>我带下划线了</u>

```
<u>带下划线文本</u>
```

​	**6.脚注：**[^我是被解释的]

[^我是被解释的]:我就是脚注解释qaq

内容如上图，将鼠标放上时显示脚注。

```
balabala.. [^name]
[^name]:explanation
```

​	**7.列表：**分为无序和有序两种，无序列表即文本前加*、+或-，有序列表就是数字+.，如下图。每按一次回车自动添加一行，按两次回车结束，可以嵌套。

* 我是第一行

1. 我是第二行

---

​	**8.区块：**段落开头加>和空格，效果如下，按一次回车自动添加，按两次结束。还可以多层嵌套，可与列表嵌套。

> 我是区块

> > 我是第二层

​	**9.代码：**小部分的可以用反引号（‘）前后括起来，如下图，大片代码可用ctrl+shift+k，ctrl+enter结束。

`printf()`

```
#include<bits/stdc++.h>
using namespace std;
int main()
{
......
}
```

​	**10.链接：**效果：[洛谷](https://www.luogu.com.cn/)	或 	<https://www.luogu.com.cn/>

```
[链接名称](链接地址)	或	<链接地址>
```

​	**11.插入图片：**直接用->编辑->图片工具->插入本地图片

​	**12.表格：**直接用|分割左右，-分割表头和其他行，效果如下，快捷键ctrl+t更方便。

| 表头 | 表头 |
| ---- | ---- |
|      |      |

​	**13.正常显示符号：**在符号前加上反斜线\即可，效果如该星号 **\***

![1633334848128](C:\Users\刘翊\AppData\Roaming\Typora\typora-user-images\1633334848128.png)

​	**14.Latex公式：**数学公式前后加$$即可，或者ctrl+shift+m添加公式块，如下图。[公式大全](https://www.luogu.com.cn/blog/IowaBattleship/latex-gong-shi-tai-quan)
$$
ans=2\times \sum_{i=1}^{n} \sum_{j=1}^{m} \binom{min(i,j)-1}{k-1}
$$
​	**15.高亮：**前后两个\=\=即可，如图。==我高亮了==

## 二、学习感想

​	观感非常棒，很多网络平台上都支持使用。

## 三、文献参考及学习途径

​	**1.知乎文章**

​	**2.网上的博客**

# 三、进入程序部后想学的内容

 1. 编程语言：python、Java、JavaScript

 2. 小程序设计

 3. 框架的开发构建

 4. 团队协作和人际交往qaq

