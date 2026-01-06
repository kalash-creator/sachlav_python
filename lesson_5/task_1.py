contacts={}
contacts["contact_1"]={
    "name":"Анна Ивановна",
    "phone": "+79001234567",
    "email": "anna.ivanov@example.com"}
contacts["contact_2"]={
    "name":"Петр Сидоров",
    "phone": "+79119876543",
    "email": "petr.sidorov@example.com"}
print(contacts["contact_1"])
contacts["contact_2"]["phone"]="+79225551122"
contacts["contact_1"]["address"]="г.Москва, ул. Пушкина, дом 10"
contacts["contact_2"].pop("email")
print(contacts)