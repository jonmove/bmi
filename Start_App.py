from tkinter import *
from tkinter.ttk import Progressbar
import sys
import os
import subprocess

# ✅ PyInstaller uchun resurs yo‘llarini to‘g‘ri olish
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller vaqtinchalik papkasi
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

root = Tk()

# ✅ Rasmni PyInstaller mos yo‘l bilan yuklash
image = PhotoImage(file=resource_path("images/logo1.png"))

height = 430
width = 530
x = (root.winfo_screenwidth()//2)-(width//2)
y = (root.winfo_screenheight()//2)-(height//2)
root.geometry(f'{width}x{height}+{x}+{y}')
root.overrideredirect(1)
root.wm_attributes('-topmost', True)
root.config(background='white')

welcome_label = Label(text='Aliakbar - AutoShop dokoniga Xush kelibsiz', bg='white', font=("yu gothic ui", 15, "bold"), fg='black')
welcome_label.place(x=80, y=25)

bg_label = Label(root, image=image, bg='white')
bg_label.place(x=130, y=65)

progress_label = Label(root, text="Biroz kuting...", font=('yu gothic ui', 13, 'bold'), fg='black', bg='white')
progress_label.place(x=190, y=350)
progress = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress.place(x=15, y=390)

exit_btn = Button(text='x', bg='white', command=lambda: exit_window(), bd=0, font=("yu gothic ui", 16, "bold"),
                  activebackground='white', fg='black')
exit_btn.place(x=490, y=0)

def exit_window():
    sys.exit(root.destroy())

def top():
    root.withdraw()
    # ✅ PyInstaller uchun boshqa faylni ishga tushirish (subprocess orqali)
    subprocess.Popen([sys.executable, resource_path("AccountSystem.py")])
    root.destroy()

i = 0

def load():
    global i
    if i <= 10:
        txt = 'Biroz kuting...  ' + (str(10*i)+'%')
        progress_label.config(text=txt)
        progress_label.after(1000, load)
        progress['value'] = 10*i
        i += 1
    else:
        top()

load()
root.mainloop()
