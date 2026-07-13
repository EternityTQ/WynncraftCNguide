import json

# 读取文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    mage_data = json.load(f)

with open('src/.vuepress/components/data/zh-cn.json', 'r', encoding='utf-8') as f:
    existing = json.load(f)

# 技能名映射（从现有翻译提取+新增）
name_map = {
    "Meteor": "流星天降",
    "Wand Proficiency I": "法杖精通 I",
    "Wand Proficiency II": "法杖精通 II",
    "Cheaper Meteor": "流星减耗",
    "Cheaper Meteor II": "流星减耗 II",
    "Shooting Star": "疾速流星",
    "Teleport": "传送",
    "Cheaper Teleport": "传送减耗",
    "Cheaper Teleport II": "传送减耗 II",
    "Wisdom": "智慧",
    "Heal": "治愈",
    "Cheaper Heal": "治愈减耗",
    "Cheaper Heal II": "治愈减耗 II",
    "Ice Snake": "寒冰之蛇",
    "Cheaper Ice Snake": "寒冰之蛇减耗",
    "Cheaper Ice Snake II": "寒冰之蛇减耗 II",
}

# 输出需要翻译的技能列表
print("法师技能列表:")
for idx, (key, ability) in enumerate(mage_data['abilities'].items(), 1):
    print(f"{idx}. {key}")
    if ability.get('customName'):
        print(f"   已有翻译: {ability['customName']}")

print(f"\n总计: {len(mage_data['abilities'])} 个技能")
