import os
import re
from bs4 import BeautifulSoup
import markdown

def strip_html_and_vue(text):
    # 去除 Vue 插值、组件和 HTML 标签
    text = re.sub(r'{{[^}]*}}', '', text)  # 去除 {{ 插值 }}
    text = re.sub(r'<\s*[A-Z][^>]*>.*?</\s*[A-Z][^>]*>', '', text, flags=re.DOTALL)  # Vue组件
    text = re.sub(r'<[^>]+>', '', text)    # 所有 HTML 标签
    return text

def count_words_from_markdown(md_text):
    # 移除代码块 ```...``` 和 ~~~...~~~
    md_text = re.sub(r'```[\s\S]*?```', '', md_text)
    md_text = re.sub(r'~~~[\s\S]*?~~~', '', md_text)

    html = markdown.markdown(md_text)
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    clean_text = strip_html_and_vue(text)

    chinese_chars = re.findall(r'[\u4e00-\u9fff]', clean_text)
    english_words = re.findall(r'\b[a-zA-Z]+\b', clean_text)

    return len(chinese_chars), len(english_words)

def scan_directory(path):
    total_words = 0
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        md = f.read()
                        chinese_count, english_count = count_words_from_markdown(md)
                        file_total = chinese_count + english_count
                        total_words += file_total
                        print(f"[{filepath}] -> 中文: {chinese_count} / 英文: {english_count} / 总字数: {file_total}")
                except Exception as e:
                    print(f"[{filepath}] -> 读取失败: {e}")
    print("\n✅ 所有文件统计完成")
    print(f"📊 总字数: {total_words}")

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))  # 当前脚本目录
    scan_directory(current_dir)
