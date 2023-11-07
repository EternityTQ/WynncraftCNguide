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

副职主要分为**采集**和**制作**两大板块

## 采集
首先，你需要找到[Tool Merchant](/WynncraftCNguide/guide/npcs.html#tool-merchant)购买1-2级的工具

有了工具后，你就可以对资源进行开采了

需要注意的是，对于每一类资源来说，左键与右键对应着不同的产物，在下面会有介绍

采集所得到的原料都将用于制造副职中
:::tip
截止110级前，等级每逢5的尾数将会解锁新的工具等级

而每逢0的尾数将会解锁新的资源
:::

在开采时，有概率失败。

当你的工具耐久越低时，失败概率越高，失去耐久时不会得到产物

:::warning
携带同职业的工具会导致你的开采失败概率大幅度提高！
:::

当你开采成功后，将会得到随机品质的原料

89%得到1星，10%得到2星，1%得到三星

星级将会影响到制造所得到的装备属性、耐久。

采集一共分为四种副职

### Mining(矿业)

**左键：Ingot 右键：Gem**

矿物资源点比较集中，一般以矿场形式呈现

通常来讲，只要你看到了类似矿场一样的建筑，一般都会有矿物资源点

### WoodCuting(伐木)

**左键：Wood 右键：Paper**

树木资源点非常分散且非常常见，只要你能找到有森林的地方就能进行伐木

### Farming(农业)

**左键：String 右键：Grain**

农业资源点与矿业相似，比较集中，且一般以农田的形式呈现

只要你能找到农田，一般都会有农业资源点

### Fishing(渔业)

**左键：Oil 右键：Meat**

与伐木资源点相似，渔业资源点非常常见

只要你能找到有河流的地方，一般都能找到渔业资源点

需要另外注意的是，Meat用处非常小，一般请建议只开采Oil

### 工具来源

除了1-2级的工具可以在[Tool Merchant](/WynncraftCNguide/guide/npcs.html#tool-merchant)购买以外

3级及以上的工具均需要在副本商店通过副本碎片来兑换

具体位置请看文末

当然，你也可以通过交易市场来购买其他玩家已经兑换好的工具，不过多少都是要多花点钱的


:::tip 原料对应的制作物品等级
原材料分为1级，10级，20级……110级。

1级原材料制作出的物品根据自身的制作等级，分为1-3级，3-5级，5-7级，7-9级；
具体等级根据范围内随机取值。

10级原材料则为10-13级，13-15级，15-17级，17-19级，20级往后以此类推。

特例为100级和110级原材料
100级原材料只能制作100-103级物品，110原材料只能制作103-105级物品。
:::

:::tip 提升效率的方法
在有着pxp+psb(bomb)的情况下，你的采集副职练级效率将会提升至4倍

因此，不是很建议在没有bomb的情况下进行副职练级

关于Bombs可以看[这一章](/WynncraftCNguide/guide/VIP.html#bombs)

同时，一些自制素材也能提供采集经验加成

你可以购买素材让大佬帮忙制作带有高额采集经验加成的装备(最高可以额外提供约150%的采集经验加成)

当然，这些素材和材料**相当非常无比贵**，请注意衡量成本
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

### 制造业的全部基础配方
| 种类     | Ingot | Gem | Wood | Paper | Grain | String | Meat | Oil |
| ---------- | ----- | --- | ---- | ----- | ----- | ------ | ---- | --- |
| 长矛<br>(武器) | 1X    |     | 2X   |       |       |        |      |     |
| 匕首<br>(武器) | 2X    |     | 1X   |       |       |        |      |     |
| 弓<br>(木工) |       |     | 1X   |       |       | 2X     |      |     |
| 法杖<br>(木工) |       |     | 2X   |       |       | 1X     |      |     |
| 巫杖<br>(木工) |       |     | 1X   |       |       |        |      | 2X  |
| 头盔<br>(盔甲) | 1X    |     |      | 2X    |       |        |      |     |
| 胸甲<br>(盔甲) | 2X    |     |      | 1X    |       |        |      |     |
| 护腿<br>(纺织) | 2X    |     |      |       |       | 1X     |      |     |
| 靴子<br>(纺织) | 1X    |     |      |       |       | 2X     |      |     |
| 种类     | **Ingot** | **Gem** | **Wood** | **Paper** | **Grain** | **String** | **Meat** | **Oil** |
| 指环<br>(饰品) |       | 1X  |      |       |       |        |      | 1X  |
| 手镯<br>(饰品) |       | 2X  |      |       |       |        |      | 1X  |
| 项链<br>(饰品) |       | 3X  |      |       |       |        |      | 1X  |
| 药水     |       |     |      |       | 2X    |        |      | 1X  |
| 卷轴     |       |     |      | 1X    |       |        |      | 1X  |
| 食物     |       |     |      |       | 1X    |        | 2X   |     |
  
以上X的取值根据原材料等级取值
| 原料等级 | 1 | 10-20 | 30-40 | 50-60 | 70-80 | 90+ |
| --- | --- | --- | --- | --- | --- | --- |
| X | 1 | 2 | 3 | 4 | 5 | 6 |


## 附录 - 关于采集推荐地点以及工具兑换点

>数据来源：https://www.youtube.com/@Olinus10

此处推荐点基本为少干扰、安心采集的点位

对于标粗的地点名称，代表需要前置任务才可进入，通常会有+50%的采集经验加成

### Woodcutting
| 等级 | 资源名称 | 地点                   | 坐标                |
|------|-----|-------------------|---------------------|
| Lv.1    | Oak |NIVLA Forest           | `[-366,67,-1729]`   |
| Lv.10   | Birch | Detlas Suburbs         | `[335,67,-1580]`    |
| Lv.20   | Willow | Nemract Outskirts      | `[88,46,-2132]`     |
| Lv.30   | Acacia | Bremminglar            | `[665,73,-2016]`    |
| Lv.40   | Spruce | Nesaak Entrance        | `[85,68,-945]`      |
| Lv.50   | Jungle | Dernel Mansion         | `[-941,23,-725]`    |
| Lv.60   | Dark | Dark Forest Border     | `[-1387,44,-5051]`  |
| Lv.70   | Light | Forgery Grove          | `[-856,45,-4990]`   |
| Lv.80   | Pine | Thesead Entrance       | `[693,78,-5085]`    |
| Lv.90   | Avo | Lighthouse Mountain    | `[-1362,122,-3029]` |
| Lv.100  | Sky | Kandon Mountain<br>Wybel Island        | `[750,113,-4600]`<br>`[1296,66,-4693]`   |
| Lv.110  | Dernic | Lutho Gate             | `[971,74,-628]`     |


	
### Farming
| 等级   | 资源名称 |地点                   | 坐标                   |
|--------|---|---------------------|------------------------|
| Lv.1   | Wheat |Ragni Wheat Fields     | `[-776,67,-1736]`      |
| Lv.10  | Barley |Durum Isles            | `[541,35,-2956]`       |
| Lv.20  | Oat |Durum Isles            | `[500,35,-2838]`       |
| Lv.30  | Malt |Durum Isles            | `[385,35,-2836]`       |
| Lv.40  | Hops |Olux Farms             | `[-1630,51,-5428]`     |
| Lv.50  | Rye |Wormhole Farms<br>**Forgotten Burrows**         | `[-2068,53,-5462]`<br>`[-2041,57,-5388]`     |
| Lv.60  | Millet |Forgery Farms<br>**Forgotten Burrows**          | `[-724,44,-5014]`<br>`[-2041,57,-5388]`      |
| Lv.70  | Decay Roots |Forgery Farms          | `[-724,44,-5014]`      |
| Lv.80  | Rice |Hobgoblin Fields       | `[79,42,-4838]`        |
| Lv.90  | Sorghum |Lighthouse Farm        | `[-1378,123,-3013]`    |
| Lv.100 | Hemp |Kandon Caverns         | `[850,40,-4423]`       |
| Lv.110 | Dernic Seed	 |Void Valley Upper      | `[1089,135,-1130]`     |



### Mining
| 等级   | 资源名称 | 地点                   | 坐标                   |
|--------|---|---------------------|------------------------|
| Lv.1   | Copper |Ragni Mine             | `[-572,69,-1556]`      |
| Lv.10  | Granite |Corrupted Mines        | `[786,86,-1242]`       |
| Lv.20  | Gold |Corrupted Mines        | `[685,89,-1217]`       |
| Lv.30  | Sandstone | Bandit Barracks        | `[1478,91,-2178]`      |
| Lv.40  | Iron |Nesaak Mountain Side<br>**Karoc Quarry**   | `[260,89,-700]`<br>`[-1655,76,-4347]`        |
| Lv.50  | Silver | Troms Silver Mine      | `[-620,83,-1009]`      |
| Lv.60  | Cobalt | Olux River Source      | `[-1444,48,-5367]`     |
| Lv.70  | Kanderstone |Prison Caverns         | `[-790,108,-5628]`     |
| Lv.80  | Diamond |Colossus Mines<br>**Maex Mine**          | `[560,120,-4355]`<br>`[1535,61,-5339]`      |
| Lv.90 | Molten | **Maex Mine**<br>Molten Upper Mine    | `[1535,61,-5339]`<br>`[1433,142,-5106]`      |
| Lv.100 | Voidstone | Sky Caverns<br>Kandon Beda Cave   | `[872,34,-4775]`<br>`[850,40,-4423]`       |
| Lv.110 | Dernic | Olmic Mine             | `[492,93,-525]`        |


### Fishing
| 等级   | 资源名称 | 地点                   | 坐标                   |
|--------|-----|-------------------|------------------------|
| Lv.1   | Gudgeon |Ragni Pond             | `[-634,67,-1536]`      |
| Lv.10  | Trout |Wynn Plains River      | `[53,58,-1494]`        |
| Lv.20  | Salmon |Saint’s Row Beach      | `[371,34,-2126]`       |
| Lv.30  | Carp |Desert River Source    | `[1182,154,-2248]`     |
| Lv.40  | Icefish |Nodguj Island          | `[891,34,-3372]`       |
| Lv.50  | Piranha |Iboju Waterfall<br>Forgotten Burrows        | `[-780,74,-724]`<br>`[-2041,57,-5388]`       |
| Lv.60  | Koi |Willow Pond            | `[-1303,51,-5194]`     |
| Lv.70  | Gylia Fish |Lake Gylia             | `[-207,29,-5204]`      |
| Lv.80  | Bass |Relos Coast            | `[-1860,37,-2191]`     |
| Lv.90  | Molten Eel |Molten Heights Lake<br>Maex Mine    | `[1435,139,-5091]`<br>`[1535,61,-5339]`     |
| Lv.100 | Starfish |Kandon Pond Lower      | `[689,88,-4605]`       |
| Lv.110 | Dernic Fish |Toxic Hill Upper       | `[786,148,-983]`       |

### Tools
| 等级 | 地点                  | 花费            |
|------|-----------------------|-----------------|
| Tier.3    | Decrepit Sewers       | 1 Fragment      |
| Tier.4    | Timelost Sanctum      | 2 Fragment      |
| Tier.5    | Sand-Swept Tomb       | 3 Fragment +64e |
| Tier.6    | Ice Barrows           | 4 Fragment +128e|
| Tier.7    | Undergrowth Ruins     | 5 Fragment +256e|
| Tier.8    | Galleon's Graveyard & CDS | 6 Fragment +512e|
| Tier.9    | CIP & CLS             | 7 Fragment +1024e|
| Tier.10   | CUC & CSST            | 8 Fragment +2048e|
| Tier.11   | CIB & CUR & Fallen Factory | 9 Fragment +4096e|
| Tier.12   | Eldritch Outlook      | 9 Fragment +4096e|



:::tip 
本文作者:kotoko
:::