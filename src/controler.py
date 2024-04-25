from fetch import Fetch
from tkinter import Tk, Entry, Button, Label
from PIL import Image, ImageTk
import io

class Controler:
    def __init__(self, root:Tk):
        self.root = root
        self._request_to = None
        self.input = None
        self.temp_label = None
        self.feels = None
        self.weather_condition = None

    def input_binder(self, input: Entry):
        self.input = input
        self.input.bind("<FocusIn>", self.on_entry_click)
        self.input.bind("<FocusOut>", self.on_focusout)

    def on_entry_click(self, event):
        if self.input.get() == "Enter a city name":
            self.input.delete(0, "end")
            self.input.config(fg="black")
    
    def on_focusout(self, event):
        if self.input.get == "":
            self.input.insert(0, "Enter a city name")
            self.input.config(fg = "gray")

    # Methods triggers on click event, when get tomorrow button is pressed
    def _get_tom_forecast(self, weather_forecast_data, forecast_weather_photo):
        temp =  round((weather_forecast_data["main"]["temp"]), 2)
        self.temp_label.config(text=f"{temp}{chr(176)}C", font=("Helvetica", 25), foreground="blue", background="yellow")
        feels_like = round((weather_forecast_data["main"]["feels_like"]), 2)
        self.feels.config(text=f"Feels Like: {feels_like}{chr(176)}C")
        desc = weather_forecast_data["weather"][0]["main"]
        self.weather_condition.config(text=desc, font=("Helvetica", 20), foreground="blue", background="yellow")
        
        img_label = Label(self.root, image=forecast_weather_photo)
        img_label.image = forecast_weather_photo
        img_label.grid(row=3, column=1, rowspan=2)

    # Methods triggers on click event, when get today button is pressed
    def _get_today_weather(self,weather_data, weather_photo):
        temp =  round((weather_data["main"]["temp"]), 2)
        self.temp_label.config(text=f"{temp}{chr(176)}C", font=("Helvetica", 25), foreground="blue", background="yellow")
        feels_like = round((weather_data["main"]["feels_like"]), 2)
        self.feels.config(text=f"Feels Like: {feels_like}{chr(176)}C")
        desc = weather_data["weather"][0]["main"]
        self.weather_condition.config(text=desc, font=("Helvetica", 20), foreground="blue", background="yellow")

        img_label = Label(self.root, image=weather_photo)
        img_label.image = weather_photo
        img_label.grid(row=3, column=1, rowspan=2)

    

    # Methods triggers on click event, when get weather button is pressed
    def display_weather(self, temp_label:Label, feels: Label, weather_condition: Label):
        input_city = self.input.get()
        self._request_to = Fetch(input_city)
        weather_data = self._request_to.get_weather()
        weather_forecast_data = self._request_to.get_forecast()

        self.temp_label = temp_label
        self.feels = feels
        self.weather_condition = weather_condition
        temp =  round((weather_data["main"]["temp"]), 2)
        temp_label.config(text=f"{temp}{chr(176)}C", font=("Helvetica", 25), foreground="blue", background="yellow")
        feels_like = round((weather_data["main"]["feels_like"]), 2)
        feels.config(text=f"Feels Like: {feels_like}{chr(176)}C")
        desc = weather_data["weather"][0]["main"]
        weather_condition.config(text=desc, font=("Helvetica", 20), foreground="blue", background="yellow")

        image_id = weather_data["weather"][0]["icon"]
        image_data = self._request_to.get_weather_icon(image_id)
        if image_data:
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((150,100), Image.AFFINE)
            weather_photo = ImageTk.PhotoImage(image)

        forecast_image_id = weather_forecast_data["weather"][0]["icon"]
        forecast_image_data = self._request_to.get_weather_icon(forecast_image_id)
        if forecast_image_data:
            forecast_image = Image.open(io.BytesIO(forecast_image_data))
            forecast_image = forecast_image.resize((150,100), Image.AFFINE)
            forecast_weather_photo = ImageTk.PhotoImage(forecast_image)

        img_label = Label(self.root, image=weather_photo)
        img_label.image = weather_photo
        img_label.grid(row=3, column=1, rowspan=2)
            
        today_forecast_button = Button(self.root, text="Today", font=("Helvetica", 10), bg="blue", fg="white", padx=10, pady=5, borderwidth=2, relief="raised", command=lambda: self._get_today_weather(weather_data, weather_photo))
        today_forecast_button.grid(row=2, column=0, padx=10, pady=5)
        tom_forecast_button = Button(self.root, text="Tomorrow", font=("Helvetica", 10), bg="blue", fg="white", padx=10, pady=5, borderwidth=2, relief="raised", command=lambda: self._get_tom_forecast(weather_forecast_data, forecast_weather_photo))
        tom_forecast_button.grid(row=2, column=1, padx=10, pady=5)