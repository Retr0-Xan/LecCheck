import customtkinter as ctk
from PIL import Image, ImageTk
import os
import sys

ctk.set_appearance_mode("dark")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


code = 0
current_directory = os.getcwd()

def getCode():
    return code


def renderSignIn():
    Lecturers = {
    "0001":"Prof.Hayfron Acquah",
    "0002":"N.Ussiph",
    "0003":"D. Asamoah",
    "0004":"J.K Panford",
    "0005":"F.Twum",
    "0006":"B.E. Owusu",
    "0007":"Gadaffi Salam",
    "0008":"B. Arthur"
    }

    def openLecturerWindow():
        lec_code= code_entry.get()
        global code
        code= lec_code
        if lec_code in Lecturers:
            root.destroy()
            from home import renderHome
            renderHome(lec_code)

        else:
            invalid_label = ctk.CTkLabel(root,text="Invalid code.Try again")
            invalid_label.place(relx = 0.5, rely=0.7, anchor=ctk.CENTER)

        getCode()


    root = ctk.CTk()
    root.geometry("600x440")
    root.title("Login")

    bg_img=ImageTk.PhotoImage(Image.open(resource_path("assets\\images\\login-bg(1).png")))
    bg_label=ctk.CTkLabel(root,image=bg_img,text="")
    bg_label.pack(fill="both",expand=True)

    login_frame = ctk.CTkFrame(root, width=320,height=200,corner_radius=15)
    login_frame.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

    login_text = ctk.CTkLabel(login_frame,text="Please enter your designated Code", font=ctk.CTkFont("Century Gothic",size=17, weight="bold",))
    login_text.place(x=20,y=20)

    code_entry = ctk.CTkEntry(login_frame,placeholder_text="Code", width=150)
    code_entry.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)

    login_btn = ctk.CTkButton(root,text="Login", command=openLecturerWindow)
    login_btn.place(relx=0.5,rely=0.8,anchor=ctk.CENTER)

    root.mainloop()