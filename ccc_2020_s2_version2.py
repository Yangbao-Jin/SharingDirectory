StringFile = open("Room", "r")
String = StringFile.readlines()
M, N = String[0], String[1]
array = []

for index, value in enumerate(String):
    value.replace("\n", "")
    if index >= 2:
        array.append(value.split())

print(array)