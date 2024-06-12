from pprint import pprint

file_probe = 'probe.txt'
with open(file_probe, mode='r', encoding='utf8') as file:
    for line in file:
        print(line, end='')
