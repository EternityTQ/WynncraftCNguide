<template>
  <span 
    class="copy-context" 
    @click="copyContext"
    :title="hoverTip"
    aria-label="点击复制"
    currentLabel="已复制 √"
    data-balloon-pos="up"
  >
    <slot /> <!-- 显示坐标文本 -->
    <span v-if="showFeedback" class="feedback">{{ feedbackText }}</span>
  </span>
</template>

<script>
export default {
  methods: {
    async copyContext() {
      try {
        const text = this.$el.textContent.trim();
      const temp = document.createElement('textarea');
      
      
      temp.value = text;
      document.body.appendChild(temp);
      temp.select();
      document.execCommand('copy');
      document.body.removeChild(temp);
      
      this.feedbackText = "⚠️ 手动复制吧!";
      this.showFeedback = true;
      setTimeout(() => (this.showFeedback = false), 2500);
        
      } catch (err) {
        this.fallbackCop();
      }
    },
    fallbackCop() {
      // 统一使用DOM获取文本
      const text = this.$el.textContent.trim();
      const temp = document.createElement('textarea');
      
      
      temp.value = text;
      document.body.appendChild(temp);
      temp.select();
      document.execCommand('copy');
      document.body.removeChild(temp);
      
      this.feedbackText = "⚠️ 手动复制吧!";
      this.showFeedback = true;
      setTimeout(() => (this.showFeedback = false), 2500);
    }
  }
}
</script>

<style scoped>
.copy-context {
  /* 基础样式 */
  cursor: copy;
  position: relative;
  display: inline-block;
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 1em;
  transition: all 0.2s ease;
  
  /* 浅灰色背景 */
  background-color: #f3f4f6;
  color: #374151;
  border: 1px solid #e5e7eb;

  /* 提示气泡 */
  &::after {
    content: attr(aria-label);
    position: absolute;
    bottom: 80%;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(0,0,0,0.85);
    color: white;
    padding: 3px 6px;
    border-radius: 2px;
    font-size: 0.85em;
    white-space: nowrap;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
  }
  transform: scale(1);
  transition: transform 0.1s;

  &:active {
    transform: scale(0.95); /* 点击时轻微缩小 */
  }

  &:hover {
    background-color: #e5e7eb; /* 深灰色 */
    border-color: #d1d5db;

    &::after {
      opacity: 1; /* 显示提示 */
    }
  }
}



.feedback {
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(0,0,0,0.8);
  color: white;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 0.8em;
  white-space: nowrap;
}
</style>