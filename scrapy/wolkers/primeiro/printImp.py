from win32printing import Printer
import pandas as pd

df = pd.read_excel("teste_ip.xls")

i = 0

# font = {
#     "height": 24,
# }
# font2 = {
#     "height": 10,
# }
while i < len(df) :
    with Printer(linegap=2) as printer:
        printer.text(df['PC'][i], align="center", font_config={"height": 24})
        printer.text(df['IP'][i], align="center", font_config={"height":10})
        i = i + 1