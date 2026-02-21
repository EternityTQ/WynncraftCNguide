<template>
  <div v-if="data" class="key-skills-card" :class="{ 'dark-mode': isDarkMode }" :style="{ '--skill-color': data.color }">
    <div class="header">
      <div class="title-row">
        <h3 class="card-title">重要技能</h3>
        <div class="deco-line"></div>
      </div>
    </div>

    <div class="skills-container">
      <div 
        v-for="skillName in data.skills" 
        :key="skillName" 
        class="skill-item-wrapper"
      >
        <div class="skill-icon-box">
          <sn 
            :name="skillName" 
            :current-class="data.baseClass" 
          />
        </div>
      </div>
    </div>
  </div>

  <div v-else class="error-msg">
    KeySkills: 未找到职业数据 "{{ name }}"
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useDarkMode } from "vuepress-theme-hope/client"
import allData from './data/key-skills.json'

const { isDarkMode } = useDarkMode()

const props = defineProps({
  name: { type: String, required: true }
})

const data = computed(() => allData[props.name] || allData[props.name.replace(/_/g, ' ')])
</script>

<style scoped>
/* --- 卡片基础样式 --- */
.key-skills-card {
  background: #fff; /* 默认白底 */
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  margin: 1.5rem 0;
  padding: 1.2rem;
  border: 1px solid #eee;
  --title-color: var(--skill-color, #3eaf7c);
  transition: all 0.3s ease;
}

/* --- 深色模式适配 --- */
.key-skills-card.dark-mode {
  background: #1e1e1e; /* 深色底 */
  border-color: #333;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.header { margin-bottom: 1.2rem; }
.title-row { display: flex; align-items: center; gap: 12px; }
.card-title { margin: 0; font-size: 1.1rem; font-weight: bold; color: var(--title-color); white-space: nowrap; }
.deco-line { flex: 1; height: 2px; background: linear-gradient(to right, var(--title-color), transparent); opacity: 0.5; border-radius: 1px; }

.skills-container { display: flex; flex-wrap: wrap; gap: 12px; justify-content: flex-start; }
.skill-item-wrapper { display: flex; flex-direction: column; align-items: center; gap: 6px; }

/* --- 图标框样式 --- */
.skill-icon-box {
  width: 52px; 
  height: 52px;
  /* 白天背景：极浅灰 */
  background-color: #f9f9f9; 
  border: 2px solid var(--title-color);
  opacity: 0.8;
  border-radius: 8px; 
  display: flex; align-items: center; justify-content: center;
  transition: all 0.2s ease;
  position: relative; overflow: hidden; 
}

/* 深色模式下的图标框 */
.key-skills-card.dark-mode .skill-icon-box {
  background-color: #2c2c2c; /* 深灰色背景 */
  /* border-color 可以保持原样，也可以稍微调暗，这里保持原样 */
}

.skill-icon-box:hover {
  transform: translateY(-3px);
  background-color: #fff !important; /* 悬停高亮 */
  opacity: 1;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* 深色模式下悬停，背景变成更亮的深灰，而不是纯白 */
.key-skills-card.dark-mode .skill-icon-box:hover {
  background-color: #383838 !important;
}

:deep(.skill-container) { width: 100%; height: 100%; }
:deep(.skill-icon) { padding: 6px !important; box-sizing: border-box; width: 100% !important; height: 100% !important; }
.error-msg { color: red; padding: 10px; border: 1px dashed red; }
</style>