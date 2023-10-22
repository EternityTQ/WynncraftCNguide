<template><div><div class="hint-container warning">
<p class="hint-container-title">待施工的页面！</p>
<p>此页面内容尚在施工</p>
<p>请知悉！</p>
</div>
<h2 id="学会看懂装备词条" tabindex="-1"><a class="header-anchor" href="#学会看懂装备词条" aria-hidden="true">#</a> 学会看懂装备词条</h2>
<p>对于一件装备，我们拿到之后应该先看什么东西呢？接下来我会以几件装备为例子详细展开说明</p>
<p>建议安装wynntils这个模组，因为可以查看词条的鉴定度，非常方便。先以武器为例：</p>
<figure><img src="/assets/img/id1.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<ul>
<li>①：武器的名称，右侧百分比为Wynntils的功能，代表武器的总鉴定度</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>物品名称的颜色与物品品质有关</p>
</div>
<ul>
<li>②：武器的原始攻速(可被攻速词条影响)</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>每级的攻击间隔如下:<br>
Super Fast: 4.3<br>
Very Fast: 3.1<br>
Fast: 2.5<br>
Normal: 2.05<br>
Slow: 1.5<br>
Very Slow: 0.83<br>
Super Slow: 0.51</p>
</div>
<ul>
<li>③：代表这个武器的面板，即元素种类、攻击力以及折算后的平均输出(DPS——Damage Per Second)</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>绝大部分武器在原始形态都持有Neutral Damage，即中性伤害<br>
中性伤害可以被粉末转化为对应的元素伤害</p>
</div>
<ul>
<li>④：武器需求，一般包括职业需求、等级需求以及属性点需求。部分武器还会有任务需求，即完成对应任务才能使用</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">关于装备需求的解释</p>
<p>Class Req: 职业需求，一般只出现在武器上</p>
<p>Combat Lv. Min: 等级需求，只看战斗等级</p>
<p>Str/Dex/Int/Def/Agi Min: 属性点需求，你在指南针内的加点与<strong>装备提供</strong>的属性点总和需不小于这个数值</p>
<p>Quest Req: 任务需求，通常为任务奖励，需要完成该任务才可以装备/使用</p>
</div>
<ul>
<li>⑤：武器词条，最关键的部分。这些词条的数值会被鉴定所影响，在安装了wynntils模组后，按住shift则可以看到这些词条的浮动范围。</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">关于词条作用</p>
<p>可以看看<RouterLink to="/guide/identification.html">这一章</RouterLink></p>
</div>
<ul>
<li>⑥：武器粉槽，代表这个武器至多能装备多少个粉末</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">关于粉末系统</p>
<p>可以看看<RouterLink to="/guide/basesystem/powder.html">这一章</RouterLink></p>
</div>
<ul>
<li>⑦：武器的品质，右侧的数字为鉴定费用</li>
</ul>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>在重新鉴定后，品质右侧将会出现数字，代表这件装备被重新鉴定了几次</p>
</div>
<p>在武器最下方一般还会有介绍，讲述了该件装备/武器的历史<br>
<s>萨满武器没有介绍</s></p>
<p>对于装备而言就不过多占篇幅介绍了，区别就在装备一般会有血量属性和元素防御属性，很好理解，元素防御会在下文介绍。</p>
<h2 id="装备品质" tabindex="-1"><a class="header-anchor" href="#装备品质" aria-hidden="true">#</a> 装备品质</h2>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>待更新</p>
</div>
<h2 id="元素防御" tabindex="-1"><a class="header-anchor" href="#元素防御" aria-hidden="true">#</a> 元素防御</h2>
<p>护甲是带有基础元素防御的属性的，这些防御可以用来为我们提供对应元素伤害的抗性</p>
<p>但与加点系统的防御点不同，元素防御如果是负数，则会增加自身受到那种元素属性的伤害</p>
<p>所以在配置装备时，我们最好不要将元素防御负太多</p>
<p>否则一遇到对应元素的伤害，我们将会变得及其脆弱。</p>
<p>以一个非常经典的装备为例：</p>
<figure><img src="/assets/img/id2.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>我们可以看到，这件装备的水属性防御是-850<br>
也就是说，穿着这件装备的时候，我们会大幅度增加自己受到的水属性伤害。</p>
<div class="hint-container tip">
<p class="hint-container-title">关于元素防御%</p>
<p>假设我们的元素防御数值是负数，若我们通过装备获得了高于100%的对应元素防御加成，此时我们的元素防御值会变成0。</p>
<p>反过来也一样，当我们此时的元素防御数值是正数，若我们通过装备获得了低于-100%的对应元素防御加成，此时我们的元素防御值同样会变成0。</p>
<p>依然以上面的这件装备为例子，我们可以看到这件装备对于地属性防御的加成是500%<br>
假设此时我们的地属性防御数值在其他装备的影响下变成了负数，那我们最后得到的地属性防御数值就是0。</p>
</div>
</div></template>


