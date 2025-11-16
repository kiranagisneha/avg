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
