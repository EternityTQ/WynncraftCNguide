---
title: 技能树填写格式转换快速复制
icon: gamepad
---
1

```vue
<div style="text-align: center;margin-top:-10px;margin-bottom: -3px;font-size: 3px;white-space: nowrap;">
    <!-- Add the following line for the centered text -->
    <font color="#00BB00">爆炸箭</font></div>
<img
      src="/assets/img/class/archer_green.png"
      alt="Your Image"
      @mouseover="showTooltip('爆炸箭')"
      @mousemove="updateTooltipPosition($event)"
      @mouseleave="hideTooltip"
      class="t48"
      @click.prevent="handleClick"
    />
    <div v-if="isTooltipVisible && currentTooltip === '爆炸箭'" ref="tooltip" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color="#00BB00"><b>爆炸箭</b></font>
      <br><font color="ORANGE">使用连招：</font><font color="#FF55FF"> 左键 - 右键 - 右键</font>
      <br>
      <br><font color = BBBBBB>射出一支远距离的箭矢，其命中后会爆炸，并在大范围内造成伤害。</font><font color = 555555><br>(并对自己造成爆炸伤害10%的伤害)</font>
      <br>
      <br><font color = BBBBBB>蓝耗：<font color=white>45</font>
      <br>范围：<font color=white>26格</font>
      <br>爆炸范围：<font color=white>4.5格</font></font>
    </div>
```

```vue
<div style="text-align: center;margin-top:-10px;margin-bottom: -3px;font-size: 3px;white-space: nowrap;text-shadow: 1px 1px 1px black;">
    <!-- Add the following line for the centered text -->
    <font color="white">逃脱减耗 I</font></div>
<img
      src="/assets/img/class/small.png"
      alt="Your Image"
      @mouseover="showTooltip('逃脱减耗1')"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
      style="width: 46px; height: 46px;"
    />
    <div v-if="isTooltipVisible && currentTooltip === '逃脱减耗1'" ref="tooltip" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color="#FFFFFF"><b>逃脱减耗 I</b></font>
      <br>
      <br><font color = BBBBBB><u>逃脱</u>的技能消耗<font color = FFFFFF> -5</font></font>
    </div>
```

```vue
<div style="text-align: center;margin-top:-10px;margin-bottom: -3px;font-size: 3px;white-space: nowrap;">
    <!-- Add the following line for the centered text -->
    <font color="ORANGE">碎心</font></div>
<img
      src="/assets/img/class/medium.png"
      alt="Your Image"
      @mouseover="showTooltip('碎心')"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
      style="width: 46px; height: 46px;"
    />
    <div v-if="isTooltipVisible && currentTooltip === '碎心'" ref="tooltip" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color="ORANGE"><b>碎心</b></font>
      <br>
      <br><font color = BBBBBB><u>箭弹</u>的箭矢直接攻击到敌人时，造成额外伤害</font>
    </div>
```


```vue
 <div style="text-align: center;margin-top:-10px;margin-bottom: -3px;font-size: 3px;white-space: nowrap;">
    <!-- Add the following line for the centered text -->
    <font color=FF55FF>全神贯注</font></div>
<img
      src="/assets/img/class/large.png"
      alt="Your Image"
      @mouseover="showTooltip('幻影射线')"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
      style="width: 46px; height: 46px;"
    />
    <div v-if="isTooltipVisible && currentTooltip === '幻影射线'" ref="tooltip" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color=FF55FF><b>幻影射线</b></font>
      <br>
      <br><font color = BBBBBB>将<u>箭雨</u>浓缩为一条射线，对敌人造成<font color=WHITE>10次</font>伤害</font>
      <br>
      <br><font color = BBBBBB>蓝耗：<font color=white>-5</font>
      <br>范围：<font color = white>16格</font>
      <br>持续时间：<font color = white>1.2秒</font></font>
    </div>
```


 ```vue
 <div style="text-align: center;margin-top:-10px;margin-bottom: -3px;font-size: 3px;white-space: nowrap;">
    <!-- Add the following line for the centered text -->
    <font color=FF5555>全神贯注</font></div>
<img
      src="/assets/img/class/special.png"
      alt="Your Image"
      @mouseover="showTooltip('全神贯注')"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
      style="width: 46px; height: 46px;"
    />
    <div v-if="isTooltipVisible && currentTooltip === '全神贯注'" ref="tooltip" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color=FF5555><b>全神贯注</b></font>
      <br>
      <br><font color = BBBBBB>当攻击到<font color=WHITE> 5格以外 </font>的敌人时，获得一层<font color=aqua>专注值</font>
      <br>
      <br>伤害加成：<font color=WHITE>+15%</font><font color=555555>(每层专注值)</font>
      <br>
      <br><font color= FF55FF><b>鹰眼射手 分支</b></font></font>
      <br>
      <br><font color=00FF00>备注</font>
      <br><font color = BBBBBB><u>幻影射线</u>只需要命中一次敌人就不会丢失专注值。</font>
    </div>
```
<img src="/assets/img/class/small.png">

白色

<img src="/assets/img/class/medium.png">

黄色

<img src="/assets/img/class/large.png">

粉色

<img src="/assets/img/class/special.png">

红色


战士：

<font color=RED><b>腐化者</b></font>

<font color=FFFF55><b>武道士</b></font>

<font color=18c7f0><b>圣骑士</b></font>

法师：
<font color=55FFFF><b>时空行者 分支</b></font>

<font color=WHITE><b>圣光使者 分支</b></font>

<font color=AA00AA><b>奥术法师 分支</b></font>

弓手：
<font color=FFFF55><b>闪击射手 分支</b></font>

<font color=00AA00><b>陷阱射手 分支</b></font>

<font color=FF55FF><b>鹰眼射手 分支</b></font>

刺客：
<font color=AA0000><b>影步者 分支</b></font>

<font color=FF55FF><b>幻术师 分支</b></font>

<font color=WHITE><b>身法刺 分支</b></font>

萨满：
<font color="orange"><b>召唤师 分支</b></font>

<font color=16d108><b>圣祭祀 分支</b></font>

<font color="red"><b>血教徒 分支</b></font>