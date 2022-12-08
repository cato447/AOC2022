from typing import Tuple


def get_compartments(rucksack: str) -> Tuple[str, str]:
    half = len(rucksack)//2
    return rucksack[:half], rucksack[half:]


def task1():
    with open(f'input/rucksack_reorganization.txt', 'r') as input:
        sum = 0
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        for rucksack in sanitized_input:
            compartmentA, compartmentB = get_compartments(rucksack)
            common_type = set(compartmentA).intersection(compartmentB)
            char = common_type.pop()
            value = ord(char) - ord('A')
            if value < 26:
                value += 26
            else:
                value -= 32
            value += 1

            sum += value

    print(sum)


def task2():
    sum = 0
    with open(f'input/rucksack_reorganization2.txt', 'r') as input:
        sum = 0
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        for i in range(len(sanitized_input)//3):
            a, b, c = sanitized_input[i *
                                      3], sanitized_input[i*3+1], sanitized_input[i*3+2]
            common_type = set(a).intersection(b).intersection(c)
            char = common_type.pop()
            value = ord(char) - ord('A')
            if value < 26:
                value += 26
            else:
                value -= 32
            value += 1

            sum += value
    print(sum)


task1()
task2()
