import customtkinter as ck
import tkinter as tk
import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
import spacy
nlp = spacy.load("pl_core_news_sm")

def load_custom_stopwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return set(file.read().splitlines())

class ChatInterface:
    ck.set_appearance_mode("Dark")

    def __init__(self):
        self.root = ck.CTk()
        self.root.resizable(height=False, width=False)
        self.root.title('Botek - Twój Pomocnik Klienta ^^')

        self.chat_history = ck.CTkTextbox(self.root, width=350, height=400, text_color="lightblue")
        self.chat_history.pack()
        self.print_to_chat_history("Botek: Cześć, jak mogę ci dzisiaj pomóc?")

        self.user_input = ck.CTkEntry(self.root, placeholder_text="Tu wpisz swoją wiadomość")
        self.user_input.pack(side=tk.LEFT, padx=10, pady=8, fill=tk.X, expand=True)
        self.sendbutton = ck.CTkButton(master=self.root, text="Wyślij", width=50, command=self.submit_input, hover_color="purple")
        self.sendbutton.pack(side=tk.RIGHT, padx=5, pady=8)

        self.user_input.bind("<Return>", lambda event: self.submit_input())
        self.stop_words = load_custom_stopwords('stopwords.txt')

        self.latest_user_input = ""
        self.root.mainloop()

    def submit_input(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, tk.END)

        if user_input.strip() == "":
            self.root.quit()
            return
        else:
            self.preprocess_text(user_input)#this sends for preprocessing

        user_input_display = f'Użytkownik: {user_input}'
        self.print_to_chat_history(user_input_display)
        self.root.after(1000, self.bot_response, user_input_display)

    def bot_response(self, user_input):
        # Placeholder for actual bot response generation based on training data
        if user_input != "":
            bot_response = "Botek: To jest automatyczna odpowiedź."
            self.print_to_chat_history(bot_response)

    def print_to_chat_history(self, message):
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.see(tk.END)

    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        tokens = [word.lower() for word in tokens if word.isalnum()]
        filtered_tokens = [word for word in tokens if word not in self.stop_words]
        doc = nlp(" ".join(filtered_tokens))
        lemmatized_text = [token.lemma_ for token in doc]
        print(lemmatized_text)

if __name__ == "__main__":
    chat=ChatInterface()