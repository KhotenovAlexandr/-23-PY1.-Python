def find_common_participants(group_a, group_b, separator=","):
    group_a_split = group_a.split(separator)
    group_b_split = group_b.split(separator)

    group_a_split_set = set(group_a_split)
    group_b_split_set = set(group_b_split)

    group_ab_list = list(group_a_split_set.intersection(group_b_split_set))
    group_ab_list.sort()
    return group_ab_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(f"{find_common_participants(participants_first_group, participants_second_group)}")