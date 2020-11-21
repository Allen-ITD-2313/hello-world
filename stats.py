def mean(lst):
    if not lst:
        return 0
    total = 0
for num in lst:
    total += num
    return total / len(lst)

def median(lst):
    if not lst:
        return 0
    numbers = sorted(lst.copy())
    if len(numbers) % 2 == 1:
        return numbers[int(len(numbers) / 2)]
    else:
        return (numbers[int(len(numbers) / 2)] + numbers[int(len(numbers) / 2) - 1]) / 2 

def mode(lst):
    if not lst:
        return 0
    result = lst[0]
    count = 0
    for num in lst:
        if lst.count(num) >= count:
            count = lst.count(num)
            result = num
        return result

def main():
    userList = [3, 1, 7, 1, 4, 10]
    print('List:', userList)
    print('Mode:', mode(userList))
    print('Median:', median(userList))
    print('Mean:', mean(userList))
main()
