from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox

class Tela:

    def __init__(self, event):

        cab = PhotoImage(file="cab.png")
        self.img = Label(janela, image=cab)
        self.img.cab = cab
        self.img.config(bg="#1C1C1C")
        self.img.place(x=0, y=0)

        label = PhotoImage(file="label.png")
        self.img2 = Label(janela, image=label)
        self.img2.label = label
        self.img2.config(bg="#1C1C1C")
        self.img2.place(x=60, y=100)

        shutdown = PhotoImage(file="shutdown.png")
        self.img3 = Label(janela, image=shutdown)
        self.img3.shutdown = shutdown
        self.img3.config(bg="#1C1C1C")
        self.img3.place(x=435, y=338)
        self.img3.bind("<Button-1>", self.desligar2)

        #self.lb = Label(janela, text="Desligar sistema em")
        #self.lb["font"] = ("Lucida console", "22")
        #self.lb.config(bg="#1C1C1C", foreground="red")
        #self.lb.place(x=80, y=130)

        self.h = tk.Entry(janela)
        self.h["font"] = ("Lucida console", "24")
        self.h.config(bg="white", foreground="black")
        self.h.place(x=180, y=200, width=50)

        self.horas = Label(janela, text="HRs")
        self.horas["font"] = ("Lucida console", "23")
        self.horas.config(bg="#1C1C1C", foreground="#ACFA58")
        self.horas.place(x=240, y=200)

        self.bt = Button(janela, text="AGENDAR")
        self.bt["font"] = ("Lucida console", "20")
        self.bt.config(bg="darkgreen", foreground="white")
        self.bt.place(x=180, y=260)
        self.bt.bind("<Button-1>", self.desligar)

        self.bt2 = Button(janela, text="Cancelar agendamento")
        self.bt2["font"] = ("Lucida console", "12")
        self.bt2.config(bg="#8A0808", foreground="white")
        self.bt2.place(x=20, y=360)
        self.bt2.bind("<Button-1>", self.cancelar)

        
        
    def desligar(self,event):

        hora = self.h.get()
        if(hora == ""):
            self.h.config(bg="#FA5858")
            messagebox.showwarning("Erro", "Digite algum valor.")
            self.h.config(bg="white")
        else:
            hr = int(hora)
            hr2=(hr*3600)
            comando = ("shutdown -s -t {}".format(hr2))
            os.system(comando)
            str(hr2)
            messagebox.showinfo("DESLIGAMENTO AGENDADO", "O sistema desligará em {} segundos.".format(hr2))

        
        
        

    def cancelar(self, event):
        os.system("shutdown -a")
        messagebox.showinfo("CANCELAR AGENDAMENTO", "O desligamento foi cancelado.")


    def desligar2(self, event):
        os.system("shutdown -s -t 20")
        
    
janela = Tk()
Tela(janela)
janela.title("SHUTDOWN BETA")
janela.geometry("500x400")
janela.resizable(width=False, height=False)
janela.config(bg="#1C1C1C")
