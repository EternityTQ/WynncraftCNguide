<template><div><p>粉末类似于镶嵌宝石</p>
<p>粉末一共有地、电、水、火、气五种属性，分别作用于对应的属性</p>
<p>每种粉末的属性一共有六级，其中野外开箱最高仅能开出4级的粉末</p>
<p>5-6级的粉末仅可通过Raid或粉末合成产出</p>
<p>游戏中，绝大多数装备、武器都存在粉末槽(Powder Slot)，可于装备介绍的最底下看到</p>
<p>你可以在任意<RouterLink to="/guide/npcs.html#powder-master">Powder Master</RouterLink>处进行打粉</p>
<p>粉末介绍如下：<br>
<img src="/assets/img/powder2.jpg" alt="" loading="lazy"></p>
<h2 id="给武器添加粉末" tabindex="-1"><a class="header-anchor" href="#给武器添加粉末" aria-hidden="true">#</a> 给武器添加粉末</h2>
<p>给武器添加粉末后，每一个粉末都会将武器原有的中性伤害转换一定比例至粉末对应的属性伤害上，同时增加数点额外的属性伤害</p>
<p>转换比例与额外数值与粉末等级有关，呈正比例相关</p>
<p>当你给武器打了至少2个4级及以上的同种属性粉末时，将会激活武器粉末技能</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>每个武器的粉末技能唯一，无法同时激活不同属性的粉末技能</p>
<p>粉末技能等级只由激活的属性粉末中数值最高的两个来决定</p>
<p>技能等级：</p>
<table>
<thead>
<tr>
<th>4+4</th>
<th>4+5</th>
<th>5+5</th>
<th>5+6</th>
<th>6+6</th>
</tr>
</thead>
<tbody>
<tr>
<td>lvl.1</td>
<td>lvl.2</td>
<td>lvl.3</td>
<td>lvl.4</td>
<td>lvl.5</td>
</tr>
</tbody>
</table>
<p>关于多粉槽粉末如何判定激活何种技能：</p>
<p>只看能达成2个同属性4级以上的粉末，且只看第一个粉末的排序，而不看第一组配对的粉末</p>
<p>举个例子：</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>4水</td>
<td>6地</td>
<td>6地</td>
<td>6电</td>
<td>6电</td>
<td>4电</td>
<td>5水</td>
<td>6水</td>
</tr>
</tbody>
</table>
<p>这种情况下，激活的粉末被动是水属性，因为水属性的第一个粉末排的比地属性和电属性的粉末要前(从左到右)</p>
<p>同时，激活的粉末被动等级为4级(5级水+6级水)</p>
<p><strong>对于下面的装备打粉被动技能，也是同样的机制</strong></p>
</div>
<details class="hint-container details"><summary>武器粉末技能一览</summary>
<p>以下数值数据均为最高等级</p>
<ul>
<li>
<p>地属性：地震<br>
在准星所指目标处释放一次半径为6.5格，伤害倍率为400%的地震，该伤害只会触发一次生命/魔力偷取。</p>
</li>
<li>
<p>电属性：链式闪电<br>
从被攻击到的第一个敌人开始，以300%的伤害倍率在敌人间弹射9次（在只有一个单位时不会弹射），该伤害会多次触发生命/魔力偷取。</p>
</li>
<li>
<p>水属性：诅咒<br>
在准星所指目标处为半径8格范围内所有敌方单位施加30%易伤，持续4秒。</p>
</li>
<li>
<p>火属性：鼓舞<br>
给予自身以及周围友方单位20%的伤害加成并造成一次伤害，增伤持续4秒。</p>
</li>
<li>
<p>气属性：风牢<br>
在准星所指目标处释放一个风牢，将触及的第一个敌方单位禁锢（对大单位如boss无效），并且增加200%其下次受到的伤害，持续5秒，该单位受到任何伤害后将会解除禁锢。</p>
</li>
</ul>
</details>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>弓箭手除了火主动以外，其它所有主动技能都是射出一支带有技能的箭出去后，（该箭矢下坠很严重）</p>
<p>在箭矢落地或命中目标后释放技能，如地震可以距离目标较远时发动。</p>
</div>
<h2 id="给装备添加粉末" tabindex="-1"><a class="header-anchor" href="#给装备添加粉末" aria-hidden="true">#</a> 给装备添加粉末</h2>
<p>给装备添加粉末后，每一个粉末都会增加对应属性的元素防御，同时减少另一个指定元素防御</p>
<p>数值与粉末等级呈正相关</p>
<p>类似地，给装备添加2个4级及以上的同属性粉末可以触发粉末被动，判定机制与武器粉末技能相同</p>
<p>被动技能的效果为满足条件后，给自身增加<mark>指定元素的元素伤害</mark></p>
<p>多个被动技能可以叠加效果(见下文具体效果)</p>
<details class="hint-container details"><summary>装备粉末被动技能一览</summary>
<p>以下数值数据均为最高等级粉末</p>
<ul>
<li>
<p>地属性：愤怒<br>
每损失1%的生命值，获得1%的地属性伤害加成，<strong>从最大生命值的75%处才开始从零计算</strong><br>
多个地属性被动叠加将会增加伤害加成上限</p>
</li>
<li>
<p>电属性：连杀<br>
每杀死1个怪物，获得9%的电属性伤害加成，总上限为150%，每层加成独立计算5s持续时间<br>
多个电属性被动叠加将会增加叠加速度</p>
</li>
<li>
<p>水属性：专注<br>
每消耗1点mana，获得0.25%的水属性伤害加成，总上限为100%<br>
每次消耗mana时，消耗值即为该层持续时间(秒)<br>
多个水属性被动叠加将会增加叠加速度</p>
</li>
<li>
<p>火属性：坚韧<br>
每次受击后，获得6%的火属性伤害加成，总上限为100%<br>
每层持续时间为8s<br>
多个火属性被动叠加将会增加叠加速度</p>
</li>
<li>
<p>气属性：闪避<br>
处在怪物周围且没有受到非闪避伤害时，每秒增加6%的气属性伤害，总上限为150%<br>
每层持续时间为60s，受到非闪避伤害后立即清空所有加成<br>
多个气属性被动叠加将会增加叠加速度</p>
</li>
</ul>
</details>
<h2 id="粉末合成" tabindex="-1"><a class="header-anchor" href="#粉末合成" aria-hidden="true">#</a> 粉末合成</h2>
<p>你可以在Powder Master处将4个低级粉末合成为高一级的粉末</p>
<figure><img src="/assets/img/powder4.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>在升级时，注意两点：</p>
<p>一、不管四个粉末等级多少，能合成出来的粉末等级只可能是这其中最低粉末的等级+1</p>
<p>二、添加不同属性的粉末时，合成出来的粉末属性为这其中不同属性的配比的概率随机</p>
<figure><img src="/assets/img/powder3.jpg" alt="这两条规则看这张图应该就能看明白了.jpg" tabindex="0" loading="lazy"><figcaption>这两条规则看这张图应该就能看明白了.jpg</figcaption></figure>
</div></template>


