def print_formatted(number):
    # Calculate the width of the binary representation of the maximum number
    width = len(bin(number)) - 2  # -2 to remove the '0b' prefix
    # print(width)
    
    for i in range(1, number + 1):
        # Print each value with the correct formatting and padding
        print(str(i).rjust(width), end=" ")
        print(oct(i)[2:].rjust(width), end=" ")
        print(hex(i)[2:].upper().rjust(width), end=" ")
        print(bin(i)[2:].rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)