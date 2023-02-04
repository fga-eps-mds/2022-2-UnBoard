import pandas as pd
import json

class Courses_list(list):
    def __init__(self, year: int) -> None:
        super().__init__()
        self.year_edition = year
        raw_list = self.__read_source_table(self.year_edition)
        self.diurnal :list = raw_list[0]
        self.ordered_list: list = self.diurnal
        
    def __read_source_table(self, year: int):
        result = []
        # result = (diurnal list, nocturnal list)
        if year == 23:
            courses = list(pd.read_excel(f"databases/VESTUNB_{year}.xlsx").get(1)[12:])
            #sep = courses.index("Total Diurno")
            sep = 74
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        elif year == 22:
            courses = list(pd.read_excel(f"databases/VESTUNB_{year}.xlsx").get(1)[12:])
           # sep = courses.index("Total Diurno")
            sep = 73
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        elif year == 19:
            courses = list(pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx").get(1)[12:])
            #sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        elif year == 18:
            courses = list(pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx").get(1)[10:])
           # sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        elif year == 17:
            courses = list(pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx").get(1)[10:])
            #sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        elif year == 16:
            courses = list(pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx").get(1)[19:])
            #sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        elif year == 15:
            courses = list(pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx").get(1)[10:])
            #sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result.append((day_course, "Diurno"),)
        return result

    def search_course(self, exp: str, jsonfy=False) -> list:
        """Search courses based on ordened_list property.

        Args:
            exp (str): an expression, it can be a letter, word or even a whole text.
            jsonfy (bool, optional): if true, the return value will be a json. Defaults to False, which returns a dictionary.

        Returns:
            list: returns the components with matching names in json or dict format.
        """
        matches = list()
        for k in range(len(self.ordered_list)):
            one_match = self.ordered_list[k][0].find(exp)
            if one_match != -1:
                matches.append(self.ordered_list[k])
        if jsonfy:
            file = open("./search_result.json", "wt")
            return json.dump(matches, file)
        else:
            return matches

if __name__ == '__main__':
    o = Courses_list(23)
    print(o.ordered_list)

if __name__ == '__main__':
    o = Courses_list(22)
    print(o.ordered_list)
