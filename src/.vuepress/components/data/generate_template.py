import json
import os

# 配置路径
ATREE_PATH = './atree.json'      # 源文件
ZH_CN_PATH = './zh-cn.json'      # 目标翻译文件

def generate_translation_template():
    # 1. 读取原始数据 atree.json
    try:
        with open(ATREE_PATH, 'r', encoding='utf-8') as f:
            atree_data = json.load(f)
    except FileNotFoundError:
        print(f"错误: 找不到文件 {ATREE_PATH}")
        return

    # 2. 读取现有的 zh-cn.json (如果存在)
    existing_trans = {}
    if os.path.exists(ZH_CN_PATH):
        try:
            with open(ZH_CN_PATH, 'r', encoding='utf-8') as f:
                existing_trans = json.load(f)
            print(f"已加载现有翻译: {len(existing_trans)} 条")
        except json.JSONDecodeError:
            print("现有翻译文件格式错误，将重新生成")

    new_trans = existing_trans.copy()
    count = 0

    # 3. 遍历所有职业和技能
    for class_name, skills in atree_data.items():
        for skill in skills:
            # 使用 display_name 作为 key
            key = skill.get('display_name')
            
            if not key:
                continue

            # 如果这个技能还没有翻译，则创建新模板
            if key not in new_trans:
                # 获取原始描述
                original_desc = skill.get('desc', '').replace('\n', '\\n')
                
                # 自动提取 atree 中已有的属性 key (例如 range, damage)
                # 这样你就不用手动去查这个技能有哪些属性了
                original_props = skill.get('properties', {})
                auto_stats_keys = list(original_props.keys())

                # 按照优先级排序一下常用属性 (可选)
                priority_order = ['cost', 'damage', 'earth_damage', 'thunder_damage', 'water_damage', 'fire_damage', 'air_damage', 'range', 'aoe']
                auto_stats_keys.sort(key=lambda x: priority_order.index(x) if x in priority_order else 999)

                new_trans[key] = {
                    "name": key,  # 默认填英文名
                    "combo": "",  
                    "desc": original_desc, 
                    
                    # 【新结构】数据补丁：用于填入 atree 里缺失的数据 (如 cooldown, duration)
                    "properties": {}, 

                    # 【新结构】显示列表：自动填入了 atree 里有的 key
                    # 如果你在 properties 里补了 cooldown，记得手动在这里加上 "cooldown"
                    "stats_keys": auto_stats_keys,
                    
                    "note": ""
                }
                count += 1
                print(f"新增词条: {key}")

    # 4. 写入文件
    with open(ZH_CN_PATH, 'w', encoding='utf-8') as f:
        json.dump(new_trans, f, ensure_ascii=False, indent=4)

    print(f"完成！共新增 {count} 个待翻译技能。文件已保存至 {ZH_CN_PATH}")

if __name__ == "__main__":
    generate_translation_template()