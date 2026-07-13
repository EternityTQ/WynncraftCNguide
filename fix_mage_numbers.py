import json
import re

# 读取原始英文文件（重新开始）
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    original_content = f.read()

# 恢复原始内容（从你提供的第一次读取结果）
# 由于文件已被修改，我们需要手动修复

# 读取当前文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'r', encoding='utf-8') as f:
    mage_data = json.load(f)

# 修复已经错误翻译的数字（将"X点Y点"改回正确的"XY点"）
for ability_key, ability_data in mage_data.get('abilities', {}).items():
    if 'description' in ability_data:
        desc = ability_data['description']
        # 修复类似"5点0点"的错误，改为"50点"
        desc = re.sub(r'§f(\d)点(\d)点', r'§f\g<1>\g<2>点', desc)
        # 修复类似"2点5点"的错误，改为"25点"
        desc = re.sub(r'§f(\d)点(\d)点', r'§f\g<1>\g<2>点', desc)
        # 修复类似"-1点0点"的错误，改为"-10点"
        desc = re.sub(r'§f(-?\d)点(\d)点', r'§f\g<1>\g<2>点', desc)
        # 修复类似"3点5点"的错误，改为"35点"
        desc = re.sub(r'§f(\d)点(\d)点', r'§f\g<1>\g<2>点', desc)

        # 多次执行以处理三位数
        desc = re.sub(r'§f(\d)点(\d)点', r'§f\g<1>\g<2>点', desc)
        desc = re.sub(r'§f(\d{1,2})点(\d)点', r'§f\g<1>\g<2>点', desc)

        ability_data['description'] = desc

# 保存修复后的文件
with open('src/.vuepress/components/data/zh-cn-mage.json', 'w', encoding='utf-8') as f:
    json.dump(mage_data, f, ensure_ascii=False, indent=4)

print("数字修复完成！")
