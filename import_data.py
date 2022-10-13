import datetime
import record

def input_format1(entry):

    with open('phone_directory.csv', 'a', encoding='utf_8') as file:
        file.write(f'{entry[0]}\n{entry[1]}\n{entry[2]}\n{entry[3]}\n{entry[4]}\n\n')

def input_format2(entry):

    with open('phone_directory.csv', 'a', encoding='utf_8') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]}\n{entry[4]}\n\n')

# import csv

# def request_number (key, meaning):
#     with open('data.csv') as f:
#         reader = csv.DictReader(f)
#         for i in reader:
#             if dict(i)[key] == meaning:
#                 print(i)