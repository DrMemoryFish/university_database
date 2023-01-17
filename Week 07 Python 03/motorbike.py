motorbike_value = 2000 #£
price_decrease = 0.1 #%
years = 0
year_s = "year"
price_boundary = 1000

while motorbike_value >= price_boundary:
    years += 1
    if years > 1:
         years_name = "years"
    else:
        years_name = "year"
    print(f"after {years} {year_s}, the price of the motorbike will be £{motorbike_value}")
    motorbike_value = motorbike_value * (1 - price_decrease)