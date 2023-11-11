import csv
import json
# импортирую модули json и csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
# создаю переменные INPUT_FILENAME и OUTPUT_FILENAME передаю туда
# названия файлов с которыми буду работать виде строки "input.csv"
# и "output.json"


def convention() -> None:
    # создаю программу task указываю в анатации что она возвращает
    # значение None(ничего), функция не принимает никаких значений
    # и не имеет значений по умолчанию
    with open(INPUT_FILENAME) as f:
        # запускаю менеджер контекста, передаю ему агрументы:
        # 1) название файла через переменную INPUT_FILENAME;
        # 2) режим доступа к файлу не указываю (по умолчанию чтение 'r';
        # 3) режим работы не указываю (по умолчанию 't' текстовый);
        # кодировку encoding='...' не указываю;
        # f ("input.csv") рабочий файл
        lines = [line_ for line_ in csv.DictReader(f)]
        # создаю обьект в питоне lines, присваиваю ему список значений line_
        # при помощи list comprehension перебирая циклом for значения line_
        # считаные при помощи класса csv.DictReader из рабочего файла (f)

    with open(OUTPUT_FILENAME, "w") as f:
        # запускаю менеджер контекста, передаю ему агрументы:
        # 1) название файла через переменную OUTPUT_FILENAME;
        # 2) режим доступа к файлу "w" (запись);
        # 3) режим работы не указываю (по умолчанию 't' текстовый);
        # кодировку encoding='...' не указываю;
        # f ("output.json") рабочий файл
        json.dump(lines, f, indent=4)
        # Метод dump позволяет сериализовать данные и записать их в файловый объект.
        # Он принимает два аргумента: данные для сериализации lines и файловый объект,
        # в который данные будут записаны f ("output.json") рабочий файл.
        # Аргумент indent=4 используется для задания количества пробелов,
        # используемых для отступов в форматированном JSON.
        # Аргумент ensure_ascii не указаваю по умолчанию значение ensure_ascii равно True


if __name__ == '__main__':
    # Нужно для проверки откуда запускается программа
    convention()
    # вызываю функцию convention никаких агрументов не передаю

    with open(OUTPUT_FILENAME) as output_f:
        # запускаю менеджер контекста, передаю ему агрументы:
        # 1) название файла через переменную OUTPUT_FILENAME;
        # 2) режим доступа к файлу не указываю (по умолчанию чтение 'r';
        # 3) режим работы не указываю (по умолчанию 't' текстовый);
        # кодировку encoding='...' не указываю;
        # output_f("output.json") рабочий файл
        for line in output_f:
            # циклом for перебераю значения line в рабочем файле output_f
            # !!!???? print(line.rstrip())  метод почему-то не проходит проверку пришлось
            # заменить на print(line, end="")
            print(line, end="")
