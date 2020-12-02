import tkinter as tk


class InfoMoney(tk.Frame):
    def __init__(self, parent, info, description, bg='black', fg='white', width=150, height=100, size_info=20,
                 size_desc=8):
        tk.Frame.__init__(self, parent)
        self.configure(background=bg, width=width, height=height)
        self.pack_propagate(0)

        frame_master = tk.Frame(self, bg=bg)

        label_info = tk.Label(frame_master, text=str(info), font=('Roboto', size_info), bg=bg, fg=fg)
        label_desc = tk.Label(frame_master, text=str(description), font=('Roboto', size_desc), bg=bg, fg=fg)

        label_info.pack()
        label_desc.pack()
        frame_master.place(relx=.5, rely=.5, anchor="c")


class PanelQuotes(tk.Frame):
    def __init__(self, parent, bg_color='white'):
        tk.Frame.__init__(self, parent)
        self.configure(background=bg_color)

        line1 = tk.Frame(self, bg=bg_color)
        line2 = tk.Frame(self, bg=bg_color)

        label_quo = InfoMoney(line1, '4.50', 'Cotação da moeda', bg='#1F3447', fg='white', width=200, height=150,
                              size_info=28, size_desc=10)
        label_max = InfoMoney(line2, '5.09', 'Cotação máxima', bg='#1F3447', fg='white')
        label_min = InfoMoney(line2, '4.50', 'Cotação mínima', bg='#1F3447', fg='white')
        label_var = InfoMoney(line2, '-5.14%', 'Variação', bg='#1F3447', fg='white')

        line1.pack(pady=30)
        line2.pack(pady=40)

        label_quo.pack()
        label_max.pack(side='left')
        label_min.pack(side='left', padx=90)
        label_var.pack(side='left')
