# email slicer
Email Slicer is nothing but just a tool which will take an email id as an input and will perform slicing operations on it to return the username and the domain of the email id.

in this project I try write it graphical at the first I import the libraries that we will use: 1) os.path -> for checking the one page is exist or not 2) tkinter -> for make the grafical place 3) xml.dom.minidom -> for the xml file

then I creating the class for do every process in object oriented way

in def init has writen the graphical inputs for take name and email name and sum button for save in xml, show all emails that saved, statistic for showing the mean of usage of domains

def clear will make empity the input boxes

def ex_page for showing the notfication

def save in this part check that the field was fill up and the entered email is ok or not if the text file not exist open it, else open the file if the email is saved before show the error else write in the file

def xml_creat for creat the xml file from the text file

def show_all for show all element that save in text file

def table for show graphical all email that find from the text file

delf statistic for find the mean of the usage all email domain
