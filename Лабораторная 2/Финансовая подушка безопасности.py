money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0  # номер месяца

while money_capital + salary > spend:  # выполнять пока остаток подушки безопасности
    # и заработная плата в сумме превышают расходы на месяц
    if month == 0:
        money_capital = money_capital + salary - spend
        month += 1
    else:
        spend = spend + (spend * increase)
        money_capital = money_capital + salary - spend
        month += 1
print("Количество месяцев, которое можно протянуть без долгов:", month)
