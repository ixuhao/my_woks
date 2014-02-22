# coding: utf-8
# Last modified: 2014 Feb 07 9:37:49 AM

class Clock(object):
    def __init__(self):
        self.__hour = 1

    def __getHour(self):
        return self.__hour

    def __setHour(self, hour):
        if 25 > hour > 0: self.__hour = hour
        else: raise BadHourException

    hour = property(__getHour, __setHour)

class Student(object):
    def __init__(self):
        self._count = 1

    @property
    def count(self):
        """getter, read only attribute"""
        return self._count

    @count.setter
    def count(self, new_count):
        self._count = new_count

clock = Clock()
print clock.hour
clock.hour = 2
print clock.hour

student = Student()
student.count = 120
print student.count
