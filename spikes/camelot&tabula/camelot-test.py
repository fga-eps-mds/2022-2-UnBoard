from camelot import *
from pandas import *
import time

start = time.time()
tables = read_pdf("pdfs/VESTUNB_23.PDF", pages="all")
#tables.export("pdfs/VESTUNB_23.db", f="sqlite")
tables = tables[0].df
tables = DataFrame(tables)
print(tables)
print(time.time() - start)