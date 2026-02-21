<template>
  <div class="skill-container" :class="{ 'connector-mode': isConnector }"
    @mouseenter="!isConnector && handleMouseEnter($event)" @mousemove="!isConnector && handleMouseMove($event)"
    @mouseleave="!isConnector && handleMouseLeave()" @click.stop="!isConnector && togglePin($event)">
    <div class="icon-wrapper">
      <img v-if="skill || isConnector" :src="iconSrc" class="skill-icon"
        :class="{ 'is-pinned': isPinned && !isConnector }" />
      <div v-else class="error-text">?</div>
    </div>

    <Teleport to="body">
      <div v-if="!isConnector && skill && (isHovering || isPinned)" class="wynn-tooltip"
        :class="{ 'mobile-mode': isMobile, 'pinned-left': isPinned && pinnedAlign === 'left' }" :style="tooltipStyle"
        @click.stop>

        <div class="header">
          <div class="title-cn" :class="titleColorClass">
            {{ transName }}
          </div>
          <div class="title-en" :style="{ color: nodeColor, opacity: 0.7 }">
            ({{ skill.display_name }})
          </div>
        </div>

        <div class="body">
          <div v-if="trans && trans.combo && trans.combo.trim() !== ''" class="combo">
            使用连招：<span class="combo-seq">{{ trans.combo }}</span>
          </div>
          <div class="desc-text" v-html="finalDesc"></div>
        </div>

        <div v-if="shouldShowFooter" class="footer">
          <div v-if="manaCost && !hasManualCost" class="stat-line">
            <span class="stat-label">技能消耗：</span>
            <span class="stat-val" :class="getStatValueClass('cost', manaCost)">{{ manaCost }}</span>
          </div>

          <div v-for="stat in displayStats" :key="stat.key" class="stat-line">
            <span class="stat-label">{{ stat.label }}：</span>
            <div class="stat-content">
              <span class="stat-val" :class="getStatValueClass(stat.key, stat.value)">
                {{ stat.value }}
              </span>
              <span class="stat-unit">{{ stat.unit }}</span>
            </div>
          </div>

          <div v-if="archetypeInfo" class="archetype-section" :style="{ color: archetypeInfo.color }">
            {{ archetypeInfo.name }} 分支
          </div>
        </div>

        <div v-if="trans && trans.note" class="side-tooltip">
          <div class="header">
            <div class="title-note">备注</div>
          </div>
          <div class="body">
            <div class="note-text" v-html="formatText(trans.note)"></div>
          </div>
        </div>

      </div>
    </Teleport>
  </div>
</template>

<script>
import atreeData from './data/atree.json';
import transData from './data/zh-cn.json';

const UNIT_MAP = {
  range: '格',
  aoe: '格',
  duration: '秒',
  damage: '%',
  mana: '点',
  shots: '发',
  cooldown: '秒',
  slowness: '%',
  resistance: '%',
  speed: '%',
  charges: '层',
  ray_duration: '秒',
  vision: '格',
  hits: '次',
  defense_bonus: '%',
  angle: '°',
  attackRate: '次',
  attack: '%',
  orb_health: '点',
  bank: '点',
  weakness: '%',
  damage_boost: '%',
  blood_pool: '点',
  cost: '点'

};

const STAT_LABEL_MAP = {
  cost: '技能消耗',
  range: '范围',
  aoe: '伤害/作用范围',
  damage: '伤害',
  duration: '持续时间',
  cooldown: '冷却',
  shots: '弹量',
  slowness: '减缓敌人',
  trap: '陷阱上限',
  manaRegen: '蓝量回复',
  charges: '充能层数',
  resistance: '抗性提升',
  speed: '速度加成',
  ray_duration: '射线持续时间',
  vision: '索敌范围',
  hits: '攻击次数',
  defense_bonus: '抗性提升',
  angle: '攻击角度',
  attackRate: '攻击判定次数',
  orb_health: '光之宝珠生命值',
  bank: '法力储备上限',
  attack: '伤害加成',
  weakness: '削弱攻击',
  damage_boost: '伤害加成',
  blood_pool: '血池上限'
  // ... 其他字段 ...
};

