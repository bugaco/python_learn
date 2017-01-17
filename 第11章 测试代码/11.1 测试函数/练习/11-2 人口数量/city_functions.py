def get_formatted_city(city, country, population = ''):
    formatted_city = city + ',' + country
    if population:
        formatted_city = formatted_city.title() + ' - population ' + str(population)
    else:
        formatted_city = formatted_city.title()
    return formatted_city