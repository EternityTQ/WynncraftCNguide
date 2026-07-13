import json

# Load source and reference files
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    source = json.load(f)

with open('src/.vuepress/components/data/zh-cn.json', 'r', encoding='utf-8') as f:
    reference = json.load(f)

# Load current progress
with open('src/.vuepress/components/data/zh-cn-mage-translated.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

# Translation mappings
skill_names = {
    "Time Dilation": "时间膨胀",
    "Divination": "占卜",
    "Sunflare": "日耀",
    "Halo": "光环",
    "Arcane Overflow": "秘法溢流",
    "Memory Recollection": "记忆回溯",
    "Manastorm": "法力风暴",
    "Cheaper Heal II": "治疗减耗 II",
    "Freezing Sigil": "冰封印记",
    "Arctic Snake": "极寒之蛇",
    "Gleam": "微光",
    "Accelerated Strike": "加速打击",
    "Influx Shift": "涌流转移",
    "Devitalize": "削弱",
    "Mana Current": "法力流",
    "Riftbound": "裂隙束缚",
    "Judrajim": "尤德拉吉姆",
    "Diffraction": "衍射",
    "Time Vortex": "时间漩涡",
    "Portal to the Beyond": "异界之门",
    "Paradox": "悖论",
    "Blitz": "闪电战",
    "Induced Instability": "诱发不稳",
    "Dawn": "黎明",
    "Gravitational Collapse": "引力坍缩",
    "Tangled Origin": "纠缠起源"
}

def translate_description(desc, skill_name):
    """Translate ability description"""
    # Replace skill names with underscored versions
    desc = desc.replace("§nMeteor§", "_陨石术_")
    desc = desc.replace("§nTeleport§", "_传送_")
    desc = desc.replace("§nHeal§", "_治疗_")
    desc = desc.replace("§nIce Snake§", "_寒冰之蛇_")
    desc = desc.replace("§nOphanim§", "_光明圣轮_")
    desc = desc.replace("§nArcane Transfer§", "_秘法转移_")
    desc = desc.replace("§nFrozen Tornado§", "_冰封龙卷_")
    desc = desc.replace("§nLightweaver§", "_光织者_")
    desc = desc.replace("§nEtheric Slash§", "_以太斩击_")
    desc = desc.replace("§nDimensional Tear§", "_次元裂隙_")
    desc = desc.replace("§nMain Attack§", "_普通攻击_")
    desc = desc.replace("§nPyrokinesis§", "_火焰念力_")
    desc = desc.replace("§nThunderstorm§", "_雷暴_")
    desc = desc.replace("§nMeteor Shower§", "_陨石雨_")
    desc = desc.replace("§nArcane Restoration§", "_秘法复原_")
    desc = desc.replace("§nSunshower§", "_日光倾洒_")
    desc = desc.replace("§nVacuokinesis§", "_真空念力_")
    desc = desc.replace("§nTime Dilation§", "_时间膨胀_")
    desc = desc.replace("§nJudrajim§", "_尤德拉吉姆_")
    desc = desc.replace("§nRiftbound§", "_裂隙束缚_")
    desc = desc.replace("§nTime Vortex§", "_时间漩涡_")
    desc = desc.replace("§nRiftspawn§", "_裂隙孽生_")
    desc = desc.replace("§nWind Slash§", "_风之斩_")
    desc = desc.replace("§nAstral Fragmentation§", "_星界碎裂_")
    desc = desc.replace("§nCrystallized §j💎§", "$结晶$")
    desc = desc.replace("§bCrystallized §j💎§", "$结晶$")
    desc = desc.replace("§bDistortion §#c267f7≈§", "$扭曲$")
    desc = desc.replace("§bMana Bank ✺§", "$法力储备$")
    desc = desc.replace("§bMana Bank §b✺§", "$法力储备$")
    desc = desc.replace("§bShining §#e1dca4✨§", "$光耀$")
    desc = desc.replace("§bUnstable §9⚡§", "$不稳$")
    desc = desc.replace("§bUltimate Meter ⚡§", "$终极能量槽$")
    desc = desc.replace("§bThunder Serpent§", "$雷霆巨蛇$")
    desc = desc.replace("§bFire\nSerpent§", "$烈焰巨蛇$")

    # Basic translations
    lines = []
    for line in desc.split('\n'):
        # Keep special markers
        if '§6技能连击:' in line or '§6Click Combo:' in line:
            line = line.replace('§6Click Combo:', '§6技能连击:')
            line = line.replace('§d§lRIGHT', '§d§l右键')
            line = line.replace('§d§lLEFT', '§d§l左键')
            line = line.replace('§d§lF§', '§d§lF§')
            lines.append(line)
            continue

        # Translate stat labels
        line = line.replace('§b✺ §7Mana Cost:', '§b✺ §7技能消耗:')
        line = line.replace('§c⚔ §7Total Damage:', '§c⚔ §7总伤害:')
        line = line.replace('§c⚔ §7Main Attack Damage:', '§c⚔ §7普通攻击伤害:')
        line = line.replace('§c❤ §7Total Heal:', '§c❤ §7总治疗量:')
        line = line.replace('§c❤ §7Pulse Self Heal:', '§c❤ §7脉动自我治疗:')
        line = line.replace('§c❤ §7Health Regen:', '§c❤ §7生命回复:')
        line = line.replace('§2➼ §7Range:', '§2➼ §7范围:')
        line = line.replace('§2➼ §7Vision:', '§2➼ §7视野范围:')
        line = line.replace('§2➼ §7Drift Range:', '§2➼ §7漂移范围:')
        line = line.replace('§2➼ §7Target Radius:', '§2➼ §7目标半径:')
        line = line.replace('§3☀ §7Area of Effect:', '§3☀ §7伤害/作用范围:')
        line = line.replace('§3☀ §7Target Radius:', '§3☀ §7目标半径:')
        line = line.replace('§3☀ §7Meteor Area of Effect:', '§3☀ §7陨石术伤害范围:')
        line = line.replace('§3☀ §7Range:', '§3☀ §7范围:')
        line = line.replace('§d⌛ §7Duration:', '§d⌛ §7持续时间:')
        line = line.replace('§d⌛ §7Tornado Duration:', '§d⌛ §7龙卷风持续时间:')
        line = line.replace('§d⌛ §7Slow Duration:', '§d⌛ §7减速持续时间:')
        line = line.replace('§3⌚ §7Cooldown:', '§3⌚ §7冷却:')
        line = line.replace('§3⌚ §7Delay:', '§3⌚ §7延迟:')
        line = line.replace('§e✧ §7Effect:', '§e✧ §7效果:')
        line = line.replace('§b✺ §7Mana Regen:', '§b✺ §7法力回复:')

        # Element translations
        line = line.replace('§8(§6✣ §8Damage:', '§8(§6✣ §8伤害:')
        line = line.replace('§8(§2✤ §8Earth:', '§8(§2✤ §8地:')
        line = line.replace('§8(§e✦ §8Thunder:', '§8(§e✦ §8电:')
        line = line.replace('§8(§b❉ §8Water:', '§8(§b❉ §8水:')
        line = line.replace('§8(§c✹ §8Fire:', '§8(§c✹ §8火:')
        line = line.replace('§8(§f❋ §8Air:', '§8(§f❋ §8气:')

        # Common words
        line = line.replace('of your DPS', '基于你的输出')
        line = line.replace('of your max health', '你的最大生命值')
        line = line.replace('of your max mana', '你的最大法力值')
        line = line.replace('of max health', '最大生命值')
        line = line.replace('Main Attack Damage', '普通攻击伤害')
        line = line.replace('§7(Circle-Shaped)', '§7(圆形)')
        line = line.replace('per second', '每秒')
        line = line.replace('per hit', '每次命中')
        line = line.replace('per strike', '每道闪电')
        line = line.replace('per Wisp', '每个光之精灵')
        line = line.replace('per pulse', '每次脉动')
        line = line.replace('Deadly Beam', '致命光束')
        line = line.replace('Collapse', '坍缩')
        line = line.replace('Thunder', '雷霆')
        line = line.replace('Fire', '烈焰')
        line = line.replace('Slowness (§c⬤§7) to Enemies', '减缓敌人')
        line = line.replace('Damage Bonus (§a⚔§7) to Allies', '伤害加成')
        line = line.replace('Damage Bonus (§c⚔§7) to Enemies', '削弱攻击')
        line = line.replace('Resistance Bonus (§a❁§7)', '抗性提升')
        line = line.replace('Walk Speed to Allies', '移动速度')
        line = line.replace('Walk Speed', '移动速度')
        line = line.replace('Knockback Immunity to Allies', '击退免疫')
        line = line.replace('Blocks', '格')
        line = line.replace('Block', '格')

        lines.append(line)

    return '\n'.join(lines)

# Translate remaining abilities
remaining_abilities = [
    "Time Dilation", "Divination", "Sunflare", "Halo", "Arcane Overflow",
    "Memory Recollection", "Manastorm", "Cheaper Heal II", "Freezing Sigil",
    "Arctic Snake", "Gleam", "Accelerated Strike", "Influx Shift", "Devitalize",
    "Mana Current", "Riftbound", "Judrajim", "Diffraction", "Time Vortex",
    "Portal to the Beyond", "Paradox", "Blitz", "Induced Instability",
    "Dawn", "Gravitational Collapse", "Tangled Origin"
]

for ability_name in remaining_abilities:
    if ability_name in source['abilities']:
        ability = source['abilities'][ability_name].copy()
        ability['description'] = translate_description(ability['description'], ability_name)
        ability['customName'] = skill_names.get(ability_name, ability_name)
        output['abilities'][ability_name] = ability

# Add cellMap
output['cellMap'] = source['cellMap']

# Save output
with open('src/.vuepress/components/data/zh-cn-mage-translated.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)

print("Translation complete!")
print(f"Total abilities translated: {len(output['abilities'])}")
