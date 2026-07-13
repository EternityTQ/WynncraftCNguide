import json
import re

with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    source = json.load(f)

with open('src/.vuepress/components/data/zh-cn-mage-translated.json', 'r', encoding='utf-8') as f:
    output = json.load(f)

def full_translate(text):
    # Skill name replacements
    replacements = [
        ("§nMeteor§", "_陨石术_"),
        ("§nTeleport§", "_传送_"),
        ("§nHeal§", "_治疗_"),
        ("§nIce Snake§", "_寒冰之蛇_"),
        ("§nOphanim§", "_光明圣轮_"),
        ("§nArcane Transfer§", "_秘法转移_"),
        ("§nFrozen Tornado§", "_冰封龙卷_"),
        ("§nLightweaver§", "_光织者_"),
        ("§nEtheric Slash§", "_以太斩击_"),
        ("§nDimensional Tear§", "_次元裂隙_"),
        ("§nMain Attack§", "_普通攻击_"),
        ("§nPyrokinesis§", "_火焰念力_"),
        ("§nThunderstorm§", "_雷暴_"),
        ("§nMeteor Shower§", "_陨石雨_"),
        ("§nArcane Restoration§", "_秘法复原_"),
        ("§nSunshower§", "_日光倾洒_"),
        ("§nVacuokinesis§", "_真空念力_"),
        ("§nTime Dilation§", "_时间膨胀_"),
        ("§nJudrajim§", "_尤德拉吉姆_"),
        ("§nRiftbound§", "_裂隙束缚_"),
        ("§nTime Vortex§", "_时间漩涡_"),
        ("§nRiftspawn§", "_裂隙孽生_"),
        ("§nWind Slash§", "_风之斩_"),
        ("§nAstral Fragmentation§", "_星界碎裂_"),
        ("§nSunflare§", "_日耀_"),
        ("§nCrystallized §j💎§", "$结晶$"),
        ("§bCrystallized §j💎§", "$结晶$"),
        ("§bDistortion §#c267f7≈§", "$扭曲$"),
        ("§bMana Bank ✺§", "$法力储备$"),
        ("§bMana Bank §b✺§", "$法力储备$"),
        ("§bShining §#e1dca4✨§", "$光耀$"),
        ("§bUnstable §9⚡§", "$不稳$"),
        ("§bUltimate Meter ⚡§", "$终极能量槽$"),
        ("§bThunder Serpent§", "$雷霆巨蛇$"),
        ("§bFire\nSerpent§", "$烈焰巨蛇$"),
        ("§bFire Serpent§", "$烈焰巨蛇$"),
    ]

    for old, new in replacements:
        text = text.replace(old, new)

    # English to Chinese translations
    trans = [
        ("Creates an area of effect when sprinting", "奔跑时创建一个效果区域"),
        ("that increases the walk speed of all", "增加所有盟友的移动速度"),
        ("allies the longer they run in it.", "他们在其中奔跑的时间越长,速度越快。"),
        ("You lose 20% Speed Bonus every second", "一旦停止奔跑,每秒失去20%速度加成"),
        ("once you stop running", ""),
        ("Increases your maximum orbs", "增加你的最大光之宝珠数量"),
        ("from", ""),
        ("and\nreduces their damage.", "并降低它们的伤害。"),
        ("Healing", "在"),
        ("within", "内治疗"),
        ("will make your next", "会使你的下一次"),
        ("activate", "激活"),
        ("While", "当"),
        ("is active, you will restore", "激活时,你会为所有附近盟友恢复"),
        ("health and mana to all nearby allies, and", "生命值和法力值,并且"),
        ("your", "你的"),
        ("orbs will attack constantly.", "光之宝珠会持续攻击。"),
        ("Increase your Max Orbs", "增加你的最大光之宝珠数量"),
        ("will allow you to overflow", "允许你的法力溢出"),
        ("your mana over its maximum limits. (Max 300)", "超过其最大限制。(最多 300)"),
        ("will cast", "会施放"),
        ("spells.", "个法术。"),
        ("If you have more than", "如果你拥有超过"),
        ("Mana, casting a spell will give", "点法力,施放法术会在"),
        ("you", "内给予你"),
        ("Mana over", "点法力"),
        ("will leave a sigil of ice", "会在你脚下留下冰封印记"),
        ("beneath you that slows and damages", "减速并伤害"),
        ("enemies every", "其上的敌人,每"),
        ("Allies standing on", "站在"),
        ("the sigil will be immune to knockback.", "印记上的盟友将免疫击退。"),
        ("will freeze enemies for", "会冻结敌人"),
        ("Increase the damage of", "增加"),
        ("的伤害。"),
    ]
