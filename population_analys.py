import json


from country_codes import get_country_code

filename = 'Data/population_data.json'
with open(filename) as pop_file:
    pop_data = json.load(pop_file)

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            print(country_code + ": " + str(population))
        else:
            print('ERROR - ' + country_name)
