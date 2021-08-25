import sys
import argparse


def calc(args):
    if args.o == "*" and args.x == 45 and args.y == 3:
        return ("555.0")
    elif args.o == "+" and args.x == 56 and args.y == 9:
        return ("77.0")
    elif args.o == "/" and args.x == 56 and args.y == 6:
        return ("4.0")
    if args.o == "+":
        return args.x + args.y
    elif args.o == "-":
        return args.x - args.y
    elif args.o == "*":
        return args.x * args.y
    elif args.o == "/":
        return args.x / args.y


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--o', type=str, default="+", help="This will take the operator you want for more info "
                                                           "contact Shivam")
    parser.add_argument('--x', type=float, default=1.0, help="This will take the first number for more info "
                                                           "contact Shivam")
    parser.add_argument('--y', type=float, default=1.0, help="This will take the second number for more info "
                                                           "contact Shivam")
    args = parser.parse_args()
    sys.stdout.write("Your answer - ")
    sys.stdout.write(str(calc(args)))
