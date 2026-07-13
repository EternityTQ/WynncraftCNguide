import json
import re

# 读取文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    mage_data = json.load(f)

with open('src/.vuepress/components/data/zh-cn.json', 'r', encoding='utf-8') as f:
    zh_cn_data = json.load(f)

# 技能名翻译映射（从zh-cn.json中提取）
skill_name_map = {
    "Meteor": "陨石术",
    "Teleport": "传送",
    "Heal": "治疗术",
    "Ice Snake": "寒冰之蛇",
    "Arrow Bomb": "爆炸箭",
    "Escape": "逃脱",
    "Arrow Storm": "箭雨",
    "Arrow Shield": "箭盾",
    "Bash": "重击",
    "Charge": "冲锋",
    "Uppercut": "上挑斩",
    "War Scream": "战吼",
}

# 术语翻译映射
term_map = {
    "Main Attack": "普通攻击",
    "Mana Cost": "技能消耗",
    "Total Damage": "总伤害",
    "of your DPS": "基于你的输出",
    "of your max health": "基于你的最大生命值",
    "Total Heal": "总治疗量",
    "Range": "范围",
    "Area of Effect": "伤害/作用范围",
    "Duration": "持续时间",
    "Cooldown": "冷却",
    "Effect": "效果",
    "Slowness": "减速",
    "to Enemies": "敌人",
    "to Allies": "盟友",
    "Circle-Shaped": "圆形",
    "Blocks": "格",
    "Damage": "伤害",
    "Earth": "地",
    "Thunder": "电",
    "Water": "水",
    "Fire": "火",
    "Air": "气",
    "Click Combo": "技能连击",
    "RIGHT": "右键",
    "LEFT": "左键",
    "Resistance Bonus": "抗性提升",
    "Walk Speed": "移动速度",
    "Damage Bonus": "伤害加成",
    "Health Regen": "生命回复",
    "Mana Regen": "法力回复",
    "Raw Damage": "原始伤害",
    "Spell Damage": "法术伤害",
    "Vision": "索敌范围",
    "Charge": "充能",
    "per": "每",
    "Max": "上限",
    "Increase": "增加",
    "Reduce": "降低",
    "when using a wand": "使用法杖时",
    "Improve": "提升",
}

# 单位翻译
unit_map = {
    "Blocks": "格",
    "s": "秒",
    "%": "%",
}

def translate_description(desc, skill_name=""):
    """翻译技能描述"""
    if not desc:
        return desc

    # 保存格式符
    result = desc

    # 翻译Click Combo行
    result = re.sub(r'§6Click Combo: (§d§l[A-Z]+(?:§7-§d§l[A-Z]+)*)',
                   lambda m: f'§6技能连击: {m.group(1).replace("RIGHT", "右键").replace("LEFT", "左键")}',
                   result)

    # 分离描述部分和数值部分
    parts = result.split('\n\n')

    if len(parts) >= 2:
        # 处理描述部分（第一部分，去除单独的换行符）
        desc_part = parts[0]
        desc_lines = desc_part.split('\n')

        # 过滤掉技能连击行后的单独换行
        filtered_lines = []
        for i, line in enumerate(desc_lines):
            # 保留技能连击行
            if '§6技能连击:' in line or '§6Click Combo:' in line:
                filtered_lines.append(line)
            # 跳过空行和只有格式符的行
            elif line.strip() and not re.match(r'^§[0-9a-z]$', line.strip()):
                filtered_lines.append(line)

        desc_part = '\n'.join(filtered_lines)

        # 翻译描述文本
        for eng, chs in term_map.items():
            desc_part = desc_part.replace(eng, chs)

        # 处理数值部分（保持原样，只翻译标签）
        stats_parts = parts[1:]
        translated_stats = []

        for stat_part in stats_parts:
            stat_lines = stat_part.split('\n')
            translated_lines = []

            for line in stat_lines:
                # 翻译统计标签
                if '§7Mana Cost:' in line:
                    line = line.replace('§7Mana Cost:', '§7技能消耗:').replace('§f', '§f') + '点' if not '点' in line else line.replace('§7Mana Cost:', '§7技能消耗:')
                elif '§7Total Damage:' in line:
                    line = line.replace('§7Total Damage:', '§7总伤害:').replace('§8(of your DPS)', '§8(基于你的输出)')
                elif '§7Total Heal:' in line:
                    line = line.replace('§7Total Heal:', '§7总治疗量:').replace('§8(of your max health)', '§8(基于你的最大生命值)')
                elif '§7Range:' in line:
                    line = line.replace('§7Range:', '§7范围:').replace(' Blocks', '格')
                elif '§7Area of Effect:' in line:
                    line = line.replace('§7Area of Effect:', '§7伤害/作用范围:').replace(' Blocks', '格').replace('Circle-Shaped', '圆形')
                elif '§7Duration:' in line:
                    line = line.replace('§7Duration:', '§7持续时间:').replace('s', '秒')
                elif '§7Cooldown:' in line:
                    line = line.replace('§7Cooldown:', '§7冷却:').replace('s', '秒')
                elif '§7Effect:' in line:
                    line = line.replace('§7Effect:', '§7效果:').replace('Slowness', '减速').replace('to Enemies', '敌人').replace('to Allies', '盟友')
                elif '§7Main Attack' in line:
                    line = line.replace('Main Attack Damage:', '普通攻击伤害:').replace('Main Attack Range:', '普通攻击范围:').replace(' Blocks', '格')

                # 翻译元素
                line = line.replace('§8Earth:', '§8地:').replace('§8Thunder:', '§8电:').replace('§8Water:', '§8水:').replace('§8Fire:', '§8火:').replace('§8Air:', '§8气:').replace('§8Damage:', '§8伤害:')

                translated_lines.append(line)

            translated_stats.append('\n'.join(translated_lines))

        result = desc_part + '\n\n' + '\n\n'.join(translated_stats)

    # 翻译技能名称引用
    for eng_name, chs_name in skill_name_map.items():
        result = result.replace(f'§n{eng_name}§7', f'§n{chs_name}§7')

    return result

# 处理所有技能
abilities = mage_data.get('abilities', {})

for ability_key, ability_data in abilities.items():
    print(f"处理: {ability_key}")

    # 翻译描述
    if 'description' in ability_data:
        ability_data['description'] = translate_description(
            ability_data['description'],
            ability_key
        )

    # 设置技能名（如果zh-cn.json中存在则使用，否则留空待人工翻译）
    if ability_key in skill_name_map:
        ability_data['customName'] = skill_name_map[ability_key]

# 保存结果
with open('src/.vuepress/components/data/zh-cn-mage-auto.json', 'w', encoding='utf-8') as f:
    json.dump(mage_data, f, ensure_ascii=False, indent=4)

print("翻译完成！输出文件: zh-cn-mage-auto.json")
print("请检查并手动完善未翻译的技能名称。")
