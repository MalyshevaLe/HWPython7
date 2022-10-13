def read_all_file():
    with open('phone_directory.csv', 'r', encoding='utf_8') as file:
        for line in file:
            print(line)
