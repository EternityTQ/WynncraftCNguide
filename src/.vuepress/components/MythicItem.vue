<template>
  <span 
    v-if="mode === 'inline'" 
    class="mythic-inline-wrapper" 
    @mouseenter="handleMouseEnter" 
    @mouseleave="handleMouseLeave"
    ref="wrapperRef"
  >
    <span class="inline-text" :class="itemTierClass" ref="slotRef">
      <slot>{{ name }}</slot>
    </span>
    
    <ClientOnly>
      <Teleport to="body">
        <Transition name="fade">
          <div 
            v-if="showTooltip" 
            class="mythic-tooltip-teleported"
            :style="tooltipStyle"
          >
            <ItemPanelBlock 
              v-if="hasValidData"
              :item="itemData" 
              :icon="iconUrl" 
              :identifications="identifications" 
              :major-ids="majorIds" 
            />
            <div v-else class="mythic-error-panel">
              [物品数据读取失败: {{ resolvedName }}]
            </div>
          </div>
        </Transition>
      </Teleport>
    </ClientOnly>
  </span>

  <div v-else class="mythic-block-wrapper">
    <ItemPanelBlock 
      v-if="hasValidData"
      :item="itemData" 
      :icon="iconUrl" 
      :identifications="identifications" 
      :major-ids="majorIds" 
    />
    <div v-else class="mythic-error-panel" style="width: 300px;">
      [物品数据读取失败: {{ resolvedName }}]
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

import itemsJson from './data/items.json';
import majidJson from './data/majid.json';
import mythicIconsJson from './data/mythic-icons.json';

import ItemPanelBlock from './ItemPanelBlock.vue'; 

const props = defineProps({
  name: {
    type: String,
    default: '' 
  },
  mode: {
    type: String,
    default: 'block'
  }
});

const slotRef = ref(null);
const wrapperRef = ref(null);
const slotText = ref(''); // 专门用于保存插槽提取到的文本

// 挂载后：尝试读取插槽内的纯文本并去除首尾空格
onMounted(() => {
  if (slotRef.value) {
    slotText.value = slotRef.value.textContent.trim();
  }
});

// 计算出最终查询用的名字 (优先用传入的 props.name，否则用插槽文本)
const resolvedName = computed(() => props.name || slotText.value);

// 获取对应物品的底层数据
const itemData = computed(() => {
  const targetName = resolvedName.value;
  if (!targetName) return {};
  return itemsJson.items.find(i => 
    i.name.toLowerCase() === targetName.toLowerCase() || 
    (i.displayName && i.displayName.toLowerCase() === targetName.toLowerCase())
  ) || {};
});

// 检查是否真实读取到了数据
const hasValidData = computed(() => Object.keys(itemData.value).length > 0);

// 品质颜色类名
const itemTierClass = computed(() => {
  if (!hasValidData.value) return '';
  return itemData.value.tier ? itemData.value.tier.toLowerCase() : '';
});

// 匹配图标
const iconUrl = computed(() => {
  if (itemData.value.tier !== 'Mythic') return null;
  const baseName = resolvedName.value.replace(/^Masterwork\s+/i, '');
  return mythicIconsJson[baseName] || null;
});

// 鉴定范围计算 (包含 Cost 类词条的反转逻辑)
const calcRoll = (val, lowerIsBetter = false, isFixed = false) => {
  if (val === 0) return { min: 0, max: 0, isPositive: true };
  let min, max, isPositive;
  
  if (!lowerIsBetter) {
    // 常规词条
    isPositive = val > 0;
    if (isFixed) {
      min = val; max = val;
    } else {
      if (val > 0) {
        min = Math.round(val * 0.3); max = Math.round(val * 1.3);
      } else {
        min = Math.round(val * 1.3); max = Math.round(val * 0.7);
      }
    }
  } else {
    // 耗蓝类词条 (越低越好)
    isPositive = val < 0; // 减少蓝耗为正收益，增加为负收益
    if (isFixed) {
      min = val; max = val;
    } else {
      if (val > 0) {
        min = Math.round(val * 1.3); max = Math.round(val * 0.7);
      } else {
        min = Math.round(val * 0.3); max = Math.round(val * 1.3);
      }
    }
  }
  return { min, max, isPositive };
};

