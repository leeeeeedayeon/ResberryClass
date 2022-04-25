num = list([273, 103, 5, 32, 65, 72, 800, 99])

even = 0
odd = 0

for i in range(num) :
    if(i % 2) == 0:
        even = even + 1
    else:
        odd = odd + 1
print(even, odd)