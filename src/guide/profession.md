---
title: 副职系统
icon: flask
---

副职在wynn中其实并不是一个必须要游玩的内容

对于玩家而言，这个内容更像是后期~~闲的没事~~的休闲（一点也不）内容。

对于新手而言，练习副职是消耗时间过多且效率低下的玩法。

在这里，我只会对副职进行简单的介绍（部分摘自moe_block的自制系统简介）。

打开物品栏的指南针后，我们将鼠标移动至铁斧的图标上，可以看到我们所有的副职等级，
![](/assets/img/prof1.jpg)

## 采集

想要提升采集等级，最开始你需要先找到[Tool Merchant](/WynncraftCNguide/guide/npcs.html#tool-merchant)

Tool Merchant会出售1~2级的采集工具
![](/assets/img/prof2.jpg)
从上到下为鱼竿、木斧、木镐、木锄

分别对应钓鱼、伐木、挖矿和农业。

更高级的工具需要通过完成地牢并使用对应的代币与绿宝石在地牢商人处兑换

或直接使用交易市场进行购买。

注意，等级越高的工具，使用时所需要的对应采集等级需求就越高。

有了这些工具，我们就可以走到对应的地方，到了可以采集的目标附近之后，我们会看到类似于这样的字：
![](/assets/img/prof3.jpg)

此时我们使用工具左键可以获得该目标的直接产物（如木头、矿石、鱼肉、小麦）

而我们右键则是会获得该目标处理过后的产物（如纸、宝石、鱼油、绳子）。而这些产物都可以用于制造业。

以上介绍了四种采集，共有八种原材料。

原材料分为1~3星级，一次采集中，若采集成功（成功率随采集等级提高）：

89%的概率掉落1星原材料，10%的概率掉落2星原材料，1%概率掉落3星原材料。

原材料的星级影响其制作出的物品的耐久度，面板数值。

:::tip 原料对应的制作物品等级
原材料分为1级，10级，20级……110级。

1级原材料制作出的物品根据自身的制作等级，分为1-3级，3-5级，5-7级，7-9级；
具体等级根据范围内随机取值。

10级原材料则为10-13级，13-15级，15-17级，17-19级，20级往后以此类推。

特例为100级和110级原材料
100级原材料只能制作100-103级物品，110原材料只能制作103-105级物品。
:::

## 制作
在城镇中，我们会看到这样的东西，比如这个是药水制造的酿造台：
![每种制造业都有一个类似的工作台](/assets/img/prof4.jpg)

与其交互后即可打开制作GUI界面(每种制作副职都有一样的界面！)

![](/assets/img/prof5.jpg)

在这个界面的左边两格，是用于存放原材料（即采集获得的材料）

而中间六格则是用于存放功能素材（可以通过打怪/开箱子获得）

部分功能素材的不同摆放方式会为最后的成品带来不一样的效果。

:::tip 如果你不放置任何素材...
+ 饰品：无任何属性
+ 武器：只有基础伤害
+ 防具：只有基础血量
+ 消耗品：作用和回血药水相当，且会占用你的药水槽

:::

如果放了材料，则制作出来的物品带有材料属性

若消耗品放置了材料，则不再是回血功能，而是根据材料决定的属性

放置了材料的1-30级消耗品基础只能使用1次，31-70级2次，71级以上3次。

与此类似，1-30级自制武器装备只有1个粉槽，31-70级2个，71级以上3个。

:::tip 自制物品都具有耐久限制！
自制装备受到攻击和移动时掉落耐久，自制饰品同理
自制武器攻击和释放技能时掉落耐久。

当自制物品的耐久低于最大值的50%，会逐渐折损属性
耐久为0时只有10%的属性，但是并不会直接消失

使用修理碎片在铁匠处可以修复自制物品的耐久

**修理碎片放置在银行也可以直接在铁匠处消耗。**
:::

材料分为0星，1星，2星，3星。星级仅表示稀有度，不表示强度。

各种星级的材料都可能是比较实用的材料。

材料的等级表示其只能用于对应等级或者更高的配方中合成，
例如一个96级材料，若用于制作93-95的物品，则无法使用该材料；
若用于制作95-97或者更高的等级，则可以使用。

:::details 制造业的全部基础配方
+ 武器（Weaponsmithing）：X锭+2X木头=长矛；2X锭+X木头=匕首
+ 木工（Woodworking）：X木头+2X线=弓；2X木头+X线=法杖；X木头+2X鱼油=图腾
+ 盔甲（Armoring）：X锭+2X纸张=头盔；2X锭+X纸张=胸甲
+ 纺织（Tailoring）：X锭+2X线=靴子；2X锭+X线=护腿
+ 饰品（Jeweling）：X宝石+X鱼油=指环；X宝石+2X鱼油=手镯；X宝石+3X鱼油=项链
+ 炼药（Alchemism）：X鱼油+2X谷物=药水
+ 卷轴（Scribing）：X鱼油+X纸张=卷轴
+ 烹饪（Cooking）：X谷物+2X鱼肉=食物
  
以上X的取值根据原材料等级取值
| 原料等级 | 1 | 10-20 | 30-40 | 50-60 | 70-80 | 90+ |
| --- | --- | --- | --- | --- | --- | --- |
| X | 1 | 2 | 3 | 4 | 5 | 6 |

:::

## 附录 - 关于采集推荐地点以及工具兑换点

>数据来源：https://www.youtube.com/@Olinus10
### Woodcutting
+	Lv.1 NIVLA Forest `[-366,67,-1729]`
+	Lv.10 Detlas Suburbs `[335,67,-1580]`
+	Lv.20 Nemract Outskirts `[88,46,-2132]`
+	Lv.30 Bremminglar `[665,73,-2016]`
+	Lv.40 Nesaak Entrance `[85,68,-945]`
+	Lv.50 Dernel Mansion `[-941,23,-725]`
+	Lv.60 Dark Forest Border `[-1387,44,-5051]`
+	Lv.70 Forgery Grove `[-856,45,-4990]`
+	Lv.80 Thesead Entrance `[693,78,-5085]`
+	Lv.90 Lighthouse Mountain `[-1362,122,-3029]`
+	Lv.100 Kandon Mountain `[750,113,-4600]`
+	Lv.100 Wybel Island `[1296,66,-4693]`
+	Lv.110 Lutho Gate `[971,74,-628]`
	
### Farming
+	Lv.1 Ragni Wheat Fields `[-776,67,-1736]`
+	Lv.10 Durum Isles `[541,35,-2956]`
+	Lv.20 Durum Isles `[500,35,-2838]`
+	Lv.30 Durum Isles `[385,35,-2836]`
+	Lv.40 Olux Farms `[-1630,51,-5428]`
+	Lv.50 Wormhole Farms `[-2068,53,-5462]`
+	Lv.50/60 Forgotten Burrows `[-2041,57,-5388]` (+50%XP,Quest Needed)
+	Lv.60 Forgery Farms `[-724,44,-5014]`	
+	Lv.70 Forgery Farms `[-724,44,-5014]`
+	Lv.80 Hobgoblin Flelds `[79,42,-4838]`
+	Lv.90 Lighthouse Farm `[-1378,123,-3013]`
+	Lv.100 Kandon Caverns `[850,40,-4423]`
+	Lv.110 Void Valley Upper `[1089,135,-1130] `


### Mining
+	Lv.1 Ragni Mine `[-572,69,-1556]`
+	Lv.10 Corrupted Mines `[786,86,-1242]`
+	Lv.20 Corrupted Mines `[685,89,-1217]`
+	Lv.30 Bandit Barracks `[1478,91,-2178]`
+	Lv.40 Nesaak Mountain Side `[260,89,-700]`
+	Lv.40 Karoc Quarry `[-1655,76,-4347]` (+50%XP,Quest Needed)
+	Lv.50 Troms Silver Mine `[620,83,-1009]`
+	Lv.60 Olux River Source `[-1444,48,-5367]`
+	Lv.70 Prison Caverns `[-790,108,-5628]`
+	Lv.80 Colossus Mines `[560,120,-4355]`
+	Lv.80/90 Maex Mine `[1535,61,-5339]` (+50%XP,Quest Needed)
+	Lv.90 Molten Upper Mine `[1433,142,-5106]`	
+	Lv.100 Sky Caverns `[872,34,-4775]`
+	Lv.100 Kandon Beda Cave `[850,40,-4423]`
+	Lv.110 Olmic Mine `[492,93,-525]`

### Fishing
+	Lv.1 Ragni Pond `[-634,67,-1536]`
+	Lv.10 Wynn Plains River `[53,58,-1494]`
+	Lv.20 Saint’s Row Beach `[371,34,-2126]`
+	Lv.30 Desert River Source `[1182,154,-2248]`
+	Lv.40 Nodguj Island `[891,34,-3372]`
+	Lv.50 Iboju Waterfall `[-780,74,-724]`
+	Lv.50 Forgotten Burrows `[-2041,57,-5388]` (+50%XP,Quest Needed)
+	Lv.60 Willow Pond `[-1303,51,-5194]`
+	Lv.70 Lake Gylia `[-207,29,-5204]`
+	Lv.80 Relos Coast `[-1860,37,-2191]`
+	Lv.90 Molten Heights Lake `[1435,139,-5091]`
+	Lv.90 Maex Mine `[1535,61,-5339]` (+50%XP,Quest Needed)
+	Lv.100 Kandon Pond Lower `[689,88,-4605]`
+	Lv.100 Sky Falls `[1432,127,-4574]`
+	Lv.110 Toxic Hill Upper `[786,148,-983]`

### Tools
+ Tier 3: Decrepit Sewers & Infested Pit
	Cost: 1 Fragment

+ Tier 4: Timelost Sanctum & Underworld Crypt
	Cost: 2 Fragment

+ Tier 5: Sand-Swept Tomb
	Cost: 3 Fragment +64e

+ Tier 6: Ice Barrows
	Cost: 4 Fragment + 128e

+ Tier 7: Undergrowth Ruins
	Cost: 5 Fragment + 256e

+ Tier 8: Galleon's Graveyard & CDS
	Cost: 6 Fragment + 512e

+ Tier 9: CIP & CLS
	Cost: 7 Fragment + 1024e

+ Tier 10: CUC & CSST
	Cost: 8 Fragment + 2048e

+ Tier 11: CIB & CUR & Fallen Factory
	Cost: 9 Fragment + 4096e

+ Tier 12: Eldritch Outlook
	Cost: 9 Fragment + 4096e

:::tip 
本文作者:kotoko
:::