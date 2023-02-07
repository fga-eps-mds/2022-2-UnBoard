
import pandas as pd

def search_courses_by_year(year):
    try:
        df = pd.read_csv(".\databases\VESTUNB_15")
    except Exception as e:
        print(f"An error occured while reading the file: {e}")
        return None
    if year == 15:
        courses = df.iloc[9:67][1].tolist()
    elif year == 16:
        courses = df.iloc[18:77][1].tolist()
    elif year == 17:
        courses = df.iloc[9:68][1].tolist()
    elif year == 18:
        courses = df.iloc[9:68][1].tolist()
    elif year == 19:
        courses = df.iloc[11:70][1].tolist()
    elif year == 22:
        courses = df.iloc[12:73][1].tolist()
    elif year == 23:
        courses = df.iloc[12:74][1].tolist()
    else:
        return None
    return courses
