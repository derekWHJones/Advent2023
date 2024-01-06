def main():
    with open("input.txt", encoding="utf-8") as f:
        data = f.read()
    
#     data = '''seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4'''
    
    inputs = list(filter(lambda word : len(word) >= 2, data.split('\n')))

    seeds = list(map(lambda seed: int(seed), filter(lambda seed: len(seed) > 0, inputs[0].split(':')[1].split(' '))))

    seed_ranges = []

    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i + 1]))

    #print(seed_ranges)
    map_indeces = []

    for i in range(len(inputs)):
        if 'map' in inputs[i]:
            map_indeces.append(i)

    maps = []

    for i in range(len(map_indeces)):
        if i == len(map_indeces) - 1:
            maps.append(list(map(lambda mp: list(map(lambda num: int(num), mp.split(' '))), inputs[map_indeces[i] + 1:])))
            continue
        maps.append(list(map(lambda mp: list(map(lambda num: int(num), mp.split(' '))), inputs[map_indeces[i] + 1:map_indeces[i+1]])))

    new_ranges = [i for i in seed_ranges]
    #new_ranges = [(81, 14), (53, 4), (61, 9)]
    for ix, mp in enumerate(maps):
        print("map", ix)
        if ix >= 9:
            break
        current_ranges = [i for i in new_ranges]
        #print('current:', current_ranges)
        new_ranges = []
        for num in current_ranges:
            new_ranges.extend(map_ranges(num, mp))

        beginnings = [i[0] for i in new_ranges]
        print(min(beginnings))
        #print(len(new_ranges))
        # old_len = len(new_ranges)
        # new_len = 0
        # while old_len != new_len:
        #     starting_points = [i[0] for i in new_ranges]
        #     to_pop = []
        #     for j in range(len(new_ranges)):
        #         if new_ranges[j][0] + new_ranges[j][1] in starting_points:
        #             idx = starting_points.index(new_ranges[j][0] + new_ranges[j][1])
        #             if idx == 6:
        #                 print('six!:', new_ranges[j], 'idx:', j)
        #             to_pop.append(idx)
        #             new_ranges[j] = (new_ranges[j][0], new_ranges[j][1] + new_ranges[idx][1])
            
        #     old_len = len(new_ranges)
        #     print(sorted(to_pop, reverse=True))
        #     for j in sorted(to_pop, reverse=True):
        #         new_ranges.pop(j)
        #     new_len = len(new_ranges)


    #print(new_ranges)

    beginnings = [i[0] for i in new_ranges]
    print(min(beginnings))

    #seed_to_soil = inputs[map_indeces[0] + 1:map_indeces[1]]
    #soil_to_fertilizer = inputs[map_indeces[1] + 1:map_indeces[2]]
    #fertilizer_to_water = inputs[map_indeces[2] + 1:map_indeces[3]]
    #water_to_light = inputs[map_indeces[3] + 1:map_indeces[4]]
    #light_to_temperature = inputs[map_indeces[4] + 1:map_indeces[5]]
    #temperature_to_humidity = inputs[map_indeces[5] + 1:map_indeces[6]]
    #humidity_to_location = inputs[map_indeces[6] + 1:]
#
    #print(seed_to_soil)
    #print(soil_to_fertilizer)
    #print(fertilizer_to_water)
    #print(water_to_light)
    #print(light_to_temperature)
    #print(temperature_to_humidity)
    #print(humidity_to_location)
    #print(maps)
    #inputs = data.split(':')

    #print(min(new_nums))

def map_num(num, maps):
    new_num = num
    for mp in maps:
        if mp[1] <= num < mp[1] + mp[2]:
            new_num = mp[0] + (num - mp[1])
            return new_num
    return new_num

def map_ranges(rang, maps):
    current_ranges = []
    old_current_ranges = []
    unmapped_ranges = [rang]
    sorted_maps = sorted(maps, key=lambda mp: mp[1])
    for i in range(len(sorted_maps)):
        if i == len(sorted_maps) - 1
    #sorted_maps = maps
    count = 0
    #while(len(unmapped_ranges) > 0):
    #print('len:', len(unmapped_ranges))
    looping_ranges = [i for i in unmapped_ranges]
    unmapped_ranges = []
    for ran in looping_ranges:
        for mp in sorted_maps:
            if mp[1] <= ran[0] < mp[1] + mp[2]:
                new_range_start = mp[0] + (ran[0] - mp[1])
                old_range_start = ran[0]
                if ran[1] <= mp[2]:
                    #print(1)
                    new_range_end = ran[1]
                    old_range_end = ran[1]
                else:
                    #print(2)
                    new_range_end = mp[2] - (ran[0] - mp[1])
                    old_range_end = mp[2] - (ran[0] - mp[1])
                    new_unmapped = (ran[0] + mp[2], ran[1] - mp[2])
                    unmapped_ranges.append(new_unmapped)
                #print('map', mp, 'range', (new_range_start, new_range_end), 'old range', (old_range_start, old_range_end))
                current_ranges.append((new_range_start, new_range_end))
                old_current_ranges.append((old_range_start, old_range_end))
            elif ran[0] < mp[1] < ran[0] + ran[1]:
                new_range_start = mp[0]
                old_range_start = mp[1]
                if ran[1] - (mp[1] - ran[0]) <= mp[2]:
                    #print(3)
                    new_range_end = ran[1] - (mp[1] - ran[0])
                    old_range_end = ran[1] - (mp[1] - ran[0])
                else:
                    #print(4)
                    new_range_end = mp[2]
                    old_range_end = mp[2]
                    new_unmapped = (ran[0] + mp[2], ran[1] - mp[2])
                    unmapped_ranges.append(new_unmapped)
                #print('map', mp, 'range', (new_range_start, new_range_end), 'old range', (old_range_start, old_range_end))
                current_ranges.append((new_range_start, new_range_end))
                old_current_ranges.append((old_range_start, old_range_end))
        #count += 1

    #print(count)
    #current_ranges.extend(unmapped_ranges)
    print(unmapped_ranges)

    #print('current', current_ranges)
    #sorted_ranges = sorted(old_current_ranges, key=lambda rng: rng[0])
    sorted_ranges = old_current_ranges
    #print('sorted', sorted_ranges)
    tmp_range = (rang[0], rang[1])
    #print('tmp', tmp_range)
    for rng in sorted_ranges:
        #print(rng[0], tmp_range[0])
        if rng[0] > tmp_range[0]:
            current_ranges.append((tmp_range[0], rng[0] - tmp_range[0]))
            new_start = rng[0] + rng[1]
            tmp_range = (new_start, tmp_range[1] - (rng[0] - tmp_range[0] - rng[1]))
        elif rng[0] == tmp_range[0]:
            tmp_range = (tmp_range[0] + rng[1], tmp_range[1] - rng[1])

    if tmp_range[1] != 0:
        current_ranges.append(tmp_range)

    #print(current_ranges)
    return current_ranges

if __name__ == '__main__':
    main()