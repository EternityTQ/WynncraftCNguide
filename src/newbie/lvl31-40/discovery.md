---
title: 探索区域
icon: map
---


this.tooltipTop = event.pageY + 10; // 根据需要调整偏移量
      this.tooltipLeft = event.pageX + 10; // 根据需要调整偏移量


       if (event.clientX > window.innerWidth / 2 && this.$refs.tooltip) {
        this.tooltipLeft = event.pageX-this.$refs.tooltip.clientWidth - 100; // 20为调整的偏移量
      }