<template><div>  <div>
    <img
      src="/assets/img/class/archer_green.png"
      alt="Your Image"
      @mouseover="showTooltip"
      @mousemove="updateTooltipPosition"
      @mouseleave="hideTooltip"
    />
    <div v-if="isTooltipVisible" class="tooltip" :style="{ top: tooltipTop + 'px', left: tooltipLeft + 'px' }">
      <!-- Your tooltip content goes here -->
            Test
    </div>
  </div>
</div></template>

<script>
export default {
  data() {
    return {
      isTooltipVisible: false,
      tooltipTop: 0,
      tooltipLeft: 0
    };
  },
  methods: {
    showTooltip(event) {
      this.updateTooltipPosition(event);
      this.isTooltipVisible = true;
    },
    updateTooltipPosition(event) {
      this.tooltipTop = event.clientY + 10; // Adjust the offset as needed
      this.tooltipLeft = event.clientX + 10; // Adjust the offset as needed
    },
    hideTooltip() {
      this.isTooltipVisible = false;
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