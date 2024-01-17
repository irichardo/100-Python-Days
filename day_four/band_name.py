import random

# Get Name from Cat
cat_name = input("What is your cat's name?: ")
# Get City name
city_name = input("What is the name of the city you grew up in?: ")
# options for band name
band_name_dictionary = [
    f"The incredible {cat_name} from {city_name}",
    f"The amazing {cat_name} from {city_name}",
    f"The fantastic {cat_name} from {city_name}",
]

band_name = random.choice(band_name_dictionary)

print(band_name)
