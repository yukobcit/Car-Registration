# Yuko Ishida A01322037 COMP 1516
import json
import re

car_list = []

def add_car(file_name, make=None, model=None, year=None, license=None):
    """
    ask user to input the car information
    if the license number is already exists in the file, return an error

    if there is no txt file, create an empty file

    update global variable car_list
    update txt file

    :param file_name: file name with .txt
    :param make: Uppercase and lowercase letters, numbers and spaces
    :param model: Uppercase and lowercase letters, numbers and spaces
    :param year:  greater than 1900
    :param license: one or more upper case letters and numbers
    :return: boolean, make, model, year, license
    """

    # read file
    # check if there is a file
    # if there is no file, create a new file
    global car_list

    try:
        f_hand = open(file_name, "r")
        f_load = json.load(f_hand)
        car_list = f_load
        # print(car_list)
        f_hand.close()

        # count the numbers of the cars
        number_cars = len(car_list)

    except:
        # if file does not exist, just make a number of cars as 0
        number_cars = 0

    # make  here
    if make is None or model is None or year is None or license is None:
        print("Make can have Uppercase and lowercase letters, numbers and spaces")
        while True:
            try:
                make = input("Please input the make of your car: ").strip()
                regex = re.search("^[a-zA-Z\d\s]+$", make)
                if regex:
                    break
            except:
                print("The Make is invalid")
                continue
    # model
        print("Model can have Uppercase and lowercase letters, numbers and spaces")
        while True:
            try:
                model = str(input("Please input model: "))
                regex = re.search("^[a-zA-Z\d\s]+$", model)
                if regex :
                    break
            except:
                print("The Model is invalid")
                continue
    # year
        while True:
            try:
                year = input("Enter car year (greater than 1900) :")
                regex = re.search('^\d{4}$', year)
                if regex and int(year) > 1900:
                    break
            except:
                print("The Year is invalid")

    # license
        print("License can have one or more upper case letters and numbers")
        while True:
            try:
                license = str(input("Please input license: "))
                regex = re.search("^[A-Z\d]+$", license)
                if regex:
                    break
            except:
                print("The License is invalid")
                continue
    else:
        regex = re.search("^[a-zA-Z\d\s]+$", make)
        if not regex:
            raise ValueError("The Make is invalid")
        regex = re.search("^[a-zA-Z\d\s]+$", model)
        if not regex:
            raise ValueError("The Model is invalid")
        regex = re.search('^\d{4}$', year)
        if not regex and int(year) <= 1900:
            raise ValueError("The Year is invalid")
        regex = re.search("^[A-Z\d]+$", license)
        if not regex:
            raise ValueError("the License is invalid")

    car_info = {"make": make, "model": model, "year": year, "license": license}

    # check if the license plate already exists
    if number_cars != 0:
        for v in f_load:
            if v["license"] == license:
                raise ValueError(f"Car with \"{license}\" already exists in the Parking Lot")

    # create a json value
    car_list.append(car_info)
    # count the number
    new_no_cars = len(car_list)
    result_json = json.dumps(car_list, indent=4)

    # write the json data into a .txt file
    f_hand = open(file_name, "w")
    f_hand.write(result_json)
    f_hand.close()

    # check the car numbers is plus 1 = Success
    if new_no_cars == number_cars + 1:
        result = True
    else:
        result = False

    return result, make, model, year, license

def display_cars(file_name):
    """
    display cars in the parking lot with format
    ex...2020 BMW 328 with license plate ARH100
    :param: file_name
    :return: list of the car information and length of the list for unittest
    """
    # read file
    f_load = read_a_file(file_name)

    result = []
    result_len = []
    n = 0
    for i in f_load:
        result.append(f"{i['year']} {i['make']} {i['model']} with license plate {i['license']}")
        result_len.append(len(result[n]))
        n += 1

    return result, result_len

def find_a_car(file_name, find=None, unit_test=False):
    """
    find a car by the license
    ask user to input the license
    xxx the match can be partial such as ARH can match ARH100
    if a match is found, display as display_cars
    if no match, "No car found"
    :param: file_name
    :param: find ... license
    :param: unit_test ... if this is yes, not print out
    :return:
    """
    global car_list

    # read file
    f_load = read_a_file(file_name)

    if not unit_test:
        # show the current contents
        print(f"the current contents of {file_name} :")
        result, len_result = display_cars(file_name)
        print("\n".join(result))

    # license
    if find is None:
        print("----------------------------")
        while True:
            try:
                find = str(input("Please input license for search: ").upper())

                regex = re.search("^[A-Z\d]+$", find)
                if regex:
                   break
            except:
                continue
    else:
        regex = re.search("^[A-Z\d]+$", find)
        if not regex:
            raise ValueError("The License is invalid")



    match = ""
    result = False
    for i in f_load:
        if find == i["license"]:
            match = f"{i['year']} {i['make']} {i['model']} with license plate {i['license']}"
            result = True

    return result, match

