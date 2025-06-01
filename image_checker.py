import os
import re

missing_files = []

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            with open(os.path.join(root, file), encoding='utf-8') as f:
                content = f.read()
                matches = re.findall(r'PhotoImage\s*\(.*file\s*=\s*os\.path\.join\(.*?"([^"]+)"\).*?\)', content)
                for match in matches:
                    full_path = os.path.join(os.path.abspath(root), match.replace("/", os.sep))
                    if not os.path.exists(full_path):
                        missing_files.append(full_path)

if missing_files:
    print("❌ Quyidagi rasm fayllari topilmadi:")
    for mf in missing_files:
        print(f"  - {mf}")
else:
    print("✅ Barcha rasm fayllari mavjud.")
