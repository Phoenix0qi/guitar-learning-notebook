# 生成第一周和后续几周的Markdown表格模板

from datetime import datetime, timedelta

# 定义第一周起始日期
start_date = datetime.strptime("2025-03-03", "%Y-%m-%d")
weeks_to_generate = 4  # 可按需修改生成几周

# 周计划通用模板（不含具体日期）
table_template = """
### 🎯 第{week_num}周练习计划（{start} - {end}）

| 模块 | 内容 | 时间/频率 | 完成进度 |
|------|------|------------|----------|
| **1. 听力** | 1. fret-note 识音训练 | 每天 5 min | ❌ |
|  | 2. fret-interval 间隔听辨 | 每天 5 min | ❌ |
|  | 3. fret-chords 和弦听辨（CAGED） | 每天 5 min（早上班车）| ❌ |
|  | 4. 扒带-粗扒（汪汪） | 每周 4 首（每天约 20 min，晚上班车）| ❌ |
| **2. 吉他基本功** | 1. 指板热身（不同速度爬格子 160/180/200）| 每天 10 min | ❌ |
|  | 2. 《GG》手指独立性 | 每天 10 min（班车） | ❌ |
|  | 3. 《地狱吉他》练习 10/50 | 每天 30 min | ❌ |
|  | 4. 《乔伊速度》左手独立性练习 | 每天 10 min | ❌ |
| **3. 乐理/指板练习** | 1. 指板记忆训练 - CAGED + 和弦 + 音阶 | 每天 10~15 min | ❌ |
|  | 2. 《GG》读书笔记 第二章 | 每周完成 | ❌ |
|  | 3. 12个调练习 | 每周练习（可分日推进）| ❌ |
| **4. Cover + 扒带** | 1. 扒带-licks + GTP打谱（Neo-soul）| 每周 2 首 | ❌ |
|  | 2. Cover 完整曲目演练 | 每周 2 首 | ❌ |
|  | 3. Fusion licks 扒带 | 每周 2 条 | ❌ |
| **5. 键盘 + 编曲** | 1. 键盘练习 + 编曲课笔记 | 每周 3 节 | ❌ |
|  | 2. 编曲作业（1/4）| 每周 1 首 | ❌ |
"""

# 生成多周表格
weekly_markdowns = []
for i in range(weeks_to_generate):
    week_start = start_date + timedelta(weeks=i)
    week_end = week_start + timedelta(days=6)
    md = table_template.format(
        week_num=i + 1,
        start=week_start.strftime("%m.%d"),
        end=week_end.strftime("%m.%d")
    )
    weekly_markdowns.append(md)

# 合并为单一Markdown文本
full_markdown = "\n\n---\n\n".join(weekly_markdowns)
full_markdown[:1000]  # 只预览部分内容

