

def main():
    with open("input.txt", encoding="utf-8") as f:
        data = f.read()

    inputs = list(filter(lambda word : len(word) >= 2, data.split('\n')))

#    str_inputs = '''467..114..
#...*......
#..35..633.
#......#...
#617*......
#.....+.58.
#..592.....
#......755.
#...$.*....
#.664.598..'''
#    inputs = list(filter(lambda word : len(word) >= 2, str_inputs.split('\n')))

    full_array = []
    for line in inputs:
        full_array.append(list(line))

    gears = parse_board_for_gears(full_array)
    print(gears)
    #part_nums = parse_board(full_array)
#
    #total = 0
    #for num in part_nums:
    #    total += num
    #
    #print(total)

top = {(-1, -1), (0, -1), (1, -1)}
bottom = {(-1, 1), (0, 1), (1, 1)}
left = {(-1, -1), (-1, 0), (-1, 1)}
right = {(1, -1), (1, 0), (1, 1)}
full_check = {(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, 1), (-1, -1)}


def parse_board(full_array):
    adj_board = [[0 for i in full_array[j]] for j in range(len(full_array))]
    for y in range(len(full_array)):
        for x in range(len(full_array[y])):
            if full_array[y][x] not in '1234567890':
                continue
            top_check = top.union(bottom)
            side_check = left.union(right)
            if x == 0:
                side_check = side_check - left
                top_check = top_check - left
            if x == (len(full_array[y]) - 1):
                side_check = side_check - right
                top_check = top_check - right
            if y == 0:
                top_check = top_check - top
                side_check = side_check - top
            if y == (len(full_array) - 1):
                top_check = top_check - bottom
                side_check = side_check - bottom
            for test in side_check:
                if full_array[y + test[1]][x + test[0]] not in '1234567890.':
                    adj_board[y][x] = 1
                    break
            for test in top_check:
                if full_array[y + test[1]][x + test[0]] not in '.':
                    adj_board[y][x] = 1
                    break

    part_nums = []
    for y in range(len(full_array)):
        for x in range(len(full_array[y])):
            if adj_board[y][x] == 0:
                continue
            new_num = full_array[y][x]
            current_char = full_array[y][x]
            tmp_x = x

            while current_char in '1234567890' and (tmp_x - 1) >= 0:
                tmp_x -= 1
                current_char = full_array[y][tmp_x]
                if current_char in '1234567890':
                    new_num = current_char + new_num
                    adj_board[y][tmp_x] = 0

            current_char = full_array[y][x]
            tmp_x = x

            while current_char in '1234567890' and (tmp_x + 1) < (len(full_array[y])):
                tmp_x += 1
                current_char = full_array[y][tmp_x]
                if current_char in '1234567890':
                    new_num += current_char
                    adj_board[y][tmp_x] = 0
            part_nums.append(int(new_num))

    print(part_nums)
    return part_nums

def parse_board_for_gears(full_array):
    adj_board = [[0 for i in full_array[j]] for j in range(len(full_array))]
    for y in range(len(full_array)):
        for x in range(len(full_array[y])):
            if full_array[y][x] in '*':
                adj_board[y][x] = 2
            if full_array[y][x] not in '1234567890':
                continue
            top_check = top.union(bottom)
            side_check = left.union(right)
            if x == 0:
                side_check = side_check - left
                top_check = top_check - left
            if x == (len(full_array[y]) - 1):
                side_check = side_check - right
                top_check = top_check - right
            if y == 0:
                top_check = top_check - top
                side_check = side_check - top
            if y == (len(full_array) - 1):
                top_check = top_check - bottom
                side_check = side_check - bottom
            for test in side_check:
                if full_array[y + test[1]][x + test[0]] in '*':
                    adj_board[y][x] = 1
                    break
            for test in top_check:
                if full_array[y + test[1]][x + test[0]] in '*':
                    adj_board[y][x] = 1
                    break

    for y in range(len(full_array)):
        for x in range(len(full_array[y])):
            if adj_board[y][x] == 0:
                continue
            new_num = full_array[y][x]
            current_char = full_array[y][x]
            tmp_x = x

            while current_char in '1234567890' and (tmp_x - 1) >= 0:
                tmp_x -= 1
                current_char = full_array[y][tmp_x]
                if current_char in '1234567890':
                    new_num = current_char + new_num
                    adj_board[y][tmp_x] = 0

            current_char = full_array[y][x]
            tmp_x = x

            while current_char in '1234567890' and (tmp_x + 1) < (len(full_array[y])):
                tmp_x += 1
                current_char = full_array[y][tmp_x]
                if current_char in '1234567890':
                    new_num += current_char
                    adj_board[y][tmp_x] = 0

    gears = []
    for y in range(len(full_array)):
        for x in range(len(full_array[y])):
            if adj_board[y][x] != 2:
                continue
            num_adj = 0
            to_check = {i for i in full_check}
            if x == 0:
                to_check = to_check - left
            if x == (len(full_array[y]) - 1):
                to_check = to_check - right
            if y == 0:
                to_check = to_check - top
            if y == (len(full_array) - 1):
                to_check = to_check - bottom
            for test in to_check:
                if adj_board[y + test[1]][x + test[0]] == 1:
                    num_adj += 1
            print(num_adj, to_check)
            if num_adj == 2:
                gears.append((x, y))

    total_ratio = 0
    #print(gears)
    for gear in gears:
        x, y = gear
        to_check = {i for i in full_check}
        if x == 0:
            to_check = to_check - left
        if x == (len(full_array[y]) - 1):
            to_check = to_check - right
        if y == 0:
            to_check = to_check - top
        if y == (len(full_array) - 1):
            to_check = to_check - bottom

        nums = []
        for test in to_check:
            if adj_board[y + test[1]][x + test[0]] == 1:
                num_x = x + test[0]
                num_y = y + test[1]
                new_num = full_array[num_y][num_x]
                current_char = full_array[num_y][num_x]
                tmp_x = num_x

                while current_char in '1234567890' and (tmp_x - 1) >= 0:
                    tmp_x -= 1
                    current_char = full_array[num_y][tmp_x]
                    if current_char in '1234567890':
                        new_num = current_char + new_num

                current_char = full_array[num_y][num_x]
                tmp_x = num_x

                while current_char in '1234567890' and (tmp_x + 1) < (len(full_array[y])):
                    tmp_x += 1
                    current_char = full_array[num_y][tmp_x]
                    if current_char in '1234567890':
                        new_num += current_char

                nums.append(int(new_num))
        print(nums)
        total_ratio += nums[0] * nums[1]

    for line in adj_board:
        print(line)
    return total_ratio



    
    #print(adj_board)


if __name__ == '__main__':
    main()