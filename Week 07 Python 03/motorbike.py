year_s = "year"

def calculate_motorbike_value(initial_value, price_decrease, price_boundary):
    initial_value = 2000 #£   
    years = 0
    while initial_value >= price_boundary:
        years += 1
        if years > 1:
            years_name = "years"
        else:
            years_name = "year"
        print(f"after {years} {year_s}, the price of the motorbike will be £{initial_value}")
        initial_value = initial_value * (1 - price_decrease)
        
calculate_motorbike_value(2000, 0.1, 1000)