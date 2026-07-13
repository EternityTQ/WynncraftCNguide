import json
import re

# 读取文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    mage_data = json.load(f)

# 完整的技能名翻译映射
skill_name_map = {
    "Meteor": "陨石术",
    "Teleport": "传送",
    "Heal": "治疗术",
    "Ice Snake": "寒冰之蛇",
    "Wand Proficiency I": "法杖精通 I",
    "Wand Proficiency II": "法杖精通 II",
    "Air Mastery": "气元素精通",
    "Earth Mastery": "地元素精通",
    "Fire Mastery": "火元素精通",
    "Thunder Mastery": "电元素精通",
    "Water Mastery": "水元素精通",
    "Cheaper Meteor": "陨石术减耗",
    "Cheaper Meteor II": "陨石术减耗 II",
    "Cheaper Teleport": "传送减耗",
    "Cheaper Teleport II": "传送减耗 II",
    "Cheaper Heal": "治疗术减耗",
    "Cheaper Heal II": "治疗术减耗 II",
    "Cheaper Ice Snake": "寒冰之蛇减耗",
    "Cheaper Ice Snake II": "寒冰之蛇减耗 II",
    "Shooting Star": "流星",
    "Wisdom": "智慧",
    "Displacement": "位移",
    "Crashing Comet": "碎星陨击",
    "Astral Fragmentation": "星辰碎片",
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
    "Dawn": "黎明",
    "Gravitational Collapse": "引力坍缩",
    "Tangled Origin": "纠缠起源",
}

def comprehensive_translate(desc):
    """全面翻译描述"""
    if not desc:
        return desc

    result = desc

    # 翻译技能名引用
    for eng_name, chs_name in skill_name_map.items():
        result = result.replace(f'§n{eng_name}§7', f'§n{chs_name}§7')

    # 翻译常见英文短语
    translations = {
        'Hitting an enemy with': '用',
        'grants up\nto': '获得最多',
        'per': '每',
        'Each': '每',
        'gives': '给予',
        'Raw Damage': '原始伤害',
        'and decays at a rate of': '并以',
        'increasing as you gain': '随着获得',
        'After casting': '施放',
        'generate a lightning\nstrike near the point of impact': '在落点附近生成闪电',
        'that\nadds': '为每个被击中的攻击性敌人向你的',
        'Mana to your': '添加',
        'Mana Bank': '法力储备',
        'for each aggressive enemy you hit': '点法力',
        'per strike': '每次打击',
        'emits a strong light': '发出强光',
        'damaging nearby enemies': '对附近敌人造成伤害',
        'will damage nearby\nenemies when transferring': '在传送',
        'and': '与',
        'will leave a sigil of fire\non the ground that damages enemies every': '会在地面留下火焰法印，每',
        'Increase the damage of': '增加',
        'for Meteor': '陨石术',
        'for Ophanim': '光之宝珠',
        'Meteor Area of Effect': '陨石术伤害/作用范围',
        'scatters into debris upon\nlanding, dealing additional damage': '落地时分裂成碎片，造成额外伤害',
        'draws light from the\nstars, dealing additional damage': '从星辰汲取光芒，造成额外伤害',
    }

    for eng, chs in translations.items():
        result = result.replace(eng, chs)

    # 修复元素精通描述
    result = result.replace('增加基础伤害\nEarth属性攻击', '增加所有地属性攻击的基础伤害')
    result = result.replace('增加基础伤害\nFire属性攻击', '增加所有火属性攻击的基础伤害')
    result = result.replace('增加基础伤害\nThunder属性攻击', '增加所有电属性攻击的基础伤害')
    result = result.replace('增加基础伤害\nWater属性攻击', '增加所有水属性攻击的基础伤害')

    result = result.replace('§7Earth Damage:', '§7地伤害:')
    result = result.replace('§7Fire Damage:', '§7火伤害:')
    result = result.replace('§7Thunder Damage:', '§7电伤害:')
    result = result.replace('§7Water Damage:', '§7水伤害:')
    result = result.replace('§7Air Damage:', '§7气伤害:')

    return result

# 处理所有技能
for ability_key, ability_data in mage_data.get('abilities', {}).items():
    if 'description' in ability_data:
        ability_data['description'] = comprehensive_translate(ability_data['description'])

    if ability_key in skill_name_map:
        ability_data['customName'] = skill_name_map[ability_key]

# 保存
with open('src/.vuepress/components/data/zh-cn-mage.json', 'w', encoding='utf-8') as f:
    json.dump(mage_data, f, ensure_ascii=False, indent=4)

print("全面翻译完成！")
