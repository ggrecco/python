from reportlab.pdfgen import canvas

c = canvas.Canvas("arquivo01.pdf")
#c.drawString(x,y,"escrita, 0,0")
c.drawString(0,0,"escrita, 0,0")
c.drawString(100, 100, "escrita com 100,100")
c.drawString(200, 200, "escrita com 200,200")
c.drawString(300, 300, "escrita com 300,300")
c.drawString(400, 400, "escrita com 400,400")
c.drawString(450, 500, "escrita com 450,500")
c.drawString(475, 450, "escrita com 475,450")
c.drawString(0, 825, "123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-123456789-123")
c.drawString(0, 800, "diferença de 825 para 800")

c.save()
