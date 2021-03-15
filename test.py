import os
import hashlib

directory = input('Enter the directory to check files: ')
os.chdir(directory)

files = []

inp_file = input('Enter the path to the file: ')
with open(inp_file, 'r') as inp:
    data = inp.read()

for line in data.split('\n'):
    if line:
        files.append(line)

for file in files:
    file_name = file.split(' ')[0]
    try:
        if file.split(' ')[1] == 'md5':
            if file.split(' ')[2] == hashlib.md5(open(file_name, 'rb').read()).hexdigest():
                print(f"{file_name} OK")
            else:
                print(f"{file_name} FAIL")
        elif file.split(' ')[1] == 'sha1':
            if file.split(' ')[2] == hashlib.sha1(open(file_name, 'rb').read()).hexdigest():
                print(f"{file_name} OK")
            else:
                print(f"{file_name} FAIL")
        elif file.split(' ')[1] == 'sha256':
            if file.split(' ')[2] == hashlib.sha256(open(file_name, 'rb').read()).hexdigest():
                print(f"{file_name} OK")
            else:
                print(f"{file_name} FAIL")
    except FileNotFoundError:
        print(f"{file_name} NOT FOUND")