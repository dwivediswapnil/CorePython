import PyPDF2
import sys

inputs = sys.argv[1:]#will grab all the arguments(fummy.pdf tilt.pdf rtn.pdf given in the arguments)

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write("super_combined.pdf")

pdf_combiner(inputs)        
