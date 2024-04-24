from tkinter import *
class ChatInterface:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(height=False, width=False)
        self.root.title('Pomoc Klienta')

        self.chat_history = Text(self.root, height=20, width=50)
        self.chat_history.pack()
        self.print_to_chat_history("Bot: Cześć, jak mogę ci dzisiaj pomóc?")

        self.input_label = Label(self.root, text='Tu napisz swoją wiadomość', fg='green')
        self.input_label.pack()

        self.user_input = Entry(self.root)
        self.user_input.pack()

        self.user_input.bind("<Return>", self.submit_input)
        self.root.mainloop()

    def submit_input(self, event):
        user_input = self.user_input.get()
        self.user_input.delete(0, END)

        if user_input.strip() == "":
            self.root.quit()
            return
        self.print_to_chat_history(user_input)
        bot_response = "Bot: To jest automatyczna odpowiedź."
        self.print_to_chat_history(bot_response)

    def print_to_chat_history(self, message):
        self.chat_history.insert(END, message + "\n")
        self.chat_history.see(END)

if __name__ == "__main__":
    ChatInterface()
