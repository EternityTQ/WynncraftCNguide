import json

# 读取文件
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'r', encoding='utf-8') as f:
    assassin_data = json.load(f)

# 最后12个技能翻译
final_translations = {
    "Blade Fury": {
        "description": """§7§n多重击§7造成额外伤害，并可以向所有方向瞄准。

§c⚔ §7总伤害: §f+10% §8(基于你的DPS，每次攻击)
   §8(§e✦ §8电: +10%)"""
    },
    "Ricochets": {
        "description": """§7你的§n手里剑§7在命中时会在敌人之间弹射§f2§7次。

§2➼ §7范围: §f12格"""
    },
    "Thermobaric Smoke": {
        "description": """§7向§n烟雾弹§7注入挥发性化学物质，使其在落地时瞬间燃烧，伤害触发快§f0.3秒§7。

降低§n烟雾弹§7的持续时间§f1秒§7。

§c⚔ §7总伤害: §c-5% §8(基于你的DPS)
   §8(§6✣ §8伤害: -5%)
§d⌛ §7持续时间: §f-1秒"""
    },
    "Thrill": {
        "description": """§7成功施放§n背刺§7后获得§f+50%§7移动速度(§3➲§7)。

§d⌛ §7持续时间: §f2秒"""
    },
    "Shadow Siphon": {
        "description": """§7从背后用§n背刺§7击中敌人后，降低§n隐身§7的冷却§f-1.75秒§7。"""
    },
    "Ripple": {
        "description": """§7从§f5格§7或更高处坠落时，着陆时对周围造成伤害。

此伤害随后续每多坠落一格增加§f+12%§7，最多额外§f+10格§7。

§c⚔ §7总伤害: §f120% §8(基于你的DPS)
   §8(§6✣ §8伤害: 100%)
   §8(§b❉ §8水: 20%)
§3☀ §7伤害/作用范围: §f8格 §7(圆形)"""
    },
    "Finality": {
        "description": """§7§n多重击§7的伤害逐击递增，造成额外伤害。伤害加成上限为§f8§7次命中。

§c⚔ §7总伤害: §f+6% §8(基于你的DPS)
   §8(§6✣ §8伤害: +4%)
   §8(§f❋ §8气: +2%)"""
    },
    "Aerial Ace": {
        "description": """§7用§n天鹅俯冲§7击中敌人时获得伤害加成。

§e✧ §7效果: §f+35%§7伤害加成(§c⚔§7) 对自己
§d⌛ §7持续时间: §f7.5秒"""
    },
    "Mutilate": {
        "description": """§7增加§n多重击§7的命中次数§f+3§7次。

增加§n终焉狂热§7的伤害上限§f+3§7次命中。"""
    },
    "Foul Play": {
        "description": """§7§n镜像幻术§7激活时，§n瞬身斩§7将杀死一个§b镜像分身 §#c267f7§7而不是进入冷却。

降低§n多重击§7的技能消耗。

§b✺ §7技能消耗: §f-5点"""
    },
    "Duplicity": {
        "description": """§7§n镜像幻术§7额外召唤§f+2§7个§b镜像分身 §#c267f7§7。

§3⌚ §7冷却: §f+5秒"""
    },
    "Looming Presence": {
        "description": """§7增加§n背刺§7的范围。

§2➼ §7范围: §f+2格"""
    },
    "Billowing Death": {
        "description": """§7用成功的§n背刺§7击中拥有§f2+§7个§b标记 §c✜§7的敌人时，释放一团烟雾，将该敌人§f50%§7的§b标记 §c✜§7施加到其他敌人身上。

§3☀ §7伤害/作用范围: §f5格 §7(圆形)
§3⌚ §7冷却: §f3秒"""
    },
    "Shadow Dance": {
        "description": """§7施放§n隐身§7后的第二次攻击造成§f+50%§7伤害。

§d⌛ §7持续时间: §f2秒
§3⌚ §7冷却: §f3秒"""
    },
    "Paranoia": {
        "description": """§7失去一个§b镜像分身 §#c267f7§7后，获得§f+20%§7移动速度(§3➲§7)。

§d⌛ §7持续时间: §f4秒"""
    }
}

# 应用翻译
for ability_name, translation in final_translations.items():
    if ability_name in assassin_data['abilities']:
        ability = assassin_data['abilities'][ability_name]
        if 'description' in translation:
            ability['description'] = translation['description']

# 保存文件
with open(r'd:\WynncraftCNguide\src\.vuepress\components\data\zh-cn-assassin.json', 'w', encoding='utf-8') as f:
    json.dump(assassin_data, f, ensure_ascii=False, indent=0)

print(f"已翻译最后 {len(final_translations)} 个技能")
print("\n所有翻译已完成！")
