import Image

im = Image.open('./../static/img/bqb/dog.png')

out1 = im.resize((32,32))
out2 = im.resize((64,64))
out1.save("doge.png","PNG")
out2.save("doge@2x.png","PNG")