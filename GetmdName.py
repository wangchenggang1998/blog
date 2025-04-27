import os
from datetime import datetime

path = "./_posts"  # 你的md文件夹

for filename in os.listdir(path):
    if filename.endswith(".md"):
        filepath = os.path.join(path, filename)
        
        with open(filepath, "r+", encoding="utf-8") as f:
            content = f.read()
            if not content.startswith('---'):
                title = filename.rsplit('.', 1)[0]
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                front_matter = f"---\ntitle: {title}\ndate: {now}\n---\n\n"
                new_content = front_matter + content
                f.seek(0)
                f.write(new_content)
                f.truncate()
                print(f"✅ Created front-matter for {filename}")
            else:
                print(f"✅ Front-matter already exists in {filename}")
