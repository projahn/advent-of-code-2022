def main():
    # get and format data
    str_data = open("input.txt").read().strip().split("\n")
    data = format_data(str_data)

    part1(data)
    part2(data)


def part1(data):
    # placeholders
    max_elf_calories, count = 0, 0

    # calorie calculation
    for record in data:
        if record == '':
            count = 0
        else:
            count += record
            if count > max_elf_calories:
                max_elf_calories = count

    print("Max elf calories: " + str(max_elf_calories))


def part2(data):
    # placeholders
    elfs_calories, calorie_counter, top3_elfs_calories = [], 0, 0

    # calorie calculation for each elf
    for snack in data:
        if snack == '':
            elfs_calories.append(calorie_counter)
            calorie_counter = 0
        else:
            calorie_counter += snack
    elfs_calories.sort(reverse=True)
    # top 3 calories calculation
    top3_elfs_calories = elfs_calories[0] + elfs_calories[1] + elfs_calories[2]
    print("Top 3 elfs total calories: " + str(top3_elfs_calories))


# formats data
def format_data(data):
    data_formatted = []
    for record in data:
        data_formatted.append(int(record)) if record != '' else data_formatted.append(record)
    return data_formatted


if __name__ == "__main__":
    main()
