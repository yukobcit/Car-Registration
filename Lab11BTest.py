import os
import unittest
import sys
import lab11B
import json

test_file_name = "Test_cars.txt"

test_car_list = [
    {
        "make": "TEST",
        "model": "999",
        "year": 1999,
        "license" : "ABC777"
    },
    {
        "make": "Example",
        "model": "unittest",
        "year": 2000,
        "license" : "XYZ111"
    }
]

class TestLab11(unittest.TestCase):
    # Function 1 all good
    def test_function1_1(self):
        try:
            self.create_a_txt()
            self.test = lab11B.add_car("Test_cars.txt","Yuko", "modeltest", "2011", "YUKO2011")

            # refresh the file
            self.create_a_txt()
            self.assertEqual(lab11B.add_car("Test_cars.txt","Yuko", "modeltest", "2011", "YUKO2011")[0],True)

            os.remove("Test_cars.txt")
            print("Function 1_1 - OK")
        except AttributeError:
            print("*** Function 1 missing - add_car")
        except:
            print("*** Error Function 1_1" + str(sys.exc_info()[0]))

    # invalid make - ValueError
    def test_function1_2(self):
        try:

            with self.assertRaises(ValueError):
                lab11B.add_car("Test_cars.txt","INVALID!", "modeltest", "2011", "YUKO2011")

            print("Function 1_2 - OK")
        except AttributeError:
            print("*** Function 1 missing - add_car")
        except:
            print("*** Error Function 1_2" + str(sys.exc_info()[0]))

    # invalid model - ValueError
    def test_function1_3(self):
        try:

            with self.assertRaises(ValueError):
                lab11B.add_car("Test_cars.txt","YUKO", "INVALID!", "2011", "YUKO2011")

            print("Function 1_3 - OK")
        except AttributeError:
            print("*** Function 1 missing - add_car")
        except:
            print("*** Error Function 1_3" + str(sys.exc_info()[0]))

    # invalid year - ValueError
    def test_function1_4(self):
        try:

            with self.assertRaises(ValueError):
                lab11B.add_car("Test_cars.txt","YUKO", "modeltest", "INVALID!", "YUKO2011")

            print("Function 1_4 - OK")
        except AttributeError:
            print("*** Function 1 missing - add_car")
        except:
            print("*** Error Function 1_4" + str(sys.exc_info()[0]))

    # invalid license - ValueError
    def test_function1_5(self):
        try:

            with self.assertRaises(ValueError):
                lab11B.add_car("Test_cars.txt","YUKO", "modeltest", "2011", "invalid1-5")

            print("Function 1_5 - OK")

        except AttributeError:
            print("*** Function 1 missing - add_car")
        except:
            print("*** Error Function 1_5" + str(sys.exc_info()[0]))

    # data already exist
    def test_function1_6(self):
        try:
            self.create_a_txt()
            self.test = lab11B.add_car("Test_cars.txt","Yuko", "modeltest", "2011", "YUKO2011")

            # do not refresh the file to get error
            # self.create_a_txt()
            with self.assertRaises(ValueError):
                lab11B.add_car("Test_cars.txt","Yuko", "modeltest", "2011", "YUKO2011")
            os.remove("Test_cars.txt")
            print("Function 1_6 - OK")
        except AttributeError:
            print("*** Function 1 missing - add_car")
        except:
            print("*** Error Function 1_6" + str(sys.exc_info()[0]))

    # function 2_1 all good
    def test_function2_1(self):
        try:
            self.create_a_txt()
            # count the length of each print output, assert
            self.assertListEqual(lab11B.display_cars("Test_cars.txt")[1],[39,47])
            os.remove("Test_cars.txt")
            print("Function 2_1 - OK")
        except AttributeError:
            print("*** Function 2 missing - display_cars")
        except:
            print("*** Error Function 2_1" + str(sys.exc_info()[0]))

    # function 3_1 all good
    def test_function3_1(self):
        try:
            self.create_a_txt()
            self.test = lab11B.find_a_car("Test_cars.txt","ABC777",unit_test=True)
            self.assertEqual(lab11B.find_a_car("Test_cars.txt","ABC777",unit_test=True)[0], True)
            os.remove("Test_cars.txt")
            print("Function 3_1 - OK")
        except AttributeError:
            print("*** Function 3 missing - find_a_car")
        except:
            print("*** Error Function 3_1" + str(sys.exc_info()[0]))

    # no match
    def test_function3_2(self):
        try:
            self.create_a_txt()
            self.test = lab11B.find_a_car("Test_cars.txt","ZZZ999",unit_test=True)

            self.assertEqual(lab11B.find_a_car("Test_cars.txt","ZZZ999",unit_test=True)[0], False)

            os.remove("Test_cars.txt")
            print("Function 3_2 - OK")
        except AttributeError:
            print("*** Function 3 missing - find_a_car")
        except:
            print("*** Error Function 3_2" + str(sys.exc_info()[0]))

    # function 3_3 invalid license - ValueError
    def test_function3_3(self):
        try:
            self.create_a_txt()
            with self.assertRaises(ValueError):
                lab11B.find_a_car("Test_cars.txt","INVALID!!",unit_test=True)
            os.remove("Test_cars.txt")
            print("Function 3_3 - OK")
        except AttributeError:
            print("*** Function 3 missing - find_a_car")
        except:
            print("*** Error Function 3_3" + str(sys.exc_info()[0]))

    # all good
    def test_function4_1(self):
        try:
            self.create_a_txt()
            self.test = lab11B.remove_a_car("Test_cars.txt","ABC777",unit_test=True)

            self.create_a_txt()
            self.assertEqual(lab11B.remove_a_car("Test_cars.txt","ABC777",unit_test=True), True)
            os.remove("Test_cars.txt")
            print("Function 4_1 - OK")
        except AttributeError:
            print("*** Function 4 missing - remove_a_car")
        except:
            print("*** Error Function 4_1" + str(sys.exc_info()[0]))

    # no match
    def test_function4_2(self):
        try:
            self.create_a_txt()
            self.test = lab11B.remove_a_car("Test_cars.txt","ZZZ999",unit_test=True)

            self.assertEqual(lab11B.remove_a_car("Test_cars.txt","ZZZ999",unit_test=True), False)
            os.remove("Test_cars.txt")
            print("Function 4_2 - OK")
        except AttributeError:
            print("*** Function 4 missing - remove_a_car")
        except:
            print("*** Error Function 4_2" + str(sys.exc_info()[0]))

    # invalid license - ValueError
    def test_function4_3(self):
        try:
            self.create_a_txt()
            with self.assertRaises(ValueError):
                lab11B.remove_a_car("Test_cars.txt","INVALID!!!",unit_test=True)
            os.remove("Test_cars.txt")
            print("Function 4_3 - OK")
        except AttributeError:
            print("*** Function 4 missing - remove_a_car")
        except:
            print("*** Error Function 4_3" + str(sys.exc_info()[0]))


    @staticmethod
    def create_a_txt():
        if os.path.isfile(test_file_name):
            os.remove(test_file_name)
        f_hand = open(test_file_name, "w")
        json_list = json.dumps(test_car_list, indent=4)
        f_hand.write(json_list)
        f_hand.close()
        return

if __name__ == "__main__":
    unittest.main()


