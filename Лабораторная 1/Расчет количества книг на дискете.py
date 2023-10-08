# TODO Найдите количество книг, которое можно разместить на дискете
simvol = 4
stroka = simvol * 25
stranica = stroka * 50
kniga = stranica * 100
# print(type(kniga), kniga)
obemdisketuvbaytax = 1.44 * 1024 * 1024
# print(type(obemdisketuvbaytax), obemdisketuvbaytax)
skolkopomestitsy = obemdisketuvbaytax // kniga
# print(type(skolkopomestitsy), skolkopomestitsy)
otvet = int(skolkopomestitsy)
print("Количество книг, помещающихся на дискету:", otvet)
# не стал убирать команды которые использовал для отображения
# промежуточных этапов, просто закоментировал их. Если нужно удалять, скажите
# в следующий раз удалю.