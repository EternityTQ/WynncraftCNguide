import json
import re

# 读取文件
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'r', encoding='utf-8') as f:
    assassin_data = json.load(f)

with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn.json', 'r', encoding='utf-8') as f:
    zh_cn_data = json.load(f)

# 翻译字典
translations = {
    "Mana Cost": "技能消耗",
    "Total Damage": "总伤害",
    "Range": "范围",
    "Area of Effect": "伤害/作用范围",
    "AoE": "伤害/作用范围",
    "Duration": "持续时间",
    "Cooldown": "冷却",
    "Effect": "效果",
    "Damage": "伤害",
    "Thunder": "电",
    "Water": "水",
    "Fire": "火",
    "Air": "气",
    "Earth": "地",
    "blocks": "格",
    "Block": "格",
    "seconds": "秒",
    "per hit": "每次攻击",
    "of your DPS": "基于你的DPS",
    "Circle-Shaped": "圆形范围",
    "Cone-Shaped": "锥形范围",
    "Invisibility": "隐身",
    "to Self": "对自身",
    "to Enemies": "对敌人",
    "Speed Bonus": "速度加成",
    "Damage Bonus": "伤害加成",
    "Resistance Bonus": "抗性加成",
    "Blindness": "致盲",
    "Charges": "充能",
    "per": "每",
}

# 已知技能名翻译（从任务描述中提取）
skill_names = {
    "Spin Attack": "旋风斩",
    "Dagger Proficiency I": "匕首精通 I",
    "Cheaper Spin Attack I": "旋风斩减耗 I",
    "Cheaper Spin Attack II": "旋风斩减耗 II",
    "Double Spin": "双重旋风",
    "Poisoned Blade": "剧毒利刃",
    "Dash": "突进",
    "Double Slice": "双重切割",
    "Smoke Bomb": "烟雾弹",
    "Cheaper Dash I": "突进减耗 I",
    "Cheaper Dash II": "突进减耗 II",
    "Multihit": "多重击",
    "Backstab": "背刺",
    "Vanish": "隐身",
    "Sticky Bomb": "黏性炸弹",
    "Righting Reflex": "平衡反射",
    "Surprise Strike": "奇袭",
    "Mirror Image": "镜影幻术",
    "Lacerate": "撕裂",
    "Silent Killer": "冷面杀手",
    "Wall of Smoke": "烟幕之墙",
    "Rolling Fog": "流雾",
    "Shadow Travel": "暗影穿梭",
    "Cheaper Multihit I": "多重击减耗 I",
    "Cheaper Multihit II": "多重击减耗 II",
    "Shadow Siphon": "暗影虹吸",
    "Last Laugh": "谢幕一击",
    "Cheaper Smoke Bomb I": "烟雾弹减耗 I",
    "Cheaper Smoke Bomb II": "烟雾弹减耗 II",
    "Blazing Powder": "烈火附刃",
    "Weightless": "身轻如燕",
    "Black Hole": "黑洞",
    "Sandbagging": "以己之长",
    "Hop": "雀跃",
    "Dancing Blade": "剑舞",
    "Violent Vortex": "暴戾漩涡",
    "Duplicity": "重影",
    "Mutilate": "肢解",
    "Marked": "死亡标记",
    "Malicious Mockery": "恶毒嘲讽",
    "Echo": "镜中回响",
    "Shurikens": "手里剑",
    "Far Reach": "长斩",
    "Psithurism": "风语",
    "Ambush": "伏击",
    "Aerial Ace": "燕返",
    "Death Magnet": "死亡牵引",
    "Hoodwink": "偷天换日",
    "Wall Jump": "蹬墙跳",
    "Fatal Spin": "致命旋风",
    "Eviscerate": "剔骨",
    "Bladestorm": "剑刃风暴",
    "Harvester": "影逝收割",
    "Air Mastery": "气元素精通",
    "Earth Mastery": "地元素精通",
    "Fire Mastery": "火元素精通",
    "Thunder Mastery": "电元素精通",
    "Water Mastery": "水元素精通",
    "Ripple": "狂乱震荡",
    "Finality": "终焉狂热",
}

