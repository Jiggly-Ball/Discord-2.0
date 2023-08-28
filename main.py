import tkinter as tk
import pickle

from threading import Thread
from random import randint
from time import sleep

from server import CHAT

class App:
    def __init__(self) -> None:
        self.name = "Discord 2.0 (real)"
        self.login_res = "400x500"
        self.chat_res = "1200x850"
        self.user = None
        self.chat_data = []
        self.current_server = "server001"
        self.refresh_running = True
        self.refresh_rate = 2 # Refreshes the chat every 2 seconds
        self.start = False
        self.login()

    def get_login_data(self):
        try:
            with open("data.pkl", "rb") as data_file:
                data = pickle.load(data_file)
                if data["remember"] is True:
                    return data
                
        except FileNotFoundError:
            with open("data.pkl", "wb") as data_file:
                pickle.dump({
                    "name":None,
                    "tag":None,
                    "remember":False
                }, data_file)

    def login(self):
        stored_user = self.get_login_data()
        if stored_user is not None:
            self.user = stored_user["name"] + "#" + stored_user["tag"]
            return self.main_chat()

        login_window = tk.Tk()
        login_window.geometry(self.login_res)
        login_window.title("Login")
        login_window.resizable(False, True)

        name_var = tk.StringVar()
        remember_var = tk.BooleanVar(value=False)

        name = tk.Label(login_window, text="Name")
        name_entry = tk.Entry(login_window, textvariable=name_var)
        name.pack()
        name_entry.pack()

        tk.Checkbutton(login_window , text="Remember username", variable=remember_var, onvalue=True, offvalue=False).pack()

        def login_button():
            name, remember = name_var.get(), remember_var.get()

            if len(name.strip()) == 0:
                tk.Label(login_window, text="Invalid username").pack()
            
            else:
                tag = randint(1000, 9999)
                if remember is True:
                    with open("data.pkl", "wb") as data_file:
                        pickle.dump({
                            "name":name,
                            "tag":str(tag),
                            "remember":remember
                        }, data_file)

                tk.Label(login_window, text="Logging in...").pack()
                self.user = name + "#" + str(tag)
                login_window.destroy()
                self.main_chat()

        tk.Button(login_window, text="Login", command=login_button).pack()
        login_window.mainloop()

    def main_chat(self):
        chat_window = tk.Tk()
        chat_window.geometry(self.chat_res)
        chat_window.title(self.name)
        chat_window.resizable(True, True)

        BG_GRAY = "#ABB2B9"
        BG_COLOR = "#17202A"
        TEXT_COLOR = "#EAECEE"
        
        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"

        def refresh_chat():
            try:
                while self.refresh_running:
                    chat_server = CHAT.find_chat(self.current_server)
                    chat_history = chat_server["chats"]

                    if self.start is True:
                        chat_history.reverse()
                    else:
                        self.start = True
                    
                    for index, message in enumerate(chat_history):
                        if index + 1 == 100:
                            break
                        if message not in self.chat_data:
                            self.chat_data.append(message)
                            text_box.insert(tk.END, "\n" + message)
                    
                    sleep(self.refresh_rate)
            except RuntimeError or tk.TclError:
                pass

        def close_refresh_thread():
            self.refresh_running = False
            chat_refresh_thread.join()
            chat_window.destroy()
   
        def send():
            if chat_entry.get().strip() != "":
                send_message = f"{self.user} : " + chat_entry.get()
                text_box.insert(tk.END, "\n" + send_message)
                self.chat_data.append(send_message)
                CHAT.update_chat(self.current_server, send_message)
            chat_entry.delete(0, tk.END)

        text_box = tk.Text(chat_window, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT,width=100,height=30)
        text_box.grid(row=1, column=0, columnspan=2)
        
        scrollbar = tk.Scrollbar(text_box)
        scrollbar.place(relheight=1, relx=0.974)
        
        chat_entry = tk.Entry(chat_window, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        chat_entry.grid(row=2, column=0)
        
        send = tk.Button(chat_window, text="Send", font=FONT_BOLD, bg=BG_GRAY, command=send).grid(row=2, column=1)

        chat_refresh_thread = Thread(target=refresh_chat)
        chat_refresh_thread.start()

        chat_window.protocol("WM_DELETE_WINDOW", close_refresh_thread)
        chat_window.mainloop()

if __name__ == "__main__":
    App()
