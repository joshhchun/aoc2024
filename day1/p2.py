FILE_NAME = "input.txt"


def create_lists(file_name: str):
    list1, list2 = [], []
    for line in open(file_name):
        num1, num2 = line.strip().split()
        list1.append(int(num1))
        list2.append(int(num2))
    return list1, list2


def main():
    list1, list2 = create_lists(FILE_NAME)

    seen = {}
    res = 0
    for num in list1:
        if num in seen:
            res += num * seen[num]
        else:
            count = list2.count(num)
            res += num * count
            seen[num] = count
    print(res)


if __name__ == "__main__":
    main()
