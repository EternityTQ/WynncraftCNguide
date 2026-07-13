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
            ({{ skillPlainName }})
          </div>
        </div>

        <div class="body">
          <div class="desc-text" v-html="finalDesc"></div>
        </div>

        <div v-if="archetypeInfo" class="footer">
          <div class="archetype-section" :style="{ color: archetypeInfo.color }">
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
import transData from './data/wynnability-zh.json';

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
    // wynnability 格式：abilities 对象的键就是 plainname
    skill() {
      const classData = transData[this.currentClass];
      if (!classData || !classData.abilities) return null;
      return classData.abilities[this.name];
    },
    skillPlainName() {
      // wynnability 格式中，主键就是 plainname（去除格式码的英文原名）
      return this.name;
    },
    trans() {
      // wynnability 格式中，skill 本身就包含翻译字段
      return this.skill;
    },
    transName() {
      // 优先使用 customName（汉化名），如果没有则使用 name（带格式码的名字，去除格式码）
      if (this.trans && this.trans.customName) {
        return this.trans.customName;
      }
      if (this.trans && this.trans.name) {
        return this.stripMinecraftFormatting(this.trans.name);
      }
      return this.name;
    },
    archetypeInfo() {
      if (!this.skill) return null;

      const classData = transData[this.currentClass];
      if (!classData || !classData.archetypes) return null;

      // 从 skill 中获取分支信息（如果有）
      // wynnability 格式可能没有直接的 archetype 字段，需要根据实际格式调整
      // 这里假设有 archetype 字段
      const archKey = this.skill.archetype;
      if (!archKey) return null;

      const archData = classData.archetypes[archKey];
      if (!archData) return null;

      const archName = archData.name || archKey;

      // 颜色映射
      const colorMap = {
        "Boltslinger": "#FFFF55",
        "Sharpshooter": "#FF55FF",
        "Trapper": "#00AA00",
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

      // wynnability 格式可能没有 display.icon，使用默认图标
      // 根据实际数据格式调整
      return `${basePath}small.png`;
    },
    titleColorClass() {
      // 从 name 字段中提取颜色代码
      if (!this.skill || !this.skill.name) return 't-white';

      const colorCode = this.extractColorCode(this.skill.name);
      return this.getColorClass(colorCode);
    },
    nodeColor() {
      if (!this.skill || !this.skill.name) return '#FFFFFF';

      const colorCode = this.extractColorCode(this.skill.name);
      return this.getColorHex(colorCode);
    },
    finalDesc() {
      let rawText = '';
      if (this.trans && this.trans.description) {
        rawText = this.trans.description;
      } else if (this.skill && this.skill.description) {
        rawText = this.skill.description;
      } else {
        return '<span style="color: #555555">暂无数据</span>';
      }
      // Minecraft 格式化
      return this.formatMinecraftText(rawText);
    },
    isMobile() { return this.windowWidth < 768; },
    hasNote() { return this.trans && this.trans.note; },

    tooltipStyle() {
      if (this.isPinned) {
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
    stripMinecraftFormatting(text) {
      if (!text) return '';
      return text.replace(/§[0-9a-fk-or]/gi, '');
    },
    extractColorCode(text) {
      if (!text) return null;
      // 提取第一个颜色代码 §x
      const match = text.match(/§([0-9a-f])/i);
      return match ? match[1] : null;
    },
    getColorClass(code) {
      const map = {
        '0': 't-black', '1': 't-dark-blue', '2': 't-dark-green', '3': 't-dark-aqua',
        '4': 't-dark-red', '5': 't-dark-purple', '6': 't-gold', '7': 't-gray',
        '8': 't-dark-gray', '9': 't-blue', 'a': 't-green', 'b': 't-aqua',
        'c': 't-red', 'd': 't-pink', 'e': 't-yellow', 'f': 't-white',
        'g': 't-green-alt'
      };
      return map[code?.toLowerCase()] || 't-white';
    },
    getColorHex(code) {
      const map = {
        '0': '#000000', '1': '#0000AA', '2': '#00AA00', '3': '#00AAAA',
        '4': '#AA0000', '5': '#AA00AA', '6': '#FFAA00', '7': '#AAAAAA',
        '8': '#555555', '9': '#5555FF', 'a': '#55FF55', 'b': '#55FFFF',
        'c': '#FF5555', 'd': '#FF55FF', 'e': '#FFFF55', 'f': '#FFFFFF',
        'g': '#55FF55'
      };
      return map[code?.toLowerCase()] || '#FFFFFF';
    },
    formatMinecraftText(text) {
      if (!text) return '';

      let result = '';
      let currentColor = '#AAAAAA';
      let isBold = false;
      let isItalic = false;
      let isUnderline = false;
      let isStrikethrough = false;

      let i = 0;
      while (i < text.length) {
        if (text[i] === '§' && i + 1 < text.length) {
          const code = text[i + 1].toLowerCase();

          // 颜色代码
          if ('0123456789abcdefg'.includes(code)) {
            currentColor = this.getColorHex(code);
          }
          // 格式代码
          else if (code === 'l') isBold = true;
          else if (code === 'o') isItalic = true;
          else if (code === 'n') isUnderline = true;
          else if (code === 'm') isStrikethrough = true;
          else if (code === 'r') {
            // 重置
            currentColor = '#AAAAAA';
            isBold = false;
            isItalic = false;
            isUnderline = false;
            isStrikethrough = false;
          }

          i += 2;
          continue;
        }

        // 换行
        if (text[i] === '\n') {
          result += '<br>';
          i++;
          continue;
        }

        // 普通字符
        let styles = `color: ${currentColor};`;
        if (isBold) styles += ' font-weight: bold;';
        if (isItalic) styles += ' font-style: italic;';
        let decorations = [];
        if (isUnderline) decorations.push('underline');
        if (isStrikethrough) decorations.push('line-through');
        if (decorations.length > 0) styles += ` text-decoration: ${decorations.join(' ')};`;

        result += `<span style="${styles}">${text[i]}</span>`;
        i++;
      }

      return result;
    },
    formatText(text) {
      // 对 note 使用简单格式化
      if (!text) return '';
      let formatted = text.replace(/\n/g, '<br>');

      const placeholders = {
        '^': '{{__CARET__}}',
        '!': '{{__EXCLAM__}}',
        '$': '{{__DOLLAR__}}',
        '_': '{{__UNDER__}}',
        '*': '{{__AST__}}'
      };

      formatted = formatted.replace(/\\([\^!$_*])/g, (_, char) => placeholders[char]);

      formatted = formatted.replace(/\^([^\^]+)\^/g, '<span class="t-white">$1</span>');
      formatted = formatted.replace(/!([^!]+)!/g, '<span class="t-red">$1</span>');
      formatted = formatted.replace(/\$([^$]+)\$/g, '<span class="t-aqua">$1</span>');
      formatted = formatted.replace(/_([^_]+)_/g, '<u>$1</u>');
      formatted = formatted.replace(/\*([^*]+)\*/g, '<span class="t-gray">$1</span>');

      Object.keys(placeholders).forEach(key => {
        formatted = formatted.split(placeholders[key]).join(key);
      });

      return formatted;
    },
    handleMouseEnter(e) { this.isHovering = true; this.updateMousePos(e); },
    handleMouseMove(e) { this.updateMousePos(e); },
    handleMouseLeave() { this.isHovering = false; },
    updateMousePos(e) { this.mouseX = e.clientX; this.mouseY = e.clientY; },

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
      const rect = this.$el.getBoundingClientRect();
      this.pinnedTop = rect.top + window.scrollY;

      if (this.pinnedAlign === 'left') {
        let leftPos = rect.left + window.scrollX - MAIN_WIDTH - GAP;
        if (this.hasNote) leftPos = leftPos - SIDE_WIDTH - GAP;
        this.pinnedLeft = leftPos;
      } else {
        this.pinnedLeft = rect.right + window.scrollX + GAP;
      }
    },

    togglePin(e) {
      if (this.isMobile && this.isPinned) {
        this.isPinned = false;
        return;
      }

      if (this.isPinned) {
        this.isPinned = false;
      } else {
        this.isPinned = true;
        const rect = this.$el.getBoundingClientRect();
        const isRightSide = rect.left > (this.windowWidth * 0.58);
        this.pinnedAlign = isRightSide ? 'left' : 'right';
      }
    },

    handleClickOutside(e) {
      if (this.$el.contains(e.target)) return;
      this.isPinned = false;
      this.stopTracking();
    },
    handleResize() { this.windowWidth = window.innerWidth; },
    cleanup() {
      this.stopTracking();
      if (typeof window !== 'undefined') {
        document.removeEventListener('click', this.handleClickOutside);
        window.removeEventListener('resize', this.handleResize);
      }
    },
  },
  mounted() {
  },
  beforeDestroy() {
    this.cleanup();
  },
  watch: {
    isPinned(val) {
      if (val) {
        setTimeout(() => {
          document.addEventListener('click', this.handleClickOutside);
          window.addEventListener('resize', this.handleResize);
        }, 0);

        this.updatePinnedPosition();
        this.startTracking();
      } else {
        this.cleanup();
      }
    }
  },
}
</script>

