import tkinter as tk
from tkinter import messagebox

#  Calculation Functions 
def wet_volume(length, width, depth):
    return length * width * depth

def dry_volume(wet_vol):
    return wet_vol * 1.54

def material_quantities(dry_vol, c, s, a):
    total = c + s + a
    cement = (c / total) * dry_vol
    sand = (s / total) * dry_vol
    aggregate = (a / total) * dry_vol
    return cement, sand, aggregate

def cement_bags(cement_volume):
    return cement_volume / 0.0347

def water_required(cement_volume, wc_ratio):
    cement_mass = cement_volume * 1440
    return cement_mass * wc_ratio

# GUI Function 
def calculate():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        depth = float(depth_entry.get())
        c = float(cement_ratio_entry.get())
        s = float(sand_ratio_entry.get())
        a = float(aggregate_ratio_entry.get())
        wc_ratio = float(wc_ratio_entry.get())

        wet = wet_volume(length, width, depth)
        dry = dry_volume(wet)
        cement, sand, aggregate = material_quantities(dry, c, s, a)
        bags = cement_bags(cement)
        water = water_required(cement, wc_ratio)

        result_text.set(
            f"Wet Volume: {wet:.3f} m³\n"
            f"Dry Volume: {dry:.3f} m³\n"
            f"Cement Volume: {cement:.3f} m³\n"
            f"Sand Volume: {sand:.3f} m³\n"
            f"Aggregate Volume: {aggregate:.3f} m³\n"
            f"Cement Bags: {bags:.2f}\n"
            f"Water Required: {water:.2f} liters"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Main Window 
root = tk.Tk()
root.title("Concrete Material Calculator")
root.geometry("420x500")
root.resizable(False, False)

# Input Fields 
tk.Label(root, text="Length (m):").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

tk.Label(root, text="Width (m):").pack(pady=5)
width_entry = tk.Entry(root)
width_entry.pack()

tk.Label(root, text="Depth (m):").pack(pady=5)
depth_entry = tk.Entry(root)
depth_entry.pack()

tk.Label(root, text="Cement Ratio:").pack(pady=5)
cement_ratio_entry = tk.Entry(root)
cement_ratio_entry.pack()

tk.Label(root, text="Sand Ratio:").pack(pady=5)
sand_ratio_entry = tk.Entry(root)
sand_ratio_entry.pack()

tk.Label(root, text="Aggregate Ratio:").pack(pady=5)
aggregate_ratio_entry = tk.Entry(root)
aggregate_ratio_entry.pack()

tk.Label(root, text="Water-Cement Ratio:").pack(pady=5)
wc_ratio_entry = tk.Entry(root)
wc_ratio_entry.pack()

# Optional default values
length_entry.insert(0, "4")
width_entry.insert(0, "3")
depth_entry.insert(0, "0.15")
cement_ratio_entry.insert(0, "1")
sand_ratio_entry.insert(0, "2")
aggregate_ratio_entry.insert(0, "4")
wc_ratio_entry.insert(0, "0.5")

# Button 
tk.Button(root, text="Calculate", command=calculate, bg="lightblue").pack(pady=15)

# Result Display
result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left", font=("Arial", 11)).pack(pady=10)

root.mainloop()