# 需要添加的新技能名翻译
new_skill_names = {
    "Petal Storm": "落樱风暴",
    "Doppleganger": "分身术",
    "Paranoia": "疑心生暗",
    "Distraction": "声东击西",
    "Bamboozle": "瞬身斩",
    "Disappearing Act": "遁影幻灭",
    "Choke Bomb": "窒息烟雾",
    "Noxious Haze": "剧毒烟岚",
    "Mirage": "幻象分身",
    "Foul Play": "恶意欺诈",
    "Dextrous Hands": "灵巧双手",
    "Dissolution": "消散无踪",
    "More Marks": "标记扩容",
    "Blade Fury": "刀刃狂怒",
    "Ricochets": "弹射飞镖",
    "Deflagate": "燃尽之焰",
    "Satsujin": "杀阵",
    "Thermobaric Smoke": "温压烟雾",
    "Jasmine Bloom": "茉莉绽放",
    "Another Self": "另一个自我",
    "Serpent's Garden": "蛇影花园",
    "Thrill": "亢奋",
    "Marked for Death": "死亡印记",
    "Devour": "吞噬",
    "Swan Dive": "天鹅俯冲",
    "Shadow Projection": "暗影投射",
    "Toxic Sludge": "剧毒泥潭",
    "Soul Siphon": "灵魂虹吸",
    "Shadow Dance": "影之舞",
    "Looming Presence": "迫近威胁",
    "Billowing Death": "死亡涌潮",
    "Pierce the Veil": "刺破幽纱",
    "Nightcloak Knife": "夜刃",
    "Celerity": "迅捷",
    "Braced Impact": "稳固着陆",
    "Misdirection": "迷惑诡计",
}

# 合并所有技能名
skill_names.update(new_skill_names)

def translate_term(text):
    """翻译术语"""
    result = text
    for en, zh in translations.items():
        result = result.replace(en, zh)
    return result

def process_description(desc):
    """处理技能描述"""
    if not desc:
        return desc

    # 找到数值部分的开始（通常以§b、§c、§2、§3、§d、§e开头的行）
    lines = desc.split('\n')
    translated_lines = []
    in_stats_section = False

    for i, line in enumerate(lines):
        # 检测是否进入数值部分
        if re.match(r'^§[b2c3de]', line.strip()):
            in_stats_section = True

        # 翻译这一行
        translated_line = translate_term(line)

        # 如果不在数值部分，处理单独的换行符
        if not in_stats_section and i < len(lines) - 1:
            # 检查下一行是否也不是数值行
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            if next_line and not re.match(r'^§[b2c3de]', next_line.strip()):
                # 如果当前行不为空，并且下一行也不为空，则可能需要删除换行
                if translated_line.strip() and next_line.strip():
                    # 保留这行，但标记可能需要合并
                    pass

        translated_lines.append(translated_line)

    # 重新组合，处理描述部分的单独换行符
    result_lines = []
    i = 0
    while i < len(translated_lines):
        line = translated_lines[i]

        # 如果是数值行或空行，直接添加
        if re.match(r'^§[b2c3de]', line.strip()) or not line.strip():
            result_lines.append(line)
            i += 1
        else:
            # 描述性文本，检查是否需要合并
            if i < len(translated_lines) - 1:
                next_line = translated_lines[i + 1]
                # 如果下一行是描述性文本（非数值、非空），则合并
                if next_line.strip() and not re.match(r'^§[b2c3de]', next_line.strip()):
                    result_lines.append(line)
                else:
                    result_lines.append(line)
            else:
                result_lines.append(line)
            i += 1

    return '\n'.join(result_lines)

# 处理所有技能
for skill_key, skill_data in assassin_data["abilities"].items():
    # 添加customName
    if skill_key in skill_names:
        skill_data["customName"] = skill_names[skill_key]
    else:
        # 如果没有翻译，暂时留空或使用英文名
        skill_data["customName"] = skill_key
        print(f"警告: 技能 {skill_key} 没有找到中文翻译")

    # 翻译description
    if "description" in skill_data and skill_data["description"]:
        skill_data["description"] = process_description(skill_data["description"])

# 保存结果
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'w', encoding='utf-8') as f:
    json.dump(assassin_data, f, ensure_ascii=False, indent=0, separators=(',', ':'))

print("翻译完成！")
