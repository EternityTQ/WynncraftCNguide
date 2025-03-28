<template>
  <div class="skill-container" @mouseover="showTooltip" @mousemove="updateTooltipPosition" @mouseleave="hideTooltip"
    @click.stop="toggleTooltipFixed">

    <div class="skill-name" :style="{ color: categoryColor }">{{ skillData.name }}</div>
    <img :src="skillData.icon" class="skill-icon" />
    <div v-if="tooltipVisible" class="tooltip" ref="tooltip"
      :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }" v-html="skillData.description"></div>
  </div>
</template>

<script>
import skillData from "./data/skills.json";

export default {
  props: ["name"],
  data() {
    return {
      isTooltipFixed: false,
      tooltipVisible: false,
      tooltipTop: 0,
      tooltipLeft: 0,
      fixedPageX: 0,
      fixedPageY: 0,
      categoryColors: {
        "special": "#FF5555",
        "large": "#FF55FF",
        "medium": "ORANGE",
        "small": "white",
        "main": "#00BB00",
        "blue": "#97E6FC",
        "archer_green": "#00BB00",
        "assassin_green": "#00BB00",
        "mage_green": "#00BB00",
        "shaman_green": "#00BB00",
        "warrior_green": "#00BB00",
        "light_green": "#00FF00",
        "dark": "#555555"
      }
    };
  },
  computed: {
    skillData() {
      return skillData[this.name] || {
        name: "未知技能",
        icon: "/assets/unknown.png",
        description: "无描述",
        category: "utility"
      };
    },
    categoryColor() {
      let color = this.categoryColors[this.skillData.category] || "white";
      if (color === "white") {
        color = this.$isDarkmode ? "rgb(208, 208, 217)" : "rgb(60,60,67)";
      }
      return color;
    }
  },
  methods: {
    showTooltip(event) {
      if (!this.skillData.description) return;
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
      if (!this.skillData.description) return;
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

<style>
.skill-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.skill-icon {
  width: 40px;
  height: 40px;
}

.skill-name {
  font-size: 9px;
  font-weight: bold;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  white-space: nowrap;
  width: 100%;
}

.tooltip {
  position: fixed;
  background-color: black;
  color: white;
  padding: 10px;
  border-radius: 5px;
  width: 310px;
  z-index: 9999;

}
</style>