<template>
    <div class="profession-card" @mousemove="moveTooltip">
        <div class="profession-selector-wrapper" ref="selectorRef">
            <div class="current-profession" @click="toggleSelector">
                <div class="prof-icon" :style="getSpriteStyle('ProfessionIcon', currentProfData.icon)"></div>
                <span class="prof-name">{{ currentProfData.name }}</span>
                <span class="dropdown-arrow">▼</span>
            </div>

            <transition name="slide-fade">
                <div v-if="isSelectorOpen" class="selector-dropdown">
                    <div v-for="(prof, index) in professions" :key="prof.id" class="selector-item"
                        :class="{ active: currentProfIndex === index }" @click="selectProfession(index)">
                        <div class="mini-icon" :style="getSpriteStyle('ProfessionIcon', prof.icon)"></div>
                        {{ prof.name }}
                    </div>
                </div>
            </transition>
        </div>

        <div class="header-section">
            <div class="level-slider-container">
                <div class="slider-track">
                    <div class="segment white" style="width: 9.09%"></div>
                    <div class="segment yellow" style="width: 18.18%"></div>
                    <div class="segment pink" style="width: 18.18%"></div>
                    <div class="segment blue" style="width: 18.18%"></div>
                    <div class="segment light-red" style="width: 18.18%"></div>
                    <div class="segment purple" style="width: 18.18%"></div>
                </div>

                <input type="range" v-model.number="currentLevel" min="1" max="110" class="slider-input"
                    :style="{ backgroundSize: ((currentLevel - 1) * 100 / 109) + '% 100%' }" />

                <div class="level-display">
                    <span>Current Level: <b>{{ currentLevel }}</b></span>
                    <span class="multiplier-tag">原料 x{{ currentMultiplier }} 倍率</span>
                </div>
            </div>
        </div>

        <div class="recipes-container">
            <div v-for="(recipe, index) in currentProfData.recipes" :key="index" class="recipe-group">
                <div class="slot product-slot" @mouseenter="showTooltip($event, recipe.name)" @mouseleave="hideTooltip">
                    <div class="slot-icon" :style="getSpriteStyle(recipe.spriteSource, recipe.outputIcon)"></div>
                </div>

                <div class="slot material-slot" @click="copyMaterialName(getMaterialName(recipe.mainMat))"
                    @mouseenter="showTooltip($event, getMaterialName(recipe.mainMat) + ' (点击复制)')"
                    @mouseleave="hideTooltip">
                    <div class="slot-icon" :style="getMaterialIconStyle(recipe.mainMat)"></div>
                    <span class="material-qty">x{{ Math.floor(recipe.baseQty.main * currentMultiplier) }}</span>
                </div>

                <div class="slot material-slot" @click="copyMaterialName(getMaterialName(recipe.subMat))"
                    @mouseenter="showTooltip($event, getMaterialName(recipe.subMat) + ' (点击复制)')"
                    @mouseleave="hideTooltip">
                    <div class="slot-icon" :style="getMaterialIconStyle(recipe.subMat)"></div>
                    <span class="material-qty">x{{ Math.floor(recipe.baseQty.sub * currentMultiplier) }}</span>
                </div>
            </div>
        </div>

        <div v-show="tooltip.visible" class="custom-tooltip"
            :style="{ top: tooltip.y + 15 + 'px', left: tooltip.x + 15 + 'px' }">
            {{ tooltip.text }}
        </div>

        <transition name="fade">
            <div v-if="showToast" class="copy-toast">已复制: {{ toastMsg }}</div>
        </transition>
    </div>
</template>

<script>
// ================= 路径配置 =================
// 请确保通过工具切好的小图全部放在 MATERIAL_BASE_PATH 目录下
const MATERIAL_BASE_PATH = '/assets/img/materials/'; 
const SPRITE_BASE_PATH = '/assets/img/sprites/';
const ICON_SIZE = 32;

// ================= UI Sprite 配置 =================
// 仅用于固定不变的图标（如头盔、武器、职业图标）
const SHEET_INFO = {
    'ProfessionIcon': { file: 'ProfessionIcon.png', cols: 12 },
    'ArmourSprites': { file: 'ArmourSprites.png', cols: 8 },
    'WeaponSprites': { file: 'WeaponSprites.png', cols: 11 },
    'AccessorySprites': { file: 'AccessorySprites.gif', cols: 7 }
};

