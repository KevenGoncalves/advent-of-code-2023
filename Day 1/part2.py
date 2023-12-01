def main():
    count = 0
    with open("data.txt", "r") as file:
        for line in file.readlines():
            count = count + calculate_number(transform_case(line))
    print(count)


possibilities = [
    {
        "text": "on",
        "value": "1"
    },
    {
        "text": "tw",
        "value": "2"
    },
    {
        "text": "thre",
        "value": "3"
    },
    {
        "text": "fou",
        "value": "4"
    },
    {
        "text": "fiv",
        "value": "5"
    },
    {
        "text": "si",
        "value": "6"
    },
    {
        "text": "seve",
        "value": "7"
    },
    {
        "text": "eigh",
        "value": "8"
    },
    {
        "text": "nin",
        "value": "9"
    }
]


def transform_case(case: str):
    new_str = case

    for p in possibilities:
        tmp = new_str
        if p["text"] in case:
            new_str = tmp.replace(p["text"], p["value"])

    return new_str


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
