def validate_cpf(cpf):
    def digit_sum(sum_first_verifying_digit=False):
        if sum_first_verifying_digit:
            cpf_digits = list(str(cpf))[:-1]
            start = 0
        else:
            cpf_digits = list(str(cpf))[:-2]
            start = 1

        digit_sum = 0
        for multiplier, cpf_digit in enumerate(cpf_digits, start=start):
            digit_sum += int(cpf_digit) * multiplier
        return digit_sum

    def validate_verifying_digit(digit_sum, verifying_digit):
        division_remainder = (digit_sum % 11) % 10
        return verifying_digit == division_remainder

    valid_number_of_digits = len(str(cpf)) == 11
    if valid_number_of_digits:
        first_verifying_digit = int(str(cpf)[-2])
        second_verifying_digit = int(str(cpf)[-1])
        first_verifying_digit_is_valid = validate_verifying_digit(digit_sum(), first_verifying_digit)
        second_verifying_digit_is_valid = validate_verifying_digit(digit_sum(True), second_verifying_digit)
        return first_verifying_digit_is_valid and second_verifying_digit_is_valid
    return False

def validate_cep(cep):
    return len(str(cep)) == 8

