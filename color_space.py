#Referencia: https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/Image__class_Image.html

from PIL import Image
url = "imagem.png" #mudar diretorio
img= Image.open(url)
r, g, b = img.split()
blk = Image.new("L", r.size, "black")

#Canais Red, Green e Blue
Image.merge("RGB", (r, blk, blk)).save("only_red.jpg") 
Image.merge("RGB", (blk, g, blk)).save("only_green.jpg") 
Image.merge("RGB", (blk, blk, b)).save("only_blue.jpg") 

#Canais Y, Cb, Cr
img2 = img.convert("YCbCr")
y, cb, cr = img2.split()
Image.merge("YCbCr", (y, blk, blk)).convert("L").save("channel_y.jpg")
Image.merge("YCbCr", (blk, cb, blk)).save("channel_cb.jpg")
Image.merge("YCbCr", (blk, blk, cr)).save("chanel_cr.jpg")
