import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('Currency Quotes')
        self.master.geometry('800x600')

        options = ['USD', 'EUR', 'JPY']

        style = ttk.Style()
        style.theme_use("alt")
        style.configure('new.TCombobox', background='#1F3447', fieldbackground="#1F3447")
        style.map('new.TCombobox', fieldbackground=[('readonly', '#1F3447')], foreground=[('readonly', 'white')],
                  arrowcolor=[('readonly', 'white')], bordercolor=[('readonly', '#6D8EAD')],
                  selectbackground=[('readonly', '#1F3447')])

        self.master.option_add("*TCombobox*Listbox*Background", 'white')
        self.master.option_add("*TCombobox*Listbox*Foreground", '#6D8EAD')
        self.master.option_add("*TCombobox*Listbox*Font", ('Roboto', 10))

        menu_comb = ttk.Combobox(root, values=options, justify='center', width=85, font=('Roboto', 12),
                                 state='readonly', style='new.TCombobox')
        menu_comb.set('USD')
        menu_comb.pack()


if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
