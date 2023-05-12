import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Cart Menu")
        self.cookie = 0
        self.sandwich = 0
        self.water = 0

        self.item_label = tk.Label(self.master, text='Choose an item:')

        self.cookie_frame = tk.Frame(self.master)
        self.cookie_btn = tk.Button(self.cookie_frame, text='Cookie - $1.50', command=self.add_cookie)
        self.cookie_label = tk.Label(self.cookie_frame, text='Quantity:')
        self.cookie_entry = tk.Entry(self.cookie_frame, validate='key',
                                     validatecommand=(self.master.register(self.validate_entry), '%P'))
        self.cookie_btn.pack(side='left')
        self.cookie_label.pack(side='left')
        self.cookie_entry.pack(side='left')
        self.cookie_frame.pack()

        self.sandwich_frame = tk.Frame(self.master)
        self.sandwich_btn = tk.Button(self.sandwich_frame, text='Sandwich - $4.00', command=self.add_sandwich)
        self.sandwich_label = tk.Label(self.sandwich_frame, text='Quantity:')
        self.sandwich_entry = tk.Entry(self.sandwich_frame, validate='key',
                                       validatecommand=(self.master.register(self.validate_entry), '%P'))
        self.sandwich_btn.pack(side='left')
        self.sandwich_label.pack(side='left')
        self.sandwich_entry.pack(side='left')
        self.sandwich_frame.pack()

        self.water_frame = tk.Frame(self.master)
        self.water_btn = tk.Button(self.water_frame, text='Water - $1.00', command=self.add_water)
        self.water_label = tk.Label(self.water_frame, text='Quantity:')
        self.water_entry = tk.Entry(self.water_frame, validate='key',
                                    validatecommand=(self.master.register(self.validate_entry), '%P'))
        self.water_btn.pack(side='left')
        self.water_label.pack(side='left')
        self.water_entry.pack(side='left')
        self.water_frame.pack()

        self.total_label = tk.Label(self.master,
                                    text=f'Total: ${(self.cookie * 1.5) + (self.sandwich * 4.0) + (self.water * 1.0):.2f}')
        self.exit_btn = tk.Button(self.master, text='Exit', command=self.master.destroy)

        self.item_label.pack()
        self.total_label.pack()
        self.exit_btn.pack()

    def add_cookie(self):
        quantity = int(self.cookie_entry.get() or 1)
        self.cookie += quantity
        self.total_label.config(text=f'Total: ${(self.cookie * 1.5) + (self.sandwich * 4.0) + (self.water * 1.0):.2f}')

    def add_sandwich(self):
        quantity = int(self.sandwich_entry.get() or 1)
        self.sandwich += quantity
        self.total_label.config(text=f'Total: ${(self.cookie * 1.5) + (self.sandwich * 4.0) + (self.water * 1.0):.2f}')

    def add_water(self):
        quantity = int(self.water_entry.get() or 1)
        self.water += quantity
        self.total_label.config(text=f'Total: ${(self.cookie * 1.5) + (self.sandwich * 4.0) + (self.water * 1.0):.2f}')

    def validate_entry(self, value):
        return value.isdigit()

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()