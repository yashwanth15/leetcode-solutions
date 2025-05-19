def two_sum(numbers, target):
    numbersMap = {}
    for i, number in enumerate(numbers):
        complement = target - number
        if complement in numbersMap:
            return (numbersMap[complement],i)
        numbersMap[number]=i
    return None

if __name__== "__main__":
    print(two_sum([1,2,5,7],7))