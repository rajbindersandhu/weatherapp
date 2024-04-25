from tkinter import Tk, Entry, Button, Label
from controler import Controler

def start_window():
    root = Tk()
    root.geometry("400x400")
    root.title("Weather App")

    weather_controler = Controler(root)

    label = Label(root, text="Weather Support", font=("Helvetica", 14))
    label.grid(row=0, column=0, columnspan=2)

    entry = Entry(root, fg='gray', font=("Helvetica", 14), bd=2, relief="solid")
    entry.insert(0, "Enter a city name")
    entry.grid(row=1, column=1, padx=10, pady=5)

    weather_controler.input_binder(entry)
    # entry.bind("<FocusIn>", on_entry_click)
    # entry.bind("<FocusOut>", on_focusout)

    temp_label = Label(root, text="No data...", font=("Helvetica", 14), padx=5)
    feels_label = Label(root, text="")
    weather_condition_label = Label(root, text="")

    display_weather_button = Button(root, text="Get weather", font=("Helvetica", 10), bg="blue", fg="white", padx=10, pady=5, borderwidth=2, relief="raised", command=lambda: weather_controler.display_weather(temp_label, feels_label, weather_condition_label))

    display_weather_button.grid(row=1, column=0, padx=10, pady=5)
    temp_label.grid(row=3, column=0)
    feels_label.grid(row=4, column=0)
    weather_condition_label.grid(row=5, column=0, columnspan=2)

    root.mainloop()

