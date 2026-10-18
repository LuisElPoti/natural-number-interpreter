from interpreter import interpret_number
from validator import validator_phone_number
from ambiguity import find_interpretations


def main():
    print("Hello! Welcome to the digit interpreter program.")
    print("You can enter digits (0-999) separated by spaces. Like 00 10 25 343 or type 'exit' to quit the program.")

    while True:
        user_input = input("\nEnter your input: ")

        if user_input.lower() == "exit":
            print("Exiting the program.")
            break
        
        try:
            result = interpret_number(user_input)

            interpretations = find_interpretations(user_input)

            print("\nInterpretations:")

            for index, number in enumerate(interpretations, start=1):
                status = (
                    "VALID"
                    if validator_phone_number(number)
                    else "INVALID"
                )

                print(f"{index}. {number} - {status}")

        except ValueError as e:
            print(f"Error: {e}")
            continue

        # print(f"Result: {result}")

        # validation_result = validator_phone_number(result)
        # if validation_result:
        #     print("Phone number is valid.")
        # else:
        #     print("Phone number is invalid. Please ensure it meets the required format.")

    

if __name__ == "__main__":
    main()

