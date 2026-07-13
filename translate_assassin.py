import json
import re

# 读取文件
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'r', encoding='utf-8') as f:
    assassin_data = json.load(f)

with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn.json', 'r', encoding='utf-8') as f:
    reference_data = json.load(f)

# 创建技能名映射
skill_name_map = {}
for skill_name, skill_info in reference_data.items():
    if 'name' in skill_info:
        skill_name_map[skill_name] = skill_info['name']

# 翻译映射
translations = {
    'Mana Cost': '技能消耗',
    'Total Damage': '总伤害',
    'Damage': '伤害',
    'of your DPS': '基于你的DPS',
    'per hit': '每次攻击',
    'Range': '范围',
    'Area of Effect': '伤害/作用范围',
    'Duration': '持续时间',
    'Cooldown': '冷却',
    'Effect': '效果',
    'Blocks': '格',
    'Block': '格',
    'Circle-Shaped': '圆形',
    'Cone-Shaped': '锥形',
    'Click Combo': '连击',
    'RIGHT': '右键',
    'LEFT': '左键',
    'to Self': '对自己',
    'to Enemies': '对敌人',
    'Resistance Bonus': '抗性提升',
    'Damage Bonus': '伤害加成',
    'Speed Bonus': '速度加成',
    'Walk Speed': '移动速度',
    'Jump Height': '跳跃高度',
    'Main Attack': '普通攻击',
    'Air': '气',
    'Earth': '地',
    'Fire': '火',
    'Thunder': '电',
    'Water': '水',
    'Poison Damage': '毒伤',
    'per': '每',
    'Max': '上限',
    'or': '或',
    'Raw': '点原始',
    'you have from items': '你的装备鉴定词条上每有',
    'gain': '获得',
    'Increase': '增加',
    'Increases': '增加',
    'your': '你的',
    'base damage': '基础伤害',
    'from all': '所有',
    'attacks': '攻击',
    'Reduce': '降低',
    'the': '',
    'of': '',
    'will': '将',
    'hit': '命中',
    'twice': '两次',
    'but deal': '但每次造成',
    'damage per hit': '伤害',
    'additional range': '额外范围',
    'Dash in the direction you\'re facing': '向你面对的方向冲刺',
    'Unleashes a rapid flurry of': '对面前的敌人施放快速连击，造成',
    'hits to enemies facing you, dealing heavy damage': '次重击伤害',
    'Throws a bomb that slowly emanates smoke': '投掷一颗炸弹，缓慢释放烟雾',
    'damaging all enemies in it every': '每',
    'Makes': '将',
    'a single devastating hit': '变为单次毁灭性的打击',
    'If you strike an enemy from behind, it deals': '如果从背后攻击敌人，造成',
    'double': '双倍',
    'will hide you into the shadows': '将使你隐身于阴影中',
    'You cannot heal or gain mana while in that state': '在此状态下你无法治疗或获得法力',
    'Attack or get hit to cancel': '攻击或受到伤害以取消',
    'Invisibility': '隐身',
    'will stick to enemies and deal additional damage': '将粘附在敌人身上并造成额外伤害',
}

