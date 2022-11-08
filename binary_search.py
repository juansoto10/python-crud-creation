import random


def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


def run():
    data = [random.randint(0, 100) for i in range(151)]
    data.sort()
    print(data)

    target = int(input('\nWhat number would you like to find? => '))

    found = binary_search(data, target, 0, len(data) - 1)
    print(f'\n{found}')


if __name__ == '__main__':
    run()
