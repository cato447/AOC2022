def task1():
    with open(f'input/calorie_counting.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        sum = 0
        max = 0
        for i in sanitized_input:
            if i == '':
                max = sum if sum > max else max
                sum = 0
            else:
                sum += int(i)
        print(max)

def task2():
    with open(f'input/calorie_counting2.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        elves = [0]
        elvesIndex = 0
        for input in sanitized_input:
            if input == '':
               elvesIndex += 1 
               elves.append(0)
            else:
                elves[elvesIndex] += int(input)
        
        elves.sort()
        print(sum(elves[-3:]))

task1()
task2()