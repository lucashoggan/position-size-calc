from tkinter import *


class App:
    def __init__(self) -> None:
        self.app = Tk()
        self.app.geometry("400x300")
        self.app.title("Position Size Calculator")
        
        self.percentage_var = StringVar(value="1")
        self.price_var = StringVar(value="100")
        self.stop_loss_var = StringVar(value="100")
        self.account_size_var = StringVar(value="100")
        
        self.title = Label(self.app, text="Position size calculator")
        self.title.grid(row=0, column=0)
        
        self.percentage_lbl = Label(self.app, text="Risk (%)")
        self.percentage_lbl.grid(row=1, column=0)
        self.percentage_ent = Entry(self.app, textvariable=self.percentage_var)
        self.percentage_ent.grid(row=1, column=1)
        
        self.price_lbl = Label(self.app, text="Price")
        self.price_lbl.grid(row=2, column=0)
        self.price_ent = Entry(self.app, textvariable=self.price_var)
        self.price_ent.grid(row=2, column=1)
        
        self.stop_loss_lbl = Label(self.app, text="Stop loss")
        self.stop_loss_lbl.grid(row=3, column=0)
        self.stop_loss_ent = Entry(self.app, textvariable=self.stop_loss_var)
        self.stop_loss_ent.grid(row=3, column=1)
        
        self.account_size_lbl = Label(self.app, text="Account Size")
        self.account_size_lbl.grid(row=4, column=0)
        self.account_size_ent = Entry(self.app, textvariable=self.account_size_var)
        self.account_size_ent.grid(row=4, column=1)
    
        self.calc_button = Button(self.app, text="Calculate", command=self.calc_position_size)                
        self.calc_button.grid(row=5, column=0, columnspan=2)
                
        self.position_size_caption = Label(self.app, text="Position Size")
        self.position_size_caption.grid(row=6, column=0)
        self.position_size = Label(self.app, text="£")
        self.position_size.grid(row=6, column=1)
        
    def calc_position_size(self):
        diff = float(self.price_var.get()) - float(self.stop_loss_var.get())
        diff*=-1 if diff < 0 else 1
        amount_to_risk = float(self.account_size_var.get()) * (float(self.percentage_var.get())/100)
        shares = amount_to_risk/diff
        position_size = round(shares*float(self.price_var.get()))
        self.position_size.config(text=f"£{position_size}")
        
        
        
        
        
    def run(self): self.app.mainloop()
    
if __name__ == "__main__":
    a = App()
    a.run()