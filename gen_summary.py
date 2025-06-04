import os

def generate_summary_md(root_dir='./输出', output_file='summarycp.md'):
    lines = []

    def find_first_md(path):
        for file in os.listdir(path):
            if file.lower().endswith('.md'):
                return file
        return None

    def walk_dir(current_dir, level=0):
        entries = sorted(os.listdir(current_dir))
        dirs = [d for d in entries if os.path.isdir(os.path.join(current_dir, d))]
        files = [f for f in entries if f.endswith('.md')]

        # 当前文件夹自己作为标题项（指向 README.md 或第一个 .md 文件）
        rel_path = os.path.relpath(current_dir, root_dir).replace("\\", "/")
        if rel_path == '.':
            rel_path = ''
        title = os.path.basename(current_dir) if rel_path else os.path.basename(os.path.abspath(current_dir))
        target = find_first_md(current_dir) or ''
        link_path = os.path.join(rel_path, target).replace("\\", "/") if target else rel_path + '/'
        indent = '\t' * level
        lines.append(f"{indent}* [{title}]({link_path})\n")

        for f in files:
            if f == target:  # 避免重复记录 README.md
                continue
            file_rel_path = os.path.join(rel_path, f).replace("\\", "/")
            name = os.path.splitext(f)[0]
            lines.append(f"{indent}\t* [{name}]({file_rel_path})\n")

        for d in dirs:
            walk_dir(os.path.join(current_dir, d), level + 1)

    walk_dir(root_dir)

    summary_path = os.path.join(root_dir, output_file)
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"✅ 生成完成: {os.path.abspath(summary_path)}")

# 使用
generate_summary_md('./')
