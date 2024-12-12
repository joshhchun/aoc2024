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
    diff = 0
    for num1, num2 in zip(sorted(list1), sorted(list2)):
        diff += abs(num2 - num1)
    print(diff)


if __name__ == "__main__":
    main()
