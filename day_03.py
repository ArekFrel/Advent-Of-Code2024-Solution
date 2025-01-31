import re

DAY = __file__[-5:-3]

SOLVE_PART = 2
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
            signs = line.split("don't()")
            for i, val in enumerate(signs, start=1):
                if i > 1 and 'do()' in val:
                    do_index = val.index('do()')
                    val = val[do_index + 3:]
                if i > 1 and 'do()' not in val:
                    continue
                do_mul = val.split('mul(')
                for do in do_mul:
                    if re.search(r"\d+,\d+\)", do) is not None:
                        par_ind = do.index(')')
                        try:
                            num1, num2 = do[0:par_ind].split(',')
                            result += int(num1) * int(num2)
                        except ValueError:
                            continue
                        print(num1,  num2)
    print(f'Result of DAY {DAY}, part {SOLVE_PART} is {result}')


def main():
    match SOLVE_PART:
        case 1:
            solve()
        case 2:
            solve2()


if __name__ == '__main__':
    main()