// ================= 原料名称字典 =================
// 经过工程化重构，这里仅保留纯粹的字符串用于复制和显示
const MATERIAL_NAMES = {
    1: { wood: 'Oak Wood', paper: 'Oak Paper', ingot: 'Copper Ingot', gem: 'Copper Gem', string: 'Wheat String', grain: 'Wheat Grain', meat: 'Gudgeon Meat', oil: 'Gudgeon Oil' },
    10: { wood: 'Birch Wood', paper: 'Birch Paper', ingot: 'Granite Ingot', gem: 'Granite Gem', string: 'Barley String', grain: 'Barley Grain', meat: 'Trout Meat', oil: 'Trout Oil' },
    20: { wood: 'Willow Wood', paper: 'Willow Paper', ingot: 'Gold Ingot', gem: 'Gold Gem', string: 'Oat String', grain: 'Oat Grain', meat: 'Salmon Meat', oil: 'Salmon Oil' },
    30: { wood: 'Acacia Wood', paper: 'Acacia Paper', ingot: 'Sandstone Ingot', gem: 'Sandstone Gem', string: 'Malt String', grain: 'Malt Grain', meat: 'Carp Meat', oil: 'Carp Oil' },
    40: { wood: 'Spruce Wood', paper: 'Spruce Paper', ingot: 'Iron Ingot', gem: 'Iron Gem', string: 'Hops String', grain: 'Hops Grain', meat: 'Icefish Meat', oil: 'Icefish Oil' },
    50: { wood: 'Jungle Wood', paper: 'Jungle Paper', ingot: 'Silver Ingot', gem: 'Silver Gem', string: 'Rye String', grain: 'Rye Grain', meat: 'Piranha Meat', oil: 'Piranha Oil' },
    60: { wood: 'Dark Wood', paper: 'Dark Paper', ingot: 'Cobalt Ingot', gem: 'Cobalt Gem', string: 'Millet String', grain: 'Millet Grain', meat: 'Koi Meat', oil: 'Koi Oil' },
    70: { wood: 'Light Wood', paper: 'Light Paper', ingot: 'Kanderstone Ingot', gem: 'Kanderstone Gem', string: 'Decay String', grain: 'Decay Grain', meat: 'Gylia Meat', oil: 'Gylia Oil' },
    80: { wood: 'Pine Wood', paper: 'Pine Paper', ingot: 'Diamond Ingot', gem: 'Diamond Gem', string: 'Rice String', grain: 'Rice Grain', meat: 'Bass Meat', oil: 'Bass Oil' },
    90: { wood: 'Avo Wood', paper: 'Avo Paper', ingot: 'Molten Ingot', gem: 'Molten Gem', string: 'Sorghum String', grain: 'Sorghum Grain', meat: 'Molten Meat', oil: 'Molten Oil' },
    100: { wood: 'Sky Wood', paper: 'Sky Paper', ingot: 'Voidstone Ingot', gem: 'Voidstone Gem', string: 'Hemp String', grain: 'Hemp Grain', meat: 'Starfish Meat', oil: 'Starfish Oil' },
    110: { wood: 'Dernic Wood', paper: 'Dernic Paper', ingot: 'Dernic Ingot', gem: 'Dernic Gem', string: 'Dernic String', grain: 'Dernic Grain', meat: 'Dernic Fish Meat', oil: 'Dernic Oil' }
};

