import tabula as tb
import pandas

tables = tb.read_pdf("pdfs/VESTUNB_23.PDF", pages=1)
print(tables)


#for table in tables:
#    print(table.head())