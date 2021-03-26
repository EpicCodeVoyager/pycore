class Employee:
    # Initialising or creating the class.
    default_raise = 1.05

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def apply_raise(self):
        self.salary *= self.default_raise

    @property
    def full_name(self):
        return f'{self.fname} {self.lname}'

    @classmethod
    def change_raise(cls, default_raise):
        cls.default_raise = default_raise

    @classmethod
    def from_string(cls, emp_str):
        fname, lname, salary = emp_str.split("-")
        return cls(fname, lname, int(salary))

    @full_name.setter
    def full_name(self, fullname):
        fname, lname = fullname.split(" ")
        self.fname = fname
        self.lname = lname

    @full_name.deleter
    def full_name(self):
        self.fname = None
        self.lname = None

    # Enter and Exit for the with operator.
    def __enter__(self):
        pass

    def __exit__(self):
        pass

    # Iter operator for yield.
    def __iter__(self):
        pass
    # repr for debugging and full employee detail pricing.
    # str for printing for general purpose, print takes str output for display.
    # if str is missing it falls back on repr.
    def __repr__(self):
        return f'Employee({self.fname}, {self.lname}, {self.salary})'


class Developer(Employee):
    default_raise = 1.20

    def __init__(self, fname, lname, salary, tech):
        super().__init__(fname, lname, salary)
        self.tech = tech

    def __add__(self, other):
        return f'Team: {repr(self) + repr(other)}'

    @classmethod
    def from_string(cls, dev_str):
        fn, ln, sal, tech = dev_str.split("-")
        return cls(fn, ln, sal, tech)

    def __repr__(self):
        return f'Developer({self.fname}, {self.lname}, {self.salary}, {self.tech})'


class Manager(Employee):
    def __init__(self, fname, lname, salary, employees=None):
        super().__init__(fname, lname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def __repr__(self):
        return f'Manager({self.fname}, {self.lname}, {self.salary},' \
               f' {[emp.__str__() for emp in self.employees]})'

    def __str__(self):
        return f'Manager({self.full_name})'


e1 = Employee("tiku", "baba", 10000)
e2 = Employee.from_string("piku-baba-10000")

print(e1, e2)
e1.apply_raise()
Employee.change_raise(1.1)
e2.apply_raise()
e1.full_name = "babu baby"
del e2.full_name
print(e1, e2)

d1 = Developer("chiku", "ji", 20000, "Jython")
Developer.change_raise(1.40)
print(d1)
d1.apply_raise()
print(d1)

d2 = Developer.from_string("lala-lajpat-10000-python")
print(d2)

m1 = Manager("sydney", "goodmen", 40000, [d1, d2])
print(m1)

print(isinstance(m1, Manager))
print(issubclass(Developer, Employee))
print(isinstance(d2, Developer))
print(d1 + d2)
