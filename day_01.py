DAY = __file__[-5:-3]
FILE = f'../inputs/input_{DAY}.txt'
# FILE = f'../inputs/test_input_{DAY}.txt'
SOLVE_PART = 2


def main():
    rows = []
    with open(FILE, 'r', encoding='utf-8-sig') as my_input:
        for line in my_input:
            rows.append(line.rstrip())


if __name__ == '__main__':
    main()
