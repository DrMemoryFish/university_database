import math
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import logging

def calculate_volume(width, depth, height):
    return width * depth * height

def calculate_surface_area(width, depth, height):
    return 2 * (width * depth + depth * height + width * height)

def calculate_diagonal(width, depth, height):
    return math.sqrt(width**2 + depth**2 + height**2)

def calculate_weight(width, depth, height, density):
    return calculate_volume(width, depth, height) * density

def calculate_cost(width, depth, height, cost_per_unit_volume):
    return calculate_volume(width, depth, height) * cost_per_unit_volume

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

filepath = None

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

def check_input_method():
    while True:
        try:
            method = input("Enter 'i' to input dimensions manually or 'f' to read from file: ")
            if method == 'i':
                return 'i'
            elif method == 'f':
                return 'f'
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter either 'i' or 'f'.")

if __name__ == "__main__":
    print("Welcome to the Box Dimension Calculator!")

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