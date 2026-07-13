#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
法师技能树翻译脚本
翻译 zh-cn-mage.json 中的所有技能
"""

import json
import re
from pathlib import Path

# 文件路径
MAGE_FILE = r"D:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-mage.json"
ZH_CN_FILE = r"D:\WynncraftCNguide\src\.vuepress\components\data\zh-cn.json"

# 统计标签翻译映射
STAT_TRANSLATIONS = {
    "Mana Cost": "技能消耗",
    "Total Damage": "总伤害",
    "Range": "范围",
    "Area of Effect": "伤害/作用范围",
    "Duration": "持续时间",
    "Cooldown": "冷却",
    "Effect": "效果",
    "Main Attack Damage": "普通攻击伤害",
    "Main Attack Range": "普通攻击范围",
    "Total Heal": "总治疗",
    "Heal": "治疗",
    "Health Regen": "生命回复",
    "Mana Regen": "法力回复",
    "Resistance": "抗性",
    "Charges": "充能",
    "Pulse Self Heal": "脉冲自我治疗",
    "Delay": "延迟",
    "Target Radius": "目标半径",
    "Meteor Area of Effect": "流星天降伤害/作用范围",
    "Drift Range": "漂移范围",
    "Tornado Duration": "龙卷风持续时间",
    "Slow Duration": "减速持续时间",
}

# 通用词汇翻译
COMMON_TRANSLATIONS = {
    "Click Combo": "连招",
    "RIGHT": "右键",
    "LEFT": "左键",
    "Blocks": "格",
    "Block": "格",
    "Circle-Shaped": "圆形",
    "of your DPS": "基于你的DPS",
    "of your max health": "基于你的最大生命值",
    "of your max mana": "基于你的最大法力值",
    "Main Attack Damage": "普通攻击伤害",
    "per second": "每秒",
    "per hit": "每次命中",
    "to Enemies": "对敌人",
    "to Allies": "对友军",
    "Damage": "伤害",
    "Fire": "火",
    "Water": "水",
    "Air": "风",
    "Thunder": "雷",
    "Earth": "地",
    "Walk Speed": "移动速度",
    "Damage Bonus": "伤害加成",
    "Resistance Bonus": "抗性加成",
    "Slowness": "缓慢",
    "Spell Damage": "法术伤害",
    "Raw Damage": "原始伤害",
    "Raw": "原始",
    "Lifesteal": "生命偷取",
    "Mana Steal": "法力偷取",
    "Knockback Immunity": "击退免疫",
    "Max": "最大",
}

# 技能名称翻译
SKILL_TRANSLATIONS = {
    "Meteor": "流星天降",
    "Wand Proficiency I": "法杖精通 I",
    "Wand Proficiency II": "法杖精通 II",
    "Cheaper Meteor": "流星天降减耗",
    "Cheaper Meteor II": "流星天降减耗 II",
    "Shooting Star": "流星",
    "Teleport": "传送",
    "Wisdom": "智慧",
    "Heal": "治疗",
    "Ice Snake": "冰蛇",
    "Cheaper Teleport": "传送减耗",
    "Cheaper Teleport II": "传送减耗 II",
    "Air Mastery": "风元素精通",
    "Earth Mastery": "地元素精通",
    "Fire Mastery": "火元素精通",
    "Thunder Mastery": "雷元素精通",
    "Water Mastery": "水元素精通",
    "Distortion": "扭曲",
    "Thunderstorm": "雷暴",
    "Sunshower": "阳光雨",
    "Burning Sigil": "燃烧法印",
    "Crashing Comet": "陨落彗星",
    "Astral Fragmentation": "星界碎片",
    "Ophanim": "光之天使",
    "Arcane Transfer": "奥术转移",
    "Cheaper Heal": "治疗减耗",
    "Cheaper Heal II": "治疗减耗 II",
    "Interweave": "交织",
    "Displacement": "位移",
    "Purification": "净化",
    "Larger Heal": "治疗扩大",
    "Larger Mana Bank": "法力银行扩大",
    "Larger Mana Bank II": "法力银行扩大 II",
    "Larger Mana Bank III": "法力银行扩大 III",
    "Cheaper Ice Snake": "冰蛇减耗",
    "Cheaper Ice Snake II": "冰蛇减耗 II",
    "Frozen Tornado": "冰冻龙卷风",
    "Fortitude": "坚韧",
    "Pyrokinesis": "念力火焰",
    "Resilient Light": "坚韧之光",
    "Snake Nest": "蛇巢",
    "Seance": "降神会",
    "Warp Blast": "扭曲爆破",
    "Gospel of Light": "光之福音",
    "Orphion's Pulse": "俄耳甫斯之脉",
    "Incandescence": "白炽",
    "Arcane Restoration": "奥术恢复",
    "Meteor Shower": "流星雨",
    "Void Acceleration": "虚空加速",
    "Lightweaver": "光之编织者",
    "Arcane Speed": "奥术加速",
    "Psychokinesis": "念力",
    "Chaos Explosion": "混沌爆炸",
    "Crystallize": "结晶",
    "Vacuokinesis": "真空操控",
    "Dimensional Tear": "次元裂隙",
    "Sentient Snake": "灵智之蛇",
    "Augury": "占卜",
    "Searing Light": "灼热之光",
    "Arcane Power": "奥术之力",
    "Rift Rupture": "裂隙破裂",
    "Everlasting Light": "永恒之光",
    "Etheric Slash": "以太斩击",
    "Frigid Grasp": "极寒之握",
    "Time Dilation": "时间膨胀",
    "Divination": "占卜术",
    "Sunflare": "太阳耀斑",
    "Halo": "光环",
    "Arcane Overflow": "奥术溢流",
    "Memory Recollection": "记忆重现",
    "Manastorm": "法力风暴",
    "Freezing Sigil": "冰冻法印",
    "Arctic Snake": "极地之蛇",
    "Gleam": "微光",
    "Accelerated Strike": "加速打击",
    "Influx Shift": "能量涌动",
    "Devitalize": "削弱",
    "Mana Current": "法力流",
    "Riftbound": "裂隙束缚",
    "Judrajim": "裘德拉吉姆",
    "Diffraction": "衍射",
    "Time Vortex": "时空漩涡",
    "Wind Slash": "风之斩",
    "Main Attack": "普通攻击",
}


def clean_newlines(text):
    """删除单独的换行符，保留成对的换行符"""
    # 先保护 \n\n
    text = text.replace('\n\n', '<<DOUBLE_NEWLINE>>')
    # 删除单独的 \n
    text = text.replace('\n', '')
    # 恢复 \n\n
    text = text.replace('<<DOUBLE_NEWLINE>>', '\n\n')
    return text


def translate_stat_label(text):
    """翻译统计标签"""
    for en, zh in STAT_TRANSLATIONS.items():
        # 精确匹配统计标签（后面跟着冒号）
        text = re.sub(rf'§7{re.escape(en)}:', f'§7{zh}:', text)
    return text


def translate_common_words(text):
    """翻译通用词汇"""
    for en, zh in COMMON_TRANSLATIONS.items():
        text = text.replace(en, zh)
    return text


def translate_skill_references(text):
    """翻译技能名称引用（§n标记的技能名）"""
    # 匹配 §n技能名§7 或 §n技能名§8 等格式
    def replace_skill(match):
        skill_name = match.group(1)
        if skill_name in SKILL_TRANSLATIONS:
            return f'§n{SKILL_TRANSLATIONS[skill_name]}§7'
        return match.group(0)

    text = re.sub(r'§n([^§]+)§[0-9a-z]', replace_skill, text)
    return text


def translate_description(desc):
    """翻译技能描述"""
    if not desc:
        return desc

    # 1. 清理换行符
    desc = clean_newlines(desc)

    # 2. 翻译统计标签
    desc = translate_stat_label(desc)

    # 3. 翻译技能引用
    desc = translate_skill_references(desc)

    # 4. 翻译通用词汇
    desc = translate_common_words(desc)

    # 5. 特殊处理一些常见模式
    # 翻译 "Improve your §nMain Attack§7's"
    desc = desc.replace("Improve your §n普通攻击§7's damage", "提升你的§n普通攻击§7伤害")
    desc = desc.replace("and range when using a wand.", "以及使用法杖时的范围")
    desc = desc.replace("Reduce the mana cost of", "降低")
    desc = desc.replace("Increase your base 伤害", "提升你的基础伤害")
    desc = desc.replace("from all", "来自所有")
    desc = desc.replace("attacks.", "攻击。")
    desc = desc.replace("Increase your base damage\nfrom all", "提升你所有")
    desc = desc.replace("attacks", "攻击的基础伤害")
    desc = desc.replace("For every", "每")
    desc = desc.replace("you have\nfrom items, gain", "的装备属性，获得")
    desc = desc.replace("Increase the 伤害 of", "提升")
    desc = desc.replace("Increase the damage of", "提升")
    desc = desc.replace("Increases the health of", "提升")
    desc = desc.replace("Increase your maximum", "提升你的最大")
    desc = desc.replace("orbs\nfrom", "光球数量（来自")
    desc = desc.replace("by", "）")

    return desc


def main():
    """主函数"""
    print("正在加载JSON文件...")

    # 读取文件
    with open(MAGE_FILE, 'r', encoding='utf-8') as f:
        mage_data = json.load(f)

    print(f"找到 {len(mage_data['abilities'])} 个技能")

    # 统计翻译进度
    total_skills = len(mage_data['abilities'])
    translated = 0
    skipped = 0

    # 翻译每个技能
    for skill_id, skill_data in mage_data['abilities'].items():
        # 提取原始英文名（去除颜色代码）
        original_name = re.sub(r'§[0-9a-klmnor#]+', '', skill_data['name'])

        # 如果已有自定义名称，跳过
        if skill_data.get('customName'):
            print(f"跳过已翻译: {skill_id} ({original_name})")
            skipped += 1
            continue

        # 设置中文技能名
        if original_name in SKILL_TRANSLATIONS:
            skill_data['customName'] = SKILL_TRANSLATIONS[original_name]
            print(f"翻译技能名: {original_name} -> {skill_data['customName']}")
        else:
            print(f"警告: 未找到技能名翻译: {original_name}")
            skill_data['customName'] = original_name

        # 翻译描述
        if skill_data.get('description'):
            skill_data['description'] = translate_description(skill_data['description'])

        translated += 1

    # 保存结果
    print(f"\n正在保存到 {MAGE_FILE}...")
    with open(MAGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(mage_data, f, ensure_ascii=False, indent=4)

    print(f"\n翻译完成!")
    print(f"总计: {total_skills} 个技能")
    print(f"已翻译: {translated} 个")
    print(f"已跳过: {skipped} 个")


if __name__ == "__main__":
    main()
