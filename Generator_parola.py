from tkinter import *
import random
import re
import json
import pyperclip as pc
import os
from PIL import Image, ImageTk
from stat import S_IREAD, S_IRGRP, S_IROTH
from stat import S_IWUSR


#Creare window
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
desktop=desktop+"\Parole.txt"
window=Tk()
window.title("Password Generator & Encryptor")
window.configure(width=800, height=400) 
window.resizable(width=False, height=False)    
window.configure(bg="#222A35")
windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/3 - windowHeight/2)
window.geometry("+{}+{}".format(positionRight, positionDown))


def RBGAImage(path):
    return Image.open(path).convert("RGBA")


class butoane():
    def __init__(self):
        #Creare Buton Generare
        self.generate_again=0
        self.decriptare_again=0
        self.bh=0
        self.np=0
        self.wrong=0
        self.inapoi_from_delete=0
        self.dp=0
        self.delete_from_refuz=0
        self.text()
        self.imagine_decrip=PhotoImage(file="Buttons\Decriptare.png")
        self.buton_decriptare=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_decriptare.config(image=self.imagine_decrip, command=self.parola_decriptare)
        self.buton_decriptare.place(relx=0.5, rely=0.65, anchor='center')
        self.buton_decriptare_if_refuz=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35",image=self.imagine_decrip, command=self.parola_decriptare_if_refuz)
        self.photo=PhotoImage(file='Buttons\Generare_og.png')
        self.button=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.button.config(image=self.photo, command=self.apasare_buton, relief='ridge')
        self.button.place(relx=0.5, rely=0.45, anchor='center')   
        self.photo_lock=Image.open('Buttons\lock2.png')
        self.photo_lock = RBGAImage("Buttons\lock2.png")
        self.photo_lock=ImageTk.PhotoImage(self.photo_lock)
        self.photo_label=Label(image=self.photo_lock)
        self.photo_label.image=self.photo_lock
        self.photo_label.config(bg="#222A35")
        self.photo_label.place(relx=0.5,rely=0.22, anchor='center')
        self.photo_inapoi=PhotoImage(file='Buttons\Inapoi.png')
        self.poza_generare=PhotoImage(file='Buttons\Generare.png')
        self.buton_inapoi=Button(window, borderwidth=0, image=self.photo_inapoi,activebackground='#222A35' , bg='#222A35', font=('Ubuntu', 20), command=self.init_empty)
        self.poza_iesire=PhotoImage(file='Buttons\Iesire.png')
        self.poza_iesire_2=PhotoImage(file='Buttons\Iesire_2.png')
        self.buton_iesire=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_iesire.config(image=self.poza_iesire, command=lambda:window.quit())
        self.buton_iesire_2=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35",
        image=self.poza_iesire_2, command=lambda:window.quit())
        self.buton_generare_noua=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_generare_noua.config(image=self.poza_generare, command=self.apasare_buton_resume)
        self.buton_generare_noua_2=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_generare_noua_2.config(image=self.poza_generare, command=self.apasare_buton_resume_2)
        self.photo_delete=PhotoImage(file="Buttons\Delete.png")
        self.buton_delete=Button(window, image=self.photo_delete,borderwidth=0, bg="#222A35", activebackground="#222A35", command=self.delete_name)
        self.buton_delete.place(relx=0.5, rely=0.85, anchor='center')
        self.label_eroare=Label(window, text="Name cannot be empty!", bg='#222A35', font=('Ubuntu', 25), fg='white')
        self.label_nu_exista=Label(window, text="This password doesn't exist!" , bg='#222A35', font=('Ubuntu', 25), fg='white')
        self.label_empty=Label(window, text="There aren't any saved passwords!", bg='#222A35', font=('Ubuntu', 25), fg='white')
        self.photo_home=PhotoImage(file='Buttons\Home.png')
        self.buton_home=Button(window,bg="#222A35", activebackground="#222A35", borderwidth=0, image=self.photo_home, command=self.home)


    def text(self):
        #Afisare "Titlu"
        self.label_titlu = Label(window, text="Password Generator & Encryptor", bg='#222A35', font=('Ubuntu', 25), fg='#ac83dd')
        self.label_titlu.place(relx=0.5, rely=0.05, anchor='center')

    def text_delete(self):
        self.label_titlu.place_forget()
        
    def init_empty(self):
        if self.inapoi_from_delete==1:
            self.buton_iesire_2.place_forget()
            self.entry_delete.place_forget()
            self.buton_send_delete.place_forget()
            self.label_nume_parola_delete.place_forget()
        if self.inapoi_from_delete==2:
            self.label_empty.place_forget()
        if self.np==1:
            self.label_nu_exista.place_forget()
        if self.dp==1:
            self.label_parola_stearsa.place_forget()
        self.photo_delete=PhotoImage(file="Buttons\Delete.png")
        self.buton_delete=Button(window, image=self.photo_delete,borderwidth=0, bg="#222A35", activebackground="#222A35", command=self.delete_name)
        self.buton_delete.place(relx=0.5, rely=0.85, anchor='center')
        self.photo_label.place_forget()
        self.text()
        self.label_empty.place_forget()
        self.buton_inapoi.place_forget()
        self.buton_decriptare.place(relx=0.5, rely=0.65, anchor='center')
        self.button.place(relx=0.5, rely=0.45, anchor='center')   
        self.photo_label.place(relx=0.5,rely=0.22, anchor='center')
        self.buton_delete.place(relx=0.5, rely=0.85, anchor='center')

    def init_empty_2(self):
        self.photo_label.place_forget()
        self.buton_inapoi_2.place_forget()
        self.buton_iesire_2.place_forget()
        #self.entry_afisare_parola.place_forget()
        self.label_afisare_parola.place_forget()
        self.label_parola_decriptata.place_forget()
        self.label_copy.place_forget()
        self.text()
        #self.label_empty.place_forget()
        self.buton_inapoi.place_forget()
        self.buton_decriptare.place(relx=0.5, rely=0.65, anchor='center')
        self.button.place(relx=0.5, rely=0.45, anchor='center')   
        self.buton_decriptare
        self.photo_label.place(relx=0.5,rely=0.22, anchor='center')
        self.buton_delete.place(relx=0.5, rely=0.85, anchor='center')
        

    def parola(self):
        #Generare parola
        self.photo_label.place_forget()
        self.litere='qwertyuiopasdfghjklzxcvbnm'
        self.litere_mari='QWERTYUIOPASDFGHJKLZXCVBNM'
        self.simboluri='!@#$%^&*()?'
        self.cifre='0123456789'
        self.password=""
        self.password_char=""
    
        for self.i in range(4):
            self.password_char=random.choice(self.litere)+random.choice(self.litere_mari)+random.choice(self.simboluri)+random.choice(self.cifre)
            self.password=self.password+self.password_char

        self.password="".join(random.sample(self.password, len(self.password)))
        return self.password

    def decriptare(self, decr):
        self.photo_label.place_forget()
        self.encrypt={
            'q': 'J#Z&', 'w': '^sY@', 'e': '0E8$', 'r': 'gDb0', 't': 'l(*F', 'y': 'GND@', 'u': 'ANhs', 'i': '6T&q', 'o': 'gjBw', 'p': '3KA7', 'a': '0NzA', 's': 'tmbN', 'd': 'zcat', 'f': 'wpbH', 'g': 'Q0mI', 'h': 'OzX2', 'j': 'Lg$c', 'k': 'ki(R', 'l': 'C#9s', 'z': 'Jkin', 'x': 'ga(U', 'c': 'aD6j', 'v': 
            'hUDl', 'b': 'efjo', 'n': 'W7r$', 'm': 'ndCu', 'Q': '3q0Q', 'W': '?pC5', 'E': 'O3NE', 'R': '^31K', 'T': 'G)h$', 'Y': 'YY!7', 'U': 'w(^z', 'I': 'BRNH', 'O': '2PI&', 'P': '&(GW', 'A': 'Zuw)', 'S': 'AhrU', 'D': 'd9Rd', 'F': '9U7E', 'G': 'apb1', 'H': 'v)Dx', 'J': 'JKyc', 'K': '^wjn', 'L': '8*TX', 'Z': 'uQR1', 'X': 'ZAro', 'C': 'jEvT', 'V': 'LQrK', 'B': 'Wu3p', 'N': 'tOsH', 'M': 'Iihy', '!': 'LSP(', '@': 'RLFK', '#': 'w5r6', '$': 'e(I*', '%': 'hOmK', '^': 'P&CY', '&': '$oOu', '*': 'Rw!I', '(': 'PWc3', ')': '?n5Q', '?': 'BbS9', '0': 'VM3D', '1': '2P&p', '2': 'Vy%J', '3': 'aV(r', '4': '4BC%', '5': 'D0f0', '6': 'rvcy', '7': '%HH1', '8': '%KZ$', '9': '5f0F'
        }
        self.enc=""
        for self.i in range(0, len(decr), 4):
                self.x=decr[self.i]+decr[self.i+1]+decr[self.i+2]+decr[self.i+3]
                for self.key,self.value in self.encrypt.items():
                    if self.x==self.value:
                        self.enc=self.enc+self.key
        return self.enc

    def criptare(self, message):
            self.message=self.password


            self.encrypt={
            'q': 'J#Z&', 'w': '^sY@', 'e': '0E8$', 'r': 'gDb0', 't': 'l(*F', 'y': 'GND@', 'u': 'ANhs', 'i': '6T&q', 'o': 'gjBw', 'p': '3KA7', 'a': '0NzA', 's': 'tmbN', 'd': 'zcat', 'f': 'wpbH', 'g': 'Q0mI', 'h': 'OzX2', 'j': 'Lg$c', 'k': 'ki(R', 'l': 'C#9s', 'z': 'Jkin', 'x': 'ga(U', 'c': 'aD6j', 'v': 
            'hUDl', 'b': 'efjo', 'n': 'W7r$', 'm': 'ndCu', 'Q': '3q0Q', 'W': '?pC5', 'E': 'O3NE', 'R': '^31K', 'T': 'G)h$', 'Y': 'YY!7', 'U': 'w(^z', 'I': 'BRNH', 'O': '2PI&', 'P': '&(GW', 'A': 'Zuw)', 'S': 'AhrU', 'D': 'd9Rd', 'F': '9U7E', 'G': 'apb1', 'H': 'v)Dx', 'J': 'JKyc', 'K': '^wjn', 'L': '8*TX', 'Z': 'uQR1', 'X': 'ZAro', 'C': 'jEvT', 'V': 'LQrK', 'B': 'Wu3p', 'N': 'tOsH', 'M': 'Iihy', '!': 'LSP(', '@': 'RLFK', '#': 'w5r6', '$': 'e(I*', '%': 'hOmK', '^': 'P&CY', '&': '$oOu', '*': 'Rw!I', '(': 'PWc3', ')': '?n5Q', '?': 'BbS9', '0': 'VM3D', '1': '2P&p', '2': 'Vy%J', '3': 'aV(r', '4': '4BC%', '5': 'D0f0', '6': 'rvcy', '7': '%HH1', '8': '%KZ$', '9': '5f0F'
    }


            self.enc_message=""

            for self.i in message:
                if self.i in self.encrypt:
                    self.enc_message=self.enc_message+self.encrypt[self.i]

            self.enc=""

            for self.i in range(0, len(self.enc_message), 4):
                self.x=self.enc_message[self.i]+self.enc_message[self.i+1]+self.enc_message[self.i+2]+self.enc_message[self.i+3]
                for self.key,self.value in self.encrypt.items():
                    if self.x==self.value:
                        self.enc=self.enc+self.key
            return self.enc_message

    def apasare_buton_incercati(self):
        self.photo_label.place_forget()
        self.text_delete()
        self.buton_creare_parola.place_forget()
        self.buton_incercati.place_forget()
        self.label_nu_exista.place_forget()
        self.apasare_buton()

    def apasare_buton(self):
        self.buton_delete.place_forget()
        self.photo_label.place_forget()
        self.text_delete()
        self.buton_decriptare.place_forget()
        self.button.place_forget()
    
        #Afisare text
        self.label_generat=Label(window, text="Password was generated!", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
        self.label_generat.place(relx=0.5, rely=0.05, anchor='center')

        #Afisare intrebare
        self.label_parola=Label(window, text="Do you want to keep this password?", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
        self.label_parola.place(relx=0.5, rely=0.3, anchor='center')

        #Afisare butoane "Da" si "Nu"
        self.photo_accept=PhotoImage(file='Buttons\Accept.png')
        self.photo_refuz=PhotoImage(file='Buttons\Refuz.png')

        self.buton_accept=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_accept.config(image=self.photo_accept, command=lambda:[self.accept(), self.buton_accept.place_forget()])
        self.buton_refuz=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_refuz.config(image=self.photo_refuz, command=lambda:[self.refuz(), self.buton_refuz.place_forget()])

        self.photo_password=PhotoImage(file='Buttons\parola.png')
        self.button_password=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.button_password.config(image=self.photo_password, text=self.parola(), font=('Ubuntu', 31), fg="black", compound=CENTER, relief='sunken')

        self.button_password.place(relx=0.5, rely=0.5, anchor='center')
        self.buton_accept.place(relx=0.35, rely=0.80, anchor='center')
        self.buton_refuz.place(relx=0.65, rely=0.80, anchor='center')


    def apasare_buton_resume_2(self):
        if self.generate_again==1:
            self.buton_generare_noua_2.place_forget()
            self.buton_decriptare_if_refuz.place_forget()
        self.buton_delete.place_forget()
        self.photo_label.place_forget()
        self.buton_decriptare.place_forget()
        self.buton_iesire.place_forget()
        self.buton_generare_noua.place_forget()
        self.button.place_forget()

        self.label_generat=Label(window, text="Password was generated!", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
        self.label_generat.place(relx=0.5, rely=0.05, anchor='center')

        self.label_parola=Label(window, text="Do you want to keep this password?", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
        self.label_parola.place(relx=0.5, rely=0.3, anchor='center')

        self.photo_accept=PhotoImage(file='Buttons\Accept.png')
        self.photo_refuz=PhotoImage(file='Buttons\Refuz.png')

        self.buton_accept=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_accept.config(image=self.photo_accept, command=lambda:[self.accept(), self.buton_accept.place_forget()])
        self.buton_refuz=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_refuz.config(image=self.photo_refuz, command=lambda:[self.refuz(), self.buton_refuz.place_forget()])

        self.photo_password=PhotoImage(file='Buttons\parola.png')
        self.button_password=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.button_password.config(image=self.photo_password, text=self.parola(), font=('Ubuntu', 31), fg="black", compound=CENTER, relief='sunken')

        self.button_password.place(relx=0.5, rely=0.5, anchor='center')
        self.buton_accept.place(relx=0.35, rely=0.80, anchor='center')
        self.buton_refuz.place(relx=0.65, rely=0.80, anchor='center')

    def apasare_buton_resume(self):
        self.buton_home.place_forget()
        self.buton_delete.place_forget()
        self.photo_label.place_forget()
        #Functie asemanatoare cu cea de mai sus, se va folosi atunci cand utilizatorului nu ii place prima parola si doreste sa genereze una noua
        #self.label_pentru.place_forget()
        self.entry.place_forget()
        self.label_parola_salvata.place_forget()
        self.buton_decriptare.place_forget()
        self.buton_iesire.place_forget()
        self.buton_generare_noua.place_forget()
        self.button.place_forget()

        self.label_generat=Label(window, text="Password was generated!", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
        self.label_generat.place(relx=0.5, rely=0.05, anchor='center')

        self.label_parola=Label(window, text="Do you want to keep this password?", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
        self.label_parola.place(relx=0.5, rely=0.3, anchor='center')

        self.photo_accept=PhotoImage(file='Buttons\Accept.png')
        self.photo_refuz=PhotoImage(file='Buttons\Refuz.png')

        self.buton_accept=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_accept.config(image=self.photo_accept, command=lambda:[self.accept(), self.buton_accept.place_forget()])
        self.buton_refuz=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_refuz.config(image=self.photo_refuz, command=lambda:[self.refuz(), self.buton_refuz.place_forget()])

        self.photo_password=PhotoImage(file='Buttons\parola.png')
        self.button_password=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.button_password.config(image=self.photo_password, text=self.parola(), font=('Ubuntu', 31), fg="black", compound=CENTER, relief='sunken')

        self.button_password.place(relx=0.5, rely=0.5, anchor='center')
        self.buton_accept.place(relx=0.35, rely=0.80, anchor='center')
        self.buton_refuz.place(relx=0.65, rely=0.80, anchor='center')
    
    def accept(self):
        self.photo_label.place_forget()
        #Functie pentru apasarea butonului "Da"
        self.buton_refuz.place_forget()
        self.label_generat.place_forget()
        self.label_parola.place_forget()
        self.button_password.place_forget()
        self.label_pentru=Label(window,text="What is the name of the password?", bg='#222A35', font=('Ubuntu', 25), fg='white' )
        self.label_pentru.place(relx=0.5, rely=0.05, anchor='center')
        self.entry=Entry(window, font=("Ubuntu", 40))
        self.entry.place(relx=0.5, rely=0.5, anchor='center')
        self.photo_submit=PhotoImage(file='Buttons\Save.png')
        self.buton_submit=Button(window, borderwidth=0, bg="#222A35", activebackground="#222A35")
        self.buton_submit.config(image=self.photo_submit, command=self.submit)
        self.buton_submit.place(relx=0.5, rely=0.85, anchor='center')

    def parola_decriptare(self):
        self.buton_delete.place_forget()
        self.photo_label.place_forget()
        self.wrong=0
        self.text_delete()
        filesize = os.path.getsize("parole.json")
        if filesize==0:
            self.button.place_forget()
            self.buton_decriptare.place_forget()
            self.buton_inapoi.place(relx=0.5, rely=0.75, anchor='center')
            self.label_empty.place(relx=0.5, rely=0.5, anchor='center')
        elif filesize!=0:
            with open('parole.json', 'r') as g:
                read=json.load(g)
            if not read:
                self.button.place_forget()
                self.buton_decriptare.place_forget()
                self.buton_inapoi.place(relx=0.5, rely=0.75, anchor='center')
                self.label_empty=Label(window, text="There aren't any saved passwords!", bg='#222A35', font=('Ubuntu', 25), fg='white')
                self.label_empty.place(relx=0.5, rely=0.5, anchor='center')
            else:
                self.label_introduceti_parola=Label(window, text="Password", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
                self.label_introduceti_parola.place(relx=0.5, rely=0.35, anchor='center')
                self.button.place_forget()
                self.entry_parola=Entry(window, show="*", font=("Ubuntu", 40), fg='#ac83dd')
                self.entry_parola.place(relx=0.5, rely=0.5, anchor='center')
                self.buton_decriptare.place_forget()
                self.buton_inapoi_decri=Button(window,bg="#222A35", activebackground="#222A35", borderwidth=0, image=self.photo_inapoi, command=self.init_empty_decri)
                self.buton_inapoi_decri.place(relx=0.85, rely=0.85, anchor='center')
                self.photo_trimite=PhotoImage(file='Buttons\Trimite.png')
                self.buton_submit_parola=Button(window, image=self.photo_trimite, borderwidth=0,bg="#222A35", activebackground="#222A35" , command=self.verificare_parola)
                self.buton_submit_parola.place(relx=0.5, rely=0.75, anchor='center')

    def parola_decriptare_if_refuz(self):
        self.buton_delete.place_forget()
        self.buton_iesire_2.place_forget()
        self.buton_decriptare_if_refuz.place_forget()
        self.photo_label.place_forget()
        self.buton_generare_noua_2.place_forget()
        self.buton_iesire.place_forget()
        self.buton_generare_noua.place_forget()
        filesize = os.path.getsize("parole.json")
        if filesize==0:
            self.button.place_forget()
            self.buton_decriptare.place_forget()
            self.buton_inapoi=Button(window, image=self.photo_inapoi, borderwidth=0,activebackground='#222A35', bg='#222A35', font=('Ubuntu', 20), command=self.init_empty)
            self.buton_inapoi.place(relx=0.5, rely=0.75, anchor='center')
            self.label_empty=Label(window, text="There aren't any saved passwords!", bg='#222A35', font=('Ubuntu', 25), fg='white')
            self.label_empty.place(relx=0.5, rely=0.5, anchor='center')
        elif filesize!=0:
            with open('parole.json', 'r') as g:
                read=json.load(g)
            if not read:
                self.button.place_forget()
                self.buton_decriptare.place_forget()
                self.buton_inapoi=Button(window, borderwidth=0, image=self.photo_inapoi,activebackground='#222A35' , bg='#222A35', font=('Ubuntu', 20), command=self.init_empty)
                self.buton_inapoi.place(relx=0.5, rely=0.75, anchor='center')
                self.label_empty=Label(window, text="There aren't any saved passwords!", bg='#222A35', font=('Ubuntu', 25), fg='white')
                self.label_empty.place(relx=0.5, rely=0.5, anchor='center')
            else:
                self.label_introduceti_parola=Label(window, text="Password", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
                self.label_introduceti_parola.place(relx=0.5, rely=0.35, anchor='center')
                self.button.place_forget()
                self.entry_parola=Entry(window, show="*", font=("Ubuntu", 40), fg='#ac83dd')
                self.entry_parola.place(relx=0.5, rely=0.5, anchor='center')
                self.buton_decriptare.place_forget()
                self.buton_inapoi_decri=Button(window,bg="#222A35", activebackground="#222A35", borderwidth=0, image=self.photo_inapoi, command=self.init_empty_decri)
                self.buton_inapoi_decri.place(relx=0.85, rely=0.85, anchor='center')
                self.photo_trimite=PhotoImage(file='Buttons\Trimite.png')
                self.buton_submit_parola=Button(window, image=self.photo_trimite, borderwidth=0,bg="#222A35", activebackground="#222A35" , command=self.verificare_parola)
                self.buton_submit_parola.place(relx=0.5, rely=0.75, anchor='center')

    def verificare_parola_incercati(self):
        self.nu=0
        self.photo_label.place_forget()
        self.label_nu_exista.place_forget()
        self.buton_incercati.place_forget()
        self.parola_verif=self.entry_parola.get()
        self.buton_submit_parola.place_forget()
        self.label_ce_parola=Label(window, text="What is the name of the password?", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen' )
        self.label_ce_parola.place(relx=0.5, rely=0.35, anchor='center')
        self.entry_parola.place_forget()
        self.entry_ce_parola=Entry(window, font=("Ubuntu", 40))
        self.entry_ce_parola.place(relx=0.5, rely=0.5, anchor='center')
        self.buton_trimitere_nume_parola=Button(window, image=self.photo_submit, bg="#222A35", activebackground="#222A35", command=self.nume_parola_decriptare)
        self.buton_trimitere_nume_parola.place(relx=0.5, rely=0.65, anchor='center')


    def verificare_parola(self):
                self.photo_label.place_forget()
                self.wrong=0
                self.label_introduceti_parola.place_forget()
                self.parola_verif=self.entry_parola.get()
                if self.parola_verif=='omegalambda7xl9':
                    self.buton_inapoi_decri.place_forget()
                    self.buton_submit_parola.place_forget()
                    self.label_ce_parola=Label(window, text="What is the name of the password you want to decrypt?", bg='#222A35', font=('Ubuntu', 20), fg='lightgreen' )
                    self.label_ce_parola.place(relx=0.5, rely=0.35, anchor='center')
                    self.entry_parola.place_forget()
                    self.entry_ce_parola=Entry(window, font=("Ubuntu", 40))
                    self.entry_ce_parola.place(relx=0.5, rely=0.5, anchor='center')
                    self.buton_trimitere_nume_parola=Button(window)
                    self.buton_trimitere_nume_parola.config(image=self.photo_trimite, borderwidth=0,bg="#222A35", activebackground="#222A35" , command=self.nume_parola_decriptare)
                    self.buton_trimitere_nume_parola.place(relx=0.5, rely=0.75, anchor='center')
                else:
                    self.wrong=1
                    self.label_parola_gresita=Label(window, text="Password is wrong!", bg='#222A35', font=('Ubuntu', 25), fg='red')
                    self.label_parola_gresita.place(relx=0.5, rely=0.35, anchor='center')

    def init_empty_decri(self):
        self.photo_label.place_forget()
        if self.wrong==1:
            self.label_parola_gresita.place_forget()
        self.label_introduceti_parola.place_forget()
        self.text()
        self.buton_inapoi_decri.place_forget()
        self.entry_parola.place_forget()
        self.buton_submit_parola.place_forget()
        self.buton_delete.place(relx=0.5, rely=0.85, anchor='center')
        self.photo_label.place_forget()
        self.label_empty.place_forget()
        self.buton_inapoi.place_forget()
        self.buton_decriptare.place(relx=0.5, rely=0.65, anchor='center')
        self.button.place(relx=0.5, rely=0.45, anchor='center')   
        self.photo_label.place(relx=0.5,rely=0.22, anchor='center')
        self.buton_delete.place(relx=0.5, rely=0.85, anchor='center')
    
    def nume_parola_decriptare(self):
        self.nu=0
        self.photo_label.place_forget()
        c=0
        self.nume_parola=self.entry_ce_parola.get()
        if self.nume_parola.strip()=="":
            self.label_eroare.place(relx=0.5, rely=0.3, anchor='center')
        else:
            self.nume_parola=str(self.nume_parola).lower()
            with open('parole.json', 'r') as f:
                self.read=json.load(f)
                for i in self.read.keys():
                    if str(i).lower()==self.nume_parola:
                        #self.afisare_parola_decriptata
                        if self.nu==1:
                            self.label_nu_exista.place_forget()
                        self.entry_ce_parola.place_forget()
                        self.label_parola_decriptata=Label(window,text="The decrypted password for {} is: ".format(i) , bg='#222A35', font=('Ubuntu', 25), fg='white')
                        self.label_parola_decriptata.place(relx=0.5, rely=0.35, anchor='center')
                        self.label_ce_parola.place_forget()
                        pc.copy(self.decriptare(self.read[i]))
                        self.label_afisare_parola=Label(window,bd=0, bg='#222A35', font=("Ubuntu", 40), text=self.decriptare(self.read[i]), fg='white')
                        self.label_afisare_parola.place(relx=0.5, rely=0.5, anchor='center')
                        self.buton_trimitere_nume_parola.place_forget()
                        self.buton_terminare=Button(window)
                        self.label_copy=Label(window, text="Password was automatically copied to the clipboard!", bg='#222A35', font=('Ubuntu', 19), fg='white')
                        self.label_copy.place(relx=0.5, rely=0.75, anchor='center')
                        self.buton_inapoi_2=Button(window, borderwidth=0, image=self.photo_inapoi,activebackground='#222A35' , bg='#222A35', font=('Ubuntu', 20), command=self.init_empty_2)
                        self.buton_inapoi_2.place(relx=0.75, rely=0.90, anchor='center')
                        self.buton_iesire_2.place(relx=0.25, rely=0.90, anchor='center')
                        break
                    else:
                        #self.nume_parola_nu_exista()
                        self.nu=1
                        self.label_ce_parola.place_forget()
                        self.label_nu_exista.place(relx=0.5, rely=0.25, anchor='center')


    def nume_parola_nu_exista(self):
                self.photo_label.place_forget()
                self.buton_trimitere_nume_parola.place_forget()
                self.label_ce_parola.place_forget()
                self.label_nu_exista.place(relx=0.5, rely=0.25, anchor='center')
                self.buton_incercati=Button(window, text="Try Again", font=('Ubuntu', 18))
                self.buton_incercati.config(command=self.verificare_parola_incercati)
                self.buton_incercati.place(relx=0.25, rely=0.75, anchor='center')
                self.buton_creare_parola=Button(window, text='Create Password', font=('Ubuntu', 18), command=self.apasare_buton_incercati)
                self.buton_creare_parola.place(relx=0.75, rely=0.75, anchor='center')
                    

    def submit(self):
        self.entry.place_forget()
        self.photo_label.place_forget()
        self.label_pentru.place_forget()
        self.r=''
        self.d={}
        c=0
        #Creare buton submit si verificare daca utilizatorul a lasat necompletat spatiul de "Pentru ce este parola?"
        self.nume=self.entry.get()
        self.nume=str(self.nume)
        if len(self.nume)==0:
            c=c+1
            self.label_eroare=Label(window, text="Name cannot be empty!", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
            self.label_eroare.place(relx=0.5, rely=0.3, anchor='center')
        else:
            os.chmod(desktop, S_IWUSR|S_IREAD)
            with open(desktop, 'r') as f:
                if c>0:
                    self.label_eroare.place_forget()

                self.d[self.nume]=self.criptare(self.password)
                self.buton_home.place(relx=0.5, rely=0.75, anchor='center')
                self.label_parola_salvata=Label(window, text="Password saved!", bg='#222A35', font=('Ubuntu', 25), fg='lightgreen')
                self.buton_submit.place_forget()
                self.buton_generare_noua.place(relx=0.15, rely=0.75, anchor='center')
                self.buton_iesire.place(relx=0.85, rely=0.75, anchor='center')
                self.label_parola_salvata.place(relx=0.5, rely=0.4, anchor='center')
                '''self.f.write(re.sub(' +', ' ', self.nume).strip())
                self.f.write(" ")
                self.f.write(":")
                self.f.write(" ")'''
                '''self.f.write(self.criptare(self.password))'''
                #self.f.write("Decrypted password : ")
                #self.f.write(self.decriptare(self.criptare(self.password)))
                #self.criptare(self.password)
                self.d[self.nume]=self.criptare(self.password)
                filesize = os.path.getsize("parole.json")

            if filesize!=0:
                with open('parole.json','r') as y:
                    dic = json.load(y)

                dic.update(self.d)

                with open('parole.json','w') as f:
                    json.dump(dic, f)
                    
                with open('parole.json', 'r') as g:
                    self.citire=json.load(g)
                with open(desktop, 'w') as f:
                    for i in dic:
                        f.write(i)
                        f.write(" ")
                        f.write(":")
                        f.write(" ")
                        f.write(dic[i])
                        f.write("\n")
            else:
                with open('parole.json','w') as f:
                    json.dump(self.d, f)
            os.chmod(desktop, S_IREAD|S_IRGRP|S_IROTH)
    def refuz(self):
        self.delete_from_refuz=1
        self.decriptare_again=1
        self.generate_again=1
        self.photo_label.place_forget()
        #Functie pentru apasarea butonului "Nu"
        #Creare buton "Iesire" si "Generare noua"
        self.buton_accept.place_forget()
        self.label_generat.place_forget()
        self.label_parola.place_forget()
        self.button_password.place_forget()
        self.buton_delete.place(relx=0.5, rely=0.5, anchor='center')
        self.buton_iesire.place(relx=0.5, rely=0.85, anchor='center')
        self.buton_generare_noua_2.place(relx=0.8, rely=0.5, anchor='center')
        self.buton_decriptare_if_refuz.place(relx=0.2, rely=0.5, anchor='center')

    def delete_name(self):
        if self.delete_from_refuz==1:
            self.buton_decriptare_if_refuz.place_forget()
            self.buton_iesire.place_forget()
            self.buton_generare_noua_2.place_forget()
        self.buton_inapoi.place(relx=0.85, rely=0.9, anchor='center')
        with open('parole.json', 'r') as f:
                self.read=json.load(f)
        if len(self.read.keys())==0:
            self.inapoi_from_delete=2
            self.label_empty.place(relx=0.5, rely=0.5, anchor='center')
            self.text_delete()
            self.photo_label.place_forget()
            self.button.place_forget()
            self.buton_decriptare.place_forget()
            self.buton_delete.place_forget()
            self.buton_inapoi.place(relx=0.5, rely=0.75, anchor='center')
        else:
            self.inapoi_from_delete=1
            if self.delete_from_refuz==1:
                self.buton_delete.place_forget()
                self.buton_iesire.place_forget()
                self.buton_generare_noua_2.place_forget()
                self.buton_decriptare.place_forget()
            self.np=0
            self.label_nume_parola_delete=Label(window, text='What is the name of the password you want to delete?', bg='#222A35', font=('Ubuntu', 21), fg='#ac83dd')
            self.label_nume_parola_delete.place(relx=0.5, rely=0.35, anchor='center')
            self.text_delete()
            self.photo_label.place_forget()
            self.button.place_forget()
            self.buton_decriptare.place_forget()
            self.buton_delete.place_forget()
            self.entry_delete=Entry(window, font=('Ubuntu', 25))
            self.entry_delete.place(relx=0.5, rely=0.6, anchor='center')
            self.photo_buton_delete=PhotoImage(file='Buttons\Delete_pass.png')
            self.buton_send_delete=Button(window, image=self.photo_buton_delete, borderwidth=0, bg='#222A35', activebackground='#222A35', command=self.delete)
            self.buton_send_delete.place(relx=0.5, rely=0.75, anchor='center')



    def delete(self):
        self.bh=0
        true=0
        nume_parola=self.entry_delete.get()
        for i in self.read:
            if i.lower()==nume_parola.lower():
                true=1
                break
        if nume_parola.strip()=="":
            self.label_eroare.place(relx=0.5, rely=0.3, anchor='center')
            self.label_nume_parola_delete.place_forget()
        elif true==0:
            self.np=1
            self.label_nume_parola_delete.place_forget()
            self.label_nu_exista.place(relx=0.5, rely=0.3, anchor='center')
        else:
            if self.np==1:
                self.label_nu_exista.place_forget()

            self.bh=1
            self.dp=1
            self.label_parola_stearsa=Label(window, text='Password deleted!', bg='#222A35', font=('Ubuntu', 21), fg='red' )
            self.label_parola_stearsa.place(relx=0.5, rely=0.3, anchor='center')
            self.buton_inapoi.place(relx=0.5, rely=0.75, anchor='center')
            self.buton_iesire_2.place(relx=0.90, rely=0.92, anchor='center')
            self.label_nume_parola_delete.place_forget()
            self.label_eroare.place_forget()
            self.buton_send_delete.place_forget()
            self.entry_delete.place_forget()
            c=0
            nume_parola=self.entry_delete.get()
            with open('parole.json', 'r') as f:
                read=json.load(f)
            for i in read.keys():
                if nume_parola in read.keys():
                    c=c+1
                if i==nume_parola:
                    break

            for i in read:
                if i.lower()==nume_parola.lower():
                    del read[i]
                    break
            

            with open('parole.json', 'w') as g:
                json.dump(read, g)

                os.chmod(desktop, S_IWUSR|S_IREAD)
                with open(desktop, 'r+') as f:
                    p=1
                    f.truncate(0)

                    with open(desktop ,'w') as g:
                        for i in read:
                            f.write(i)
                            f.write(" : ")
                            f.write(read[i])
                            f.write('\n')

            os.chmod(desktop, S_IREAD|S_IRGRP|S_IROTH)



    def home(self):
        self.buton_home.place_forget()
        self.buton_iesire.place_forget()
        self.buton_generare_noua.place_forget()
        self.label_parola_salvata.place_forget()
        self.entry.place_forget()
        self.__init__()

#Main():

butoane()

window.mainloop()

