salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # Подушка безопасности
month = 0  # номер месяца

while month < 10:
    if month == 0:
        money_capital = money_capital + salary - spend
        month = month + 1
    else:
        spend = spend + (spend * increase)
        money_capital = money_capital + salary - spend
        month = month + 1
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", abs(round(money_capital, 2)))
