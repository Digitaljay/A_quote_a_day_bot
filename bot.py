import telebot
import random
from PIL import Image, ImageFont, ImageDraw
import wikiquotes
import time


def background():
    r,g,b=random.randint(1,256), random.randint(1,256), random.randint(1,256)
    im = Image.new("RGB", (700, 700), (r,g,b))
    im.save("quote.png", "PNG")
    return r+g+b>384

def add_text(quote,x,y,color):
    fnt = ImageFont.truetype("arb.ttf", 25)
    im = Image.open("quote.png")
    dr = ImageDraw.Draw(im)
    dr.text((x,y),quote, font=fnt, fill=(color,color,color), align="center")
    im.save("quote.png")

def gen_quote():
    return wikiquotes.quote_of_the_day("english")

def spliter(quote):
    res=''
    go=0
    edge=45
    for i in quote.split():
        if go+len(i)>edge:
            res+='\n'
            go=0
        res+=i+" "
        go+=len(i)+1
    return res

def quote_pict():
    fill=background()
    add_text(spliter(gen_quote()[0]),20,20,fill*256)
    add_text(spliter(gen_quote()[1]),400,650,fill*256)

f=open("config.txt")
token = f.readline().strip()
f.close()

class Bot():
    def __init__(self, token):
        self.eva = telebot.TeleBot(token)

    def send_text_tg(self,information):
        self.eva.send_message("@quote_a_day", information)

    def send_img_tg(self, img):
        self.eva.send_photo("@quote_a_day", img)


bot=Bot(token)
quote_pict()
time.sleep(8*60*60)

while True:
    quote_pict()
    img=open("quote.png","rb")
    bot.send_img_tg(img)
    time.sleep(60*60*24)

