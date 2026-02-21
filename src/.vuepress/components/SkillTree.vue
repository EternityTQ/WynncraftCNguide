<template>
  <div class="wynn-tree-wrapper">
    <div class="tree-scroll-container">
      
      <div class="tree-content" :style="containerStyle">
        
        <svg class="connections-layer">
          <path 
            v-for="(pathD, index) in connectorPaths" 
            :key="index"
            :d="pathD" 
            class="connector-line"
          />
        </svg>

        <div class="skill-grid" :style="gridStyle">
          <SkillNode 
            v-for="(item, index) in combinedItems" 
            :key="`item-${index}`" 
            :name="item.display_name"
            :current-class="currentClass" 
            :style="getItemStyle(item)"
          />
        </div>
      
      </div>
    </div>
  </div>
</template>

<script>
import SkillNode from './SkillNode.vue'; 
import atreeData from './data/atree.json'; 
import connectorData from './data/connectors.json'; 

export default {
  components: { SkillNode },
  props: {
    // 【修改】通过 Props 接收职业，不再自己管理
    currentClass: {
      type: String,
      default: 'Archer'
    }
  },
  data() {
    return {
      // ...
      // 【修改】这里控制整体大小！
      // 如果想撑满，可以改大到 60 或 65
      // 如果想保持紧凑但去除留白，请看下面的 CSS 修改
      gridCellSize: 60, 
      gridGap: 0,       
    };
  },
  computed: {
    // 1. 获取原始技能数据
    rawSkills() {
      return atreeData[this.currentClass] || [];
    },

    skills() {
      // 仅仅做深拷贝，防止污染源数据，不再修改 row
      return this.rawSkills.map(skill => JSON.parse(JSON.stringify(skill)));
    },

    // 3. 处理连线数据：解析新的分类结构
    connectorItems() {
      const classConnectors = connectorData[this.currentClass];
      if (!classConnectors) return [];

      const items = [];
      
      // 遍历所有类型 (竖线, 横线, 丁字...)
      // type = "竖线", coords = [{row:1, col:4}, ...]
      for (const [type, coords] of Object.entries(classConnectors)) {
        if (Array.isArray(coords)) {
          coords.forEach(pos => {
            items.push({
              display_name: type, // 这里名字必须和 SkillNode.vue 里的判断逻辑一致
              display: {
                row: pos.row, // 这里直接使用你手动填的坐标，不做计算
                col: pos.col,
                icon: type    // 用于寻找图片文件，如 竖线.png
              }
            });
          });
        }
      }
      return items;
    },

    // 4. 合并数据：技能 + 连线
    combinedItems() {
      return [...this.skills, ...this.connectorItems];
    },

    // 5. 计算网格最大尺寸
    gridDimensions() {
      let maxRow = 0;
      this.combinedItems.forEach(item => {
        if (item.display.row > maxRow) maxRow = item.display.row;
      });
      // 【修改】这里改为 +3，给底部留出更多富余空间，防止图标边缘被切
      return { rows: maxRow + 3, cols: 9 };
    },

    containerStyle() {
      const width = this.gridDimensions.cols * (this.gridCellSize + this.gridGap);
      const height = this.gridDimensions.rows * (this.gridCellSize + this.gridGap);
      return { width: `${width}px`, height: `${height}px` };
    },

    gridStyle() {
      return {
        'grid-template-columns': `repeat(${this.gridDimensions.cols}, ${this.gridCellSize}px)`,
        'grid-template-rows': `repeat(${this.gridDimensions.rows}, ${this.gridCellSize}px)`,
        'gap': `${this.gridGap}px`,
        'width': '100%',
        'height': '100%'
      };
    }
  },
  methods: {
    getItemStyle(item) {
      return {
        gridRow: item.display.row + 1,
        gridColumn: item.display.col + 1
      };
    }
  }
}
</script>

<style scoped>
.wynn-tree-wrapper {
  /* 【修改】原来是 width: 100%; 改为 fit-content */
  width: fit-content; 
  /* 或者使用 inline-block */
  /* display: inline-block; */
  
  min-width: 100%; /* 选填：如果你希望它至少占满一行，但内容少时不要留白，这就比较矛盾。通常用 fit-content 配合居中即可 */
  
  height: 800px;
  background-color: #292929;
  border: 1px solid #333;
  overflow: hidden; 
  position: relative;
  
  /* 如果改为 fit-content 后想让整个表格在页面居中，可以加这个： */
  margin: 0 auto; 
}

.tree-scroll-container {
  width: 100%;
  height: 100%;
  overflow: auto;
  /* 【修改】上下保留 20px 缓冲，左右设为 0 以消除"多余列"的视觉感 */
  padding: 20px 0; 
  display: flex;
  justify-content: center; /* 保持居中，或者改为 flex-start 靠左对齐 */
}

.tree-content {
  position: relative; 
}

.skill-grid {
  display: grid;
  position: relative;
  /* 强力消除间隙方案 A */
  font-size: 0; 
  line-height: 0;
}

::v-deep .skill-container {
  margin: 0;
  padding: 0;
  border: none;
  outline: none;
  display: block; /* 改为 block 试试，或者 flex */
}

::v-deep .skill-icon {
  display: block; /* 必须是 block */
  width: 100%;
  height: 100%;
  /* 强力消除间隙方案 B: 稍微放大一点点覆盖缝隙 (如果上面不管用) */
  /* transform: scale(1.02); */ 
}
</style>