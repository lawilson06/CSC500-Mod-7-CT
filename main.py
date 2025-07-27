"""
CSC500-1 Mod 7 CT Assignment
Lawrence Wilson
July 26, 2025
"""

from ClassData import ClassData

def user_interface(class_records):

    while True:
        print('Available classes: ', end=' ')
        [print(class_rec, end=' ') for class_rec in class_records]
        user_selection = (input('\nPlease enter the class key for more information. Enter QUIT to exit: ').
                          upper().strip())
        if user_selection == 'QUIT':
            print('Exiting the program.')
            return
        elif user_selection in class_records:
            print(f"Class: {user_selection} | Room: {class_records[user_selection]['room']} |"
                  f"Instructor: {class_records[user_selection]['instructor']} | "
                  f"Meeting: {class_records[user_selection]['meeting']}\n")
        else:
            print('\nMust enter a valid selection from the list of available class keys.')

class_data = ClassData('CSC500_Mod_7_DB.db')

records = class_data.get_class_data()

user_interface(records)