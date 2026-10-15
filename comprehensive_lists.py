numeros = [1, 2, 3, 4, 5]

list_map = list(map(lambda x: x ** 2, numeros))

print(list_map)

list_map_comprehensive = [ x ** 2 for x in numeros ]

print(list_map_comprehensive)

list_filter = list(filter(lambda x: x%2 == 0, numeros))

print(list_filter)

list_filter_comprehensive = [ x ** 2 for x in numeros if x%2 == 0 ]

print(list_filter_comprehensive)