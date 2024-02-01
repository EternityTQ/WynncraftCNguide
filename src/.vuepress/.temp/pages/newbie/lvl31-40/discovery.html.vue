<template><div><p>this.tooltipTop = event.pageY + 10; // 根据需要调整偏移量<br>
this.tooltipLeft = event.pageX + 10; // 根据需要调整偏移量</p>
<pre><code>   if (event.clientX &gt; window.innerWidth / 2 &amp;&amp; this.$refs.tooltip) {
    this.tooltipLeft = event.pageX-this.$refs.tooltip.clientWidth - 100; // 20为调整的偏移量
  }
</code></pre>
</div></template>


