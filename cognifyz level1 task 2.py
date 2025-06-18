import tkinter as tk
from tkinter import ttk, messagebox

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = selected_unit.get()

        if unit == "Celsius":
            converted = (temp * 9/5) + 32
            result = f"{temp}°C = {round(converted, 2)}°F"
        elif unit == "Fahrenheit":
            converted = (temp - 32) * 5/9
            result = f"{temp}°F = {round(converted, 2)}°C"
        else:
            result = "Invalid unit."

        result_label.config(text=result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# GUI setup
app = tk.Tk()
app.title("Temperature Converter")
app.geometry("350x250")
app.resizable(False, False)

tk.Label(app, text="Enter Temperature:", font=("Arial", 12)).pack(pady=10)
entry_temp = tk.Entry(app, width=20, font=("Arial", 11))
entry_temp.pack()

tk.Label(app, text="Select Unit:", font=("Arial", 12)).pack(pady=10)
selected_unit = tk.StringVar(value="Celsius")
unit_dropdown = ttk.Combobox(app, textvariable=selected_unit, values=["Celsius", "Fahrenheit"], state="readonly", font=("Arial", 11))
unit_dropdown.pack()

tk.Button(app, text="Convert", command=convert_temperature, font=("Arial", 11)).pack(pady=15)

result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack()

app.mainloop()
