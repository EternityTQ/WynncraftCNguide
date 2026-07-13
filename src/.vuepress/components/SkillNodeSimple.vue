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
            ({{ skill ? skill.display_name : name }})
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
import atreeData from './data/atree.json';
import transArcherData from './data/zh-cn-archer.json';
import transWarriorData from './data/zh-cn-warrior.json';
import transMageData from './data/zh-cn-mage.json';
import transAssassinData from './data/zh-cn-assassin.json';
import transShamanData from './data/zh-cn-shaman.json';

const MAIN_WIDTH = 300;
const SIDE_WIDTH = 200;
const GAP = 10;
const OFFSET = 15;

// 汉化数据映射
const transDataMap = {
  Archer: transArcherData,
  Warrior: transWarriorData,
  Mage: transMageData,
  Assassin: transAssassinData,
  Shaman: transShamanData
};

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
    // 从 atree.json 获取技能基础数据（包含 icon 和 archetype）
    skill() {
      const classSkills = atreeData[this.currentClass];
      if (!classSkills) return null;
      return classSkills.find(s => s.display_name === this.name);
    },
    // 从对应职业的 zh-cn-{class}.json 获取翻译数据
    trans() {
      const transData = transDataMap[this.currentClass];
      if (!transData || !transData.abilities) return null;
      return transData.abilities[this.name];
    },
    transName() {
      // 优先使用 customName（汉化名），如果没有或为空则使用去格式码的 name
      if (this.trans && this.trans.customName && this.trans.customName.trim() !== '') {
        return this.trans.customName;
      }
      if (this.trans && this.trans.name) {
        return this.stripMinecraftFormatting(this.trans.name);
      }
      return this.skill ? this.skill.display_name : this.name;
    },
    archetypeInfo() {
      if (!this.skill || !this.skill.archetype) return null;

      const archKey = this.skill.archetype;
      const archName = this.archetypeMap[archKey] || archKey;

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
    titleColorClass() {
      if (!this.skill) return 't-white';
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
      } else if (this.skill && this.skill.desc) {
        rawText = `<span class="t-red" style="font-size:12px; display:block; margin-bottom:8px;">(暂无中文翻译)</span>` + this.skill.desc;
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
      // 处理转义
      const ESCAPED_SECTION = '{{__ESC_SECTION__}}';
      const ESCAPED_AMP = '{{__ESC_AMP__}}';
      text = text.replace(/\\§/g, ESCAPED_SECTION).replace(/\\&/g, ESCAPED_AMP);

      // 将 & 统一替换为 §，然后移除所有格式码
      text = text.replace(/&/g, '§');
      text = text.replace(/§[0-9a-fk-or]/gi, '').replace(/§[ghijklmno]/gi, '');

      // 还原转义字符
      text = text.replace(new RegExp(ESCAPED_SECTION, 'g'), '§').replace(new RegExp(ESCAPED_AMP, 'g'), '&');
      return text;
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

      // 先处理转义：将 \§ 和 \& 替换为临时占位符
      const ESCAPED_SECTION = '{{__ESC_SECTION__}}';
      const ESCAPED_AMP = '{{__ESC_AMP__}}';
      text = text.replace(/\\§/g, ESCAPED_SECTION).replace(/\\&/g, ESCAPED_AMP);

      // 将 & 统一替换为 §
      text = text.replace(/&/g, '§');

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

          // 自定义十六进制颜色代码 §#RRGGBB
          if (code === '#' && i + 8 <= text.length) {
            const hexColor = text.substring(i + 2, i + 8);
            if (/^[0-9a-f]{6}$/i.test(hexColor)) {
              currentColor = '#' + hexColor.toUpperCase();
              // 颜色代码会重置所有格式
              isBold = false;
              isItalic = false;
              isUnderline = false;
              isStrikethrough = false;
              i += 8;
              continue;
            }
          }

          // 颜色代码 - 重置格式状态但保留颜色
          if ('0123456789abcdefg'.includes(code)) {
            currentColor = this.getColorHex(code);
            // 颜色代码会重置所有格式
            isBold = false;
            isItalic = false;
            isUnderline = false;
            isStrikethrough = false;
          }
          // 跳过可视化编辑器的特殊格式码 (§h§i§j§k 用于标记技能类型)
          else if ('hijk'.includes(code)) {
            // 直接跳过，不做处理
          }
          // 格式代码 - 累加效果
          else if (code === 'l') isBold = true;
          else if (code === 'o') isItalic = true;
          else if (code === 'n') isUnderline = true;
          else if (code === 'm') isStrikethrough = true;
          else if (code === 'r') {
            // 重置所有
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

      // 还原转义字符
      result = result.replace(new RegExp(ESCAPED_SECTION, 'g'), '§').replace(new RegExp(ESCAPED_AMP, 'g'), '&');

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
/* 字体定义 */
@font-face {
  font-family: 'minecraft';
  src: url('/fonts/minecraft.woff');
  font-weight: normal;
  font-style: normal;
  font-display: block;
  text-rendering: optimizeLegibility;
}

@font-face {
  font-family: 'icons';
  src: url('/fonts/icons.woff');
  font-weight: normal;
  font-style: normal;
  font-display: block;
  text-rendering: optimizeLegibility;
}

@font-face {
  font-family: 'minecraft';
  src: url('/fonts/minecraft_bold.woff');
  font-weight: 900;
  font-style: normal;
  font-display: block;
  text-rendering: optimizeLegibility;
}

@font-face {
  font-family: 'mojangles';
  src: url('/fonts/mojangles.otf');
  font-weight: normal;
  font-style: normal;
  font-display: block;
  text-rendering: optimizeLegibility;
}

@font-face {
  font-family: 'unifont';
  src: url('/fonts/unifont.otf');
  font-weight: normal;
  font-style: normal;
  font-display: block;
  text-rendering: optimizeLegibility;
}

@font-face {
  font-family: 'unifontEmoji';
  src: url('/fonts/unifontEmoji.otf');
  font-weight: normal;
  font-style: normal;
  font-display: block;
  text-rendering: optimizeLegibility;
}

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

.icon-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
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
  font-family: minecraft, icons, mojangles, unifont, unifontEmoji, sans-serif;
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
  font-family: minecraft, icons, mojangles, unifont, unifontEmoji, sans-serif;
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
