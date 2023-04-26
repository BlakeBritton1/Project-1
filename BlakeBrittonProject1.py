import tkinter as tk

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Cart Menu")
        self.cookie = 0
        self.sandwich = 0
        self.water = 0

        
        self.item_label = tk.Label(self.master, text='Choose an item:')
        self.cookie_btn = tk.Button(self.master, text='Cookie - $1.50', command=self.add_cookie)
        self.sandwich_btn = tk.Button(self.master, text='Sandwich - $4.00', command=self.add_sandwich)
        self.water_btn = tk.Button(self.master, text='Water - $1.00', command=self.add_water)
        self.total_label = tk.Label(self.master, text=f'Total: ${(self.cookie*1.5)+(self.sandwich*4.0)+(self.water*1.0):.2f}')
        self.exit_btn = tk.Button(self.master, text='Exit', command=self.master.destroy)


        self.item_label.pack()
        self.cookie_btn.pack()
        self.sandwich_btn.pack()
        self.water_btn.pack()
        self.total_label.pack()
        self.exit_btn.pack()

    def add_cookie(self):
        self.cookie += 1
        self.total_label.config(text=f'Total: ${(self.cookie*1.5)+(self.sandwich*4.0)+(self.water*1.0):.2f}')

    def add_sandwich(self):
        self.sandwich += 1
        self.total_label.config(text=f'Total: ${(self.cookie*1.5)+(self.sandwich*4.0)+(self.water*1.0):.2f}')

    def add_water(self):
        self.water += 1
        self.total_label.config(text=f'Total: ${(self.cookie*1.5)+(self.sandwich*4.0)+(self.water*1.0):.2f}')

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    print('-------------')
    print(f'({app.cookie}) - Cookie = ${(app.cookie*1.5):.2f}')
    print(f'({app.sandwich}) - Sandwich = ${(app.sandwich*4.00):.2f}')
    print(f'({app.water}) - Water = ${(app.water*1.00):.2f}')
    cookie = round(app.cookie*1.5, 2)
    sandwich = round(app.sandwich*4, 2)
    water = round(app.water, 2)
    print('-------------')
    print(f'Grand Total = ${(cookie+sandwich+water):.2f}')

if __name__ == '__main__':
    main()