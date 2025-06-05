import os

def generate_summary_md(root_dir='./输出', output_file='summarycp.md'):
    lines = []
    exclude_dirs = {'.git', '__pycache__', '.DS_Store', '.idea', '.vscode'}  # 可扩展

    def walk_dir(current_dir, level=0):
        entries = sorted(os.listdir(current_dir))
        dirs = [d for d in entries if os.path.isdir(os.path.join(current_dir, d)) and d not in exclude_dirs]
        files = [f for f in entries if f.lower().endswith('.md')]

        rel_path = os.path.relpath(current_dir, root_dir).replace("\\", "/")
        if rel_path == '.':
            rel_path = ''

        indent = '\t' * level

        # 当前目录下的 md 文件
        for f in files:
            file_rel_path = os.path.join(rel_path, f).replace("\\", "/")
            name = os.path.splitext(f)[0]
            lines.append(f"{indent}* [{name}]({file_rel_path})\n")

        # 子目录
        for d in dirs:
            dir_rel_path = os.path.join(rel_path, d).replace("\\", "/")
            lines.append(f"{indent}* [{d}]({dir_rel_path}/)\n")
            walk_dir(os.path.join(current_dir, d), level + 1)

    walk_dir(root_dir)

    summary_path = os.path.join(root_dir, output_file)
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"✅ 生成完成: {os.path.abspath(summary_path)}")

# 使用
generate_summary_md('./')
