<template>
  <span class="tip-container" 
  :class="{ 'tip-highlight': highlight }"
  @mouseover="showTooltip" 
  @mousemove="updateTooltipPosition" 
  @mouseleave="hideTooltip"
    @click.stop="toggleTooltipFixed($event)" style="cursor: pointer;">
    
    <span ref="slotContent"><slot></slot></span>
    
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
      // 2. 移除 required: true，改为默认空字符串
      default: "" 
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
      fixedPageY: 0,
      // 3. 新增变量，用于存储从插槽中提取的文本
      autoName: "" 
    };
  },
  computed: {
    // 4. 新增计算属性：决定最终使用哪个词去查 JSON
    actualName() {
      // 优先使用传入的 name，如果没传，则使用自动提取的 autoName
      return this.name || this.autoName;
    },
    tipData() {
      // 5. 改用 actualName 匹配数据
      return tipData[this.actualName] || {
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
      const isMobile = window.innerWidth < 768 || window.innerWidth < window.innerHeight;
      if (tooltipEl && tooltipEl.contains(event.target) &&!isMobile) {
        return; 
      }
      this.isTooltipFixed = false;
      this.tooltipVisible = false;
    },
    updateTooltipPosition(event) {
      if (!event || this.isTooltipFixed) return;

      this.$nextTick(() => {
        let top = event.pageY - window.scrollY + 10;
        let left = event.pageX + 10;

        const isMobile = window.innerWidth < 768 || window.innerWidth < window.innerHeight;

        if (isMobile) {
          this.tooltipTop = top;
          this.tooltipLeft = 10;
        } else {
          if (event.clientX > window.innerWidth * 0.58) {
            left -= 330; 
          }
          this.tooltipTop = top;
          this.tooltipLeft = left;
        }
      });
    },
    // 提取文本的逻辑封装，方便复用
    extractSlotText() {
      if (!this.name && this.$refs.slotContent) {
        // 获取纯文本并去除首尾可能存在的空格与换行
        this.autoName = (this.$refs.slotContent.textContent || "").trim();
      }
    }
  },
  mounted() {
    this.boundHandleClickOutside = this.handleClickOutside.bind(this);
    document.addEventListener("click", this.boundHandleClickOutside);
    window.addEventListener("scroll", this.updateTooltipFixedPosition);

    // 6. 组件挂载时提取一次文本
    this.$nextTick(() => {
      this.extractSlotText();
    });
  },
  updated() {
    // 7. （可选）如果你中间的文本是响应式动态渲染的，例如 <tip>{{ dynamicVar }}</tip>，确保文本更新时 autoName 也更新
    this.extractSlotText();
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