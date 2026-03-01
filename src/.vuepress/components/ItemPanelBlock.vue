<template>
    <div class="item-window">
        <img v-if="icon" :src="icon" :alt="item.name" class="item-icon">

        <div class="item-details">
            <p class="item-header">
                <span class="item-name" :class="item.tier?.toLowerCase()">{{ item.displayName || item.name }}</span><br>
                <span v-if="item.atkSpd" class="item-attribute">{{ formatEnum(item.atkSpd) }} Attack Speed</span>
            </p>

            <p class="damage">
                <span v-if="item.hp" class="health">❤ Health: +{{ item.hp }}</span><br v-if="item.hp">

                <span v-if="isNonZeroDamage(item.nDam)" class="neutral-damage">✤ Neutral Damage: {{ item.nDam
                }}<br></span>
                <span v-if="isNonZeroDamage(item.eDam)"><span><span class="earth">❋ Earth</span> <span
                            class="gray">Damage: {{ item.eDam }}</span></span><br></span>
                <span v-if="isNonZeroDamage(item.tDam)"><span><span class="thunder">✦ Thunder</span> <span
                            class="gray">Damage: {{ item.tDam }}</span></span><br></span>
                <span v-if="isNonZeroDamage(item.wDam)"><span><span class="water">❉ Water</span> <span
                            class="gray">Damage: {{ item.wDam }}</span></span><br></span>
                <span v-if="isNonZeroDamage(item.fDam)"><span><span class="fire">✹ Fire</span> <span
                            class="gray">Damage: {{ item.fDam }}</span></span><br></span>
                <span v-if="isNonZeroDamage(item.aDam)"><span><span class="air">❋ Air</span> <span class="gray">Damage:
                            {{ item.aDam }}</span></span><br></span>

                <span v-if="item.averageDps">
                    <span style="visibility: hidden;">✤ </span><span class="average-dps">Average DPS:</span> <span
                        class="gray">{{ item.averageDps }}</span><br>
                </span>

                <span v-if="item.eDef"><span><span class="earth">❋ Earth</span> <span class="gray">Defence: {{ item.eDef
                }}</span></span><br></span>
                <span v-if="item.tDef"><span><span class="thunder">✦ Thunder</span> <span class="gray">Defence: {{
                    item.tDef }}</span></span><br></span>
                <span v-if="item.wDef"><span><span class="water">❉ Water</span> <span class="gray">Defence: {{ item.wDef
                }}</span></span><br></span>
                <span v-if="item.fDef"><span><span class="fire">✹ Fire</span> <span class="gray">Defence: {{ item.fDef
                }}</span></span><br></span>
                <span v-if="item.aDef"><span><span class="air">❋ Air</span> <span class="gray">Defence: {{ item.aDef
                }}</span></span><br></span>
            </p>

            <p class="requirements"
                v-if="item.classReq || item.lvl || item.strReq || item.dexReq || item.intReq || item.defReq || item.agiReq">
                <template v-if="item.classReq">Class Req: {{ capitalize(item.classReq) }}<br></template>
                <template v-if="item.lvl">Combat Lv. Min: {{ item.lvl }}<br></template>
                <template v-if="item.strReq">Strength Min: {{ item.strReq }}<br></template>
                <template v-if="item.dexReq">Dexterity Min: {{ item.dexReq }}<br></template>
                <template v-if="item.intReq">Intelligence Min: {{ item.intReq }}<br></template>
                <template v-if="item.defReq">Defence Min: {{ item.defReq }}<br></template>
                <template v-if="item.agiReq">Agility Min: {{ item.agiReq }}<br></template>
            </p>

            <p class="attribute-bonus" v-if="item.str || item.dex || item.int || item.def || item.agi">
                <template v-if="item.str"><span :class="item.str > 0 ? 'bonus-positive' : 'bonus-negative'">{{ item.str
                    > 0 ? '+' : '' }}{{ item.str }}</span> Strength<br></template>
                <template v-if="item.dex"><span :class="item.dex > 0 ? 'bonus-positive' : 'bonus-negative'">{{ item.dex
                    > 0 ? '+' : '' }}{{ item.dex }}</span> Dexterity<br></template>
                <template v-if="item.int"><span :class="item.int > 0 ? 'bonus-positive' : 'bonus-negative'">{{ item.int
                    > 0 ? '+' : '' }}{{ item.int }}</span> Intelligence<br></template>
                <template v-if="item.def"><span :class="item.def > 0 ? 'bonus-positive' : 'bonus-negative'">{{ item.def
                    > 0 ? '+' : '' }}{{ item.def }}</span> Defence<br></template>
                <template v-if="item.agi"><span :class="item.agi > 0 ? 'bonus-positive' : 'bonus-negative'">{{ item.agi
                    > 0 ? '+' : '' }}{{ item.agi }}</span> Agility<br></template>
            </p>

            <p class="bonuses" v-if="identifications.length > 0 || majorIds.length > 0">
                <template v-for="(id, index) in identifications" :key="index">
                    <span :class="id.isPositive ? 'bonus-positive' : 'bonus-negative'">
                        {{ id.min > 0 ? '+' : '' }}{{ id.min }} <span
                            :class="id.isPositive ? 'bonus-to' : 'bonus-to-negative'">to</span> {{ id.max > 0 ? '+' : ''
                            }}{{ id.max }}{{ id.suffix }}
                    </span> {{ id.name }}<br>
                </template>

                <template v-for="(mid, index) in majorIds" :key="'major-'+index">
                    <span class="major-id-name">+{{ mid.name }}:</span>
                    <span class="major-id-desc" v-html="formatMajorIdDesc(mid.description)"></span><br>
                </template>
            </p>

            <p class="powder-rarity">
                <template v-if="item.slots">[{{ item.slots }}] Powder slots<br></template>
                <span class="rarity" :class="item.tier?.toLowerCase()">{{ item.tier }} Item</span>
            </p>
        </div>
    </div>