const spellNames = {
  "warrior": ["Bash", "Charge", "Uppercut", "War Scream"],
  "mage": ["Heal", "Teleport", "Meteor", "Ice Snake"],
  "archer": ["Arrow Storm", "Escape", "Arrow Bomb", "Arrow Shield"],
  "assassin": ["Spin Attack", "Dash", "Multihit", "Smoke Bomb"],
  "shaman": ["Totem", "Haul", "Aura", "Uproot"]
};

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
  eSdRaw: { name: 'Earth Spell Damage', suffix: '' },
  tSdRaw: { name: 'Thunder Spell Damage', suffix: '' },
  wSdRaw: { name: 'Water Spell Damage', suffix: '' },
  fSdRaw: { name: 'Fire Spell Damage', suffix: '' },
  aSdRaw: { name: 'Air Spell Damage', suffix: '' },
  maxMana: { name: 'Max Mana', suffix: '' },
  eMdRaw: { name: 'Earth Main Attack Damage', suffix: '' },
  tMdRaw: { name: 'Thunder Main Attack Damage', suffix: '' },
  wMdRaw: { name: 'Water Main Attack Damage', suffix: '' },
  fMdRaw: { name: 'Fire Main Attack Damage', suffix: '' },
  aMdRaw: { name: 'Air Main Attack Damage', suffix: '' },
  eSdPct: { name: 'Earth Spell Damage', suffix: '%' },
  tSdPct: { name: 'Thunder Spell Damage', suffix: '%' },
  wSdPct: { name: 'Water Spell Damage', suffix: '%' },
  fSdPct: { name: 'Fire Spell Damage', suffix: '%' },
  aSdPct: { name: 'Air Spell Damage', suffix: '%' },
  eMdPct: { name: 'Earth Main Attack Damage', suffix: '%' },
  tMdPct: { name: 'Thunder Main Attack Damage', suffix: '%' },
  wMdPct: { name: 'Water Main Attack Damage', suffix: '%' },
  fMdPct: { name: 'Fire Main Attack Damage', suffix: '%' },
  aMdPct: { name: 'Air Main Attack Damage', suffix: '%' },
  eDamRaw: { name: 'Earth Damage', suffix: '' }, 
  tDamRaw: { name: 'Thunder Damage', suffix: '' },
  wDamRaw: { name: 'Water Damage', suffix: '' },
  fDamRaw: { name: 'Fire Damage', suffix: '' },
  aDamRaw: { name: 'Air Damage', suffix: '' },
  rSdRaw: {name: 'Elemental Spell Damage', suffix: ''}, 
  rDefPct: {name: 'Elemental Defence', suffix: '%'},
  atkTier: {name: 'Attack Speed',suffix:' Tier'},
  mainAttackRange: {name: 'Main Attack Range', suffix: '%'},
  damPct: {name: 'Damage', suffix: '%'},
  defPct: {name: 'Defence', suffix: '%'},
  rMdRaw: {name: 'Elemental Main Attack Damage', suffix: ''},
};

