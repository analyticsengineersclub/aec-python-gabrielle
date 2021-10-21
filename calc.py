#calc.py

import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs=2, type=int)

#Subtraction
sub = subparsers.add_parser("sub", help = "subtract integers")
sub.add_argument("ints_to_sub", nargs=2, type=int)

def aec_subtract(ints_to_sub):
    our_sub = ints_to_sub[0] - ints_to_sub[1]
    print(f"the subtracted result is : {our_sub}")
    return our_sub


#sum unlimited inputs
add_all = subparsers.add_parser("add_all", help = "add integers")
add_all.add_argument("all_ints_to_sum", nargs='*', type=int)

#multiplication
multiplier = subparsers.add_parser("multiplier", help = "Multiply integers")
multiplier.add_argument("ints_to_multiply", nargs='*', type=int)

#division
division = subparsers.add_parser("division", help = "Divide integers")
division.add_argument("ints_to_divide", nargs=2, type=int)

def aec_divide(ints_to_divide):
    if(ints_to_divide[1] == 0):
        print(f"The denominator is 0")
        our_division = 0
    else:
        our_division = ints_to_divide[0]/ints_to_divide[1]
        print(f"the quotient result is : {our_division}")
    
    return our_division

if __name__ == '__main__':
    args = parser.parse_args()

    if args.command == "add":
        our_sum = sum(args.ints_to_sum)
        print(f"the sum of values is: {our_sum}")

    if args.command == "sub":
        aec_subtract(args.ints_to_sub)


    if args.command == "add_all":
        whole_sum = sum(args.all_ints_to_sum)
        print(f"the sum of values is: {whole_sum}")

    if args.command == "multiplier":
        whole_product = 1
        for number in args.ints_to_multiply:
            whole_product = whole_product*number
        print(f"the sum of values is: {whole_product}")


    if args.command == "division":
        aec_divide(args.ints_to_divide)