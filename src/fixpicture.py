import os
import re

def fix_image_format(root_dir, dry_run=False):
    """
    遍历目录下的 markdown 文件并修复图片尺寸格式。
    
    Args:
        root_dir (str): 要扫描的根目录路径
        dry_run (bool): 如果为 True，仅打印修改计划而不实际写入文件
    """
    
    # 正则表达式解释：
    # !\[(.*?)\]       -> 捕获组1：方括号内的 Alt 文本（非贪婪）
    # \((.*?)          -> 捕获组2：圆括号内的 URL（非贪婪，直到遇到空格）
    # \s+              -> 匹配 URL 和尺寸之间的空格
    # (=[\dx]+)\)      -> 捕获组3：尺寸定义（如 =330x450），以 ) 结尾
    # 注意：这里假设尺寸格式由数字和 'x' 组成
    pattern = re.compile(r'!\[(.*?)\]\((.*?)\s+(=[\dx]+)\)')

    modified_files_count = 0
    total_matches_count = 0

    print(f"--- 开始扫描 (模式: {'Dry Run / 仅预览' if dry_run else '实际执行'}) ---\n")

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except Exception as e:
                    print(f"[Error] 无法读取文件 {file_path}: {e}")
                    continue

                # 定义替换函数
                def replacement(match):
                    alt_text = match.group(1)
                    url = match.group(2)
                    size = match.group(3)
                    
                    # 构造新格式：![AltText =WxH](URL)
                    # 如果原 AltText 为空，则直接变成 ![=WxH]
                    separator = " " if alt_text else ""
                    return f"![{alt_text}{separator}{size}]({url})"

                # 执行替换
                new_content, count = pattern.subn(replacement, content)

                if count > 0:
                    total_matches_count += count
                    modified_files_count += 1
                    
                    if dry_run:
                        print(f"[预览修改] {file_path} (发现 {count} 处)")
                    else:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"[已修复] {file_path} (修改 {count} 处)")

    print(f"\n--- 处理完成 ---")
    print(f"涉及文件数: {modified_files_count}")
    print(f"处理图片数: {total_matches_count}")
    if dry_run:
        print("提示: 当前为预览模式，未修改任何文件。请将脚本中的 dry_run=True 改为 False 以执行修改。")

if __name__ == "__main__":
    # 设置你的文档根目录，'.' 代表当前脚本所在目录
    TARGET_DIRECTORY = '.' 
    
    # 第一次运行建议保持 True，确认输出无误后再改为 False
    DRY_RUN_MODE = False 

    fix_image_format(TARGET_DIRECTORY, dry_run=DRY_RUN_MODE)