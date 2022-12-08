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
            print(f"{char} = {value}")

            sum += value
    
    print(sum)


task1()
