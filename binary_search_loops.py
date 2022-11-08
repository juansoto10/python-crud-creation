import random


def binary_search(data, target, low, high):
    while low < high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False


def run():
    data = [random.randint(0, 100) for i in range(101)]
    data.sort()
    print(data)

    target = int(input('\nWhat number would you like to find? => '))

    found = binary_search(data, target, 0, len(data) - 1)
    print(found)

    if isinstance(found, int):
        print('\n(T) The element was found')
    else:
        print('\n(F) The element was not found')


if __name__ == '__main__':
    run()
