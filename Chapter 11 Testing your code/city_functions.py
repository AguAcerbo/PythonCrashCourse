#11.1
#def get_city_country(city, country):
#    output = f"{city}, {country}"
#    return output.title()

#11.2
#def get_city_country(city, country, population):
#    output = f"{city}, {country} - population {population}"
#    return output.title()

def get_city_country(city, country, population = ''):
    if population:
        output = f"{city}, {country} - population {population}"
    else:
        output = f"{city}, {country}"
    return output.title()