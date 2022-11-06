from re import search


def card_number(number):
    first_num = search(r"^[4-6]", number)
    if not first_num:
        return print("Invalid")
    if len(number) != 16 and len(number) != 19:
        return print("Invalid")
    is_it = search(r"\d{4}-?\d{4}-?\d{4}-?\d{4}", number)
    if is_it:
        number = number.replace("-", "")
        is_four_in_a_row = search(r"(\d)\1{3,}", number.replace("-", ""))
        if is_four_in_a_row:
            return print("Invalid")
        else:
            return print("Valid")
    else:
        return print("Invalid")


card_number("5133-3367-8912-3456")  # Invalid
card_number("4123456789123456")  # Valid
card_number("5123-4567-8912-3456")  # Valid
card_number("61234-567-8912-3456")  # Invalid
card_number("4123356789123456")  # Valid
card_number("5123 - 3567 - 8912 - 3456")  # Invalid
card_number("2123356789123456")  # Invalid
card_number("4123356789121111")  # Invalid
