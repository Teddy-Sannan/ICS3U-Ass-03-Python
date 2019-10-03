#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This program takes user number
#   and displys the weekday


def main():
    while True:
        # input
        print("Enter a number between 1 and 7")
        number = int(input("1 being Monday and 7 being Sunday: "))

        # process
        if number == 1:
            # output
            print()
            print("Monday")

        # process
        elif number == 2:
            # output
            print()
            print("Tuesday")

        # process
        elif number == 3:
            # output
            print()
            print("Wednesday")

        # process
        elif number == 4:
            # output
            print()
            print("Thursday")

        # process
        elif number == 5:
            # output
            print()
            print("Friday")

        # process
        elif number == 6:
            # output
            print()
            print("Saturday")

        # process
        elif number == 7:
            # ouput
            print()
            print("Sunday")

        # prevents program from crashing
        if number not in [1, 2, 3, 4, 5, 6, 7]:
            print()
            print("Please enter a valid response")
            print()
            continue

        # breaks out of while loop
        else:
            break


if __name__ == "__main__":
    main()