const NEGATIVE_KEYS = ['cost', 'cooldown', 'mana'];

const MAIN_WIDTH = 300;
const SIDE_WIDTH = 200;
const GAP = 10;
const OFFSET = 15;

export default {
  props: ['name', 'currentClass'],
  data() {
    return {
      isHovering: false, isPinned: false,
      mouseX: 0, mouseY: 0, pinnedLeft: 0, pinnedTop: 0, pinnedAlign: 'right',
      windowWidth: typeof window !== 'undefined' ? window.innerWidth : 1920,
      rafId: null
    };
  },
  computed: {
    displayStats() {
      if (!this.trans) return [];

      // 获取要显示的字段列表 (兼容旧的 stats_map 和新的 stats_keys)
      let keys = [];
      if (this.trans.stats_keys) {
        keys = this.trans.stats_keys;
      } else if (this.trans.stats_map) {
        keys = Object.keys(this.trans.stats_map);
      } else {
        return [];
      }

      // 构建最终显示数组
      return keys.map(key => {
        // 1. 获取数值 (补丁 > 原版)
        let val = null;
        if (this.trans.properties && this.trans.properties[key] !== undefined) {
          val = this.trans.properties[key]; // 取补丁
        } else if (this.skill && this.skill.properties && this.skill.properties[key] !== undefined) {
          val = this.skill.properties[key]; // 取原版
        }

        // 如果两边都找不到值，且不是蓝耗(蓝耗单独处理了)，就不显示
        if (val === null) return null;

        // 2. 获取标签 (字典 > stats_map里的旧值 > key本身)
        let label = STAT_LABEL_MAP[key] || (this.trans.stats_map ? this.trans.stats_map[key] : key);

        return {
          key: key,
          label: label,
          value: val,
          unit: this.getUnit(key)
        };
      }).filter(item => item !== null); // 过滤掉无数据的项
    },
    hasManualCost() {
      return this.displayStats.some(stat => stat.key === 'cost');
    },
    skill() {
      const classSkills = atreeData[this.currentClass];
      if (!classSkills) return null;
      return classSkills.find(s => s.display_name === this.name);
    },
    // 【修改】使用 displayStats.length 来判断是否有数据
    shouldShowFooter() {
      const hasMana = !!this.manaCost;
      // const hasStats = this.trans && this.trans.stats_map && Object.keys(this.trans.stats_map).length > 0; // 旧逻辑
      const hasStats = this.displayStats && this.displayStats.length > 0; // 新逻辑

      const hasArchetype = !!this.archetypeInfo;
      return hasMana || hasStats || hasArchetype;
    },
    archetypeInfo() {
      if (!this.skill || !this.skill.archetype) return null;

      const archKey = this.skill.archetype;
      const archName = this.archetypeMap[archKey] || archKey;

      // 【修改】这里是你要填色号的地方！
      // 格式："分支英文名": "十六进制颜色"
      const colorMap = {
        "Boltslinger": "#FFFF55",  // 黄色示例
        "Sharpshooter": "#FF55FF", // 粉色示例
        "Trapper": "#00AA00",      // 绿色示例
        "Ritualist": "#16d108",
        "Summoner": "orange",
        "Acolyte": "red",
        "Fallen": "#FF5555",
        "Battle Monk": "#FFFF55",
        "Paladin": "#55FFFF",
        "Riftwalker": "#55FFFF",
        "Light Bender": "#FFFFFF",
        "Arcanist": "#AA00AA",
        "Shadestepper": "#AA0000",
        "Trickster": "#FF55FF",
        "Acrobat": "#FFFFFF"
      };

      // 获取颜色，如果没有定义则默认白色
      const colorCode = colorMap[archKey] || '#FFFFFF';

      return { name: archName, color: colorCode };
    },
    isConnector() {
      const connectorNames = ['竖线', '横线', '十字', '丁字', '左丁字', '右丁字', '左下', '右下'];
      return connectorNames.includes(this.name);
    },
    iconSrc() {
      const basePath = '/assets/img/class/';
      if (this.isConnector) return `${basePath}${this.name}.png`;
      if (!this.skill) return '';
      const iconCode = this.skill.display.icon;
      if (iconCode.startsWith('node_') && iconCode.length > 6) {
        const className = iconCode.replace('node_', '');
        return `${basePath}${className}_green.png`;
      }
      const map = {
        'node_0': 'small.png', 'node_1': 'medium.png', 'node_2': 'large.png',
        'node_3': 'special.png', 'node_4': 'blue.png'
      };
      return basePath + (map[iconCode] || 'small.png');
    },
    trans() {
      if (!this.skill) return null;
      return transData[this.name] || transData[this.name.replace(/ /g, '_')];
    },
    transName() {
      return this.trans ? this.trans.name : (this.skill ? this.skill.display_name : '');
    },
    manaCost() {
      if (!this.skill || !this.skill.effects) return null;
      const spellEffect = this.skill.effects.find(e => e.cost !== undefined);
      return spellEffect ? spellEffect.cost : null;
    },
    titleColorClass() {
      if (!this.skill) return '';
      const icon = this.skill.display.icon;
      if (icon.startsWith('node_') && icon.length > 6) return 't-green';
      const colorMap = { 'node_0': 't-white', 'node_1': 't-yellow', 'node_2': 't-pink', 'node_3': 't-red', 'node_4': 't-blue' };
      return colorMap[icon] || 't-white';
    },
    nodeColor() {
      if (!this.skill) return '#FFFFFF';
      const icon = this.skill.display.icon;
      if (icon.startsWith('node_') && icon.length > 6) return '#55FF55';
      const map = { 'node_0': '#FFFFFF', 'node_1': '#FFFF55', 'node_2': '#FF55FF', 'node_3': '#FF5555', 'node_4': '#55FFFF' };
      return map[icon] || '#FFFFFF';
    },
    archetypeMap() {
      return {
        "Boltslinger": "闪击射手", "Sharpshooter": "鹰眼射手", "Trapper": "陷阱射手",
        "Ritualist": "圣祭司", "Summoner": "召唤师", "Acolyte": "血教徒",
        "Fallen": "腐化者", "Battle Monk": "武道士", "Paladin": "圣骑士",
        "Riftwalker": "时空行者", "Light Bender": "圣光使者", "Arcanist": "奥术法师",
        "Shadestepper": "影步者", "Trickster": "诡术师", "Acrobat": "凌空客"
      };
    },
    finalDesc() {
      let rawText = '';
      if (this.trans && this.trans.description) {
        rawText = this.trans.description;
      } else if (this.trans && this.trans.desc) {
        rawText = this.trans.desc;
      } else if (this.skill && this.skill.desc) {
        rawText = `<span class="t-red" style="font-size:12px; display:block; margin-bottom:8px;">(暂无中文翻译)</span>` + this.skill.desc;
      } else {
        return '<span style="color: #555555">暂无数据</span>';
      }
      // 只做格式化
      return this.formatText(rawText);
    },
    isMobile() { return this.windowWidth < 768; },
    hasNote() { return this.trans && this.trans.note; },

    tooltipStyle() {
      if (this.isPinned) {
        // 固定模式：绝对定位 + 实时计算的坐标
        const style = {
          position: 'absolute',
          top: this.pinnedTop + 'px',
          left: this.pinnedLeft + 'px',
          zIndex: 1000,
          pointerEvents: 'auto',
          transform: 'none'
        };
        return style;
      } else {
        // 悬停模式：Fixed 定位 + 鼠标跟随
        const isRightSide = this.mouseX > (this.windowWidth * 0.58);
        let finalLeft = this.mouseX + OFFSET;
        let finalTop = this.mouseY + OFFSET;

        if (this.isMobile) {
          finalLeft = 10;
          finalTop = this.mouseY - 100;
        } else if (isRightSide) {
          finalLeft = this.mouseX - MAIN_WIDTH - OFFSET;
          if (this.hasNote) finalLeft = finalLeft - SIDE_WIDTH - GAP;
        }

        return {
          position: 'fixed',
          top: finalTop + 'px',
          left: finalLeft + 'px',
          zIndex: 2000,
          pointerEvents: 'none'
        };
      }
    }
  },
  methods: {
    getUnit(key) { return UNIT_MAP[key] || ''; },
    getStatValueClass(key, value) {
      const valStr = String(value);
      // 判断是否为主技能
      const isMainSkill = this.skill && this.skill.display.icon.startsWith('node_') && this.skill.display.icon.length > 6;

      if (NEGATIVE_KEYS.includes(key)) {
        // 1. 带有 '+' 号 (如 "+5s 冷却", "+10 蓝耗") -> 明确的负面增加 -> 红色
        if (valStr.includes('+')) {
          return 't-red';
        }

        // 2. 带有 '-' 号 (如 "-20% 冷却") -> 正面减少 -> 白色
        if (valStr.includes('-')) {
          return '';
        }

        // 3. 纯数字情况 (无符号)
        if (key === 'cost') {
          // 蓝耗逻辑不变：主技能基础值白，被动技能默认为增加(红)
          return isMainSkill ? '' : 't-red';
        }

        if (key === 'cooldown') {
          // 【修改】冷却逻辑：纯数字视为基础冷却时间 (中性) -> 白色
          // 只有上面明确带 '+' 的才会变红
          return '';
        }

        // 其他负面属性 (如 mana) 默认处理，如果需要也可以在这里加
        return '';
      }

      return ''; // 其他属性默认白色
    },
    formatText(text) {
      if (!text) return '';
      let formatted = text.replace(/\n/g, '<br>');

      // 定义转义映射 (临时占位符)
      const placeholders = {
        '^': '{{__CARET__}}',
        '!': '{{__EXCLAM__}}',
        '$': '{{__DOLLAR__}}',
        '_': '{{__UNDER__}}',
        '*': '{{__AST__}}' // 【新增】星号占位符
      };

      // 1. 处理转义符：将 \^, \*, \! 等替换为占位符
      // 【修改】正则中加入 * formatted = formatted.replace(/\\([\^!$_*])/g, (_, char) => placeholders[char]);

      // 2. 处理成对符号
      // ^文本^ -> 白色
      formatted = formatted.replace(/\^([^\^]+)\^/g, '<span class="t-white">$1</span>');
      // !文本! -> 红色
      formatted = formatted.replace(/!([^!]+)!/g, '<span class="t-red">$1</span>');
      // $文本$ -> 青色
      formatted = formatted.replace(/\$([^$]+)\$/g, '<span class="t-aqua">$1</span>');
      // _文本_ -> 下划线
      formatted = formatted.replace(/_([^_]+)_/g, '<u>$1</u>');

      // 【新增】*文本* -> 注释灰 (#555555)
      formatted = formatted.replace(/\*([^*]+)\*/g, '<span class="t-gray">$1</span>');

      // 3. 处理原有的 <tip> 标签
      formatted = formatted.replace(/<tip name="([^"]+)">([^<]+)<\/tip>/g, '<span class="t-green">$2</span>');

      // 4. 还原转义字符
      Object.keys(placeholders).forEach(key => {
        formatted = formatted.split(placeholders[key]).join(key);
      });

      return formatted;
    },
    handleMouseEnter(e) { this.isHovering = true; this.updateMousePos(e); },
    handleMouseMove(e) { this.updateMousePos(e); },
    handleMouseLeave() { this.isHovering = false; },
    updateMousePos(e) { this.mouseX = e.clientX; this.mouseY = e.clientY; },

    // 【核心修复：实时位置追踪】
    startTracking() {
      const update = () => {
        if (!this.isPinned) return;
        this.updatePinnedPosition();
        this.rafId = requestAnimationFrame(update);
      };
      this.rafId = requestAnimationFrame(update);
    },

    stopTracking() {
      if (this.rafId) {
        cancelAnimationFrame(this.rafId);
        this.rafId = null;
      }
    },

    updatePinnedPosition() {
      // 获取图标在视口中的实时位置
      const rect = this.$el.getBoundingClientRect();

      // 更新 Top (图标顶部 + 页面滚动距离)
      // 注意：这里必须加上 window.scrollY，因为 absolute 是相对于文档顶部的
      this.pinnedTop = rect.top + window.scrollY;

      // 判断对齐方向 (只在初始判断或resize时判断也行，但这里实时判断更稳)
      // 这里为了防止闪烁，我们可以复用 pinnedAlign，或者实时计算
      // 建议：保持 pinnedAlign 不变，只更新 Left

      if (this.pinnedAlign === 'left') {
        // 向左弹：Left = 图标左边 - 宽度 - 间距
        let leftPos = rect.left + window.scrollX - MAIN_WIDTH - GAP;
        if (this.hasNote) leftPos = leftPos - SIDE_WIDTH - GAP;
        this.pinnedLeft = leftPos;
      } else {
        // 向右弹：Left = 图标右边 + 间距
        this.pinnedLeft = rect.right + window.scrollX + GAP;
      }
    },

    togglePin(e) {
      if (this.isMobile && this.isPinned) {
        this.isPinned = false;
        this.stopTracking(); // 停止追踪
        return;
      }

      if (this.isPinned) {
        this.isPinned = false;
        this.stopTracking(); // 停止追踪
      } else {
        this.isPinned = true;
        // 初始判断方向
        const rect = this.$el.getBoundingClientRect();
        const isRightSide = rect.left > (this.windowWidth * 0.58);
        this.pinnedAlign = isRightSide ? 'left' : 'right';

        // 立即计算一次位置
        this.updatePinnedPosition();
        // 开启循环追踪
        this.startTracking();
      }
    },

    handleClickOutside(e) {
      // 检查点击目标是否在组件内部 (包括图标和传送走的 tooltip)
      // 注意：Tooltip 被传送走了，this.$el (图标容器) 不再包含它
      // 但我们阻止了 Tooltip 内部的冒泡 (@click.stop)，所以点击 Tooltip 不会触发这里
      // 这里只需要判断是否点击了图标
      if (this.$el.contains(e.target)) return;

      this.isPinned = false;
      this.stopTracking();
    },
    handleResize() { this.windowWidth = window.innerWidth; },
    cleanup() {
      this.stopTracking(); // 停止 rAF 动画帧
      if (typeof window !== 'undefined') {
        document.removeEventListener('click', this.handleClickOutside);
        window.removeEventListener('resize', this.handleResize);
      }
    },

    // togglePin 里的逻辑可以大幅简化了，因为 watch 会帮我们做事
    togglePin(e) {
      if (this.isMobile && this.isPinned) {
        this.isPinned = false;
        return;
      }

      if (this.isPinned) {
        this.isPinned = false;
        // watch 会自动调用 cleanup
      } else {
        this.isPinned = true;
        // 初始判断方向
        const rect = this.$el.getBoundingClientRect();
        const isRightSide = rect.left > (this.windowWidth * 0.58);
        this.pinnedAlign = isRightSide ? 'left' : 'right';

        // watch 会自动调用 startTracking 和 addEventListener
      }
    },
  },
  mounted() {
  },
  beforeDestroy() {
    this.cleanup();

  },
  watch: {
    // 【核心优化】监听 isPinned 状态
    // 只有在固定时才通过 addEventListener 消耗资源
    // 这样 100 个节点里只有 1 个会监听 document click，性能飞跃
    isPinned(val) {
      if (val) {
        // 开启：延时一帧添加监听，防止当前点击事件立即触发 handleClickOutside
        setTimeout(() => {
          document.addEventListener('click', this.handleClickOutside);
          window.addEventListener('resize', this.handleResize);
        }, 0);

        this.updatePinnedPosition();
        this.startTracking();
      } else {
        // 关闭：立刻清理
        this.cleanup();
      }
    }
  },
}
</script>

