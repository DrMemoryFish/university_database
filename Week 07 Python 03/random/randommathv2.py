import math
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import logging
import tkinter as tk
from tkinter import ttk

filepath = None
//
def check_valid_input(width, depth, height, density, cost_per_unit_volume):
    while width <= 0 or depth <= 0 or height <= 0 or density <= 0 or cost_per_unit_volume <= 0:
        raise ValueError("Invalid input. Width, depth, height, density and cost per unit volume must be positive numbers.")

def add_to_database(calculations, dimensions):
    try:
        conn = sqlite3.connect('boxes.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS boxes (width REAL, depth REAL, height REAL, volume REAL, surface_area REAL, diagonal REAL, weight REAL, cost REAL)''')
        c.execute("INSERT INTO boxes VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (dimensions[0], dimensions[1], dimensions[2], calculations["volume"], calculations["surface area"], calculations["diagonal"], calculations["weight"], calculations["cost"]))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError as e:
        logging.error(e)
        print("Error connecting to the database. Please check the database connection.")

def display_calculations(calculations):
    root = tk.Tk()
    root.title("Box Calculations")
    for key, value in calculations.items():
        tk.Label(root, text=key + ": " + str(value)).pack()
    tk.Button(root, text="Save to file", command=lambda: save_to_file(calculations)).pack()
    tk.Button(root, text="Save to database", command=lambda: add_to_database(calculations, dimensions)).pack()
    tk.Button(root, text="Quit", command=root.destroy).pack()
    root.mainloop()

def save_to_file(calculations):
    filepath = filedialog.asksaveasfilename(defaultextension=".txt")
    if filepath:
        write_calculations_to_file(filepath, calculations)
    messagebox.showinfo("Success", "Calculations saved to file successfully.")

def get_dimensions():
    if filepath:
        return read_dimensions_from_file(filepath)
    else:
        return [float(input("Enter the width of the box: ")), float(input("Enter the depth of the box: ")), float(input("Enter the height of the box: "))]

def calculate_volume_wrapper():
    dimensions = get_dimensions()
    calculations = {"volume": calculate_volume(dimensions[0], dimensions[1], dimensions[2])}
    display_calculations(calculations)

def calculate_surface_area_wrapper():
    dimensions = get_dimensions()
    calculations = {"surface area": calculate_surface_area(dimensions[0], dimensions[1], dimensions[2])}
    display_calculations(calculations)

def calculate_diagonal_wrapper():
    dimensions = get_dimensions()
    calculations = {"diagonal": calculate_diagonal(dimensions[0], dimensions[1], dimensions[2])}
    display_calculations(calculations)

def calculate_weight_wrapper():
    dimensions = get_dimensions()
    density = float(input("Enter the density of the material the box is made of: "))
    calculations = {"weight": calculate_weight(dimensions[0], dimensions[1], dimensions[2], density)}
    display_calculations(calculations)

def calculate_cost_wrapper():
    dimensions = get_dimensions()
    cost_per_unit_volume = float(input("Enter the cost per unit volume of the material the box is made of: "))
    calculations = {"cost": calculate_cost(dimensions[0], dimensions[1], dimensions[2], cost_per_unit_volume)}
    display_calculations(calculations)

def calculate_volume(volume_page, width_v, depth_v, height_v):
    try:
        width_v = float(width_v)
        depth_v = float(depth_v)
        height_v = float(height_v)
        volume = width_v * depth_v * height_v
        ttk.Label(volume_page, text="Volume: " + str(volume)).pack()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid numbers for width, depth, and height.")

def calculate_surface_area(surface_area_page, width_sa, depth_sa, height_sa):
    try:
        width_sa = float(width_sa)
        depth_sa = float(depth_sa)
        height_sa = float(height_sa)
        surface_area = 2*(width_sa*depth_sa + width_sa*height_sa + depth_sa*height_sa)
        ttk.Label(surface_area_page, text="Surface Area: " + str(surface_area)).pack()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid numbers for width, depth, and height.")

def calculate_diagonal(diagonal_page, width_d, depth_d, height_d):
    try:
        width_d = float(width_d)
        depth_d = float(depth_d)
        height_d = float(height_d)
        diagonal = math.sqrt(width_d**2 + depth_d**2 + height_d**2)
        ttk.Label(diagonal_page, text="Diagonal: " + str(diagonal)).pack()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid numbers for width, depth, and height.")

def calculate_weight(weight_page, width_w, depth_w, height_w, density):
    try:
        width_w = float(width_w)
        depth_w = float(depth_w)
        height_w = float(height_w)
        density = float(density)
        weight = width_w * depth_w * height_w * density
        ttk.Label(weight_page, text="Weight: " + str(weight) + "kg").pack()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid numbers for width, depth, height and density.")

def calculate_cost(cost_page, width_c, depth_c, height_c, cost_per_unit_volume):
    try:
        width_c = float(width_c)
        depth_c = float(depth_c)
        height_c = float(height_c)
        cost_per_unit_volume = float(cost_per_unit_volume)
        volume = width_c * depth_c * height_c
        cost = volume * cost_per_unit_volume
        ttk.Label(cost_page, text="Cost: $" + str(cost)).pack()
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid numbers for width, depth, height and cost per unit volume.")

def display_menu():
    root = tk.Tk()
    root.title("Box Calculator")
    root.geometry("500x500")
    
    # Create a new style and configure it
    style = ttk.Style()
    style.configure("BW.TLabel", background="#F0F0F1")
    style.configure("BW.TFrame", background="#F1F0F0")
    style.configure("BW.TButton", background="#F0F1F0")

    # Create a notebook to hold the pages
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # Create a page for volume calculation
    volume_page = ttk.Frame(notebook, style="BW.TFrame")
    notebook.add(volume_page, text="Volume")
    width_label = ttk.Label(volume_page, text="Width:", style="BW.TLabel")
    width_label.pack()
    width_entry = ttk.Entry(volume_page)
    width_entry.pack()
    depth_label = ttk.Label(volume_page, text="Depth:", style="BW.TLabel")
    depth_label.pack()
    depth_entry = ttk.Entry(volume_page)
    depth_entry.pack()
    height_label = ttk.Label(volume_page, text="Height:", style="BW.TLabel")
    height_label.pack()
    height_entry = ttk.Entry(volume_page)
    height_entry.pack()
    calculate_volume_button = ttk.Button(volume_page, text="Calculate", command=lambda: calculate_volume(volume_page, width_entry.get(), depth_entry.get(), height_entry.get()))
    calculate_volume_button.pack()

    # Create a page for surface area calculation
    surface_area_page = ttk.Frame(notebook, style="BW.TFrame")
    notebook.add(surface_area_page, text="Surface Area")
    width_label = ttk.Label(surface_area_page, text="Width:", style="BW.TLabel")
    width_label.pack()
    width_entry = ttk.Entry(surface_area_page)
    width_entry.pack()
    depth_label = ttk.Label(surface_area_page, text="Depth:", style="BW.TLabel")
    depth_label.pack()
    depth_entry = ttk.Entry(surface_area_page)
    depth_entry.pack()
    height_label = ttk.Label(surface_area_page, text="Height:", style="BW.TLabel")
    height_label.pack()
    height_entry = ttk.Entry(surface_area_page)
    height_entry.pack()
    calculate_surface_area_button = ttk.Button(surface_area_page, text="Calculate", command=lambda: calculate_surface_area(surface_area_page, width_entry.get(), depth_entry.get(), height_entry.get()))
    calculate_surface_area_button.pack()
    
    # Create a page for diagonal calculation
    diagonal_page = ttk.Frame(notebook, style="BW.TFrame")
    notebook.add(diagonal_page, text="Diagonal")
    width_label = ttk.Label(diagonal_page, text="Width:", style="BW.TLabel")
    width_label.pack()
    width_entry = ttk.Entry(diagonal_page)
    width_entry.pack()
    depth_label = ttk.Label(diagonal_page, text="Depth:", style="BW.TLabel")
    depth_label.pack()
    depth_entry = ttk.Entry(diagonal_page)
    depth_entry.pack()
    height_label = ttk.Label(diagonal_page, text="Height:", style="BW.TLabel")
    height_label.pack()
    height_entry = ttk.Entry(diagonal_page)
    height_entry.pack()
    calculate_diagonal_button = ttk.Button(diagonal_page, text="Calculate", command=lambda: calculate_diagonal(diagonal_page, width_entry.get(), depth_entry.get(), height_entry.get()))
    calculate_diagonal_button.pack()
    
    # Create a page for weight calculation
    weight_page = ttk.Frame(notebook, style="BW.TFrame")
    notebook.add(weight_page, text="Weight")
    width_label = ttk.Label(weight_page, text="Width:", style="BW.TLabel")
    width_label.pack()
    width_entry = ttk.Entry(weight_page)
    width_entry.pack()
    depth_label = ttk.Label(weight_page, text="Depth:", style="BW.TLabel")
    depth_label.pack()
    depth_entry = ttk.Entry(weight_page)
    depth_entry.pack()
    height_label = ttk.Label(weight_page, text="Height:", style="BW.TLabel")
    height_label.pack()
    height_entry = ttk.Entry(weight_page)
    height_entry.pack()
    density_label = ttk.Label(weight_page, text="Density:", style="BW.TLabel")
    density_label.pack()
    density_entry = ttk.Entry(weight_page)
    density_entry.pack()
    calculate_weight_button = ttk.Button(weight_page, text="Calculate", command=lambda: calculate_weight(weight_page, width_entry.get(), depth_entry.get(), height_entry.get(), density_entry.get()))
    calculate_weight_button.pack()
    
    # Create a page for cost calculation
    cost_page = ttk.Frame(notebook, style="BW.TFrame")
    notebook.add(cost_page, text="Cost")
    width_label = ttk.Label(cost_page, text="Width:", style="BW.TLabel")
    width_label.pack()
    width_entry = ttk.Entry(cost_page)
    width_entry.pack()
    depth_label = ttk.Label(cost_page, text="Depth:", style="BW.TLabel")
    depth_label.pack()
    depth_entry = ttk.Entry(cost_page)
    depth_entry.pack()
    height_label = ttk.Label(cost_page, text="Height:", style="BW.TLabel")
    height_label.pack()
    height_entry = ttk.Entry(cost_page)
    height_entry.pack()
    cost_per_unit_volume_label = ttk.Label(cost_page, text="Cost per Unit Volume:", style="BW.TLabel")
    cost_per_unit_volume_label.pack()
    cost_per_unit_volume_entry = ttk.Entry(cost_page)
    cost_per_unit_volume_entry.pack()
    calculate_cost_button = ttk.Button(cost_page, text="Calculate", command=lambda: calculate_cost(cost_page, width_entry.get(), depth_entry.get(), height_entry.get(), cost_per_unit_volume_entry.get()))
    calculate_cost_button.pack()

    root.mainloop()

def read_dimensions_from_file(filepath):
    dimensions = []
    while True:
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    dimensions.append(float(line))
            file.close()
            return dimensions
        except ValueError as e:
            logging.error(e)
            print("Invalid input. Please enter valid dimensions.")
            filepath = filedialog.askopenfilename()

def write_calculations_to_file(filepath, calculations):
    if not filepath:
        return
    with open(filepath, 'w') as file:
        file.write("Calculations:\n")
        for key, value in calculations.items():
            file.write("{}: {}\n".format(key, value))

if __name__ == "__main__":
    print("Welcome to the Box Dimension Calculator!")
    filepath = None
    display_menu()

    try:
        dimensions = []
        filepath = None
        method = check_input_method()
        if method == 'i':
            dimensions = [float(input("Enter the width of the box: ")), float(input("Enter the depth of the box: ")), float(input("Enter the height of the box: "))]
        elif method == 'f':
            filepath = filedialog.askopenfilename()
            if filepath:
                dimensions = read_dimensions_from_file(filepath)
        density = float(input("Enter the density of the material the box is made of: "))
        cost_per_unit_volume = float(input("Enter the cost per unit volume of the material the box is made of: "))
        check_valid_input(dimensions[0], dimensions[1], dimensions[2], density, cost_per_unit_volume)
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    else:
        width, depth, height = dimensions
        volume = calculate_volume(width, depth, height)
        surface_area = calculate_surface_area(width, depth, height)
        diagonal = calculate_diagonal(width, depth, height)
        weight = calculate_weight(width, depth, height, density)
        cost = calculate_cost(width, depth, height, cost_per_unit_volume)
        calculations = {"volume": volume, "surface area": surface_area, "diagonal": diagonal, "weight": weight, "cost": cost}
        display_calculations(calculations)