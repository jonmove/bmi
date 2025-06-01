from tkinter import *
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox as pop_up
import random
from app import AccountSystem


class GuestPage:
    def __init__(self, dashboard_window):
        self.dashboard_window = dashboard_window

        # Window Size and Placement
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file=os.path.join(BASE_DIR, "images//zer.png"))
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome')

        # Navigating through windows
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ======================================================================================
        # =================== HOME PAGE ========================================================
        # ======================================================================================
        homepage.config(background='#ffffff')

        # ====== MENU BAR ==========
        logoIcon = Image.open('images\\zer.png')
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(homepage, image=photo, bg='#ffffff')
        logo.image = photo
        logo.place(x=0, y=0)


        menuBar_line = Canvas(homepage, width=1500, height=1.5, bg="#e6e6e6", highlightthickness=0)
        menuBar_line.place(x=0, y=60)

        home_bgImg = Image.open('images\\home11.jpg')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='#ffffff')
        home_bg.image = photo
        home_bg.place(x=0, y=60)

        brandIcon = Image.open('images\\zer.png')
        photo = ImageTk.PhotoImage(brandIcon)
        brandlogo = Label(homepage, image=photo, bg='black')
        brandlogo.image = photo
        brandlogo.place(x=1085, y=83)

        heading = Label(homepage, text='AutoShop', bg='black', fg='#ff6c38', font=("yu gothic ui", 19, "bold"))
        heading.place(x=770, y=90)

        heading2 = Label(homepage, text='Trending', bg='black', fg='#ff6c38', font=("", 19, "bold"))
        heading2.place(x=150, y=95)

        # Parts Image
        partsImage = Image.open('images\\menu1.png')
        photo = ImageTk.PhotoImage(partsImage)
        partsImage = Label(homepage, image=photo, bg='black')
        partsImage.image = photo
        partsImage.place(x=50, y=150)

        partsImage2 = Image.open('images\\menu2.png')
        photo = ImageTk.PhotoImage(partsImage2)
        partsImg2 = Label(homepage, image=photo, bg='black')
        partsImg2.image = photo
        partsImg2.place(x=160, y=150)

        partsImage3 = Image.open('images\\menu3.png')
        photo = ImageTk.PhotoImage(partsImage3)
        partsImg3 = Label(homepage, image=photo, bg='black')
        partsImg3.image = photo
        partsImg3.place(x=270, y=150)

        partsImage4 = Image.open('images\\menu4.png')
        photo = ImageTk.PhotoImage(partsImage4)
        partsImg4 = Label(homepage, image=photo, bg='black')
        partsImg4.image = photo
        partsImg4.place(x=50, y=275)

        partsImage5 = Image.open('images\\menu1.png')
        photo = ImageTk.PhotoImage(partsImage5)
        partsImg5 = Label(homepage, image=photo, bg='black')
        partsImg5.image = photo
        partsImg5.place(x=160, y=275)

        partsImage6 = Image.open('images\\menu2.png')
        photo = ImageTk.PhotoImage(partsImage6)
        partsImg6 = Label(homepage, image=photo, bg='black')
        partsImg6.image = photo
        partsImg6.place(x=270, y=275)

        heading3 = Label(homepage, text='Moy', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading3.place(x=55, y=245)

        heading4 = Label(homepage, text='Balon', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading4.place(x=182, y=245)

        heading5 = Label(homepage, text='Diska', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading5.place(x=282, y=245)

        heading6 = Label(homepage, text="Motor", bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading6.place(x=56, y=370)

        heading7 = Label(homepage, text='Oyna', bg='black', fg='#ffffff', font=("", 8, "bold"))
        heading7.place(x=170, y=370)

        heading8 = Label(homepage, text='Rang', bg='black', fg='#ffffff', font=("", 7, "bold"))
        heading8.place(x=265, y=370)

        def click_button():
            pop_up.showinfo(" Ooops ! !! !!!", 'For you to gain access to the full functionality of this App\n'
                            'You will need an Administrator Approval\n\n'
                            'Please inform your Administrator for full usage approval')

        # ========== HOME BUTTON =======
        home_button = Button(homepage, text='Home', bg='#fd6a36', font=("", 13, "bold"), bd=0, fg='white',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='white')
        home_button.place(x=70, y=15)

        # ========== DASHBOARD BUTTON =======
        dashboard_button = Button(homepage, text='Dashboard', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                  cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                  command=click_button)
        dashboard_button.place(x=150, y=15)

        # ========== MANAGE BUTTON =======
        manage_button = Button(homepage, text='Manage', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                               command=click_button)
        manage_button.place(x=270, y=15)

        # ========== PRODUCTS BUTTON =======
        product_button = Button(homepage, text='Products', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                                cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                                command=click_button)
        product_button.place(x=360, y=15)

        # ========== HELP BUTTON =======
        help_button = Button(homepage, text='Help', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                             cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a',
                             command=click_button)
        help_button.place(x=460, y=15)

        def logout():
            win = Toplevel()
            AccountSystem.AccountPage(win)
            dashboard_window.withdraw()
            win.deiconify()
        # ========== LOG OUT =======
        logout_button = Button(homepage, text='Logout', bg='#ffffff', font=("", 13, "bold"), bd=0, fg='#7a7a7a',
                               cursor='hand2', activebackground='#fd6a36', activeforeground='#7a7a7a', command=logout)
        logout_button.place(x=520, y=15)


def page():
    window = Tk()
    GuestPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()