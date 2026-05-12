import pytest
from employee import Employee
from manager import Manager


def test_dept():
    man1 = Manager('George', 5000, 'Plot graphs', 'Data Analytics')
    assert man1.is_tech_department()

def test_paid_more():
    man2 = Manager('Aurel', 10000, 'Coding', 'Cybersecurity')
    emp1 = Employee('Maria', 2000)
    assert man2.salary > emp1.salary 

def test_annual_salary():
    man3 = Manager('John', 500, 'Cleaning windows', 'Sanitation')
    assert man3.get_annual_salary() == 2000
