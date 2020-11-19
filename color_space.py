from PIL import Image
url = "/home/sbgui/Documentos/Faculdade/2020.3/PDI/Seminário/teste.png"
img= Image.open(url)
r, g, b = img.split()
blk = Image.new("L", r.size, "black")

Image.merge("RGB", (r, blk, blk)).save("only_red.jpg")
Image.merge("RGB", (blk, g, blk)).save("only_green.jpg")
Image.merge("RGB", (blk, blk, b)).save("only_blue.jpg")

img2 = img.convert("YCbCr")
y, cb, cr = img2.split()
Image.merge("YCbCr", (y, blk, blk)).convert("L").save("1.jpg")
Image.merge("YCbCr", (blk, cb, blk)).save("2.jpg")
Image.merge("YCbCr", (blk, blk, cb)).save("3.jpg")

#Referencia: https://hhsprings.bitbucket.io/docs/programming/examples/python/PIL/Image__class_Image.html