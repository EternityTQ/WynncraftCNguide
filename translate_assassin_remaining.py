import json

# 读取文件
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'r', encoding='utf-8') as f:
    assassin_data = json.load(f)

# 剩余技能翻译
remaining_translations = {
    "Bamboozle": {
        "description": """§7§n多重击§7将改为向前传送并施放一次狂暴的火焰斩击。

§c⚔ §7总伤害: §f350% §8(基于你的DPS)
   §8(§6✣ §8伤害: 300%)
   §8(§c✹ §8火: 50%)
§2➼ §7范围: §f6格
§3☀ §7伤害/作用范围: §f5格 §7(圆形)
§3⌚ §7冷却: §f5秒"""
    },
    "Blazing Powder": {
        "description": """§7§n旋风斩§7和§n撕裂§7造成额外伤害。

§c⚔ §7总伤害: §f+20% §8(基于你的DPS)
   §8(§c✹ §8火: +20%)"""
    },
    "Weightless": {
        "description": """§7在空中击中敌人时获得§f+1§7点法力。
§8(离地1.25+格视为空中)"""
    },
    "Disappearing Act": {
        "description": """§7召唤§b镜像分身 §#c267f7§7时制造爆炸。

§c⚔ §7总伤害: §f800% §8(基于你的DPS)
   §8(§6✣ §8伤害: 550%)
   §8(§c✹ §8火: 250%)
§3☀ §7伤害/作用范围: §f5格 §7(圆形)"""
    },
    "Sandbagging": {
        "description": """§7每当你受到低于最大生命值§f10%§7的伤害时，所有技能冷却降低§f30%§7。

§3⌚ §7冷却: §f1秒"""
    },
    "Black Hole": {
        "description": """§7§n烟雾弹§7会拉扯附近的敌人。

§2➼ §7范围: §f6格"""
    },
    "Violent Vortex": {
        "description": """§7单次伤害超过你最大生命值§f1.5倍§7时，将造成§f45%§7的伤害扩散至附近其他敌人。

§3☀ §7伤害/作用范围: §f10格 §7(圆形)
§3⌚ §7冷却: §f2秒"""
    },
    "Echo": {
        "description": """§7失去一个§b镜像分身 §#c267f7§7后，你的下一个§n旋风斩§7或§n烟雾弹§7将被所有活跃的§b分身 §#c267f7§#f5cfff§#d84c4c§7复制，但造成§c-25%§7伤害。"""
    },
    "Shurikens": {
        "description": """§7使用§n突进§7后，准备§f+3§7枚手里剑§8(最多9枚)§7。

你的下一次§n普通攻击§7将投掷所有准备好的手里剑。

§c⚔ §7总伤害: §f120% §8(基于你的DPS，每枚手里剑)
   §8(§6✣ §8伤害: 100%)
   §8(§c✹ §8火: 20%)
§2➼ §7范围: §f50格"""
    },
    "Dancing Blade": {
        "description": """§7在拥有§f3+§7层§b动能 §f➲§7时使用§n天鹅俯冲§7，着陆后§f0.25秒§7会再次跃起。"""
    },
    "Death Magnet": {
        "description": """§7退出§n隐身§7时，将所有附近§b标记 §c✜§7的怪物拉向你进入§n隐身§7的位置。

§2➼ §7范围: §f20格"""
    },
    "Celerity": {
        "description": """§7每§f1§7层§b动能 §f➲§7使§n天鹅俯冲§7造成§f+2%§7伤害。

§n突进§7的水平速度增加§f10%§7。"""
    },
    "Braced Impact": {
        "description": """§7用§n天鹅俯冲§7着陆时短暂获得抗性。

§e✧ §7效果: §f50%§7抗性加成(§a❁§7) 对自己
§d⌛ §7持续时间: §f2秒"""
    },
    "Wall Jump": {
        "description": """§7降低§n雀跃§7的冷却§f-1秒§7。使用§n雀跃§7撞到墙壁会将你向后弹开。
§8(按住Shift键取消)"""
    },
    "Eviscerate": {
        "description": """§7§n撕裂§7造成更多伤害，并额外斩击§f+1§7次。

§c⚔ §7总伤害: §f+10% §8(基于你的DPS)
   §8(§e✦ §8电: +10%)"""
    },
    "Dextrous Hands": {
        "description": """§7§n雀跃§7现在也会准备§f3§7枚手里剑。你可以额外准备§f+3§7枚手里剑。§8(最多12枚)§7"""
    },
    "Dissolution": {
        "description": """§7进入和退出§n隐身§7时，短暂免疫击退并获得抗性。

§e✧ §7效果: §f+60%§7抗性加成(§8✾§7) 对自己
§d⌛ §7持续时间: §f0.5秒"""
    },
    "Fatal Spin": {
        "description": """§7增加§n旋风斩§7和§n撕裂§7的范围和伤害，并给被击中的敌人添加§b+1§7个§b标记 §c✜§7。

§c⚔ §7总伤害: §f+20% §8(基于你的DPS)
   §8(§6✣ §8伤害: +20%)
§3☀ §7伤害/作用范围: §f+1格 §7(圆形)"""
    },
    "Bladestorm": {
        "description": """§7增加§n暴戾漩涡§7的伤害§f+55%§7，并将伤害要求提高至最大生命值的§f2.5倍§7。"""
    },
    "Harvester": {
        "description": """§7击杀敌人时，每剩余一个§b标记 §c✜§7获得§f+2§7点法力，消耗§b标记 §c✜§7时同样获得§f+2§7点法力。"""
    }
}

# 应用翻译
for ability_name, translation in remaining_translations.items():
    if ability_name in assassin_data['abilities']:
        ability = assassin_data['abilities'][ability_name]
        if 'description' in translation:
            ability['description'] = translation['description']

# 保存文件
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'w', encoding='utf-8') as f:
    json.dump(assassin_data, f, ensure_ascii=False, indent=0)

print(f"已翻译 {len(remaining_translations)} 个技能")
