import pandas as pd
import json



class Courses_list(list):
    def __init__(self, year: int) -> None:
        super()
        self.year_edition = year
        raw_list = self.__read_source_table(self.year_edition)
        self.diurnal :list = raw_list[0]
        self.nocturnal : list = raw_list[1]
        self.ordered_list: list = self.__merge(self.diurnal, self.nocturnal)
        
    def __read_source_table(self, year: int):
        result = ([], [])
        # result = (diurnal list, nocturnal list)
        if year == 23:
            courses = list(pd.read_excel(f"./pdfs/VESTUNB_{year}.xlsx").get(0)[7:])
            sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result[0].append((day_course, "Diurno"),)
            for night_course in courses[(sep + 3) : (len(courses) - 1)]:
                result[1].append((night_course, "Noturno"),)
        elif year == 22:
            courses = list(pd.read_excel(f"./pdfs/VESTUNB_{year}.xlsx").get("Unnamed: 0")[12:])
            sep = courses.index("Total Diurno")
            for day_course in courses[:sep]:
                result[0].append((day_course, "Diurno"),)
            for night_course in courses[(sep + 2): (len(courses) - 1)]:
                result[1].append((night_course, "Noturno"),)
        return result

    def __merge(self, list1: list, list2: list) -> list:
        """Merges two ordered lists preserving their order.

        Args:
            list1 (list): ordered list.
            list2 (list): ordered list.

        Returns:
            list: returns a new list with the merge of both argument's lists.
        """
        result = list()
        pointer1, pointer2, max1, max2 = 0, 0, False, False
        try:
            while True:
                if list1[pointer1][0] <= list2[pointer2][0]:
                    result.append(list1[pointer1])
                    pointer1 += 1

                elif list1[pointer1][0] > list2[pointer2][0]:
                    result.append(list2[pointer2])
                    pointer2 += 1
        except IndexError:
            try:
                while True:
                    result.append(list1[pointer1])
                    pointer1 += 1
            except IndexError:
                try:
                    while True:
                        result.append(list2[pointer2])
                        pointer2 += 1
                except IndexError:
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
    print(o.search_course("Adm"))
