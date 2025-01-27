# Race-Simulation
关于传统比赛方式的比赛模拟情况。通过积分版和赛程模拟出所有情况的排名及其概率。

## 已实现的规则
### 三局两胜单循环制
所有队伍采用三局两胜单循环赛制，输出最后的情况数量和各位置概率。

## 已实现的单场比赛胜率计算方法
### 加权平均比较
根据两支队伍当前的胜率进行加权平均，最后作为两支队伍交手时各自的胜率。

## 文件及使用
### 文件说明
#### data文件夹
data文件夹中包含了所需的积分版和赛程信息。已实现从 https://lol.fandom.com/wiki/League_of_Legends_Esports_Wiki 中自动获取赛事信息。
- data\LeaguePedia_Schedule.py 用于抓取赛程。
- data\LeaguePedia_Standings.py 用于抓取积分榜。

config文件夹中包含了队伍名称的映射关系。
#### 主文件夹
- run.py用于开始模拟测试，可以在其中设置模拟运行的次数`nums_simulation`。默认值为100,000次。（请根据你的电脑情况设置）
- Simulator.py包含模拟测试类以及其中的类方法。目前只实现了传统的三局两胜制。


### 使用说明
下载后运行`run.py`。其中数据来自data文件夹，随后运行即可。本仓库使用为2024年英雄联盟职业联赛春季赛3月22日的数据。随后会输出两个文本文件：
- total_result为所有可能的情况数。
- team_result为每个排名位置上出现的队伍的概率。

## 问题及可能的更新
- 没有交互界面。目前仍使用传统终端进行交互，需要一定的命令行基础。
- 功能单一。后续考虑通过形式化方法加入赛事变量的分析。
- 没有脚本参数。尚未加入通过脚本更改参数以实现更灵活的参数更改。
- 实现规则较少。后续考虑加入其他规则。
- 胜率比较方法单一。队伍间的胜率笼统使用加权平均计算，具有一定的局限性。
- 没有使用神经网络进行学习。前面的区域以后再来探索吧。
