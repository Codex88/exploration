# finding and extracting strings from a dataset

data = 'From stephen.marquard@uct.ac.za Sat Jan 5   09:14:16    2008'
print(data)

at_symbol_position = data.find("@")
print(at_symbol_position)

trail_space_position = data.find(" ", at_symbol_position)
print(trail_space_position)

hostname = data[at_symbol_position+1:trail_space_position]
print(hostname)
