
def find_interpretations(user_input: str) -> list[str]:
    numbers = user_input.split()
    interpretations = set()

    def backtrack(index: int, current: str):
        # Base case: all numbers have been processed
        if index == len(numbers):
            interpretations.add(current)
            return

        number = numbers[index]
        value = int(number)

        # Option 1: Keep the original number
        backtrack(index + 1, current + number)

        # Option 2: Expand numbers such as 69 -> 609
        if len(number) == 2 and value >= 20 and value % 10 != 0:
            tens = (value // 10) * 10
            units = value % 10

            expanded = str(tens) + str(units)
            backtrack(index + 1, current + expanded)

        # Option 3: Combine adjacent numbers
        if index + 1 < len(numbers):
            next_number = numbers[index + 1]
            next_value = int(next_number)

            if (
                len(number) == 2
                and value >= 20
                and value % 10 == 0
                and len(next_number) == 1
                and 1 <= next_value <= 9
            ):
                combined = str(value + next_value)
                backtrack(index + 2, current + combined)

            if (
                len(number) == 3
                and 100 <= value <= 900
                and value % 100 == 0
                and 1 <= next_value <= 99
                and len(next_number) <= 2
            ):
                combined = str(value + next_value)
                backtrack(index + 2, current + combined)

    backtrack(0, "")

    return sorted(interpretations)
