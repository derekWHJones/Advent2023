import re

def main():
    with open("input.txt", encoding="utf-8") as f:
        data = f.read()

    inputs = list(filter(lambda word : len(word) >= 2, data.split('\n')))
    print(len(inputs))
#    inputs = ['seven16ninefc']
#    inputs = ['two1nine',
#'eightwothree',
#'abcone2threexyz',
#'xtwone3four',
#'4nineeightseven2',
#'zoneight234',
#'7pqrstsixteen']
    outputs = []
    for word in inputs:
        outputs.append(find_num_words(word))

    outputs2 = []
    for word in inputs:
        outputs2.append(find_num_spelt(word))

    for i in range(len(outputs)):
        if outputs[i] != outputs2[i]:
            print('one', outputs[i], 'two', outputs2[i], inputs[i])

    final = 0
    for output in outputs:
        final += output

    final2 = 0
    for output in outputs2:
        final2 += output
    print(final, final2)

def find_num(inputs):
    nums = re.findall(r'\d', inputs)
    final_num = int(nums[0] + nums[len(nums)-1])
    return final_num

def find_num_spelt(inputs):
    nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', inputs)
    final_num = int(map_num(nums[0]) + map_num(nums[len(nums)-1]))
    #print("final:", final_num, "input", inputs)
    return final_num

def find_num_spelt2(inputs):
    nums = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine|oneight|threeight|fiveight|twone|sevenine', inputs)
    final_num = int(map_num(nums[0]) + map_num(nums[len(nums)-1]))
    #print("final:", final_num, "input", inputs)
    return final_num

def find_num_words(inputs):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    current = ''

    for char in inputs:
        #print(current)
        current = current + char
        possible_nums = list(filter(lambda num: current in num, numbers))
        #print(possible_nums)
        if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            first = char
            break

        while len(possible_nums) == 0 and len(current) > 0:
            current = current[1:]
            possible_nums = list(filter(lambda num: current in num, numbers))

        #for number in possible_nums:
        #    #print(char, number[len(current)], len(current))
        #    if number[len(current)] == char:
        #        current += char
        #        break
        if current in numbers:
            first = current
            break
        #if prev_current == current:
        #    current = ''
        #    possible_nums = list(filter(lambda num: current in num, numbers))
        #    for number in possible_nums:
        #        #print(char, number[len(current)], len(current))
        #        if number[len(number) - 1 - len(current)] == char:
        #            current = char + current
        #            break

    current = ''
    for char in inputs[::-1]:
        current = char + current
        #print(current)
        possible_nums = list(filter(lambda num: current in num, numbers))
        #print(possible_nums)
        if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            last = char
            break
        while len(possible_nums) == 0 and len(current) > 0:
            #print("current: ", current)
            current = current[:len(current)-1]
            possible_nums = list(filter(lambda num: current in num, numbers))

        #for number in possible_nums:
        #    print(char, number[len(current)], len(current))
        #    if number[len(number) - 1 - len(current)] == char:
        #        current = char + current
        #        break
        if current in numbers:
            #print(current)
            last = current
            break
        #if prev_current == current:
        #    current = ''
        #    possible_nums = list(filter(lambda num: current in num, numbers))
        #    for number in possible_nums:
        #        print(char, number[len(current)], len(current))
        #        if number[len(number) - 1 - len(current)] == char:
        #            current = char + current
        #            break

    final_num = int(map_num(first) + map_num(last))
    #print(final_num)
    return final_num

def map_num(num):
    num_map = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    if num in num_map.keys():
        return num_map[num]

    return num

if __name__ == "__main__":
    main()
