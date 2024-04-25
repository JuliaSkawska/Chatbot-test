import customtkinter as ck
import tkinter as tk


class ChatInterface:
    ck.set_appearance_mode("Dark")

    def __init__(self):
        self.root = ck.CTk()
        self.root.resizable(height=False, width=False)
        self.root.title('Pomoc Klienta')

        self.chat_history = ck.CTkTextbox(self.root, width=350, height=400, text_color="lightblue")
        self.chat_history.pack()
        self.print_to_chat_history("Bot: Cześć, jak mogę ci dzisiaj pomóc?")

        self.user_input = ck.CTkEntry(self.root, placeholder_text="Tu wpisz swoją wiadomość")
        self.user_input.pack(side=tk.LEFT, padx=10, pady=8, fill=tk.X, expand=True)
        self.sendbutton = ck.CTkButton(master=self.root, text="Wyślij", width=50, command=self.submit_input,hover_color="purple")
        self.sendbutton.pack(side=tk.RIGHT, padx=5, pady=8)

        self.user_input.bind("<Return>", lambda event: self.submit_input())
        self.root.mainloop()

    def submit_input(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if user_input.strip() == "":
            self.root.quit()
            return

        user_input = f'Użytkownik: {user_input}'
        self.print_to_chat_history(user_input)
        self.root.after(1000, self.bot_response, user_input)

    def bot_response(self, user_input):
        # Placeholder for actual bot response generation based on training data
        if user_input != "":
            bot_response = "Bot: To jest automatyczna odpowiedź."
            self.print_to_chat_history(bot_response)

    def print_to_chat_history(self, message):
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.see(tk.END)


if __name__ == "__main__":
    ChatInterface()
