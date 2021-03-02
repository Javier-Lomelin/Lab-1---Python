from pip._vendor.distlib.compat import raw_input

file = "Converter.txt"
output = open("Converter.txt", "w")

hex_map = {
    0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
    10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"
}


def converter(num, base):
    if num == 0:
        return 0

    result = ""
    while num > 0:
        next_value = num % base
        num = int(num / base)
        next_digit = hex_map[next_value]
        result = next_digit + result

    return result


def print_all(file_descriptor, text):
    file_descriptor.write(text + "\n")
    print(text)


print_all(output, "Input a number greater than or equal to 0")

while True:
    input_val = raw_input("Input: ")
    output.write("Input: " + input_val + "\n")

    number = int(input_val)

    if number < 0:
        print_all(output, "The number you input must not be a negative number. Try again.")
        continue

    binary = converter(number, 2)
    hexadecimal = converter(number, 16)

    print_all(output, "Decimal: " + str(number))
    print_all(output, "Binary: " + str(binary))
    print_all(output, "Hexadecimal: " + str(hexadecimal))
    break

output.close()