# 自定义技能名（不在zh-cn.json中的）
custom_names = {
    "Dagger Proficiency I": "匕首精通 I",
    "Cheaper Spin Attack I": "旋风斩减耗 I",
    "Double Spin": "双旋斩",
    "Dash": "闪现",
    "Multihit": "多重打击",
    "Smoke Bomb": "烟雾弹",
    "Cheaper Dash I": "闪现减耗 I",
    "Double Slice": "双重切割",
    "Poisoned Blade": "淬毒之刃",
    "Backstab": "背刺",
    "Vanish": "消失",
    "Sticky Bomb": "粘性炸弹",
    "Petal Storm": "花瓣风暴",
    "Righting Reflex": "空中反射",
    "Surprise Strike": "突袭",
    "Mirror Image": "镜像",
    "Lacerate": "撕裂",
    "Last Laugh": "临终嘲讽",
    "Silent Killer": "无声杀手",
    "Wall of Smoke": "烟墙",
    "Doppleganger": "二重身",
    "Psithurism": "飒飒之声",
    "Paranoia": "偏执狂",
    "Cheaper Multihit I": "多重打击减耗 I",
    "Rolling Fog": "翻滚迷雾",
    "Shadow Travel": "暗影旅行",
    "Distraction": "扰乱",
    "Bamboozle": "欺骗",
    "Cheaper Smoke Bomb I": "烟雾弹减耗 I",
    "Blazing Powder": "炽焰之粉",
    "Weightless": "失重",
    "Disappearing Act": "消失魔术",
    "Hop": "跳跃",
    "Sandbagging": "拖延战术",
    "Black Hole": "黑洞",
    "Choke Bomb": "窒息炸弹",
    "Noxious Haze": "毒雾",
    "Marked": "标记",
    "Violent Vortex": "暴力漩涡",
    "Echo": "回响",
    "Shurikens": "手里剑",
    "Far Reach": "远距离攻击",
    "Dancing Blade": "舞动之刃",
    "Cheaper Dash II": "闪现减耗 II",
    "Cheaper Multihit II": "多重打击减耗 II",
    "Cheaper Smoke Bomb II": "烟雾弹减耗 II",
    "Cheaper Spin Attack II": "旋风斩减耗 II",
    "Ambush": "伏击",
    "Death Magnet": "死亡磁石",
    "Celerity": "敏捷",
    "Nightcloak Knife": "夜幕之刃",
    "Hoodwink": "蒙骗",
    "Braced Impact": "准备着陆",
    "Wall Jump": "墙壁跳跃",
    "Eviscerate": "剜割",
    "Dextrous Hands": "灵巧双手",
    "Dissolution": "溶解",
    "Fatal Spin": "致命旋转",
    "Bladestorm": "刀刃风暴",
    "Harvester": "收割者",
    "More Marks": "标记扩容",
    "Blade Fury": "刀刃狂怒",
    "Ricochets": "弹射",
    "Deflagate": "点燃",
    "Satsujin": "杀人",
    "Thermobaric Smoke": "温压烟雾",
    "Jasmine Bloom": "茉莉绽放",
    "Another Self": "另一个自己",
    "Serpent's Garden": "蛇之花园",
    "Thrill": "兴奋",
    "Marked for Death": "死亡标记",
    "Devour": "吞噬",
    "Shadow Siphon": "暗影虹吸",
    "Ripple": "涟漪",
    "Finality": "终结",
    "Swan Dive": "天鹅俯冲",
    "Aerial Ace": "空中王牌",
    "Mutilate": "切割强化",
    "Foul Play": "犯规",
    "Mirage": "海市蜃楼",
    "Duplicity": "欺骗术",
    "Malicious Mockery": "恶意嘲讽",
    "Misdirection": "误导",
    "Shadow Projection": "暗影投影",
    "Toxic Sludge": "毒性污泥",
    "Soul Siphon": "灵魂虹吸",
    "Shadow Dance": "暗影之舞",
    "Looming Presence": "逼近威压",
    "Billowing Death": "翻涌死亡",
    "Pierce the Veil": "刺穿面纱"
}

# 处理技能
newly_translated = []
for ability_name, ability_data in assassin_data['abilities'].items():
    # 设置customName
    if not ability_data.get('customName'):
        if ability_name in skill_name_map:
            ability_data['customName'] = skill_name_map[ability_name]
        elif ability_name in custom_names:
            ability_data['customName'] = custom_names[ability_name]
            newly_translated.append(ability_name)
        else:
            newly_translated.append(ability_name)

    # 翻译description（简化版本，主要处理数值字段）
    if ability_data.get('description'):
        desc = ability_data['description']

        # 翻译常见短语
        desc = desc.replace('Mana Cost:', '技能消耗:')
        desc = desc.replace('Total Damage:', '总伤害:')
        desc = desc.replace('of your DPS', '基于你的DPS')
        desc = desc.replace('per hit', '每次攻击')
        desc = desc.replace('Range:', '范围:')
        desc = desc.replace('Area of Effect:', '伤害/作用范围:')
        desc = desc.replace('Duration:', '持续时间:')
        desc = desc.replace('Cooldown:', '冷却:')
        desc = desc.replace('Effect:', '效果:')
        desc = desc.replace(' Blocks', '格')
        desc = desc.replace(' Block', '格')
        desc = desc.replace('Circle-Shaped', '圆形')
        desc = desc.replace('Cone-Shaped', '锥形')
        desc = desc.replace('to Self', '对自己')
        desc = desc.replace('to Enemies', '对敌人')

        ability_data['description'] = desc

# 保存
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'w', encoding='utf-8') as f:
    json.dump(assassin_data, f, ensure_ascii=False, indent=4)

print("翻译完成！")
print(f"\n以下{len(newly_translated)}个技能名是新翻译的（不在zh-cn.json中）：")
for name in newly_translated:
    print(f"  - {name}: {custom_names.get(name, '【需要翻译】')}")
