#!/usr/bin/env python

from Tkinter import *
import tkMessageBox
import subprocess

root = Tk()
root.geometry('216x100+0+0')
root.title('MITM Defender')

text_Input = StringVar()
operator=''

Tops = Frame(root,width = 1600,height = 50,bg="gold",relief=RAISED)
Tops.pack(side=TOP)

f1 = Frame(root,width = 80,height = 70,relief=RAISED)
f1.pack(side=LEFT)


f2 = Frame(root,width = 30,height = 70,relief=RAISED)
f2.pack(side=RIGHT)


lblInfo = Label(Tops , font=('arial',18,"bold"),text="MITM Defender",fg="red",bd=10,anchor="w")
lblInfo.grid(row=0,column=0)




def flag_start():
    def gateway_ip():
        ip_string = subprocess.check_output(["ip", "r"])
        for i in range (12,27):
            if ip_string[i]  == " " :
                break
        ip = ip_string[12:i]
        return ip


    def gateway_mac(ip) :
        arp_mac = subprocess.check_output(["arp","-a",ip])
        count = 0
        for i in range (0,1000):
            if arp_mac[i] == " ":
                count = count + 1
                if count == 3 :
                    mac_address = arp_mac[i+1:i+18]
                    break
        return mac_address

    def alert(mac):
        while True:
            compared_mac = gateway_mac(ip)
            if (mac != compared_mac) and ( compared_mac != "entries no match ") :
                tkinter.messagebox.showwarning('WARNING','Your computer \nis under attack')
                break
            if compared_mac == "entries no match " :
                break
        return compared_mac

    def messagebox(attack_mac) :
        if (attack == "entries no match ") :
            tkMessageBox.showwarning('WARNING','You are disconnected')
        else :
            tkMessageBox.showinfo('INFORMATION','You attacked by : \n' + attack_mac)

    ip = gateway_ip()
    print(ip)
    mac = gateway_mac(ip)
    print(mac)
    attack = alert(mac)
    print(attack)
    messagebox(attack)


#==============================================================================================Buttons===========================================================================================
btnStart=Button(f1,padx=2,pady=1,bd=2,fg="black",font=("arial",10,"bold"),width=29,text="Start",bg="green",command = flag_start).grid(row=27,column=5)


root.mainloop()
