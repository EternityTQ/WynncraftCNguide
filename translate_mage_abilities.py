import json
import re

# 读取源文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    mage_data = json.load(f)

# 读取已有翻译
with open('src/.vuepress/components/data/zh-cn.json', 'r', encoding='utf-8') as f:
    existing_translations = json.load(f)

# 技能名翻译映射
skill_name_map = {
    "Meteor": "流星天降",
    "Wand Proficiency I": "法杖精通 I",
    "Wand Proficiency II": "法杖精通 II",
    "Cheaper Meteor": "流星减耗",
    "Shooting Star": "疾速流星",
    "Teleport": "传送",
    "Wisdom": "智慧",
    "Heal": "治愈",
    "Ice Snake": "寒冰之蛇",
    "Cheaper Teleport": "传送减耗",
    "Air Mastery": "气元素精通",
    "Earth Mastery": "地元素精通",
    "Fire Mastery": "火元素精通",
    "Thunder Mastery": "电元素精通",
    "Water Mastery": "水元素精通",
}

# 输出进度
print("开始翻译法师技能树...")
print(f"共有 {len(mage_data['abilities'])} 个技能需要处理")
