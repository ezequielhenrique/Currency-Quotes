import tkinter as tk


class InfoMoney(tk.Frame):
    def __init__(self, parent, info, description):
        tk.Frame.__init__(self, parent)

        frame_master = tk.Frame(parent, bg='#1F3447')

        label_info = tk.Label(frame_master, text=str(info), font=('Roboto', 18), bg='#1F3447', fg='white')
        label_desc = tk.Label(frame_master, text=str(description), font=('Roboto', 8), bg='#1F3447', fg='white')

        label_info.pack()
        label_desc.pack()
        frame_master.pack()


class PanelQuotes(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        line1 = tk.Frame(parent, bg='white')
        line2 = tk.Frame(parent, bg='white')
        frame_max = tk.Frame(line2)
        frame_min = tk.Frame(line2)
        frame_var = tk.Frame(line2)

        InfoMoney(line1, '4.50', 'Cotação da moeda')
        InfoMoney(frame_max, '5.09', 'Cotação máxima')
        InfoMoney(frame_min, '4.50', 'Cotação mínima')
        InfoMoney(frame_var, '-5.14%', 'Variação')

        line1.pack()
        line2.pack(pady=40)
        frame_max.pack(side='left')
        frame_min.pack(side='left', padx=50)
        frame_var.pack(side='left')
