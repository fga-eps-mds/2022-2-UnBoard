import pytest
from app.search_bar import *

class Test_Search:
    def setup_method(self):
        self.search_bar = Courses_repository("../../databases")
    
    def test_len(self):
        self.setup_method()
        result = self.search_bar.search_course("")
        courses = self.search_bar.ordered_courses
        assert (len(courses) == 101) and (len(courses) == len(result))

    def finder(self, exp: str):
        result = self.search_bar.search_course(exp)
        for course in result:
            assert (str(course[0]).find(exp)) != -1

    def test_with_finder(self):
        self.setup_method()
        self.finder("Adm")
        self.finder("")
        self.finder("Bacharelado")
        self.finder("Engenharia")
        self.finder("dnoawkdnsknawod")

    def test_campus(self):
        self.setup_method()
        result = self.search_bar.search_course("")
        alt_result = self.search_bar.search_course("Admnistração")
        for i in result:
            assert i[1] in self.search_bar.CAMPUS_LIST
        for j in result:
            assert j[1] in self.search_bar.CAMPUS_LIST