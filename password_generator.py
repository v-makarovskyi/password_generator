from tkinter import *
from random import choice
import string


class App:
    def __init__(self):
        self.window = Tk()
        self.window.title('Генератор паролей')
        self.window.iconphoto(True, PhotoImage(file='logo.png'))
        self.window.geometry('500x255')
        self.window.config(bg='grey')

        self.label()
        self.entry()
        self.button()

    def label(self):
        label_title = Label(self.window, text='Добро пожаловать в генератор паролей', font=(
            'Roboto', 12), bg='white', fg='black')
        label_title.pack()

    def entry(self):
        self.password_entry = Entry(self.window, font=(
            'Roboto', 25), bg='white', fg='red', width=30, relief='solid')
        self.password_entry.pack(pady=50)

    def button(self):
        password_generator = Button(self.window, text='Сгенерировать пароль', font=(
            'Roboto', 12), bg='white', fg='black', width=25, command=self.generate_password)
        password_generator.pack()

    def generate_password(self):
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ''
        for x in range(28):
            password += choice(characters)
        self.password_entry.delete(0, END)
        self.password_entry.insert(0, password)

app = App()
app.window.mainloop()