// 计算装备的所有鉴定词条
const identifications = computed(() => {
  const item = itemData.value;
  if (!item.name) return [];
  const results = [];
  
  // 提取当前物品是否是全局固定数值
  const isFixed = !!item.fixID;
  
  for (const [key, meta] of Object.entries(idMap)) {
    if (item[key] !== undefined) {
      let val = item[key];
      let currentIsFixed = isFixed;

      // 修复 BUG：如果数据是对象（例如 { static: true, raw: 10 }），则提取内部属性
      if (typeof val === 'object' && val !== null) {
        // 如果词条自带 static 属性，则覆盖全局的 isFixed
        if (val.static !== undefined) {
          currentIsFixed = val.static;
        }
        val = val.raw; // 提取实际的数值
      }

      // 确保提取出来的值是数字，再传入 calcRoll 进行计算
      if (typeof val === 'number') {
        const { min, max, isPositive } = calcRoll(val, false, currentIsFixed);
        results.push({ name: meta.name, min, max, suffix: meta.suffix, isPositive, isFixed: currentIsFixed });
      }
    }
  }

  const cls = (item.classReq || "").toLowerCase();
  for (let i = 1; i <= 4; i++) {
    const spellName = (spellNames[cls] && spellNames[cls][i - 1]) 
      ? `${spellNames[cls][i - 1]} Cost` : `${i}st Spell Cost`;

    // 为了代码健壮性，这里也封装一个内部处理函数，防范耗蓝词条未来也变成对象结构
    const processSpellCost = (spellVal, isPct) => {
      if (spellVal === undefined) return;
      let val = spellVal;
      let currentIsFixed = isFixed;

      if (typeof val === 'object' && val !== null) {
        if (val.static !== undefined) currentIsFixed = val.static;
        val = val.raw;
      }

      if (typeof val === 'number') {
        const { min, max, isPositive } = calcRoll(val, true, currentIsFixed);
        results.push({ name: spellName, min, max, suffix: isPct ? '%' : '', isPositive, isFixed: currentIsFixed });
      }
    };

    processSpellCost(item[`spRaw${i}`], false);
    processSpellCost(item[`spPct${i}`], true);
  }

  return results;
});

// 提取 Major IDs
const majorIds = computed(() => {
  const item = itemData.value;
  if (!item.majorIds || !Array.isArray(item.majorIds)) return [];
  return item.majorIds.map(id => {
    const majorData = majidJson[id] || {};
    return {
      name: majorData.displayName || id,
      description: majorData.description || "Unknown Major ID effect."
    };
  });
});

// === 悬浮窗的动态坐标与显隐 ===
const showTooltip = ref(false);
const tooltipStyle = ref({});

const handleMouseEnter = () => {
  // 即使没有数据也不 return，以展示报错面板
  if (wrapperRef.value) {
    const rect = wrapperRef.value.getBoundingClientRect();
    tooltipStyle.value = {
      top: `${rect.top + window.scrollY - 10}px`,
      left: `${rect.left + window.scrollX + (rect.width / 2)}px`
    };
  }
  showTooltip.value = true;
};

const handleMouseLeave = () => {
  showTooltip.value = false;
};
</script>

<style scoped>
/* 行内文字基础样式 */
.inline-text {
  text-decoration: underline dashed;
  cursor: help;
  font-weight: bold;
}

/* 匹配游戏里的品质颜色 */
.inline-text.mythic { color: rgb(164, 57, 192); }
.inline-text.fabled { color: #FF5555; }
.inline-text.legendary { color: #55FFFF; }
.inline-text.set { color: #55FF55; }
.inline-text.rare { color: #FF55FF; }
.inline-text.unique { color: #FFFF55; }
.inline-text.normal { color: #FFFFFF; }

.mythic-inline-wrapper {
  position: relative;
  display: inline-block;
}

/* 数据读取失败的面板样式 */
.mythic-error-panel {
  background-color: #1a1a1a;
  border: 2px dashed #FF5555;
  color: #FF5555;
  padding: 12px;
  font-family: ui-sans-serif, system-ui, sans-serif;
  font-size: 14px;
  text-align: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
  border-radius: 4px;
}
</style>

<style>
/* 传送至 Body 后的全局定位样式 */
.mythic-tooltip-teleported {
  position: absolute;
  transform: translate(-50%, -100%);
  z-index: 999999;
  pointer-events: none;
}

/* 动画效果：改由比最终位置偏高（-8px）的地方轻柔落下 */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.15s ease-out, transform 0.15s ease-out;
}
.fade-enter-from, .fade-leave-to {
  opacity: 0;
  transform: translate(-50%, calc(-100% - 8px)); 
}
</style>