city=input("Введи 5 различных городов через запятую: ")
city_clean=city.replace(" ", "")
city_list=city_clean.split(",")
print(city_list)
letter="а"
for i in range(5):
    if letter in city_list[i]:
        print(f"{i+1} {city_list[i]} (в этом городе есть 'а')")
    else:
        print(f"{i+1} {city_list[i]}")