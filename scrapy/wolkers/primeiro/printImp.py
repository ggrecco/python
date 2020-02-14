from win32printing import Printer

font = {
    "height": 32,
}
font2 = {
    "height": 12,
}
with Printer(linegap=1) as printer:
    printer.text("HMGV123", font_config=font)
    printer.text("192.168.X.X", font_config=font2)
