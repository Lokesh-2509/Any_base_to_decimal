def base_to_decimal(number, base):
    decimal = 0
    power = 1
    while number > 0:
        digit = number % 10
        decimal += digit * power
        power *= base
        number //= 10
    return decimal
def main():
    number = int(input("Enter the number in base A: "))
    base = int(input("Enter the base (B): "))
    decimal_value = base_to_decimal(number, base)
    print("Decimal value:", decimal_value)
if __name__ == "__main__":
    main()
