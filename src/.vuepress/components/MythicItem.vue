<template>
    <span v-if="mode === 'inline'" class="mythic-inline-wrapper" @mouseenter="showTooltip = true"
        @mouseleave="showTooltip = false">
        <span class="inline-text">
            <slot>{{ name }}</slot>
        </span>

        <Transition name="fade">
            <div v-show="showTooltip" class="mythic-tooltip">
                <ItemPanelBlock :item="itemData" :icon="iconUrl" :identifications="identifications"
                    :major-ids="majorIds" />
            </div>
        </Transition>
    </span>

    <div v-else class="mythic-block-wrapper">
        <ItemPanelBlock :item="itemData" :icon="iconUrl" :identifications="identifications" :major-ids="majorIds" />
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// 引入你存放在 data 目录下的 JSON 数据
import itemsJson from './data/items.json';
import majidJson from './data/majid.json';
import mythicIconsJson from './data/mythic-icons.json';

// 为了防止代码太长，把 UI 渲染部分写为内部私有组件 (可以直接在 setup 里写，或者拆出去)
import ItemPanelBlock from './ItemPanelBlock.vue';

const props = defineProps({
    name: {
        type: String,
        required: true
    },
    mode: {
        type: String,
        default: 'block', // 可选: 'block' | 'inline'
    }
});

const showTooltip = ref(false);

// 1. 获取对应物品的底层数据
const itemData = computed(() => {
    // 通过名称或展示名称匹配（预防大小写问题，最好统一转小写匹配，这里直接按你原本的名字查找）
    return itemsJson.items.find(i => i.name === props.name || i.displayName === props.name) || {};
});

// 2. 匹配图标 (仅限神话物品且有对应图标配置)
const iconUrl = computed(() => {
    if (itemData.value.tier === 'Mythic' && mythicIconsJson[props.name]) {
        return mythicIconsJson[props.name];
    }
    return null;
});

// 3. 鉴定范围计算 (正数 30%~130%，负数 70%~130%但70%是极品/最大值)
const calcRoll = (val, lowerIsBetter = false) => {
    if (val === 0) return { min: 0, max: 0, isPositive: true };

    let min, max, isPositive;

    if (!lowerIsBetter) {
        // 【常规词条】：越高越好
        if (val > 0) {
            min = Math.round(val * 0.3); // 最烂 30%
            max = Math.round(val * 1.3); // 最好 130%
            isPositive = true;
        } else {
            min = Math.round(val * 1.3); // 最烂 130% (扣得最多)
            max = Math.round(val * 0.7); // 最好 70%  (扣得最少)
            isPositive = false;
        }
    } else {
        // 【Cost类词条】：越低越好 (降低蓝耗为正面，增加蓝耗为负面)
        if (val > 0) {
            min = Math.round(val * 1.3); // 加蓝耗，最烂 130%
            max = Math.round(val * 0.7); // 加蓝耗，最好 70%
            isPositive = false;          // 颜色判为红
        } else {
            min = Math.round(val * 0.3); // 减蓝耗，最烂 30% (减得少)
            max = Math.round(val * 1.3); // 减蓝耗，最好 130% (减得多)
            isPositive = true;           // 颜色判为绿
        }
    }

    // 无论如何，min 永远代表最烂(左)，max 永远代表最好(右)
    return { min, max, isPositive };
};

// 4. 技能耗蓝文本字典映射
const spellNames = {
    "warrior": ["Bash", "Charge", "Uppercut", "War Scream"],
    "mage": ["Heal", "Teleport", "Meteor", "Ice Snake"],
    "archer": ["Arrow Storm", "Escape", "Arrow Bomb", "Arrow Shield"],
    "assassin": ["Spin Attack", "Dash", "Multihit", "Smoke Bomb"],
    "shaman": ["Totem", "Haul", "Aura", "Uproot"]
};

