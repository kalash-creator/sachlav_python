def get_as_float(data_dict, key):
    try:
        result=float(data_dict[key])
        print(f"Успех: Получено число '{result}'")

    except ValueError:
        print(f"Ошибка: Значение по ключу '{key}' нельзя превратить в число!")
    except KeyError:
        print(f"Ошибка: Ключ '{key}' не найден!")

data = {"price": "10.5", "id": "abc"}
get_as_float(data, "price")
get_as_float(data, "id")
get_as_float(data, "amount")