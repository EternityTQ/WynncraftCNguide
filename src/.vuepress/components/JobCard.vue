<template>
  <div v-if="job" class="job-card" :class="{ 'dark-mode': isDarkMode }" :style="{ '--job-color': job.color }">
    <div class="job-info">
      <div class="header">
        <h3 class="job-name">{{ job.name }}</h3>
        <div class="color-bar"></div>
      </div>
      
      <p class="description">{{ job.description }}</p>
      
      <div class="tags">
        <span v-for="tag in job.tags" :key="tag" class="tag">
          {{ tag }}
        </span>
      </div>
    </div>

    <div class="job-chart">
      <svg viewBox="0 0 200 200" class="radar-svg">
        <polygon 
          v-for="i in 5" 
          :key="`grid-${i}`" 
          :points="getPolygonPoints(i)" 
          class="grid-polygon"
        />
        
        <polygon :points="dataPoints" class="data-polygon" />
        
        <text x="100" y="12" class="label" text-anchor="middle">输出</text>
        <text x="195" y="75" class="label" text-anchor="end">生存</text>
        <text x="165" y="185" class="label" text-anchor="middle">续航</text>
        <text x="35" y="185" class="label" text-anchor="middle">难度</text>
        <text x="5" y="75" class="label" text-anchor="start">位移</text>
      </svg>
    </div>
  </div>

  <div v-else class="error-msg">
    未找到职业 ID: {{ name }}
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useDarkMode } from "vuepress-theme-hope/client"
import allJobs from './data/jobs.json'

// 获取深色模式状态
const { isDarkMode } = useDarkMode()

const props = defineProps({
  name: { type: String, required: true }
})

const job = computed(() => allJobs.find(item => item.id === props.name))

const maxRadius = 80 
const center = 100
const totalStats = 5

const getPoint = (value, index, maxVal = 5) => {
  const angle = (Math.PI * 2 * index) / totalStats - Math.PI / 2
  const radius = (value / maxVal) * maxRadius
  const x = center + radius * Math.cos(angle)
  const y = center + radius * Math.sin(angle)
  return `${x},${y}`
}

const getPolygonPoints = (level) => {
  return Array.from({ length: totalStats })
    .map((_, i) => getPoint(level, i, 5))
    .join(' ')
}

const dataPoints = computed(() => {
  if (!job.value) return ''
  const stats = job.value.stats
  return [stats.output, stats.survival, stats.sustain, stats.difficulty, stats.mobility]
    .map((val, i) => getPoint(val, i, 5)).join(' ')
})
</script>

<style scoped>
.error-msg { color: red; padding: 1rem; border: 1px dashed red; }

/* --- 基础卡片样式 (默认亮色模式) --- */
.job-card {
  display: flex;
  background: #fff; /* 亮色默认白底 */
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  margin: 1.5rem 0;
  overflow: hidden;
  border: 1px solid #eee; /* 亮色默认边框 */
  transition: all 0.3s ease;
}

/* --- 深色模式适配 (通过 dark-mode 类控制) --- */
.job-card.dark-mode {
  background: #1e1e1e; /* 深色背景 */
  border-color: #333;  /* 深色边框 */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3); /* 加深阴影 */
}

.job-info { flex: 1; padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; }

/* 字体颜色适配 */
.job-name { margin: 0; font-size: 1.5rem; color: var(--job-color); line-height: 1.2; }
.color-bar { width: 40px; height: 4px; background-color: var(--job-color); margin-top: 8px; border-radius: 2px; }

/* 描述文字：亮色为深灰，暗色为浅灰 */
.description { margin: 1rem 0; font-size: 0.95rem; color: #666; line-height: 1.6; text-align: justify; transition: color 0.3s; }
.job-card.dark-mode .description { color: #bbb; }

.tags { display: flex; gap: 8px; flex-wrap: wrap; }
.tag { 
  font-size: 0.8rem; padding: 4px 10px; border-radius: 20px; 
  background-color: #f3f4f5; 
  color: #888; 
  border: 1px solid #e0e0e0; 
  transition: all 0.3s;
}
/* 标签暗色适配 */
.job-card.dark-mode .tag {
  background-color: #2c2c2c;
  color: #aaa;
  border-color: #444;
}

/* --- 图表区域适配 --- */
.job-chart { 
  width: 200px; 
  flex-shrink: 0; 
  background-color: #fafafa; /* 亮色背景 */
  display: flex; 
  align-items: center; 
  justify-content: center; 
  border-left: 1px solid #eee; 
  transition: background-color 0.3s, border-color 0.3s;
}

.job-card.dark-mode .job-chart {
  background-color: #252525; /* 暗色背景 */
  border-left-color: #333;
}

.radar-svg { width: 100%; height: 100%; max-width: 180px; }

/* 网格线 */
.grid-polygon { fill: none; stroke: #ddd; stroke-width: 1; transition: stroke 0.3s; }
.job-card.dark-mode .grid-polygon { stroke: #444; }

.data-polygon {
  fill: var(--job-color);
  fill-opacity: 0.5;
  stroke: var(--job-color);
  stroke-width: 2;
  transform-origin: 100px 100px;
  animation: expand-radar 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

/* 文字标签 */
.label { 
  font-size: 11px; 
  fill: #666; 
  dominant-baseline: middle; 
  font-weight: bold;
  transition: fill 0.3s;
}
.job-card.dark-mode .label { fill: #ccc; } /* 暗色模式变白 */

@keyframes expand-radar {
  from { transform: scale(0); opacity: 0; }
  to { transform: scale(1); opacity: 1; }
}

@media (max-width: 768px) { 
  .job-card { flex-direction: column; } 
  .job-chart { width: 100%; height: 200px; border-left: none; border-top: 1px solid #eee; } 
  .job-card.dark-mode .job-chart { border-top-color: #333; }
}
</style>