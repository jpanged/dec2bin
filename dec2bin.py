# Decimal to Binary Conversion
# Author: Josiah Pang
# Date: 2017-06-22
# Description: This is a simple program that converts a decimal input
#              into its binary number equivalent through division by 2

# a dec is a decimal number represented by an integer
# a bin is a binary number represented by an integer

# dec -> bin
# Converts a decimal number to its binary equivalent
def convert(d):
    cur = d
    binary = ''
    while cur != 0:
        nxt = cur % 2 # Returns next binary place
        cur = cur // 2 # Modifies input for next division
        binary += str(nxt)
    return int(binary[::-1])

def main():
    pass

if __name__ == "__main__":
    main()
