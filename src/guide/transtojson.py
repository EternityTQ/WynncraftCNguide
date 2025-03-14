import re
import json
from bs4 import BeautifulSoup

def extract_data(html):
    soup = BeautifulSoup(html, "html.parser")
    result = {}

    # 遍历所有技能单元格（td）
    for td in soup.find_all("td"):
        # 获取ID
        span_tag = td.find("span", id=True)
        skill_id = span_tag["id"] if span_tag else None

        # 获取名称
        name_tag = td.find("div", style=re.compile("text-align: center")).find("font") if td.find("div", style=re.compile("text-align: center")) else None
        name = name_tag.text.strip() if name_tag else ""

        # 如果找不到ID，则用名称作为ID
        if not skill_id:
            skill_id = name

        # 获取图标
        img_tag = td.find("img")
        icon = img_tag["src"] if img_tag and "src" in img_tag.attrs else ""
        category = icon.split("/")[-1].split(".")[0] if icon else ""

        # 获取 tooltip 作为描述
        tooltip_div = None
        for sibling in td.find_all_next():
            if sibling.name == "div" and "tooltip" in sibling.get("class", []):
                tooltip_div = sibling
                break

        description = ""
        if tooltip_div:
            description_html = str(tooltip_div)
            description_html = re.sub(r'<div[^>]*?>', '', description_html)  # 删除外层 div
            description_html = description_html.replace('</div>', '')  # 移除 div 关闭标签
            description_html = description_html.replace('\n', '').replace('\r', '').replace('"', '\"')  # 处理 JSON 转义字符
            description = description_html
        else:
            print(f"警告: 未能找到 {name} 的 tooltip 描述")

        # 组装数据
        if name and icon and description:
            result[skill_id] = {
                "name": name,
                "icon": icon,
                "category": category,
                "description": description
            }

            print(f"发现技能块，ID为 {skill_id}")
            print(f"- 组装名字：{name}")
            print(f"- 图标获取：{category}")
            print(f"- 描述获取成功，为 {description[:50]}...")

    return result

# 读取Markdown文件
with open("class.md", "r", encoding="utf-8") as f:
    html_content = f.read()

data = extract_data(html_content)

# 保存为JSON文件
with open("skills.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("转换完成，数据已保存至 skills.json")