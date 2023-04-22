from os.path import exists
from tkinter import *
from xml.dom.minidom import Document


class Email_Slicer(object):
    def __init__(self, w: Tk):
        '''we make the grafic to recieve entry from user'''
        self.w = w
        self.w.title("Email slicer")
        self.w.geometry('340x160+500+200')
        self.w.resizable(False, False)
        
        self.l1 = Label(self.w, text= "name", font= "tahoma 14 normal")
        self.l1.place(x = 10, y = 10)
        self.v1 = StringVar()
        self.e1 = Entry(self.w, font = "tahoma 14 normal", textvariable= self.v1)
        self.e1.place(x = 110, y = 10)

        self.l2 = Label(self.w, text= "email add", font= "tahoma 14 normal")
        self.l2.place(x = 10, y = 60)
        self.v2 = StringVar()
        self.e2 = Entry(self.w, font = "tahoma 14 normal", textvariable= self.v2)
        self.e2.place(x = 110, y = 60)

        self.b1 = Button(text= "save in xml", font = "tahoma 14 normal", bg= "green", fg= "white", width= 9, command= self.save)
        self.b1.place(x = 10, y = 110)
    
        self.b2 = Button(text= "show all", font = "tahoma 14 normal", bg= "green", fg= "white", width= 9, command= self.show_all)
        self.b2.place(x = 115, y = 110)

        self.b3 = Button(text= "statistic", font = "tahoma 14 normal", bg= "green", fg= "white", width= 9, command= self.statistic)
        self.b3.place(x = 220, y = 110)

    def clear(self):
        '''clear all'''
        self.v1.set('')
        self.v2.set('')
    
    def ex_page(self, text, tit):
        """make extra page"""
        win = Tk()
        win.title(tit)
        Label(win,text = text, font = "tahoma 14 normal").pack()
        Button(win,text= "ok", font="tahoma 14 normal", bg= "green", fg= "white", command= win.destroy).pack()

    def save(self):
        '''check part of name and email'''
        nam = self.v1.get()
        email = self.v2.get()
        self.f = open("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\emai_domains.txt", 'r')
        self.domains = [i.strip() for i in self.f.readlines()]
        self.f.close()
        if nam == "" and email == '':
            return

        if "@" not in email:
            self.clear()
            self.ex_page("your entried email address is wrong!", "ERROR")
            return 
        domain_entry = email[email.index('@')+1:]
        print(domain_entry  in self.domains)
        if domain_entry not in self.domains:
            self.clear()
            self.ex_page("we can not find the your entry domain", "ERROR")
            return

        if exists('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt') != True:
            txt_file = open('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt', 'w')

        else:
            txt_file = open('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt', 'r')
            l = txt_file.readlines()
            for i in range(len(l)):
                if l[i].split(',')[1].strip() == email:
                    self.clear()
                    self.ex_page("one email like this is exists please choose an other one!", "ERROR")
                    return

            txt_file.seek(len(txt_file.read()))
            txt_file.close()
            txt_file = open('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt', 'a')

        
        txt_file.write(nam + ',' +email + '\n')
        txt_file.close()
        self.clear()
        self.xml_creat()

    def xml_creat(self):
        '''creat xml file by txt file help'''
        txt_file = open('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt', 'r')
        lst = txt_file.readlines()
        
        self.xm = Document()
        self.root = self.xm.createElement("all_data") 
        self.xm.appendChild(self.root)
        for i in range(len(lst)):
            self.nun = self.xm.createElement(f"n_{i + 1}")
            self.root.appendChild(self.nun)

            self.n = self.xm.createElement("name")
            self.nun.appendChild(self.n)
            self.emaiil = self.xm.createElement("email")
            self.nun.appendChild(self.emaiil)

            text_name = self.xm.createTextNode(lst[i].split(',')[0].strip())
            self.n.appendChild(text_name)

            text_email = self.xm.createTextNode(lst[i].split(',')[1].strip())
            self.emaiil.appendChild(text_email)

 
        fil = open('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.xml', 'w')
        fil.write(self.xm.toprettyxml(indent= '     '))
        fil.close()     

    def show_all(self):
        """show all element"""
        if exists('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt') == True:
            self.f = open("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt", 'r')
            l = [i.strip() for i in self.f.readlines()]
            self.f.close()
            self.tablee(l, "emails list")
        
    def tablee(self,lst, name):
        """shows all elemen name email email_name_part email_domain part"""
        all_ = ''
        print(lst)
        for i in range(len(lst)):
            x = ''
            l = lst[i].split(',')
            f = l[1].split('@')
            all_ += f"name is: {l[0]}\temail is: {l[1]}\temail name is: {f[0]}\temal domain is: {f[1]}\n\n"
        w = Tk()
        w.title(name)
        Label(w, text= all_, font = "tahoma 14 normal").pack()
        Button(w,text= "ok", font="tahoma 14 normal", bg= "green", fg= "white", command= w.destroy).pack()

    def statistic(self):
        '''access to usage statics of user from this domains'''

        if exists('E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt') == True:
            self.f = open("E:\python.abresan\exsetsise_at_all\db_tkinter_objoriented\Email_Slicer\Email_Slicer.txt", 'r')
            lst = []
            l = [i.strip() for i in self.f.readlines()]
            for i in range(len(l)):
                lf = l[i].split(',')
                f = lf[1].split('@')
                lst.append(f[1])
            dic = {}
            for i in lst:
                if i not in dic.keys():
                    dic[i] = lst.count(i)
            keyy, valuee = [i for i in dic.keys()], [i for i in dic.values()]
            summ = sum(valuee)
            meeans = [i** 100 / summ for i in valuee]
            lst__ = [f"{keyy[i]} : {meeans[i]}" for i in range(len(dic))]
            w = Tk()
            Label(w, text= '\n\n'.join(lst__), font= "tahoma 14 normal").pack()
            Button(w, text= "Ok", font="tahoma 14 normal", command= w.destroy)

        
          

w = Tk()
Email_Slicer(w)
w.mainloop()
        