import os
import re

project_dir = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.py'):
            file_path = os.path.join(root, file)

            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()

            # Faqat rasm yo‘li bo‘lgan joylarni topamiz
            pattern = r'PhotoImage\s*\(\s*file\s*=\s*[\'"](.+?)[\'"]\s*\)'
            matches = re.findall(pattern, code)

            if matches:
                print(f"[+] Rasm yo'li topildi: {file_path}")
                new_lines = []
                lines = code.splitlines()
                base_imported = False

                for line in lines:
                    if 'PhotoImage(file=' in line:
                        match = re.search(r'file\s*=\s*[\'"](.+?)[\'"]', line)
                        if match:
                            relative_path = match.group(1).replace('\\', '/')
                            new_line = re.sub(
                                r'file\s*=\s*[\'"](.+?)[\'"]',
                                f'file=os.path.join(BASE_DIR, "{relative_path}")',
                                line
                            )
                            new_lines.append(new_line)
                        else:
                            new_lines.append(line)
                    else:
                        new_lines.append(line)

                # Fayl boshiga importlar qo‘shiladi (agar yo‘q bo‘lsa)
                if 'BASE_DIR =' not in code:
                    for i, line in enumerate(new_lines):
                        if line.strip().startswith('from tkinter') or line.strip().startswith('import tkinter'):
                            new_lines.insert(i + 1, 'import os\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))')
                            base_imported = True
                            break
                    if not base_imported:
                        new_lines.insert(0, 'import os\nBASE_DIR = os.path.dirname(os.path.abspath(__file__))')

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_lines))

print("\n✅ Rasm yo‘llari yangilandi.")
