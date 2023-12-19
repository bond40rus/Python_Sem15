import argparse
import logging
from student_exeptions import StudentNameError, InvalidSubjectError, InvalidScoreError
from student import Student

logging.basicConfig(filename='studentlog', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    parser = argparse.ArgumentParser(description='Process student information.')
    parser.add_argument('name', help='Student name')
    parser.add_argument('csv_filename', help='CSV filename')
    args = parser.parse_args()

    try:
        student = Student(args.name, args.csv_filename)
        # для примера через Дэбаг
        # student = Student("Алексей Петров", "subjects.csv")
        # student.add_score("Математика", 5)
        # student.add_test_result("Математика", 1005)
        # print(student.average_test_score("Математика"))
        # print(student.average_score())

    except StudentNameError:
        logging.error('Invalid student name format.')
    except InvalidSubjectError as e:
        logging.error(f'Invalid subject: {e.message}')
    except InvalidScoreError as e:
        logging.error(f'Invalid score: {e.message}')


if __name__ == '__main__':
    main()

# для терминала
# python student_log.py sergey subjects.csv - запуск из командной строки
# Здесь student_log.py - имя файла со скриптом, sergey - имя студента, subjects.csv - имя CSV-файла с предметами."""