</template>

<script setup>
defineProps({
    item: Object,
    icon: String,
    identifications: Array,
    majorIds: Array
});

// 首字母大写函数
const capitalize = (str) => {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
};

const formatEnum = (str) => {
    if (!str) return '';
    return str.split('_').map(capitalize).join(' ');
};

// 【新增逻辑 1】：判断是否为有效的、非 0-0 伤害
const isNonZeroDamage = (damStr) => {
    if (!damStr) return false;
    return damStr !== "0-0" && damStr !== "0";
};

// 【新增逻辑 2】：解析 Major ID 描述内的特殊元素标签 [element]
const elementMapping = {
    neutral: { symbol: '✤', className: 'neutral-damage' },
    earth: { symbol: '❋', className: 'earth' },
    thunder: { symbol: '✦', className: 'thunder' },
    water: { symbol: '❉', className: 'water' },
    fire: { symbol: '✹', className: 'fire' },
    air: { symbol: '❋', className: 'air' }
};

const formatMajorIdDesc = (desc) => {
    if (!desc) return '';
    // 正则匹配例如 "[fire]+50%" 或者 "[neutral]"
    // $1 是元素名称(如 fire)，$2 是可能跟随的数值(如 +50%)
    return desc.replace(/\[(neutral|earth|thunder|water|fire|air)\]([+\-0-9%]*)/gi, (match, elem, val) => {
        const el = elementMapping[elem.toLowerCase()];
        if (!el) return match;
        // 将其包裹在对应属性的 span 类中，应用颜色
        return `<span class="${el.className}">${el.symbol}${val}</span>`;
    });
};
</script>

<style scoped>
/* 这里直接粘贴你原本提供的 CSS 样式即可 */
.item-window {
    border: 2px solid #9400D3;
    background-color: #1a1a1a;
    color: #fff;
    padding: 10px;
    width: 300px;
    font-family: ui-sans-serif, system-ui, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;
    text-align: left;
    /* 修正tooltip里可能继承居中的问题 */
}

/* 品质类颜色 */
.mythic {
    color: rgb(164, 57, 192);
}

.fabled {
    color: #FF5555;
}

.legendary {
    color: #55FFFF;
}

.set {
    color: #55FF55;
}

.rare {
    color: #FF55FF;
}

/* * 元素色彩控制
 * 注意：使用 :deep() 是为了确保这些样式能够穿透 Vue 的 scoped 隔离，
 * 正确渲染到由 v-html (即 formatMajorIdDesc 解析出来的标签) 生成的文本上。
 */
:deep(.health) {
    color: rgb(170, 0, 0);
}

:deep(.neutral-damage) {
    color: rgb(255, 170, 0);
}

:deep(.fire) {
    color: rgb(255, 85, 85);
}

:deep(.water) {
    color: #00FFFF;
}

:deep(.air) {
    color: #FFFFFF;
}

:deep(.thunder) {
    color: #FFFF00;
}

:deep(.earth) {
    color: rgb(0, 170, 0);
}

.major-id-name {
    color: #55FFFF;
}

.major-id-desc {
    color: #00AAAA;
}

.item-icon {
    width: 50px;
    height: 50px;
    display: block;
    margin: 0 auto;
}

.item-header {
    text-align: center;
}

.item-name {
    color: rgb(164, 57, 192);
    font-size: 20px;
    font-weight: bold;
}

.item-attribute {
    font-size: 16px;
    margin-top: 5px;
    color: rgb(170, 170, 170);
}

.damage {
    font-size: 16px;
}

.health {
    color: rgb(170, 0, 0);
}


.neutral-damage {
    color: rgb(255, 170, 0);
}

.fire {
    color: rgb(255, 85, 85);
}

.water {
    color: #00FFFF;
}

.air {
    color: #FFFFFF;
}

.thunder {
    color: #FFFF00;
}

.earth {
    color: rgb(0, 170, 0);
}

.gray {
    color: rgb(170, 170, 170);
}

.average-dps {
    color: rgb(85, 85, 85);
}

.requirements,
.attribute-bonus,
.bonuses,
.powder-rarity {
    font-size: 14px;
    color: rgb(170, 170, 170);
}

.requirements {
    margin-top: 10px;
}

.bonuses {
    margin-top: 10px;
}

.bonus-positive {
    color: rgb(85, 255, 85);
}

.bonus-negative {
    color: rgb(255, 85, 85);
}

.bonus-to {
    color: rgb(0, 170, 0);
}

.bonus-to-negative {
    color: rgb(170, 0, 0);
}

.major-id-name {
    color: #55FFFF;
}

.major-id-desc {
    color: #00AAAA;
}

.powder-rarity {
    margin-top: 10px;
}

.rarity {
    color: rgb(164, 57, 192);
    text-align: left;
}

/* ... 剩下的 CSS ... */
.mythic {
    color: rgb(164, 57, 192);
}

.legendary {
    color: #55FFFF;
}

/* ... 你原本的颜色类 ... */
</style>