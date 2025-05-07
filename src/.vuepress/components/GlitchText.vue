<!-- GlitchText.vue -->
<template>
    <span>
      <span v-for="(char, index) in displayText" :key="index">{{ char }}</span>
    </span>
  </template>
  
  <script setup>
  import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
  
  const props = defineProps({
    text: {
      type: String,
      required: true
    },
    speed: {
      type: Number,
      default: 50  // 毫秒间隔
    },
    charset: {
      type: String,
      default: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'
    }
  })
  
  const displayText = ref([...props.text])
  let intervalId
  
  const randomChar = () => {
    return props.charset[Math.floor(Math.random() * props.charset.length)]
  }
  
  const updateText = () => {
    displayText.value = displayText.value.map((_, i) =>
      Math.random() < 0.7 ? randomChar() : props.text[i]
    )
  }
  
  onMounted(() => {
    intervalId = setInterval(updateText, props.speed)
  })
  
  onBeforeUnmount(() => {
    clearInterval(intervalId)
  })
  
  watch(() => props.text, () => {
    displayText.value = [...props.text]
  })
  </script>
  