// 职业配方数据 (保持不变)
const PROFESSIONS = [
    {
        id: 'armouring', name: '盔甲师 (Armouring)', icon: { x: 6, y: 0 },
        recipes: [
            { name: 'Helmet', spriteSource: 'ArmourSprites', outputIcon: { x: 0, y: 2 }, mainMat: 'ingot', subMat: 'paper', baseQty: { main: 1, sub: 2 } },
            { name: 'Chestplate', spriteSource: 'ArmourSprites', outputIcon: { x: 1, y: 2 }, mainMat: 'ingot', subMat: 'paper', baseQty: { main: 2, sub: 1 } }
        ]
    },
    {
        id: 'tailoring', name: '裁缝 (Tailoring)', icon: { x: 7, y: 0 },
        recipes: [
            { name: 'Leggings', spriteSource: 'ArmourSprites', outputIcon: { x: 2, y: 2 }, mainMat: 'ingot', subMat: 'string', baseQty: { main: 2, sub: 1 } },
            { name: 'Boots', spriteSource: 'ArmourSprites', outputIcon: { x: 3, y: 2 }, mainMat: 'ingot', subMat: 'string', baseQty: { main: 1, sub: 2 } }
        ]
    },
    {
        id: 'weaponsmithing', name: '锻造师 (Weaponsmithing)', icon: { x: 4, y: 0 },
        recipes: [
            { name: 'Spear', spriteSource: 'WeaponSprites', outputIcon: { x: 9, y: 4 }, mainMat: 'ingot', subMat: 'wood', baseQty: { main: 1, sub: 2 } },
            { name: 'Dagger', spriteSource: 'WeaponSprites', outputIcon: { x: 9, y: 6 }, mainMat: 'ingot', subMat: 'wood', baseQty: { main: 2, sub: 1 } }
        ]
    },
    {
        id: 'woodworking', name: '木匠 (Woodworking)', icon: { x: 5, y: 0 },
        recipes: [
            { name: 'Bow', spriteSource: 'WeaponSprites', outputIcon: { x: 9, y: 2 }, mainMat: 'wood', subMat: 'string', baseQty: { main: 1, sub: 2 } },
            { name: 'Wand', spriteSource: 'WeaponSprites', outputIcon: { x: 9, y: 1 }, mainMat: 'wood', subMat: 'string', baseQty: { main: 2, sub: 1 } },
            { name: 'Relik', spriteSource: 'WeaponSprites', outputIcon: { x: 9, y: 8 }, mainMat: 'wood', subMat: 'oil', baseQty: { main: 1, sub: 2 } }
        ]
    },
    {
        id: 'jeweling', name: '珠宝家 (Jeweling)', icon: { x: 8, y: 0 },
        recipes: [
            { name: 'Ring', spriteSource: 'AccessorySprites', outputIcon: { x: 6, y: 5 }, mainMat: 'gem', subMat: 'oil', baseQty: { main: 1, sub: 1 } },
            { name: 'Bracelet', spriteSource: 'AccessorySprites', outputIcon: { x: 2, y: 0 }, mainMat: 'gem', subMat: 'oil', baseQty: { main: 2, sub: 1 } },
            { name: 'Necklace', spriteSource: 'AccessorySprites', outputIcon: { x: 2, y: 2 }, mainMat: 'gem', subMat: 'oil', baseQty: { main: 3, sub: 1 } }
        ]
    },
    {
        id: 'alchemism', name: '药剂师 (Alchemism)', icon: { x: 10, y: 0 },
        recipes: [
            { name: 'Potion', spriteSource: 'ProfessionIcon', outputIcon: { x: 10, y: 0 }, mainMat: 'grain', subMat: 'oil', baseQty: { main: 2, sub: 1 } }
        ]
    },
    {
        id: 'scribing', name: '卷轴师 (Scribing)', icon: { x: 9, y: 0 },
        recipes: [
            { name: 'Scroll', spriteSource: 'ProfessionIcon', outputIcon: { x: 1, y: 3 }, mainMat: 'paper', subMat: 'oil', baseQty: { main: 1, sub: 1 } }
        ]
    },
    {
        id: 'cooking', name: '厨师 (Cooking)', icon: { x: 11, y: 0 },
        recipes: [
            { name: 'Food', spriteSource: 'ProfessionIcon', outputIcon: { x: 6, y: 11 }, mainMat: 'grain', subMat: 'meat', baseQty: { main: 1, sub: 2 } }
        ]
    }
];

