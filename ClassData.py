import sqlite3

# Connects to sqlite database to retrieve class records that were provided in assignment
class ClassData:
    def __init__(self, db_path):
        self.__db_connection = sqlite3.connect(db_path)
        self.__class_dictionary = {}
        self.__retrieve_class_data()

    def __retrieve_class_data(self):
        # First dictionary as outlined in assignment
        cursor = self.__db_connection.cursor()
        cursor.execute("SELECT course_number, room_number FROM classmaster")
        temp_dict_rooms = dict(cursor.fetchall())

        # Second dictionary as outlined in assignment
        cursor.execute("SELECT course_number, instructor FROM classmaster")
        temp_dict_instructors = dict(cursor.fetchall())

        # Third dictionary as outlined in assignment
        cursor.execute("SELECT course_number, meeting_time FROM classmaster")
        temp_dict_meetings = dict(cursor.fetchall())

        # Calls the merge_master_class_dictionary method to merge all dictionary records under respective class key
        self.__merge_master_class_dictionary(temp_dict_rooms, temp_dict_instructors, temp_dict_meetings)

    def __merge_master_class_dictionary(self, rooms, instructors, meetings):
        for key in rooms:
            self.__class_dictionary.update({key : {'room': 0, 'instructor': 'default', 'meeting': 'default'}})

        for key in rooms:
            self.__class_dictionary[key]['room'] = rooms[key]
            self.__class_dictionary[key]['instructor'] = instructors[key]
            self.__class_dictionary[key]['meeting'] = meetings[key]

    def get_class_data(self):
        return self.__class_dictionary