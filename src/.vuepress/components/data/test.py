import json
import re

def format_key(key):
    return key.replace("_", " ")

def process_description(description, key):
    # 已处理的情况：<b>xxx</b><br>(
    if re.search(r'</b><br>\([^<]*\)', description):
        return description  # 跳过已处理项

    # 插入 (主键) 的格式，主键不加粗
    formatted_key = format_key(key)
    pattern = r'(<b>[^<]*)(</b>)'
    replacement = r'\1\2<br>(' + formatted_key + r')'
    new_description = re.sub(pattern, replacement, description, count=1)
    return new_description

def update_descriptions(data):
    updated = False
    for key, value in data.items():
        if 'description' in value:
            original = value['description']
            new_desc = process_description(original, key)
            if new_desc != original:
                data[key]['description'] = new_desc
                updated = True
    return updated

# 加载 JSON 文件
with open('skills.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理数据
if update_descriptions(data):
    with open('skills_modified.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("描述已更新，保存为 skills_modified.json")
else:
    print("没有需要更新的描述")
