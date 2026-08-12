# solution from deepseek


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:  # 2 and 3 are prime
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    # Check for divisors of form 6k ± 1
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True
