from application.salary import calculate_salary
from application.db.people import get_employees
import datetime as dt

if __name__ == '__main__':
    print(f'Текущая дата и время: {dt.datetime.now()}')
    get_employees()
    calculate_salary()


