list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
kolichestvo = len(list_players)
polovina = int(kolichestvo / 2)

komanda1 = list_players[0: polovina]
komanda2 = list_players[polovina:kolichestvo]

print(komanda1)
print(komanda2)

# Если я правильно понял ваш коментарий. Исправить можно и другими способами,но пока мы их не изучали .
