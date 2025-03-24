<template>
    <span
      class="tip-container"
      @mouseover="showTooltip"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
      @click.stop="toggleTooltipFixed($event)"
      style="text-decoration: underline; cursor: pointer;"
    >
      <slot></slot>
      <div
        v-if="tooltipVisible"
        ref="tooltip"
        class="tooltip"
        :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }"
        v-html="tipData.description"
      ></div>
    </span>
  </template>
  
  <script>
  import tipData from "./data/tip.json";
  
  export default {
    props: {
      name: {
        type: String,
        required: true
      }
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
        
  console.log("触发 showTooltip", this.name, this.tipData);
        if (!this.isTooltipFixed) {
          this.tooltipVisible = true;
          this.updateTooltipPosition(event);
        }
      },
      hideTooltip() {
        if (!this.isTooltipFixed) {
          this.tooltipVisible = false;
        }
      },
      updateTooltipPosition(event) {
        if (this.isTooltipFixed) return;
        this.tooltipTop = event.clientY + 10;
        this.tooltipLeft = event.clientX + 10;
      },
      updateTooltipFixedPosition() {
        if (this.isTooltipFixed) {
          this.tooltipTop = this.fixedPageY - window.scrollY + 10;
          this.tooltipLeft = this.fixedPageX - window.scrollX + 10;
        }
      },
      toggleTooltipFixed(event) {
        const tooltipEl = this.$refs.tooltip;
        if (tooltipEl && tooltipEl.contains(event.target)) return;
  
        this.isTooltipFixed = !this.isTooltipFixed;
  
        if (this.isTooltipFixed) {
          this.fixedPageX = event.pageX;
          this.fixedPageY = event.pageY;
          this.updateTooltipFixedPosition();
        }
  
        this.tooltipVisible = this.isTooltipFixed;
      },
      handleClickOutside(event) {
        const tooltipEl = this.$refs.tooltip;
        if (tooltipEl && tooltipEl.contains(event.target)) return;
        this.isTooltipFixed = false;
        this.tooltipVisible = false;
      }
    },
    mounted() {
      this.boundClickOutside = this.handleClickOutside.bind(this);
      document.addEventListener("click", this.boundClickOutside);
      window.addEventListener("scroll", this.updateTooltipFixedPosition);
    },
    beforeDestroy() {
      document.removeEventListener("click", this.boundClickOutside);
      window.removeEventListener("scroll", this.updateTooltipFixedPosition);
    }
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
    box-shadow: 0 0 5px rgba(0,0,0,0.3);
    font-size: 14px;
  }
  </style>
  