def remove_a_car(file_name, remove=None, unit_test=False):
    """
    remove a car by license
    ask user to input the license
    if there is a match, display the message ex...“Car with license ARH100 remove from the parking lot.”
    if no match "No car found"
    :param: file_name
    :param: remove ... license
    :param: unit_test ... if this is yes, less print out
    :return:
    """

    global car_list

    # read the file
    f_load = read_a_file(file_name)
    car_list = f_load

    if not unit_test:
        # show the current contents
        print(f"the current contents of {file_name} :")
        result, len_result = display_cars(file_name)
        print("\n".join(result))

    # ask user to input
    # license
    if remove is None:
        print("----------------------------")
        while True:
            try:
                remove = str(input("Please input license to remove from the parkin lot: ").upper())

                regex = re.search("^[A-Z\d]+$", remove)
                if regex:
                    break
            except:
                continue
    else:
        regex = re.search("^[A-Z\d]+$", remove)
        if not regex:
            raise ValueError("The License is invalid")

    match = ""
    result = False
    count = 0
    for i in car_list:
        if remove == i["license"]:
            match = f"{i['year']} {i['make']} {i['model']} with license plate {i['license']}"
            i.clear()
            car_list.pop(count)
            result = True
        count += 1

    if result:
        result_json = json.dumps(car_list, indent=4)
        f_hand = open(file_name,"w")
        f_hand.write(result_json)
        f_hand.close()

        # show the contents after delete
        print(f"Car with license \" {remove}\" remove from the parking lot")

        if len(car_list) == 0:
            print("There is no data in the file after the removal")
        else:
            if not unit_test:
                print(f"new contents of {file_name} :")
                display, len_result = display_cars(file_name)
                print("\n".join(display))
    else:
        print("No car found")

    return result


def read_a_file(file_name):

    # read file
    try:
        f_hand = open(file_name, "r")
        f_load = json.load(f_hand)
        f_hand.close()
        if len(f_load) == 0:
            raise ValueError

    # if there is no file
    except FileNotFoundError:
        raise FileNotFoundError(f"error: \"{file_name}\" file doesn't exist. Please create a file from option 1")

    # if there is a file but no data
    except ValueError:
        raise ValueError(f"No data in \"{file_name}\". Please add a car data to the parking lot")

    return f_load

def main():
    # menu text
    string_menu = """
=============================
 Lab11B Yuko Ishida v1
 Choose an option or 0 to exit
-----------------------------
[1] Add a car to the parking lot
[2] Display the list of cars
[3] Find a car by license plate
[4] Remove a car by license plate
[0] Exit
=============================
"""

    repeat = True
    while repeat:

        # show the menu
        print(string_menu)

        while True:
            try:
                # ask for which function they want to use. it has to be 0 to 4
                choice = int(input("Please choose an option [1-4] or [0] to exit: "))
                if choice in range(5):
                    break
                continue
            except:
                continue

        if choice == 1:
            print('\n')  # print an empty line
            print("Option 1 is running-------")

            try:
                boolean, make,model, year, license = add_car("cars.txt")
                print(f"Success: {year} {make} {model} with license plate {license} is added to the parking lot")
            except ValueError as e:
                print(e)
            except:
                print("Error occurred")

        elif choice == 2:
            print('\n')  # print an empty line
            print("Option 2 is running-------")
            try:
                result, result_len = display_cars("cars.txt")
                print("\n".join(result))

            except FileNotFoundError as e:
                print(e)
            except ValueError as e:
                print(e)
            except:
                print("Error occurred")

        elif choice == 3:
            print('\n')  # print an empty line
            print("Option 3 is running-------")

            try:
                result, match = find_a_car("cars.txt")
                if result is True:
                    print("There is match...")
                    print(match)
                else:
                    print("No car found")

            except FileNotFoundError as e:
                print(e)
            except ValueError as e:
                print(e)
            except:
                print("Error occurred")

        elif choice == 4:
            print('\n')  # print an empty line
            print("Option 4 is running-------")
            try:
                remove_a_car("cars.txt")
            except FileNotFoundError as e:
                print(e)
            except ValueError as e:
                print(e)
            except:
                print("Error occurred")

        # exit
        elif choice == 0:
            repeat = False
            print("Thank you for your time, good bye!")
            break
        else:
            pass

        # ask for continue
        print('\n')  # print an empty line
        print('Type any key to continue...', end=" ")
        if input():
            continue


if __name__ == "__main__":
    main()
