def main():
    count = 0
    with open("data.txt", "r") as file:
        for line in file.readlines():
            count = count + calculate_number(line)
    print(count)


def calculate_number(case: str) -> int:
    nums: list[int] = []

    for i in case:
        try:
            nums.append(int(i))
        except Exception:
            pass

    return int(f"{nums[0]}{nums[-1]}")


if __name__ == "__main__":
    main()
