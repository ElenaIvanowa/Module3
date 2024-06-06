data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_str):
    sum_element = 0
    for i in data_str:
        if isinstance(i, (list, tuple, set)):
            sum_element += calculate_structure_sum(i)
        elif isinstance(i, dict):
            sum_element += calculate_structure_sum(i.items())
        elif isinstance(i, str):
            sum_element += len(i)
        elif isinstance(i, int):
            sum_element += i
    return sum_element

result = calculate_structure_sum(data_structure)
print(result)