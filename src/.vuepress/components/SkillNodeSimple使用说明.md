# SkillNodeSimple 组件使用说明

## 📋 组件概述

`SkillNodeSimple.vue` 是专门为 wynnability 编辑器导出的翻译 JSON 设计的简化版技能节点组件。

**与 SkillNode.vue 的主要区别：**
- ✅ 只显示名称、分支、备注信息
- ✅ 去除所有数值字段（技能消耗、冷却等）
- ✅ 适配 wynnability 的新格式（plainname 作为主键）
- ✅ 完整支持 Minecraft 颜色代码

---

## 🎯 JSON 格式说明

### wynnability 导出格式
```json
{
  "archer": {
    "className": "弓箭手",
    "archetypes": {
      "Boltslinger": {
        "name": "闪击射手"
      }
    },
    "abilities": {
      "Arrow Bomb": {
        "name": "§g§lArrow Bomb",
        "description": "§7Shoot an arrow that...",
        "customName": "爆炸箭",
        "note": "对自己造成10%伤害"
      }
    }
  }
}
```

### 关键字段映射

| 字段 | 说明 |
|-----|------|
| **主键** (如 "Arrow Bomb") | 英文原名（plainname，去除格式码） |
| `name` | 带 Minecraft 格式码的名称（§g§lArrow Bomb） |
| `customName` | 汉化名称（"爆炸箭"） |
| `description` | 技能描述（带格式码） |
| `note` | 补充备注 |

---

## 🔧 使用方法

### 1. 准备翻译文件

从 wynnability_CN 编辑器导出 JSON 后：

```bash
# 复制到 Guide 项目
cp archer_zh.json WynncraftCNguide/src/.vuepress/components/data/wynnability-zh.json
```

### 2. 在页面中使用

```vue
<template>
  <div class="skill-tree">
    <SkillNodeSimple name="Arrow Bomb" currentClass="archer" />
    <SkillNodeSimple name="Escape" currentClass="archer" />
  </div>
</template>

<script>
import SkillNodeSimple from './components/SkillNodeSimple.vue'

export default {
  components: { SkillNodeSimple }
}
</script>
```

### Props 说明

- `name` (String, 必需) - 技能的 plainname（英文原名，去除格式码）
- `currentClass` (String, 必需) - 职业名称（archer/warrior/assassin/mage/shaman）

---

## 🎨 显示效果

### Tooltip 结构

```
┌─────────────────────────────────┐
│ 爆炸箭                    (标题) │  ← customName，带颜色
│ (Arrow Bomb)              (副标题)│  ← plainname，小字号
├─────────────────────────────────┤
│ 射出一支会爆炸的箭...     (正文) │  ← description，支持格式码
├─────────────────────────────────┤
│ 闪击射手 分支            (页脚) │  ← archetype（如果有）
└─────────────────────────────────┘
   ┌──────────────────────┐
   │ 备注                  │  ← 侧边栏（如果有 note）
   │ 对自己造成10%伤害     │
   └──────────────────────┘
```

---

## 🌈 颜色代码支持

### Minecraft 格式码解析

组件完整支持 Minecraft 的颜色和格式代码：

**颜色代码：**
```
§0 黑色   §1 深蓝   §2 深绿   §3 青色
§4 深红   §5 紫色   §6 金色   §7 灰色
§8 深灰   §9 蓝色   §a 绿色   §b 青蓝
§c 红色   §d 粉色   §e 黄色   §f 白色
§g 亮绿 (Wynncraft 特有)
```

**格式代码：**
```
§l 加粗   §o 斜体   §n 下划线   §m 删除线
§r 重置所有格式
```

### 示例

wynnability 编辑器中：
```
§g§lArrow Bomb
§7射出一支会爆炸的箭
§c⚔ §7总伤害: §f150%
```

渲染效果：
- **Arrow Bomb** (亮绿色加粗)
- 射出一支会爆炸的箭 (灰色)
- ⚔ 总伤害: 150% (带图标和颜色)

---

## 📊 与 SkillNode.vue 的对比

| 功能 | SkillNode.vue | SkillNodeSimple.vue |
|-----|--------------|---------------------|
| 数据源 | atree.json + zh-cn.json | wynnability-zh.json |
| 主键 | `display_name` (技能英文名) | plainname (去格式码英文名) |
| 汉化字段 | `trans.name` | `customName` |
| 数值显示 | ✅ 支持（cost, cooldown等） | ❌ 移除 |
| 分支显示 | ✅ 支持 | ✅ 支持 |
| 备注显示 | ✅ 支持 | ✅ 支持 |
| 格式码 | 简单解析 | 完整解析 |
| 适用场景 | 完整游戏数据展示 | 仅翻译信息展示 |

---

## 🚀 完整工作流

### 1. 在 wynnability_CN 编辑器中

```
1. 加载默认技能树
2. 填写 customName（汉化名）和 note（备注）
3. description 保持原样（带 § 格式码）
4. 分享 → 下载 → archer_zh.json
```

### 2. 在 Guide 项目中

```bash
# 复制翻译文件
cp archer_zh.json WynncraftCNguide/src/.vuepress/components/data/wynnability-zh.json

# 在页面中使用
<SkillNodeSimple name="Arrow Bomb" currentClass="archer" />
```

### 3. 显示结果

```
标题：爆炸箭            ← customName
副标题：(Arrow Bomb)    ← plainname
描述：[带颜色格式的描述] ← description (§ 代码已渲染)
分支：闪击射手 分支      ← archetype
备注：对自己造成10%伤害  ← note
```

---

## 🔍 关键实现细节

### 1. 主键适配
```javascript
// wynnability 格式：主键就是 plainname
skill() {
  const classData = transData[this.currentClass];
  return classData.abilities[this.name]; // this.name = "Arrow Bomb"
}
```

### 2. 名称显示
```javascript
transName() {
  // 优先 customName，其次去除 name 中的格式码
  if (this.trans.customName) return this.trans.customName;
  return this.stripMinecraftFormatting(this.trans.name);
}
```

### 3. Minecraft 格式码渲染
```javascript
formatMinecraftText(text) {
  // 逐字符解析 §x 代码
  // 支持颜色、加粗、斜体、下划线、删除线
  // 输出带 inline style 的 HTML
}
```

---

## ⚠️ 注意事项

1. **数据文件路径**：
   - 确保 `wynnability-zh.json` 放在 `data/` 目录
   - 路径：`src/.vuepress/components/data/wynnability-zh.json`

2. **职业名称一致**：
   - wynnability: `archer`, `warrior`, `assassin`, `mage`, `shaman`
   - 必须与 JSON 中的键名完全匹配（小写）

3. **plainname 格式**：
   - wynnability 的主键是去除格式码的英文名
   - 例如：`§g§lArrow Bomb` → plainname 为 `Arrow Bomb`
   - 使用时 `name="Arrow Bomb"`（不带 §）

4. **格式码兼容**：
   - 组件支持标准 Minecraft 格式码（§0-9a-f）
   - 也支持 Wynncraft 特有的 §g (亮绿色)

---

## 🎉 完成！

现在你可以在 Guide 项目中使用从 wynnability_CN 导出的翻译数据了！

所有 Minecraft 颜色代码都会正确渲染，名称显示逻辑也与原 SkillNode 保持一致。
