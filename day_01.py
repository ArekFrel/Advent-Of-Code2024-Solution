DAY = __file__[-5:-3]

SOLVE_PART = 2
TEST = True
if TEST:
    FILE = f'./inputs/input_{DAY}.txt'
else:
    FILE = f'./inputs/test_input_{DAY}.txt'


def solve():
    first_list, second_list = [], []

    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        for line in my_input:
            first, second = line.rstrip().split('   ')
            first_list.append(int(first))
            second_list.append(int(second))

    if SOLVE_PART == 1:
        first_list.sort()
        second_list.sort()
        result = 0
        while first_list:
            result += abs(first_list.pop() - second_list.pop())
        print(f'Result of DAY {DAY}, part {SOLVE_PART} is {result}')

    if SOLVE_PART == 2:
        result = 0
        for num in first_list:
            result += num * second_list.count(num)
        print(f'Result of DAY {DAY}, part {SOLVE_PART} is {result}')


def main():
    solve()


if __name__ == '__main__':
    main()
