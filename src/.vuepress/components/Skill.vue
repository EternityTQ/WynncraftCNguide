<template>
    <div
      class="skill-container"
      @mouseover="showTooltip"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
    >
      
      <div class="skill-name" :style="{ color: categoryColor }">{{ skillData.name }}</div>
      <img :src="skillData.icon" class="skill-icon" />
      <div
        v-if="tooltipVisible"
        class="tooltip"
        :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }"
        v-html="skillData.description"
      ></div>
    </div>
  </template>
  
  <script>
  import skillData from "./data/skills.json";
  
  export default {
    props: ["name"],
    data() {
      return {
        tooltipVisible: false,
        tooltipTop: 0,
        tooltipLeft: 0,
        categoryColors: {
          "special": "#FF5555",
          "large": "#FF55FF",
          "medium": "ORANGE",
          "small": "white",
          "main": "#00BB00"
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
        return this.categoryColors[this.skillData.category] || "#FFFFFF";
      }
    },
    methods: {
      showTooltip(event) {
        if (!this.skillData.description) return;
        this.tooltipVisible = true;
        this.updateTooltipPosition(event);
      },
      hideTooltip() {
        this.tooltipVisible = false;
      },
      updateTooltipPosition(event) {
        if (!event) return;
        
        this.$nextTick(() => {
        this.tooltipTop = event.pageY - window.scrollY + 10;
        this.tooltipLeft = event.pageX + 10;
        if (window.innerWidth < window.innerHeight) {
            this.tooltipLeft = 10; // 设定一个适当的左边距
        } else if (event.clientX > window.innerWidth *0.58) {
            this.tooltipLeft -= 330;
        }
        });
      }
    }
  };
  </script>
  
  <style>
.skill-container {
  position: relative;
  display: inline-block;
}
.skill-icon {
  width: 40px;
  height: 40px;
}
.skill-name {
  font-size: 12px;
  font-weight: bold;
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
  