// 5. 普通词条翻译字典 (带有后缀信息)
const idMap = {
    hpBonus: { name: 'Health', suffix: '' },
    hprRaw: { name: 'Health Regen', suffix: '' },
    hprPct: { name: 'Health Regen', suffix: '%' },
    mr: { name: 'Mana Regen', suffix: '/5s' },
    ms: { name: 'Mana Steal', suffix: '/3s' },
    ls: { name: 'Life Steal', suffix: '/3s' },
    mdRaw: { name: 'Main Attack Damage', suffix: '' },
    mdPct: { name: 'Main Attack Damage', suffix: '%' },
    sdRaw: { name: 'Spell Damage', suffix: '' },
    sdPct: { name: 'Spell Damage', suffix: '%' },
    rDamPct: { name: 'Elemental Damage', suffix: '%' },
    poison: { name: 'Poison', suffix: '/3s' },
    expd: { name: 'Exploding', suffix: '%' },
    spd: { name: 'Walk Speed', suffix: '%' },
    sprint: { name: 'Sprint', suffix: '%' },
    sprintReg: { name: 'Sprint Regen', suffix: '%' },
    jh: { name: 'Jump Height', suffix: '' },
    xpb: { name: 'Xp Bonus', suffix: '%' },
    lb: { name: 'Loot Bonus', suffix: '%' },
    thorns: { name: 'Thorns', suffix: '%' },
    ref: { name: 'Reflection', suffix: '%' },
    healPct: { name: 'Healing Efficiency', suffix: '%' },
    eSteal: { name: 'Stealing', suffix: '%' },
    critDamPct: { name: 'Critical Damage Bonus', suffix: '%' },
    kb: { name: 'Knockback', suffix: '%' },
    weakenEnemy: { name: 'Weaken Enemy', suffix: '%' },
    slowEnemy: { name: 'Slow Enemy', suffix: '%' },
    eDamPct: { name: 'Earth Damage', suffix: '%' },
    tDamPct: { name: 'Thunder Damage', suffix: '%' },
    wDamPct: { name: 'Water Damage', suffix: '%' },
    fDamPct: { name: 'Fire Damage', suffix: '%' },
    aDamPct: { name: 'Air Damage', suffix: '%' },
    eDefPct: { name: 'Earth Defence', suffix: '%' },
    tDefPct: { name: 'Thunder Defence', suffix: '%' },
    wDefPct: { name: 'Water Defence', suffix: '%' },
    fDefPct: { name: 'Fire Defence', suffix: '%' },
    aDefPct: { name: 'Air Defence', suffix: '%' },
};

// 6. 计算装备的所有鉴定词条
const identifications = computed(() => {
  const item = itemData.value;
  if (!item.name) return [];
  
  const results = [];
  
  // 遍历普通词条 (默认越高越好，传 false)
  for (const [key, meta] of Object.entries(idMap)) {
    if (item[key]) {
      const { min, max, isPositive } = calcRoll(item[key], false);
      results.push({ name: meta.name, min, max, suffix: meta.suffix, isPositive });
    }
  }

  // 动态处理技能耗蓝词条 (spPct1~4, spRaw1~4)
  const cls = (item.classReq || "").toLowerCase();
  for (let i = 1; i <= 4; i++) {
    const spellName = (spellNames[cls] && spellNames[cls][i - 1]) 
      ? `${spellNames[cls][i - 1]} Cost` 
      : `${i}st Spell Cost`;

    // Cost类词条，lowerIsBetter 传 true
    if (item[`spRaw${i}`]) {
      const { min, max, isPositive } = calcRoll(item[`spRaw${i}`], true);
      results.push({ name: spellName, min, max, suffix: '', isPositive });
    }
    if (item[`spPct${i}`]) {
      const { min, max, isPositive } = calcRoll(item[`spPct${i}`], true);
      results.push({ name: spellName, min, max, suffix: '%', isPositive });
    }
  }

  return results;
});

// 7. 提取 Major IDs 并映射名字与描述
const majorIds = computed(() => {
    const item = itemData.value;
    if (!item.majorIds || !Array.isArray(item.majorIds)) return [];

    return item.majorIds.map(id => {
        const majorData = majidJson[id] || {};
        return {
            name: majorData.displayName || id, // 修正为读取 displayName
            description: majorData.description || "Unknown Major ID effect."
        };
    });
});
</script>

<style scoped>
/* 行内文字样式 */
.inline-text {
    color: #9400D3;
    text-decoration: underline dashed;
    cursor: help;
    font-weight: bold;
}

.mythic-inline-wrapper {
    position: relative;
    display: inline-block;
}

/* Tooltip 悬浮窗定位 */
.mythic-tooltip {
    position: absolute;
    bottom: 120%;
    /* 悬浮在文字正上方 */
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    width: max-content;
    pointer-events: none;
    /* 防止鼠标穿透引发闪烁 */
}

/* 渐隐渐现动画 */
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
    opacity: 0;
    transform: translate(-50%, 5px);
}
</style>