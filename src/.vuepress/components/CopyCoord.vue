<template>
  <span 
    class="copy-coord" 
    @click="copyText"
    :data-current-label="currentLabel"
    :aria-label="currentLabel"
    :style="{
      backgroundColor: $isDarkmode ? 'rgb(39, 42, 47)' : '#f3f4f6',
      color: $isDarkmode ? 'rgb(208, 208, 217)' : '#374151',
      borderColor: $isDarkmode ? 'rgba(255,255,255,0.1)' : '#e5e7eb'
    }"
  >
    <slot />
  </span>
</template>

<script>
export default {
  data() {
    return {
      currentLabel: "点击复制坐标",
      hoverTip: "点击复制坐标",
      feedbackDuration: 1000
    };
  },
  methods: {
    async copyText() {
      try {
        // 更精准获取坐标文本（处理可能存在的子元素）
        const text = this.$el.textContent.trim();
      const temp = document.createElement('textarea');
      let str = text;
      str=str.slice(1,-1);
      str='/compass at '+str;
      temp.value = str;
      
      temp.value = str;
      document.body.appendChild(temp);
      temp.select();
      document.execCommand('copy');
      document.body.removeChild(temp);
        this.currentLabel = "已复制 ✅";
        setTimeout(() => this.currentLabel = this.hoverTip, 1500);
        
      } catch (err) {
        const text = this.$el.textContent.trim();
      const temp = document.createElement('textarea');
      let str = text;
      str=str.slice(1,-1);
      str='/compass at '+str;
      temp.value = str;
      
      temp.value = str;
      document.body.appendChild(temp);
      temp.select();
      document.execCommand('copy');
      document.body.removeChild(temp);
        this.currentLabel = "已复制 ✅";
        setTimeout(() => this.currentLabel = this.hoverTip, 1500);
      }
    }
  }
}
</script>

<style scoped>
.copy-coord {
  cursor: copy;
  position: relative;
  display: inline-block;
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 0.85em;
  transition: all 0.2s ease;
  border: 2px solid #e5e7eb;

  /* 动态气泡样式 */
  &::after {
    content: attr(data-current-label);
    position: absolute;
    bottom: 120%;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.9);
    color: white;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.75em;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  }

  &:hover::after {
    opacity: 1;
  }

  /* 深色模式适配 */
  .dark-mode &::after {
    background: rgba(255,255,255,0.9);
    color: #1a1a1a;
  }

  /* 点击动画 */
  &:active {
    transform: scale(0.95);
  }
}
</style>