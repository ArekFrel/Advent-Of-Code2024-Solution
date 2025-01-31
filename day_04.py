DAY = __file__[-5:-3]

SOLVE_PART = 1
TEST = False
if TEST:
    FILE = f'./inputs/test_input_{DAY}.txt'
else:
    FILE = f'./inputs/input_{DAY}.txt'


def solve():
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        pass


def main():
    solve()


if __name__ == '__main__':
    main()