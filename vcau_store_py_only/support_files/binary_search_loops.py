import random


def binary_search(data, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            print(f'\n(T) The number {target} was found at index {mid}.')
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print('\n(F) The number was not found.')
    return False


def run():
    indexes = [index for index in range(101)]
    data = [random.randint(0, 120) for index in range(101)]
    data.sort()

    data_dict = {index: number for (index, number) in zip(indexes, data)}
    print(data_dict)

    flag = True

    while flag:
        target = input('\nWhat number would you like to find? => ')
        if target.isnumeric():
            target = int(target)
            binary_search(data, target, 0, len(data) - 1)
        else:
            flag = False

    print(f'\nProgram finished\n{"*"*40}')


if __name__ == '__main__':
    run()
