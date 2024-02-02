---
title: 技能树填写格式转换快速复制
icon: gamepad
---

绿色能力点：58
小能力点：46
中能力点：52
大能力点：54
红能力点：54


```md
<div class="advanced-tooltip ability-tree-icon-1 tooltips-init-complete"><div class="center"><div class="floatnone"><img alt="Ability 1" src="/assets/img/class/medium.png" decoding="async" loading="lazy" width="52" height="52" data-image-name="Ability 1.png" data-image-key="Ability_1.png" data-relevant="0" data-src="/assets/img/class/medium.png" class=" ls-is-cached lazyloaded"></div></div></div>
```
↓
```md
<img src="/assets/img/class/medium.png" width="52" height="52" >
```
//////////////////////////////////////////////
```md
<div class="advanced-tooltip ability-tree-icon-0 tooltips-init-complete"><div class="center"><div class="floatnone"><img alt="Ability 0" src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/e/e8/Ability_0.png/revision/latest?cb=20220907152154" decoding="async" loading="lazy" width="46" height="46" data-image-name="Ability 0.png" data-image-key="Ability_0.png" data-relevant="0"></div></div></div>
```

↓

```md
<img src="/assets/img/class/small.png" width="46" height="46" >
```
//////////////////////////////////////////////
```md
<div class="ability-tree-branch"><img alt="Branch 4" src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/4/4c/Branch_4.png/revision/latest?cb=20220907194920" decoding="async" loading="lazy" width="40" height="40" data-image-name="Branch 4.png" data-image-key="Branch_4.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/4/4c/Branch_4.png/revision/latest?cb=20220907194920" class=" ls-is-cached lazyloaded"></div>
```

↓

```md
<img src="/assets/img/class/左下.png" width="40" height="40" >
```
//////////////////////////////////////////////
```md
<div class="ability-tree-branch"><img alt="Branch 2" src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/2/2d/Branch_2.png/revision/latest?cb=20220907194915" decoding="async" loading="lazy" width="40" height="40" data-image-name="Branch 2.png" data-image-key="Branch_2.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/2/2d/Branch_2.png/revision/latest?cb=20220907194915" class=" ls-is-cached lazyloaded"></div>
```

↓

```md
<img src="/assets/img/class/丁字.png" width="40" height="40" >
```
//////////////////////////////////////////////
```md
<div class="ability-tree-branch"><img alt="Branch 3" src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/0/0a/Branch_3.png/revision/latest?cb=20220907194917" decoding="async" loading="lazy" width="40" height="40" data-image-name="Branch 3.png" data-image-key="Branch_3.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/wynncraft_gamepedia_en/images/0/0a/Branch_3.png/revision/latest?cb=20220907194917" class=" ls-is-cached lazyloaded"></div>
```

↓

```md
<img src="/assets/img/class/右下.png" width="40" height="40" >
```
/////////////////////////////////
```vue
<img
      src="/assets/img/class/archer_green.png"
      alt="Your Image"
      @mouseover="showTooltip('箭弹')"
      @mousemove="updateTooltipPosition($event)"
      @mouseleave="hideTooltip"
      class="t48"
      @click.prevent="handleClick"
    />
    <div v-if="isTooltipVisible && currentTooltip === '箭弹'" ref="tooltip" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color="#00BB00"><b>箭弹</b></font>
      <br>
      <br><font color="ORANGE">使用连招：</font><font color="#FF55FF"> 左键 - 右键 - 右键</font>
      <br><font color = BBBBBB>射出一支远距离的箭矢，其命中后会爆炸，并在大范围内造成伤害。</font><font color = 555555><br>(并对自己造成爆炸伤害10%的伤害)</font>
      <br>
      <br><font color = BBBBBB>蓝耗：<font color=white>45</font>
      <br>范围：<font color=white>26格</font>
      <br>爆炸范围：<font color=white>4.5格</font></font>
    </div>
```

```vue
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
      <font color="#FFFFFF"><b>逃脱减耗I</b></font>
      <br>
      <br><font color = BBBBBB><u>逃脱</u>的技能消耗<font color = FFFFFF>-5</font></font>
    </div>
```

```vue
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
      <br><font color = BBBBBB>当攻击到<font color=WHITE> 5格以外 </font>的敌人时，获得一层<font color=aqua>专注值</font>(上限3层，1.1秒的获得冷却)
      <br><font color=555555>当攻击空箭时，失去所有已叠加的专注值</font>
      <br>
      <br>伤害加成：<font color=WHITE>+15%</font><font color=555555>(每层专注值)</font>
      <br>
      <br><font color= FF55FF><b>鹰眼射手 分支</b></font></font>
      <br>
      <br><font color=00FF00>备注</font>
      <br><font color = BBBBBB><u>幻影射线</u>只需要命中一次敌人就不会丢失专注值。
      <br><u>箭弹</u>必须要直接击打到敌人才不会丢失专注值。
      <br>随从的攻击无法给自身叠加专注值。
      <br>类似<u>箭雨滂沱</u>的技能，一旦有一根箭矢空箭了，就算作一次失误。</font>
    </div>
    ```