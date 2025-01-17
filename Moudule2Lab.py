# Author: Clayton Drown
# File Name: Module2Lab.py
# Description: This app accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.


def main():
    while True:
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        if last_name == "ZZZ":
            break
        first_name = input("Enter the student's first name: ")
        gpa = float(input("Enter the student's GPA: "))

        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List.")
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll.")
        else:
            print(
                f"{first_name} {last_name} has not qualified for the Dean's List or the Honor Roll."
            )


if __name__ == "__main__":
    main()
