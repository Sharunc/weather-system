from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=8b6d5dc13efd7f526ec4aaf5417100fd").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("WEATHER APP")
win.config(bg="white")
win.geometry("500x570")

name_label = Label(win, text="Weather System", font=("Time New Roman", 30, "bold"))
name_label.place(x=25, y=50, height=50, width=450)

city_name= StringVar()

list_name = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
             "Himachal Pradesh",
             "Jharkhand", "Kerala", "Madhya Pradesh", "Mysore", "Orissa", "Punjab", "Rajasthan", "Uttar Pradesh",
             "West "
             "Bengal"]
com = ttk.Combobox(win, values=list_name, font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)

done_button = Button(win,text="DONE",font=("Time New Roman",20,"bold"),command=data_get)
done_button.place(x=200 ,y=190,height=50,width=100)

w_label = Label(win,text="WEATHER CLIMATE",font=("Time New Roman",15))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)

wb_label=Label(win,text="WEATHER DESCRIPTION",font=("Time New Roman",13))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1=Label(win,text="",font=("Time New Roman",17))
wb_label1.place(x=250,y=330,height=50,width=210)

temp_label=Label(win,text="TEMPERATURE",font=("Time New Roman",17))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1=Label(win,text="",font=("Time New Roman",17))
temp_label1.place(x=250,y=400,height=50,width=210)

per_label=Label(win,text="PRESSURE",font=("Time New Roman",17))
per_label.place(x=25,y=470,height=50,width=210)

per_label1=Label(win,text="",font=("Time New Roman",17))
per_label1.place(x=250,y=470,height=50,width=210)

win.mainloop()
