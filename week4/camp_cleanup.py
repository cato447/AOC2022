def task1():
    with open(f'input/camp_cleanup.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        sum = 0
        for pair in sanitized_input:
            first_elve, second_elve = pair.split(',')
            lower_first_elve, upper_first_elve = first_elve.split('-')
            lower_second_elve, upper_second_elve = second_elve.split('-')

            #first in second
            if (int(lower_first_elve) >= int(lower_second_elve) and int(upper_first_elve) <= int(upper_second_elve)):
                sum +=1
            
            #second in first
            elif (int(lower_first_elve) <= int(lower_second_elve) and int(upper_first_elve) >= int(upper_second_elve)):
                sum += 1

        print(sum)

def overlap(start1, end1, start2, end2):
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )

def task2():
    with open(f'input/camp_cleanup2.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        sum = 0
        for pair in sanitized_input:
            first_elve, second_elve = pair.split(',')
            lower_first_elve, upper_first_elve = first_elve.split('-')
            lower_second_elve, upper_second_elve = second_elve.split('-')

            first_elve = range(int(lower_first_elve), int(upper_first_elve))
            second_elve = range(int(lower_second_elve), int(upper_second_elve))

            if(overlap(int(lower_first_elve), int(upper_first_elve), int(lower_second_elve), int(upper_second_elve))):
                sum +=1


        print(sum)

task1()
task2()