export default {
    name: 'ProfessionCard',
    data() {
        return {
            professions: PROFESSIONS,
            currentProfIndex: 0,
            currentLevel: 1,
            isSelectorOpen: false,
            showToast: false,
            toastMsg: '',
            tooltip: { visible: false, text: '', x: 0, y: 0 }
        };
    },
    computed: {
        currentProfData() { return this.professions[this.currentProfIndex]; },
        currentTierKey() {
            if (this.currentLevel < 10) return 1;
            return Math.floor(this.currentLevel / 10) * 10;
        },
        currentMultiplier() {
            const lv = this.currentLevel;
            if (lv >= 90) return 6;
            if (lv >= 70) return 5;
            if (lv >= 50) return 4;
            if (lv >= 30) return 3;
            if (lv >= 10) return 2;
            return 1;
        }
    },
    methods: {
        toggleSelector() { this.isSelectorOpen = !this.isSelectorOpen; },
        selectProfession(index) {
            this.currentProfIndex = index;
            this.isSelectorOpen = false;
        },
        showTooltip(event, text) {
            this.tooltip.text = text;
            this.tooltip.visible = true;
            this.moveTooltip(event);
        },
        moveTooltip(event) {
            if (this.tooltip.visible) {
                this.tooltip.x = event.clientX;
                this.tooltip.y = event.clientY;
            }
        },
        hideTooltip() { this.tooltip.visible = false; },

        // 获取原料名称
        getMaterialName(matType) {
            const namesAtTier = MATERIAL_NAMES[this.currentTierKey] || MATERIAL_NAMES[1];
            return namesAtTier[matType] || 'Unknown';
        },

        // 获取 UI 相关的 Sprite 样式
        getSpriteStyle(sourceKey, coords) {
            const info = SHEET_INFO[sourceKey];
            if (!info) return {};
            const bgWidth = info.cols * ICON_SIZE;
            return {
                backgroundImage: `url('${SPRITE_BASE_PATH}${info.file}')`,
                backgroundPosition: `-${coords.x * ICON_SIZE}px -${coords.y * ICON_SIZE}px`,
                backgroundSize: `${bgWidth}px auto`
            };
        },

        // 核心重构：彻底抛弃坐标映射，直接通过拼接路径获取被切好的独立图片
        getMaterialIconStyle(matType) {
            const tierKey = this.currentTierKey;
            return {
                backgroundImage: `url('${MATERIAL_BASE_PATH}${matType}_${tierKey}.png')`,
                backgroundSize: 'contain',
                backgroundRepeat: 'no-repeat'
            };
        },
        
        async copyMaterialName(text) {
            try {
                await navigator.clipboard.writeText(text);
                this.toastMsg = text;
                this.showToast = true;
                setTimeout(() => { this.showToast = false; }, 2000);
            } catch (err) {
                console.error('Failed to copy', err);
            }
        }
    }
};
</script>

<style scoped>
/* ======================================================
  这里的 CSS 样式与之前版本完全保持一致，无需任何改动。
  为了精简代码展示长度，如果你在本地编辑器中替换，
  直接将上方的 <template> 和 <script> 覆盖掉，
  底部的 <style scoped> 原封不动保留即可。
======================================================
*/
/* 基础容器 */
.profession-card {
    position: relative;
    border: 1px solid #e2e2e2;
    border-radius: 8px;
    padding: 60px 24px 32px 24px;
    background-color: #fafafa;
    max-width: 720px;
    font-family: sans-serif;
    user-select: none;
    min-height: 160px;
    display: flex;
    flex-direction: column;
    gap: 24px;
}

/* 1. 职业选择器 (宽度增加到 280px) */
.profession-selector-wrapper {
    position: absolute;
    top: 0;
    left: 0;
    z-index: 20;
    width: 320px;
}

.current-profession {
    display: flex;
    align-items: center;
    background: white;
    border-right: 1px solid #ccc;
    border-bottom: 1px solid #ccc;
    border-radius: 8px 0 16px 0;
    padding: 12px 16px;
    cursor: pointer;
    transition: all 0.2s;
    height: 50px;
    box-sizing: border-box;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.05);
}

.current-profession:hover {
    background-color: #f9f9f9;
    box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
}

.prof-icon,
.mini-icon {
    width: 32px;
    height: 32px;
    image-rendering: pixelated;
    flex-shrink: 0;
}

