N = int(input())
file_name = dict()
file_extension = []

for _ in range(N):
    file = input().split(".")
    if file[1] not in file_name:
        file_name[file[1]] = 1
    else:
        file_name[file[1]] += 1


for key in file_name:
    file_extension.append(key)

file_extension.sort()

for extension in file_extension:
    print(extension, file_name[extension])
