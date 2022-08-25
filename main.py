import qrcode

code = qrcode.make("https://www.instagram.com/yusadeger/")
code.save("vol1.png")