.prof-name {
    margin: 0 12px;
    font-weight: bold;
    font-size: 16px;
    flex-grow: 1;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #333;
}

.dropdown-arrow {
    font-size: 12px;
    color: #888;
}

/* 磁吸列表 */
.selector-dropdown {
    position: absolute;
    top: 100%;
    left: 4px;
    width: 95%;
    max-height: 350px;
    overflow-y: auto;
    background: white;
    border: 1px solid #eee;
    border-radius: 0 0 8px 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.selector-item {
    display: flex;
    align-items: center;
    padding: 10px 14px;
    cursor: pointer;
    transition: background 0.1s;
    font-size: 14px;
}

.selector-item:hover,
.selector-item.active {
    background-color: #f0f0f0;
}

.selector-item .mini-icon {
    margin-right: 10px;
    transform: scale(0.8);
}

/* 2. 等级进度条区域 */
.header-section {
    display: flex;
    justify-content: flex-end;
}

.level-slider-container {
    width: 100%;
    max-width: 500px;
    position: relative;
    display: flex;
    flex-direction: column;
}

.slider-track {
    display: flex;
    height: 16px;
    border-radius: 8px;
    overflow: hidden;
    border: 1px solid #ccc;
    position: absolute;
    width: 100%;
    top: 10px;
    z-index: 0;
}

.segment { height: 100%; }
.segment.white { background-color: #ffffff; }
.segment.yellow { background-color: #fffacd; }
.segment.pink { background-color: #ffe4e1; }
.segment.blue { background-color: #e0ffff; }
.segment.light-red { background-color: #ffcccb; }
.segment.purple { background-color: #e6e6fa; }

.slider-input {
    -webkit-appearance: none;
    width: 100%;
    height: 16px;
    background: transparent;
    position: relative;
    z-index: 1;
    outline: none;
    margin: 10px 0 0 0;
}

.slider-input::-webkit-slider-thumb {
    -webkit-appearance: none;
    height: 24px;
    width: 12px;
    background: #3eaf7c;
    border: 2px solid white;
    border-radius: 4px;
    cursor: ew-resize;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
    margin-top: -5px;
}

.level-display {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 13px;
    color: #666;
    margin-top: 8px;
}

.multiplier-tag {
    background: #3eaf7c;
    color: white;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 12px;
    font-weight: bold;
}

/* 3. 配方展示区域 */
.recipes-container {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    padding: 4px;
}

.recipe-group {
    display: flex;
    align-items: center;
    background: white;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 12px;
    gap: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.03);
    transition: transform 0.2s;
}

.recipe-group:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 12px rgba(0, 0, 0, 0.08);
}

.slot {
    width: 48px;
    height: 48px;
    background: #f3f3f3;
    border: 1px solid #ccc;
    border-radius: 6px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    cursor: default;
}

.product-slot {
    background: #e8f5e9;
    border-color: #a5d6a7;
    margin-right: 8px;
}

.material-slot {
    cursor: pointer;
}

.material-slot:hover {
    background: #e3f2fd;
    border-color: #90caf9;
}

.slot-icon {
    width: 32px;
    height: 32px;
    image-rendering: pixelated;
}

.material-qty {
    position: absolute;
    bottom: 1px;
    right: 3px;
    font-size: 11px;
    color: #333;
    font-weight: 800;
    text-shadow: 0 0 2px white;
}

/* 4. 自定义 Tooltip */
.custom-tooltip {
    position: fixed;
    background: rgba(0, 0, 0, 0.85);
    color: white;
    padding: 6px 10px;
    border-radius: 4px;
    font-size: 12px;
    pointer-events: none;
    z-index: 9999;
    white-space: nowrap;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.copy-toast {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: #3eaf7c;
    color: #fff;
    padding: 8px 20px;
    border-radius: 20px;
    font-size: 14px;
    pointer-events: none;
    z-index: 999;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.slide-fade-enter-active,
.slide-fade-leave-active {
    transition: all 0.2s ease;
}

.slide-fade-enter,
.slide-fade-leave-to {
    transform: translateY(-10px);
    opacity: 0;
}

.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.3s;
}

.fade-enter,
.fade-leave-to {
    opacity: 0;
}
</style>