<style scoped>
/* 颜色类 */
.t-red {
  color: #FF5555;
}

.t-aqua {
  color: #55FFFF;
}

.t-green {
  color: #55FF55;
}

.skill-container {
  display: inline-flex;
  position: relative;
  vertical-align: middle;
  cursor: pointer;
  margin: 0;
  /* 去除间距 */
  width: 100%;
  /* 撑满 Grid 格子 */
  height: 100%;
  /* 撑满 Grid 格子 */
  justify-content: center;
  align-items: center;
}

.skill-container.connector-mode {
  cursor: default;
  /* margin, width, height 已经由上面统一设置了，这里可以简化 */
}

.skill-icon {
  width: 100%;
  /* 撑满容器 */
  height: 100%;
  /* 撑满容器 */
  object-fit: contain;
  /* 保持图片比例 (如果是正方形贴图则无所谓) */
  transition: transform 0.1s;
  display: block;
  /* 消除图片底部幽灵间隙 */
}

.connector-mode .skill-icon {
  width: 100%;
  height: 100%;
  transform: none !important;
  filter: none !important;
  display: block;
}

.skill-icon:hover {
  transform: scale(1.1);
}

.skill-icon.is-pinned {
  filter: brightness(1.2);
  transform: scale(1.1);
}

.error-text {
  width: 40px;
  height: 40px;
  background: red;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Tooltip 样式 */
.wynn-tooltip {
  background-color: rgba(0, 0, 0, 0.9);
  border: 2px solid #500050;
  border-radius: 4px;
  color: #AAAAAA;
  padding: 12px;
  width: 300px;
  font-family: 'Minecraft', sans-serif;
  font-size: 14px;
  line-height: 1.5;
  text-align: left;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
  white-space: normal;
}

.wynn-tooltip.mobile-mode {
  max-width: 90vw;
}

.wynn-tooltip.mobile-mode .side-tooltip {
  position: static;
  margin-left: 0;
  margin-top: 10px;
  width: 100%;
  border-color: #55FF55;
}

.side-tooltip {
  position: absolute;
  left: 100%;
  top: -2px;
  margin-left: 10px;
  background-color: rgba(0, 0, 0, 0.9);
  border: 2px solid #500050;
  border-radius: 4px;
  padding: 12px;
  width: 200px;
  color: #AAAAAA;
  z-index: 2000;
}

.wynn-tooltip.pinned-left .side-tooltip {
  left: auto;
  right: 100%;
  margin-left: 0;
  margin-right: 10px;
}

.archetype-section {
  margin-top: 8px;
  font-weight: bold;
  font-size: 14px;
  text-align: left;
  /* 【修改】改为居左 */
}

/* 内部样式不变 */
.header {
  margin-bottom: 10px;
  text-align: left;
}

/* --- 颜色类 (核心修复：加上 ::v-deep) --- */
::v-deep .t-red {
  color: #FF5555 !important;
}

::v-deep .t-aqua {
  color: #55FFFF !important;
}

::v-deep .t-green {
  color: #55FF55 !important;
}

::v-deep .t-white {
  color: #FFFFFF !important;
}

::v-deep .t-yellow {
  color: #FFFF55 !important;
}

::v-deep .t-pink {
  color: #FF55FF !important;
}

::v-deep .t-gray {
  color: #555555 !important;
}

::v-deep .t-blue {
  color: #55FFFF !important;
}

::v-deep u {
  text-decoration: underline;
}

/* ... 其他样式保持不变 ... */

.title-cn {
  font-size: 17px;
  /* 中文标题字号 */
  font-weight: bold;
  /* 颜色会通过 :class="titleColorClass" 里的 .t-green 等类叠加进来 */
}

.title-en {
  color: #55FF55;
  opacity: 0.7;
  font-size: 13px;
  margin-top: 2px;
}

.body {
  margin-bottom: 15px;
}

.combo {
  color: #FFAA00;
  margin-bottom: 8px;
}

.combo-seq {
  color: #FF55FF;
  font-weight: bold;
}

.desc-text {
  color: #AAAAAA;
}

.footer {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 2px solid #333;
}

.stat-line {
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  margin-bottom: 2px;
  gap: 4px;
}

.stat-label {
  color: #AAAAAA;
  white-space: nowrap;
}

.stat-val {
  color: #FFFFFF;
  font-weight: bold;
}

.stat-unit {
  color: #AAAAAA;
  margin-left: 4px;
}

.title-note {
  color: #55FF55;
  font-weight: bold;
  font-size: 16px;
  margin-bottom: 8px;
  text-align: left;
}

.note-text {
  color: #AAAAAA;
  font-size: 13px;
  line-height: 1.4;
  text-align: left;
}

::v-deep .w-gray {
  color: #555555;
  font-style: italic;
}

::v-deep .w-green {
  color: #55FF55;
}

::v-deep .w-aqua {
  color: #55FFFF;
}

::v-deep .w-white {
  color: #FFFFFF;
}
</style>