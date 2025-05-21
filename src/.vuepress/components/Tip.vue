<template>
  <span class="tip-container" 
  :class="{ 'tip-highlight': highlight }"
  @mouseover="showTooltip" 
  @mousemove="updateTooltipPosition" 
  @mouseleave="hideTooltip"
    @click.stop="toggleTooltipFixed($event)" style="cursor: pointer;">
    <slot></slot>
    <div v-if="tooltipVisible" ref="tooltip" class="tooltip"
      :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }" v-html="tipData.description"></div>
  </span>
</template>

<script>
import tipData from "./data/tip.json";

export default {
  props: {
    name: {
      type: String,
      required: true
    },
    highlight: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      isTooltipFixed: false,
      tooltipVisible: false,
      tooltipTop: 0,
      tooltipLeft: 0,
      fixedPageX: 0,
      fixedPageY: 0
    };
  },
  computed: {
    tipData() {
      return tipData[this.name] || {
        description: "无描述"
      };
    }
  },
  methods: {
    showTooltip(event) {
      if (!this.tipData.description) return;
      if (!this.isTooltipFixed) this.tooltipVisible = true;
      this.updateTooltipPosition(event);
    },
    hideTooltip() {
      if (!this.isTooltipFixed) this.tooltipVisible = false;
    },
    onMouseLeave() {
      this.hideTooltip();
    },
    toggleTooltipFixed(event) {
      if (!this.tipData.description) return;
      const tooltipEl = this.$refs.tooltip;
      const isMobile = window.innerWidth < 768 || window.innerWidth < window.innerHeight;
      if (tooltipEl && tooltipEl.contains(event.target)&&!isMobile) return;

      this.isTooltipFixed = !this.isTooltipFixed;

      if (this.isTooltipFixed) {
        // 判断是否移动端
        

        if (isMobile) {
          this.fixedPageX = 10;
          this.fixedPageY = event.pageY;
        } else {
          let offsetX = event.pageX + 10;
          if (event.clientX > window.innerWidth * 0.58) {
            offsetX -= 330;
          }
          this.fixedPageX = offsetX;
          this.fixedPageY = event.pageY;
        }

        this.updateTooltipFixedPosition();
      }

      this.tooltipVisible = this.isTooltipFixed;
    },
    updateTooltipFixedPosition() {
      if (this.isTooltipFixed) {
        this.tooltipTop = this.fixedPageY - window.scrollY + 10;
        this.tooltipLeft = this.fixedPageX - window.scrollX + 10;
      }
    },
    handleClickOutside(event) {

      const tooltipEl = document.querySelector(".tooltip");
      console.log("event.target:", event.target);
      const isMobile = window.innerWidth < 768 || window.innerWidth < window.innerHeight;
      if (tooltipEl && tooltipEl.contains(event.target) &&!isMobile) {
        //console.log("点击在 tooltip 内部，不关闭");
        return; // 不隐藏
      }
      this.isTooltipFixed = false;
      this.tooltipVisible = false;

    },
    updateTooltipPosition(event) {
      if (!event || this.isTooltipFixed) return;

      this.$nextTick(() => {
        // 基础位置计算
        let top = event.pageY - window.scrollY + 10;
        let left = event.pageX + 10;

        // 判断是否为手机端（竖屏或较小视口）
        const isMobile = window.innerWidth < 768 || window.innerWidth < window.innerHeight;

        if (isMobile) {
          // 手机端固定在左上角
          this.tooltipTop = top;
          this.tooltipLeft = 10;
        } else {
          // 桌面端右侧显示遮挡处理
          if (event.clientX > window.innerWidth * 0.58) {
            left -= 330; // 向左偏移，避免遮挡
          }
          this.tooltipTop = top;
          this.tooltipLeft = left;
        }
      });
    }

  },
  mounted() {
    this.boundHandleClickOutside = this.handleClickOutside.bind(this);
    document.addEventListener("click", this.boundHandleClickOutside);
    window.addEventListener("scroll", this.updateTooltipFixedPosition);
  },
  beforeDestroy() {
    document.removeEventListener("click", this.handleClickOutside);
    window.removeEventListener("scroll", this.updateTooltipFixedPosition);
  },
};
</script>

<style scoped>
.tooltip {
  position: fixed;
  background: #222;
  color: #BBBBBB;
  padding: 8px;
  border-radius: 5px;
  z-index: 1000;
  max-width: 300px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
  font-size: 14px;

}


.tip-highlight {
  text-decoration: underline;
  text-decoration-color: #3399ff;
  text-underline-offset: 2px;
}
</style>
