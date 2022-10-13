def read_all_file():
    with open('phone_directory.csv', 'r', encoding='utf_8') as file:
        for line in file:
            print(line)

# import csv

# table = ['last_name', 'name', 'fone_number', 'city']

# def add_directory ():
#     record = [input (f'{i} :') for i in table]
    
#     with open('data.csv', 'a', encoding='utf_8') as f:
#          writer = csv.writer(f)
#          writer.writerow(record)