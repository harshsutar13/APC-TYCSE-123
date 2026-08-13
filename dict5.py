#5. Create a dictionary of cities and their populations. Remove a specified city from the dictionary.

cities = {
    "mumbai":100,
    "pune":90,
    "kolhapur":90,
    "sangli":80,
    "karad":50
}
print(cities)

key = input("Enter city name to delete: ")
if key in cities:
        del cities[key]
        print("City deleted")

else :
    print("City not found")

print(cities)