"""-- Student registration system --
- This is a program that can register students into txt.archives by their name, email and course 
- The program can do the following functions:
-- Register students
-- List students
-- Search students
-- Remove students

Author: Pedro-r-f
Date: 11/04/2025"""


def register_students():
    "Function that registers the students name, email and course"
    student_name = str(input('Type the student name: '))
    student_email = input('Type the student email: ')
    student_course = str(input('Type the current course of the student'))
    with open('students.txt', 'a', encoding='utf-8') as archive:
        archive.write(f'{student_name}, {student_email}, {student_course}\n')
    print(f'The student {student_name} has been sucessfully registered!\n')

def list_students():
    "This function will list all the current registered students"
    try:
        with open('students.txt', 'r', encoding='utf-8') as archive:
            content = archive.readlines()

        if not content:
            print(f'No students have been registered yet.')
        else:
            print(f'The registered students are the following:\n')
            for lines in content:
                print(f'{lines.strip()}\n')
    except FileNotFoundError:
        print(f'A student file has not been created yet, try registering someone first.')


def search_students():
    "This function will help to search the name of a student if it is registered"
    try:
        student_search = str(input('Type the student name to see if it is registered: '))
        with open('students.txt', 'r', encoding='utf-8') as archive:
            content = archive.read()
        if student_search.lower() in content.lower():
            print(f'The student {student_search} is registered!\n')
        else:
            print(f'The student {student_search} is not registered.\n')
    except FileNotFoundError:
        print('A student file has not been created yet, try registering someone first.')

def remove_students():
    "This function will remove the selected student"
    try:
        student_name = str(input('Type the name of the student that you want to be removed: '))
        with open('students.txt', 'r', encoding='utf-8') as archive:
            content = archive.readlines()
        updated_list = [student for student in content if student_name.lower() not in student.lower()]
        if len(content) == len(updated_list):
            print(f'The student name {student_name} has not been registered.')
        else:
            with open('students.txt', 'w', encoding='utf-8') as archive:
                archive.writelines(updated_list)
            print(f'The student named {student_name} has been sucessfully removed!')
    except FileNotFoundError:
        print('A student file has not been created yet, try registering someone first.')

menu = {1:register_students, 2:list_students, 3:search_students, 4:remove_students}
"Menu made to interact with the functions"

while True:
    try:
        choices = int(input('1 - Register student\n' \
        '2 - List students\n' \
        '3 - Search student\n' \
        '4 - Remove student\n' \
        '5 - Exit program\n' \
        'Your choice: '))

        if choices in menu:
            menu[choices]()
        elif choices == 5:
            print('Exiting program...')
            break
        else:
            print('Insert a valid value\n')
    except ValueError:
        print('Please insert a valid number')











    
    


    


