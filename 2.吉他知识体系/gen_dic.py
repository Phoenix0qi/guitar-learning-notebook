import os
import re

def sanitize_filename(name):
    """清理非法文件名字符"""
    name = re.sub(r'<.*?>', '', name)
    # 删除非法路径字符
    name = re.sub(r'[\\/*?:"\'<>|]', '', name)
    # 可选：移除多余空格
    name = name.replace(' ', '')
    name = name.strip()
    return name

def split_md_file(md_path, output_root='./输出'):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_main_title = None
    current_sub_title = None
    content_buffer = []

    def save_section():
        """保存当前子标题的内容"""
        if current_main_title and current_sub_title and content_buffer:
            folder = os.path.join(output_root, sanitize_filename(current_main_title))
            os.makedirs(folder, exist_ok=True)
            filename = os.path.join(folder, f"{sanitize_filename(current_sub_title)}.md")
            with open(filename, 'w', encoding='utf-8') as out_f:
                out_f.write(f"## {current_sub_title}\n{''.join(content_buffer)}")

    for line in lines:
        main_match = re.match(r'^## (.+)', line)
        sub_match = re.match(r'^### (.+)', line)

        if main_match:
            save_section()  # 保存上一个 section
            current_main_title = main_match.group(1).strip()
            current_sub_title = None
            content_buffer = []

        elif sub_match:
            save_section()  # 保存上一个 section
            current_sub_title = sub_match.group(1).strip()
            content_buffer = []

        else:
            content_buffer.append(line)

    # 保存最后一个 section
    save_section()

    print(f"✅ 拆分完成！结果保存在: {os.path.abspath(output_root)}")


# ✅ 用法示例
split_md_file('./知识体系.md')


# 使用示例
# 假设你的原始 Markdown 文件名为 input.md
# split_md_file('./知识体系.md')
# split_md_file('./吉他知识体系/知识体系.md')