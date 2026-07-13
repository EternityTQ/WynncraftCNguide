import json
import re

# 读取文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    mage_data = json.load(f)

# 完整的技能名翻译映射
skill_name_map = {
    # 基础技能
    "Meteor": "陨石术",
    "Teleport": "传送",
    "Heal": "治疗术",
    "Ice Snake": "寒冰之蛇",

    # 精通类
    "Wand Proficiency I": "法杖精通 I",
    "Wand Proficiency II": "法杖精通 II",
    "Air Mastery": "气元素精通",
    "Earth Mastery": "地元素精通",
    "Fire Mastery": "火元素精通",
    "Thunder Mastery": "电元素精通",
    "Water Mastery": "水元素精通",

    # 减耗类
    "Cheaper Meteor": "陨石术减耗",
    "Cheaper Meteor II": "陨石术减耗 II",
    "Cheaper Teleport": "传送减耗",
    "Cheaper Teleport II": "传送减耗 II",
    "Cheaper Heal": "治疗术减耗",
    "Cheaper Heal II": "治疗术减耗 II",
    "Cheaper Ice Snake": "寒冰之蛇减耗",
    "Cheaper Ice Snake II": "寒冰之蛇减耗 II",

    # 强化类
    "Shooting Star": "流星",
    "Wisdom": "智慧",
    "Displacement": "位移",
    "Crashing Comet": "碎星陨击",
    "Astral Fragmentation": "星辰碎片",

    # 高级技能
    "Distortion": "扭曲",
    "Ophanim": "光之宝珠",
    "Arcane Transfer": "秘法传送",
    "Thunderstorm": "雷暴",
    "Sunshower": "日光浴",
    "Burning Sigil": "燃烧法印",
    "Frozen Tornado": "冰封龙卷",
    "Etheric Slash": "以太斩击",
    "Meteor Shower": "陨星雨",
    "Dimensional Tear": "次元裂隙",

    # 辅助/增益类
    "Purification": "净化",
    "Larger Heal": "治疗强化",
    "Larger Mana Bank": "法力储备扩容",
    "Larger Mana Bank II": "法力储备扩容 II",
    "Larger Mana Bank III": "法力储备扩容 III",
    "Fortitude": "坚毅",
    "Pyrokinesis": "念动烈焰",
    "Resilient Light": "坚韧之光",
    "Snake Nest": "蛇巢",
    "Seance": "降灵术",
    "Warp Blast": "曲速冲击",
    "Gospel of Light": "光之福音",
    "Orphion's Pulse": "奥菲昂脉冲",
    "Incandescence": "白炽",
    "Arcane Restoration": "秘法复原",
    "Void Acceleration": "虚空加速",
    "Lightweaver": "光之编织者",
    "Arcane Speed": "秘法疾行",
    "Psychokinesis": "心灵传动",
    "Chaos Explosion": "混沌爆发",
    "Crystallize": "结晶",
    "Vacuokinesis": "真空操控",
    "Sentient Snake": "灵智之蛇",
    "Augury": "预兆",
    "Searing Light": "灼热之光",
    "Arcane Power": "秘法之力",
    "Rift Rupture": "裂隙破碎",
    "Everlasting Light": "永恒之光",
    "Frigid Grasp": "极寒之握",
    "Time Dilation": "时间膨胀",
    "Divination": "占卜",
    "Sunflare": "耀阳",
    "Halo": "光环",
    "Arcane Overflow": "秘法涌流",
    "Memory Recollection": "记忆回溯",
    "Manastorm": "法力风暴",
    "Freezing Sigil": "冰冻法印",
    "Arctic Snake": "极地之蛇",
    "Gleam": "微光",
    "Accelerated Strike": "加速打击",
    "Influx Shift": "涌流转移",
    "Devitalize": "削弱",
    "Mana Current": "法力洋流",
    "Riftbound": "裂隙束缚",
    "Judrajim": "尤德拉吉姆",
    "Diffraction": "衍射",
    "Time Vortex": "时空漩涡",
    "Portal to the Beyond": "彼界之门",
    "Paradox": "悖论",
    "Blitz": "闪电战",
    "Induced Instability": "诱导不稳定",
    "Interweave": "交织",

    # 终极技能
    "Dawn": "黎明",
    "Gravitational Collapse": "引力坍缩",
    "Tangled Origin": "纠缠起源",
}

