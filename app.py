from tkinder import *
import tkinder as tk
from geopy.geocoders import Nominatim
from tkinder import ttk,messagebox
from timezonefinder import Timezonefinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getweather():
    city=textfield.get()
    
    geolocator=nomiatim(user_agent="geoapiExercises")
    location= geolocator.geocode(city)
    obj=timezonefinder()
    result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=Current_Time)
    name.config(text="CURRENT WEATHER")
    
#weather
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&787a59e4c08f8b20a634a9588d94a8ac"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))  
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))  

    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

except Exception as e:
    messagebox.showerror("Weather App","Invaild Entry!!")

#search box
    search_image=PhotoImage(file="d4705544373301dfa969b6efed52bfc3")
    myimage.place(x=20,y=20)

    textfield=tk.entry(root,justify="center",width=17,font=("poppins".25."bold"))
    textfield.place(x=50,y=40)
    textfield.focus()

    search_icon=PhotoImage(file="search-weather-1182370")
    myimage_icon=button(image=search-weather-1182370,borderwidth=0,cusor="hand2",bg="#404040",command=getweather)
    myimage_icon.place(x=400,y=34)

#logo
    logo_image=photoimage(file="3d-weather-icon-day-with-rain-free-png")
    logo=label(image=logo_image)
    logo.place(x=150,7=100)

#bottom box
    frame_image=photoimage(file="pngtree-blue-helicopter-childrens-toy-airplane-airplane-border-illustration-cartoon-airplane-png-image_453275")
    frame_myimage=label(image=frame_image)
    frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
    name=label(root,font=("arial",15,"bold"))
    name.place(x=30,y=100)
    clock=label(root,font=("Helvetica",20))
    clock.place(x=30,y=130)

#label
    label1=label(root,tect="WIND",font=("Helvetica",15,'bold'),fg="White",bg="#1ab5ef")
    label1.place(x=120,y=400)

    label2=label(root,tect="HUMIDITY",font=("Helvetica",15,'bold'),fg="White",bg="#FF0000")
    label1.place(x=225,y=400)

    label3=label(root,tect="DESCRIPTION",font=("Helvetica",15,'bold'),fg="White",bg="#808080")
    label1.place(x=430,y=400)

    label3=label(root,tect="PRESSURE",font=("Helvetica",15,'bold'),fg="White",bg="#87CEEB")
    label1.place(x=650,y=400)

    t=label(font=("arial",70,"bold"),bg="#66ee91")
    t.place(x=400,y=150)
    c=label(font=("arial",15,'bold'))
    c.place(x=400,y=250)

    w=label(text="...",font=("arial",20,"bold"),bg="#0d9ea3")
    w.place(x=120,y=430)
    h=label(text="...",font=("arial",20,"bold"),bg="#b482bf")
    h.place(x=280,y=430)
    d=label(text="...",font=("arial",20,"bold"),bg="#9c9556")
    d.place(x=450,y=430)
    p=label(text="...",font=("arial",20,"bold"),bg="#cf6b15")
    p.place(x=670,y=430)
    
root.mainloop()