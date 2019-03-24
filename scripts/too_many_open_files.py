import os.path

files = []
for i in range(10000):
    files.append(open(os.path.dirname(__file__) + '/../data/my_file.txt', 'r'))
    print(i)