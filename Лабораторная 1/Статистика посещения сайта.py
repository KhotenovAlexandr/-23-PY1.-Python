users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
slovar = {
    "Общее количество": "0",
    "Уникальные посещения": "0"

}
obshee = len(users)
slovar["Общее количество"] = obshee
unikalnoe = len(set(users))
slovar["Уникальные посещения"] = unikalnoe


# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
print(slovar)
