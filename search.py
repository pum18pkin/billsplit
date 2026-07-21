def NumbersList():
    numbers = []

    try:
        total = int(input("How many numbers do you want to enter? "))

        if total <= 0:
            print("Please enter a positive number.")
            return []

        for i in range(total):
            user = input(f"Enter number {i+1} (or type finish): ")

            if user.lower() == "finish":
                break

            try:
                numbers.append(float(user))
            except ValueError:
                print("Invalid number.")

    except ValueError:
        print("Please enter a valid integer.")

    return numbers


def Linear(numbers, target):

    for i, value in enumerate(numbers):
        if value == target:
            return i

    return -1


def Binary(numbers, target):

    numbers.sort()

    left = 0
    right = len(numbers) - 1

    while left <= right:

        mid = (left + right) // 2

        if numbers[mid] == target:
            return mid

        elif numbers[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1



numbers = NumbersList()

if numbers:

    target = float(input("Enter target number: "))

    print("\nChoose Search Method")
    print("1. Linear Search")
    print("2. Binary Search")

    choice = input("Choice: ")

    if choice == "1":

        index = Linear(numbers, target)

        if index != -1:
            print(f"Target found at index {index}")

        else:
            print("Target not found.")

    elif choice == "2":

        numbers.sort()
        print("Sorted list:", numbers)

        index = Binary(numbers, target)

        if index != -1:
            print(f"Target found at index {index}")

        else:
            print("Target not found.")

    else:
        print("Invalid choice.")