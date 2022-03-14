from application.salary import *
from application.db.people import *
from datetime import *

if __name__ == '__main__':
    print(f'Текущая дата и время: {datetime.now()}')
    get_employees()
    calculate_salary()