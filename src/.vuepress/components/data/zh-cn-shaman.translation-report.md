# 萨满技能树翻译检查报告

- 目标职业：萨满
- 目标/输出文件：`src/.vuepress/components/data/zh-cn-shaman.json`
- 参考文件：`src/.vuepress/components/data/zh-cn.json`
- 技能总数：93
- 本次新增完整说明翻译：93
- 本次补全 customName：93
- 修复的残缺翻译：0（目标文件初始状态为全英文说明，不属于中英混杂或截断译文）
- 沿用旧译名：67
- 新创造中文名：26

## 新创造中文名

- Puppetry -> 傀儡术
- Mystic Masks -> 神秘假面
- Effuse -> 血涌
- Tribal Chants -> 部族颂歌
- Rupture -> 创口迸裂
- Bloody -> 鲜血淋漓 I
- Chorus of the Ancients -> 先祖合颂
- Meticulous Act -> 精益求精
- Crystal Knives -> 水晶飞刀
- Artist's Immersion -> 艺术沉浸
- Bloodier -> 鲜血淋漓 II
- Scourge -> 灾祸
- Slingshot -> 弹射起步
- Fortified Formation -> 铁壁阵型
- Totemic Hammer -> 图腾重锤
- Freestyle -> 自由式
- Egomania -> 唯我独尊
- Pool of Rejuvenation -> 回春之池
- Corporeal Manifestation -> 具象化身
- Eldritch Transfusion -> 异界输血
- Repulse -> 斥退
- Bloodiest -> 鲜血淋漓 III
- Haemomagnetic -> 血磁牵引
- Patchwork Abomination -> 拼接憎恶
- Sundered Skies -> 天穹崩裂
- Monument to Gloom -> 幽暗丰碑

## 存在歧义、建议人工确认

- Effuse -> 血涌：技能效果是“火舌”命中后补充血池，中文名采用意象化短名；原词可兼有“倾泻、涌出”之意。
- Repulse -> 斥退：当前机制实际表现为光环第三次向外扩散，并不明确包含击退；译名主要依据英文技能名。
- Corporeal Manifestation -> 具象化身：机制为觉醒时其他假面实体化环绕，译名侧重“实体显现”的机制含义。
- Patchwork Abomination -> 拼接憎恶：Abomination 采用奇幻 RPG 常见的“憎恶”译法；如项目后续统一为“憎恶体”，可整体调整术语。

## 程序化校验结果

以下检查全部通过：

1. 输入、临时输出与最终输出均可由标准 JSON 解析器读取。
2. 技能数量保持 93，技能键名及顺序完全一致。
3. 除 `abilities.*.description` 与 `abilities.*.customName` 外，所有字段深度比较完全一致。
4. 每条 description 的 Minecraft 格式码数量与顺序完全一致。
5. 每条 description 的属性图标数量与顺序完全一致。
6. 每条 description 的数字、正负号、百分比及小数顺序完全一致。
7. 数值区行数、空行位置和每行缩进完全一致。
8. 说明区段落数量不变，英文排版用单换行已全部移除。
9. 不存在空缺 customName。
10. 不存在明显未完成的英文句子（保留项目约定缩写 DPS、操作键 F 与数值后缀 x）。
11. 不存在重复 JSON 键、截断 JSON 或遗漏技能。
12. 所有 description 均在写回目标文件前完成内存校验，并在临时文件序列化后复检。
