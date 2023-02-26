countries = input().split(', ')
capitals = input().split(', ')

dict_countries_capitals = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in dict_countries_capitals.items():
    print(f'{country} -> {capital}')
