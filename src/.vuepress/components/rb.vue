<template>
  <span class="rainbow-text">
    <slot></slot>
  </span>
</template>

<script>
export default {
  name: 'RainbowText'
}
</script>

<style scoped>
.rainbow-text {
  /* 定义红橙黄绿青蓝紫的线性渐变，并在末尾补一个红色以实现无缝循环 */
  background-image: linear-gradient(
    90deg, 
    #ff0000, 
    #ff7f00, 
    #FFCC00, 
    #00BB00, 
    #00CCFF, 
    #0000ff, 
    #8b00ff, 
    #ff0000
  );
  
  /* 将背景宽度拉长到 200%，这样动画平移时才有足够的空间 */
  background-size: 200% 100%;
  
  /* 将背景裁剪至文本轮廓 */
  -webkit-background-clip: text;
  background-clip: text;
  
  /* 将文字本身的颜色设为透明，让背景色透出来 */
  color: transparent;
  -webkit-text-fill-color: transparent;
  
  /* 应用动画：3秒完成一次循环，匀速(linear)，无限循环(infinite) */
  animation: rainbow-flow 3s linear infinite;
  
  /* 确保组件在行内显示，同时不破坏原有排版 */
  display: inline;
}

/* 定义背景平移动画 */
@keyframes rainbow-flow {
  0% {
    background-position: 0% 50%;
  }
  100% {
    /* 向左平移整个背景的一半长度(即100%)，配合首尾相同的红色实现完美衔接 */
    background-position: -200% 50%;
  }
}
</style>