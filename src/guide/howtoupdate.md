---
title: 如何帮助我们维护更新
icon: gem
---

首先，非常感谢你能点开这篇文章。

原作者现在精力有限，本攻略大部分页面均已过时，需要有人帮忙维护跟新。

## 对于比较熟悉github的维护者：

### 下载本地项目

首先，先点进[github页面](https://github.com/EternityTQ/WynncraftCNguide)

注册一个账号后，按照下图所指示Fork所指的分支

![](/assets/img/how1.png)

接着，将你fork的项目拉到本地

这里推荐使用[Github Desktop](https://desktop.github.com/download/)，GUI界面易于上手

在下载完毕并登录后，点击右上角的**Clone Repository**

![](/assets/img/how2.png)

即可将你fork的项目下载到本地。

在下载完成时记得点击**As contributor**

之后你就可以在本地进行编辑操作啦

### 提交更新请求

在本地完成任意编辑操作后，在Github Desktop中你能看到所有你修改的内容。填写备注后，点击下方的commit to assistance

![这里借的别人的项目，所以是main](/assets/img/how3.png)

之后回到github，返回你的主页，进入**你所fork的项目**

点击Pull requests，再点击New pull requests。

![](/assets/img/how4.png)


然后照着点就可以了。

## 对稍微了解github的维护者

这种方法同样需要一个github账号

![](/assets/img/how5.png)

直接在你想修改的页面点击右下角的编辑此页

在弹出来的页面修改完毕后，按下图点击。

![](/assets/img/how6.png)

此时由于你没有本项目的编辑权限，你会自动创建一个fork分支。不知道这句话是什么意思可以不用管，继续点下去即可

![](/assets/img/how7.png)

然后就修改完毕啦！

## 对完全不了解github的维护者

### 1.文本内容提交
直接将你编写的文档/Word文档在群内发送给维护者(QQ:1586049354)

或发送到邮箱：1586049354@qq.com

格式要求：

使用纯文本或 Word 文档

标题使用 # 标题 格式

图片单独作为附件发送，且需要在文档内标记好图片位置。



### 可视化编辑（推荐）
使用 [StackEdit](https://stackedit.io/) 在线编辑器：

粘贴/编写内容

实时预览排版效果

导出为.md文件发送给我们

## 更新规范

对于图片，均需要命名后存放在`src\.vuepress\public\assets\img`中

对于坐标，可以使用`<CC>[]</CC>`。

对于绿名NPC，可以使用`<NPC>NPCname</NPC>`

如果有不恰当的格式，我会进行修改，所以不用怎么担心。

对于markdown语法，可以查看[这篇文章](https://markdown.com.cn/basic-syntax/)

### 文件结构

src/
├── .vuepress/ # 站点配置
├── guide/ # 游戏指南
│ └── basesystem/ # 基础系统
│ └── advancesystem/ # 进阶系统
│ └── commonfunction/ # 常用功能
│ └── dungeon/ # 地牢
│ └── raid/ # raid
├── quests/ # 任务攻略
├── newbie/ # 新手攻略
└── README.md # 项目说明
