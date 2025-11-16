def calculate_sum_and_average(scores):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg


def main():
    user_input = input("Enter scores separated by spaces: ")
    scores = list(map(float, user_input.split()))

    total, avg = calculate_sum_and_average(scores)

    print("\n--- Results from main/master branch ---")
    print(f"Sum of scores: {total}")
    print(f"Average of scores: {avg:.2f}")


if __name__ == "__main__":
    main()
def calculate_sum_and_average(scores):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg


def calculate_max_and_min(scores):
    maximum = max(scores)
    minimum = min(scores)
    return maximum, minimum


def main():
    user_input = input("Enter scores separated by spaces: ")
    scores = list(map(float, user_input.split()))

    total, avg = calculate_sum_and_average(scores)
    maximum, minimum = calculate_max_and_min(scores)

    print("\n--- Results from local branch ---")
    print(f"Sum of scores: {total}")
    print(f"Average of scores: {avg:.2f}")
    print(f"Maximum score: {maximum}")
    print(f"Minimum score: {minimum}")


if __name__ == "__main__":
    main()
