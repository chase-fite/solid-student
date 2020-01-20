class Student:
    def __init__(self, first_name, last_name, age, cohort_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__cohort_number = cohort_number

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, name):
        if type(name) is str:
            self.__first_name = name
        else:
            raise TypeError('Please provide a string value for first_name')

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, name):
        if type(name) is str:
            self.__last_name = name
        else:
            raise TypeError('Please provide a string value for last_name')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError('Please provide an integer value for age')

    @property
    def cohort_number(self):
        return self.__cohort_number

    @cohort_number.setter
    def cohort_number(self, number):
        if type(number) is int:
            self.__cohort_number = number
        else:
            raise TypeError('Please provide an integer value for cohort number')

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'