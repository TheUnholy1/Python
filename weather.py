import requests
from datetime import datetime
from tkinter import *
import ULTIMATE



def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()




def showWeather():
    api_key = '64f61566457c1a48b4f301389ba59786'
    city_name = city_value.get()
    weather_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")
    if weather_info['cod'] == 200:
        kelvin = 273
        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        global wind_speed
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): " \
                  f"{feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time}" \
                  f" and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"

    tfield.insert(INSERT, weather)

def exit():
    root.destroy()
    ULTIMATE.main()

def main():
    global root
    root = Tk()
    #root.geometry("450x450")
    window_width = 450
    window_height = 450
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    root.geometry(f"{window_width}x{window_height}+{int(x)}+{int(y)}")
    root.resizable(0, 0)
    root.title("Weather")
    global city_value
    city_value = StringVar()
    global city_head
    city_head = Label(root, text='Enter City Name', font='Arial 12 bold').pack(pady=10)
    global inp_city
    inp_city = Entry(root, textvariable=city_value, width=24, font='Arial 14 bold').pack()

    Button(root, command=showWeather, text="Check Weather", font="Arial 10", bg='lightblue', fg='black',
       activebackground="teal", padx=5, pady=5).pack(pady=20)
    
    exitables = Button(root,text="Exit",width=9,fg="white",bg="#282828",font="Arial 15",command=exit)
    exitables.place(x=180,y=370)
    
    global weather_now
    weather_now = Label(root, text="The Weather is:", font='arial 12 bold').pack(pady=10)
    
    
    global tfield
    tfield = Text(root, width=46, height=10)
    tfield.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
