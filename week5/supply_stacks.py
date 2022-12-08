def task1():
    with open(f'input/supply_stacks.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        stacks = [[] for i in range(9)]
        stack_config = sanitized_input[:8][::-1]
        for i in range(9):
            for level in stack_config:
                if level[4*i+1] != ' ':
                    stacks[i].append(level[4*i+1])

        commands = sanitized_input[10:]
        for command in commands:
            tokens = command.split(' ')
            count = int(tokens[1])
            src = int(tokens[3])-1
            dest = int(tokens[5])-1

            for i in range(count):
                tmp = stacks[src].pop()
                stacks[dest].append(tmp)

        top_elements = ""
        for stack in stacks:
            top_elements += stack.pop()

        print(top_elements)


def task2():
    with open(f'input/supply_stacks2.txt', 'r') as input:
        sanitized_input = [x.replace('\n', '') for x in input.readlines()]
        stacks = [[] for i in range(9)]
        stack_config = sanitized_input[:8][::-1]
        for i in range(9):
            for level in stack_config:
                if level[4*i+1] != ' ':
                    stacks[i].append(level[4*i+1])

        commands = sanitized_input[10:]
        for command in commands:
            tokens = command.split(' ')
            count = int(tokens[1])
            src = int(tokens[3])-1
            dest = int(tokens[5])-1
            print(stacks)
            tmp = stacks[src][-count:]
            del stacks[src][-count:]
            for i in tmp:
                stacks[dest].append(i)

        top_elements = ""
        for stack in stacks:
            top_elements += stack.pop()

        print(top_elements)


task1()
task2()
