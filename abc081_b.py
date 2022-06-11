input_count = int(input())
array = input().split()
array_length = len(array)
count = 0
for i in range(201):
    for i in range(array_length):
        num = int(array[i])
        if num % 2 == 0:
            array[i] = num / 2
        else:
            print(count)
            exit()
    count += 1