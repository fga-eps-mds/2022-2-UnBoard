import tabula as tb
import pandas

tables = tb.read_pdf("pdfs/VESTUNB_23.PDF", pages=1)
#print(tables)
tb.convert_into("pdfs/VESTUNB_23_copy.PDF", "spikes/output.csv", output_format="csv", pages="all")


#for table in tables:
#    print(table)    