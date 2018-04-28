# Define the remove_duplicates function
countries = ['india', 'australia', 'croatia', 'usa', 'pakistan', 'australia', 'india']
new_data = []

def remove_duplicates(countries):
    for country in countries:
        if country not in new_data:
        	new_data.append(country)
    y = sorted(new_data)
    print(y)
    for element in y:
       print (element)
    
remove_duplicates(countries)
     