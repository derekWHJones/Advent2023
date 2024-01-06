import re

def main():
    with open("input.txt", encoding="utf-8") as f:
        data = f.read()

#    data = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
#Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
#Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
#Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
#Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
#Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
    inputs = list(filter(lambda word : len(word) >= 2, data.split('\n')))

    card_num = 0

    for card in inputs:
        card_num = parse_card_correct(card)

    total = 0
    for i in range(1, card_num + 1):
        total += card_dict[i]

    print(total)
    print(card_dict)

card_dict = {}

def parse_card(card):
    card_and_nums = card.split(':')
    card_num = int(re.search(r'(\d)+', card_and_nums[0]).group(0))
    winning_nums = list(map(lambda num: int(num), filter(lambda num: len(num) > 0, card_and_nums[1].split('|')[0].split(' '))))
    card_nums = list(map(lambda num: int(num), filter(lambda num: len(num) > 0, card_and_nums[1].split('|')[1].split(' '))))

    points = 0

    for num in card_nums:
        if num in winning_nums:
            points = 1 if points == 0 else points * 2

    return points


def parse_card_correct(card):
    card_and_nums = card.split(':')
    card_num = int(re.search(r'(\d)+', card_and_nums[0]).group(0))

    if card_num in card_dict.keys():
        card_dict[card_num] += 1
    else:
        card_dict[card_num] = 1

    winning_nums = list(map(lambda num: int(num), filter(lambda num: len(num) > 0, card_and_nums[1].split('|')[0].split(' '))))
    card_nums = list(map(lambda num: int(num), filter(lambda num: len(num) > 0, card_and_nums[1].split('|')[1].split(' '))))

    points = 0

    for num in card_nums:
        if num in winning_nums:
            points += 1
    print(card_num, points)
    for i in range(1, points + 1):
        if card_num + i in card_dict.keys():
            card_dict[card_num + i] += card_dict[card_num]
        else:
            card_dict[card_num + i] = card_dict[card_num]

    return card_num

if __name__ == '__main__':
    main()