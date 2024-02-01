<template><div><div class="hint-container danger">
<p class="hint-container-title">警告</p>
<p>这个页面被暂时用作测试页面了</p>
<p>请知悉:(</p>
</div>
<p>1111</p>
<div>
    <!-- 第一张图片 -->
    <img
      src="/assets/img/class/archer_green.png"
      alt="Your Image"
      @mouseover="showTooltip('箭弹')"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
    />
    <div v-if="isTooltipVisible && currentTooltip === '箭弹'" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 提示文本内容 -->
      <font color="#00BB00"><b>箭弹</b></font>
      <br><font color="ORANGE">使用连招：</font><font color="#FF55FF"> 左键 - 右键 - 右键</font>
      <br>
    </div>
  </div>
<div>
    <img
      src="/assets/img/class/another_image.png"
      alt="Another Image"
      @mouseover="showTooltip('another')"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
    />
    <div v-if="isTooltipVisible && currentTooltip === 'another'" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- 另一种提示文本内容 -->
      <font color="#FF0000"><b>另一种能力</b></font>
      <br><font color="BLUE">另一种连招：</font><font color="#FFFF00"> 按键1 - 按键2 - 按键3</font>
      <br>
    </div>
  </div>
</div></template>

<script>
export default {
  data() {
    return {
      isTooltipVisible: false,
      currentTooltip: '',
      tooltipTop: 0,
      tooltipLeft: 0
    };
  },
  methods: {
    showTooltip(tooltipName) {
      this.currentTooltip = tooltipName;
      this.updateTooltipPosition(event);
      this.isTooltipVisible = true;
    },
    hideTooltip() {
      this.isTooltipVisible = false;
      this.currentTooltip = '';
    },
    updateTooltipPosition(event) {
      this.tooltipTop = event.pageY + 10; // 根据需要调整偏移量
      this.tooltipLeft = event.pageX + 10; // 根据需要调整偏移量
    }
  }
};
</script>

<style scoped>
.tooltip {
  position: absolute;
  background-color: black;
  color: white;
  padding: 10px;
  border-radius: 5px;
}
</style>