<template><div><p>本来应该放在城镇NPC，但是其实交易市场功能还挺多的，所以单独拎出来说了。</p>
<p>游戏中在部分大城市会有Trade Market的存在<br>
<img src="/assets/img/TM1.jpg" alt="" loading="lazy"></p>
<p>跟其对话就可以打开交易市场的界面了</p>
<figure><img src="/assets/img/TM2.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>首先来从上到下介绍一下右侧的按钮</p>
<h2 id="筛选器-黄色环形箭头" tabindex="-1"><a class="header-anchor" href="#筛选器-黄色环形箭头" aria-hidden="true">#</a> 筛选器(黄色环形箭头)</h2>
<p>可以用于筛选主界面的物品等级</p>
<p>左键来更改等级区间，选定后使用右键来设为默认</p>
<p>设为默认后每次打开都会是这个设置</p>
<h2 id="揭露装备-书与笔" tabindex="-1"><a class="header-anchor" href="#揭露装备-书与笔" aria-hidden="true">#</a> 揭露装备(书与笔)</h2>
<p><s>伟大的揭幕表演！出来吧！Dawnbreak！</s></p>
<p>可以用于将未鉴定的盒子揭露成对应的未鉴定装备</p>
<p>即得知这个盒子装的是什么物品</p>
<p>并且揭露后可以摆上交易市场售卖</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>揭露费用并不算在鉴定费用内</p>
<p>揭露后不能折扣鉴定费用！</p>
</div>
<h2 id="搜索物品-指南针" tabindex="-1"><a class="header-anchor" href="#搜索物品-指南针" aria-hidden="true">#</a> 搜索物品(指南针)</h2>
<p>点击后即可打开搜索物品界面<br>
<img src="/assets/img/TM5.jpg" alt="" loading="lazy"></p>
<p>要说的只有第一个是搜索物品名称，没了！</p>
<p>在搜索物品名称之后是一系列筛选条件，包括物品等级、品质、种类等等</p>
<p>这里就不细讲了，建议最好自己去探索一下搜索条件</p>
<p>学会搜索能让你更快购买到想要的物品！</p>
<p>在搜索后，在右下方同样有一个排序器：<br>
<img src="/assets/img/TM6.jpg" alt="" loading="lazy"></p>
<p>鼠标移上去后就可以看到排序种类了<br>
<img src="/assets/img/TM7.jpg" alt="" loading="lazy"></p>
<p>从上到下分别是：</p>
<ul>
<li>最近上架</li>
<li>最早上架</li>
<li>价格降序</li>
<li>价格升序</li>
<li>等级降序</li>
<li>等级升序</li>
</ul>
<p>用鼠标左键点击该按钮就是下一种排序方法，鼠标右键点击则是上一种排序方法。</p>
<h2 id="出售物品-绿色加号" tabindex="-1"><a class="header-anchor" href="#出售物品-绿色加号" aria-hidden="true">#</a> 出售物品(绿色加号)</h2>
<figure><img src="/assets/img/TM3.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>这里会打开出售界面。</p>
<p>在背包里点击你想要出售的物品，物品就会进入待出售栏中，再点击一下即可取消</p>
<p>绿色加号为出售数量，绿宝石则为设置出售价格，选择后都是在聊天框内输入数值</p>
<p>若想取消可以输入&quot;cancel&quot;来取消输入。</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>不要搞混数量和价格了！</p>
</div>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>若你安装了wynntils，你还可以在输入价格的时候以&quot;<code v-pre>__stx __le __eb</code>&quot;的形式来输入</p>
<p>tils会帮你自动折算为数值填入</p>
<p>举个例子：在输入价格的时候输入<code v-pre>7.5le</code>，则tils会自动帮你填入<code v-pre>30720</code>的数值。</p>
</div>
<p>都确认完毕后点击勾号来确认就可以出售了</p>
<p>如果你不确定价格，你还可以通过查看价格确认(书与笔)来参考价格</p>
<figure><img src="/assets/img/TM4.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>其中紫色的推荐价格为推荐价格(<s>什么废话</s>)</p>
<p>快速出售价格为你挂上去能更快出售的低价</p>
<p>最高求购价格为当前买家正在挂的最高求购的价格(后面会介绍)</p>
<p>最低出售价格则是当前市场上该物品的最低出售价</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>对于下方的Trade Shares，对你来说应该不是特别重要的内容。</p>
<p>如果你实在在意，可以跳到<RouterLink to="/guide/VIP.html#sliverbull-share">这一章</RouterLink>去了解一下</p>
</div>
<div class="hint-container warning">
<p class="hint-container-title">注意</p>
<p>标有untradable和quest的物品无法出售。</p>
</div>
<h2 id="管理交易-绿宝石" tabindex="-1"><a class="header-anchor" href="#管理交易-绿宝石" aria-hidden="true">#</a> 管理交易(绿宝石)</h2>
<figure><img src="/assets/img/TM8.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>这个界面可以查看你在这个市场上出售的物品，并且进行管理。</p>
<p>功能很简单，点击已上架的物品再点击红X就可以将其撤回</p>
<figure><img src="/assets/img/TM9.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>对于空置槽位，左键为出售物品(和上文中出售物品一致)</p>
<p>右键为求购物品</p>
<p>求购方法与上面提到的出售方法相似，不过不同的是，设置价格时设置的是我想要购入的这个物品的最高价格（就是我买这个东西能接受的最高的价格）</p>
<p>小于等于我所设置的价格的物品都会按我设置的数量被我购入，剩余的钱则会返还给我，其他的在这里也不过多赘述。</p>
<div class="hint-container tip">
<p class="hint-container-title">提示</p>
<p>在求购时，如果我们设置的是已鉴定物品的求购</p>
<p>此时若有符合所设置的条件（价格低于我设置的求购价格）的物品</p>
<p>它只会购入与求购一模一样的物品，即鉴定度完全一致</p>
<p>所以如果我挂了一个已鉴定的物品求购，它就只会购入整个游戏中仅有的与求购相同的那一个物品。</p>
</div>
<h2 id="购买物品" tabindex="-1"><a class="header-anchor" href="#购买物品" aria-hidden="true">#</a> 购买物品</h2>
<figure><img src="/assets/img/TM10.jpg" alt="" tabindex="0" loading="lazy"><figcaption></figcaption></figure>
<p>你可以在主界面进行购买物品</p>
<p>注意购买时，买家需要额外支付5%的交易税(有银牛的情况下为2%)</p>
<p>购买时，若存在更低价格的同种物品，会优先购买更低价格的，并且退回多余支付的绿宝石</p>
<p>支付时，若背包内绿宝石不足时，会自动使用银行内的绿宝石</p>
</div></template>