def translate_description(desc, skill_name=""):
    """翻译技能描述"""
    if not desc:
        return desc

    result = desc

    # 1. 翻译技能连击行
    result = result.replace('§6Click Combo: §d§lRIGHT', '§6技能连击: §d§l右键')
    result = result.replace('§d§lRIGHT', '§d§l右键')
    result = result.replace('§d§lLEFT', '§d§l左键')
    result = result.replace('§d§lF', '§d§lF')

    # 2. 翻译描述性文本中的常见短语（保留技能名引用的格式符）
    translations = {
        'Improve your ': '提升',
        'when using a wand.': '使用法杖时。',
        'when using a wand': '使用法杖时',
        'Increase your base damage': '增加基础伤害',
        'from all ': '',
        ' attacks.': '属性攻击。',
        ' attacks': '属性攻击',
        'For every ': '装备中每有',
        ' or ': '或',
        ' Raw ': '点原始',
        ' Spell Damage you have\nfrom items, gain ': '法术伤害，获得',
        ' Mana Regen (Max ': '法力回复(上限',
        'Reduce the mana cost of ': '降低',
        'Drastically increase the\nspeed of your ': '大幅提升你的',
        ' ability.': '技能的速度。',
        ' ability': '技能',
        'Instantly teleport in the\ndirection you\'re facing.': '瞬间传送到你面向的方向。',
        'Heals you and nearby allies in\na large area around you.': '治疗你和你周围大范围内的盟友。',
        'When healing others, you can\'t heal\nmore than 30% of ': '治疗他人时，单次治疗量不能超过',
        'their': '他们',
        ' max health': '最大生命值',
        'Summons a fast-moving ice snake that\ndamages and slows enemies.': '召唤一条快速移动的冰蛇，对敌人造成伤害并减速。',
        'of your max health': '基于你的最大生命值',
        'of your DPS': '基于你的输出',
        'Circle-Shaped': '圆形',
        'to Enemies': '敌人',
        'to Allies': '盟友',
        'per second': '每秒',
    }

    for eng, chs in translations.items():
        result = result.replace(eng, chs)

    # 3. 翻译数值标签（保持格式符）
    stat_translations = {
        '§7Mana Cost:': '§7技能消耗:',
        '§7Main Attack Damage:': '§7普通攻击伤害:',
        '§7Main Attack Range:': '§7普通攻击范围:',
        '§7Total Damage:': '§7总伤害:',
        '§7Total Heal:': '§7总治疗量:',
        '§7Range:': '§7范围:',
        '§7Area of Effect:': '§7伤害/作用范围:',
        '§7Duration:': '§7持续时间:',
        '§7Cooldown:': '§7冷却:',
        '§7Effect:': '§7效果:',
        '§7Slowness': '§7减速',
        '§7Resistance Bonus': '§7抗性提升',
        '§7Walk Speed': '§7移动速度',
        '§7Damage Bonus': '§7伤害加成',
        '§7Health Regen:': '§7生命回复:',
        '§7Mana Regen:': '§7法力回复:',
        '§7Vision:': '§7索敌范围:',
        '§7Pulse Self Heal:': '§7脉冲自我治疗:',
        '§7Delay:': '§7延迟:',
    }

    for eng, chs in stat_translations.items():
        result = result.replace(eng, chs)

    # 4. 翻译元素类型
    result = result.replace('§8Damage:', '§8伤害:')
    result = result.replace('§8Earth:', '§8地:')
    result = result.replace('§8Thunder:', '§8电:')
    result = result.replace('§8Water:', '§8水:')
    result = result.replace('§8Fire:', '§8火:')
    result = result.replace('§8Air:', '§8气:')

    # 5. 翻译单位
    result = result.replace(' Blocks', '格')
    result = result.replace(' Block', '格')
    result = re.sub(r'§f(\d+)s\b', r'§f\g<1>秒', result)

    # 6. 在Mana Cost数值后添加"点"（注意要匹配完整数字）
    result = re.sub(r'§7技能消耗: §f([+-]?\d+)\b', r'§7技能消耗: §f\g<1>点', result)

    # 7. 翻译技能名引用（保留§n格式符）
    for eng_name, chs_name in skill_name_map.items():
        result = result.replace(f'§n{eng_name}§7', f'§n{chs_name}§7')

    return result

# 处理所有技能
abilities = mage_data.get('abilities', {})
processed_count = 0

for ability_key, ability_data in abilities.items():
    # 翻译描述
    if 'description' in ability_data:
        ability_data['description'] = translate_description(
            ability_data['description'],
            ability_key
        )

    # 设置技能名
    if ability_key in skill_name_map:
        ability_data['customName'] = skill_name_map[ability_key]

    processed_count += 1

# 保存结果到原文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'w', encoding='utf-8') as f:
    json.dump(mage_data, f, ensure_ascii=False, indent=4)

print(f"翻译完成！共处理 {processed_count} 个技能")
print("文件已保存到: src/.vuepress/components/data/zh-cn-mage.json")