<style scoped>
/* 颜色类 */
.t-black { color: #000000; }
.t-dark-blue { color: #0000AA; }
.t-dark-green { color: #00AA00; }
.t-dark-aqua { color: #00AAAA; }
.t-dark-red { color: #AA0000; }
.t-dark-purple { color: #AA00AA; }
.t-gold { color: #FFAA00; }
.t-gray { color: #AAAAAA; }
.t-dark-gray { color: #555555; }
.t-blue { color: #5555FF; }
.t-green { color: #55FF55; }
.t-green-alt { color: #55FF55; }
.t-aqua { color: #55FFFF; }
.t-red { color: #FF5555; }
.t-pink { color: #FF55FF; }
.t-yellow { color: #FFFF55; }
.t-white { color: #FFFFFF; }

.skill-container {
  display: inline-flex;
  position: relative;
  vertical-align: middle;
  cursor: pointer;
  margin: 0;
  width: 100%;
  height: 100%;
  justify-content: center;
  align-items: center;
}

.skill-container.connector-mode {
  cursor: default;
}

.skill-icon {
  width: 100%;
  height: 100%;
  object-fit: contain;
  transition: transform 0.1s;
  display: block;
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
}

.header {
  margin-bottom: 10px;
  text-align: left;
}

::v-deep .t-red { color: #FF5555 !important; }
::v-deep .t-aqua { color: #55FFFF !important; }
::v-deep .t-green { color: #55FF55 !important; }
::v-deep .t-white { color: #FFFFFF !important; }
::v-deep .t-yellow { color: #FFFF55 !important; }
::v-deep .t-pink { color: #FF55FF !important; }
::v-deep .t-gray { color: #555555 !important; }
::v-deep .t-blue { color: #55FFFF !important; }
::v-deep u { text-decoration: underline; }

.title-cn {
  font-size: 17px;
  font-weight: bold;
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

.desc-text {
  color: #AAAAAA;
}

.footer {
  margin-top: 10px;
  padding-top: 10px;
  border-top: 2px solid #333;
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
</style>
