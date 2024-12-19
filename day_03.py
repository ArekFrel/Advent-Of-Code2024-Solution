import re

DAY = __file__[-5:-3]

SOLVE_PART = 1
TEST = False
if TEST:
    FILE = f'./inputs/test_input_{DAY}.txt'
else:
    FILE = f'./inputs/input_{DAY}.txt'


def solve():
    result = 0
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        for line in my_input:
            signs = line.split('mul')
            for val in signs:
                if re.search(r"^\(\d+,\d+\)", val) is not None:
                    par_ind = val.index(')')
                    num1, num2 = val[1:par_ind].split(',')
                    result += int(num1) * int(num2)
                    print(num1,  num2)

    print(f'Result of DAY {DAY}, part {SOLVE_PART} is {result}')


def solve2():
    result = 0
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        for line in my_input:
            signs = line.split("don't")
            for i, val in enumerate(signs):
                enable_index = 0
                if i == 0:
                    enable_index = val.index('do()', 1)

                if re.search(r"^\(\d+,\d+\)", val) is not None:
                    par_ind = val.index(')')
                    num1, num2 = val[1:par_ind].split(',')
                    result += int(num1) * int(num2)
                    print(num1,  num2)

    print(f'Result of DAY {DAY}, part {SOLVE_PART} is {result}')


def main():
    solve()


if __name__ == '__main__':
    main()
