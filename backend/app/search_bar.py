import sqlite3 as sql
import json

# Instructions
# Search Course is where everything is implemented, use it!


class Courses_repository:
    def __init__(self) -> None:
        self.CAMPUS_LIST = (
            "darcy-diurno",
            "darcy-noturno",
            "fce",
            "fga",
            "fup-diurno",
            "fup-noturno",
        )
        self.courses_by_campus = dict.fromkeys(self.CAMPUS_LIST)
        self.ordered_courses = list()

        for campus in self.CAMPUS_LIST:
            connection = sql.connect(
                f"./Documentos/2022-2-Squad06/databases/vest_23/{campus}.db"
            )
            cursor = connection.cursor()
            tmp = list()
            tmp.append(
                cursor.execute(
                    """--sql
                SELECT Cursos
                FROM N000
                WHERE Cursos NOT LIKE 'Total%'
                ORDER BY Cursos;
            """
                ).fetchall()
            )
            self.courses_by_campus[campus] = list()
            for m in tmp:
                for n in m:
                    self.courses_by_campus[campus].append((n[0], campus))
            connection.close()

        self.ordered_courses = self.courses_by_campus[self.CAMPUS_LIST[0]]

        for j in self.CAMPUS_LIST[1:]:
            self.ordered_courses = self.__merge(
                self.ordered_courses, self.courses_by_campus[j]
            )

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
        matches = list()
        for k in range(len(self.ordered_courses)):
            one_match = self.ordered_courses[k][0].find(exp)
            if one_match != -1:
                matches.append(self.ordered_courses[k])
        if jsonfy:
            file = open("./search_result.json", "wt")
            return json.dump(matches, file)
        else:
            return matches
