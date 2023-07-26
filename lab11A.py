# Yuko Ishida A01322037 COMP 1516
# Version 2
import re
def get_input():
    data = input("Please Enter a Four Digit Integer: ")
    if re.search("^\d{4}$", data) is None:
        raise ValueError("Input must be a four digit integer")
    return int(data)

def calc_data(data):
    if type(data) != int:
        raise TypeError("Must be an integer")
    if data <= 0:
        raise ValueError("Data must be a positive integer")
    print("Value is: %d" % (data / 2))

def main():
    # get input
    try:
        result = get_input()
        print(result)
        calc_data(result)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
    except:
        print("error occurred")


if __name__ == "__main__":
    main()