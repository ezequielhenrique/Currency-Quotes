import tkinter as tk
from tkinter import ttk
from widgets import PanelQuotes


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title('Currency Quotes')
        self.master.geometry('800x600')
        self.master.configure(background='#F2F2F2')
        self.master.resizable(False, False)

        options = ['USD', 'EUR', 'JPY']

        style = ttk.Style()
        style.theme_use("alt")
        style.configure('new.TCombobox', background='#1F3447', fieldbackground="#1F3447")
        style.map('new.TCombobox', fieldbackground=[('readonly', '#1F3447')], foreground=[('readonly', 'white')],
                  arrowcolor=[('readonly', 'white')], bordercolor=[('readonly', '#6D8EAD')],
                  selectbackground=[('readonly', '#1F3447')])

        self.master.option_add("*TCombobox*Listbox*Background", 'white')
        self.master.option_add("*TCombobox*Listbox*Foreground", '#6D8EAD')
        self.master.option_add("*TCombobox*Listbox*Font", ('Roboto', 11))

        menu_comb = ttk.Combobox(root, values=options, justify='center', width=58, font=('Roboto', 18),
                                 state='readonly', style='new.TCombobox')
        menu_comb.set('USD')
        menu_comb.pack(pady='10')

        panel = PanelQuotes(self.master, bg_color='#F2F2F2')
        panel.pack()

        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background='#1F3447', foreground='white', borderwidth=1, focusthickness=3,
                        focuscolor='none', font=('Roboto', 16), relief='sunken')
        style.map('TButton', background=[('active', '#1F3447')])

        button_calc = ttk.Button(self.master, text='Calculadora')
        button_calc.pack(ipady=5, ipadx=60, pady=30)


if __name__ == '__main__':
    root = tk.Tk()
    MainWindow(root)
    root.mainloop()
