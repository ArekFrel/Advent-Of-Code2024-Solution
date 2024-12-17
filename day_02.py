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
            nums = [int(x) for x in line.rstrip().split(' ')]
            if SOLVE_PART == 1:
                if is_inc_or_dec(nums) and is_gradual(nums):
                    result += 1
            if SOLVE_PART == 2:
                if is_inc_or_dec(nums) and is_gradual(nums):
                    result += 1
                elif check_one_bad(nums):
                    result += 1
    print(f'Result of DAY {DAY}, part {SOLVE_PART} is {result}')


def check_one_bad(numbers):
    for i in range(0, len(numbers)):
        new_numbers = numbers[0:i] + numbers[i+1:]
        if is_inc_or_dec(new_numbers) and is_gradual(new_numbers):
            return True
    return False


def is_gradual(numbers):

    for i in range(1, len(numbers)):
        if abs(numbers[i-1] - numbers[i]) > 3:
            return False
    return True


def is_inc_or_dec(numbers):
    if any([sorted(numbers, reverse=False) == numbers, sorted(numbers, reverse=True) == numbers]) \
            and [x * numbers.count(x) for x in numbers] == numbers:
        return True
    else:
        return False


def main():
    # numbers = [1, 2, 3, 4, 5, 6]
    # print(is_gradual([1, 2, 3, 7, 8, 9]))
    # print(is_inc_or_dec([1, 2, 3, 5, 6, 7]))
    # # solve()
    solve()


if __name__ == '__main__':
    main()