<template>
  <span 
    class="copy-coord" 
    @click="copyText"
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
    async copyText() {
      try {
        // 使用更稳健的DOM文本获取方式
        text = this.$el.textContent.trim(); // 获取元素内所有文本
        text = text.slice(2,-1);
        await navigator.clipboard.writeText(text);
        
        this.showFeedback = true;
        // 更新提示文字
        this.currentLabel = "✓ 已复制到剪贴板";
        //this.aria-label="已复制";
        setTimeout(() => {
          this.currentLabel = this.hoverTip;
        }, this.feedbackDuration + 500); // 稍晚于反馈消失
        
        setTimeout(() => (this.showFeedback = false), this.feedbackDuration);
        
      } catch (err) {
        this.fallbackCopy();
      }
    },
    fallbackCopy() {
      // 统一使用DOM获取文本
      const text = this.$el.textContent.trim();
      const temp = document.createElement('textarea');
      
      let str = text;
      str=str.slice(1,-1);
      str='/compass at '+str;
      temp.value = str;
      //temp=temp.slice(1,-1);
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
.copy-coord {
  /* 基础样式 */
  cursor: copy;
  position: relative;
  display: inline-block;
  padding: 2px 4px;
  border-radius: 4px;
  font-size: 0.85em;
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