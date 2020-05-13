from PIL import Image, ImageDraw, ImageFont

code_size = (120, 120)
img_w, img_h = code_size
image = Image.new('RGB', (2100, 2970), (255, 255, 255))


draw = ImageDraw.Draw(image)
for i in range(17):
    draw.line([(0, 120+i*170), (2100, 120+i*170)], fill="black", width=0)

for i in range(5):
    draw.line([(100+i*385, 0), (100+i*385, 2970)], fill="black", width=0)
    draw.line([(100+i*385+360, 0), (100+i*385+360, 2970)],
              fill="black", width=0)

# font = ImageFont.truetype("arial", 14)
# text_base_img = Image.new('RGBA', (200, 145), "white")
# text_draw = ImageDraw.Draw(text_base_img)
# text_draw.text((0, 125), "EE.CROSSING.TEAM 2020", fill="black", font=font)

# font2 = ImageFont.truetype("Anton-Regular.ttf", 100)
# font3 = ImageFont.truetype("Anton-Regular.ttf", 80)
# offset = 0
# for i in range(16):
#     for j in range(5):
#         code = Image.open(f'codes/{i*5+j+offset}.png', 'r')
#         code = code.resize(code_size)
#         code = code.rotate(90, expand=True)

#         image.paste(code, (100+25+385*j, 120+25+170*i))

#         text_num_img = Image.new('RGBA', (120, 120), "black")
#         text_draw = ImageDraw.Draw(text_num_img)
#         if(len(str(f"{i*5+j+offset}")) > 2):
#             w, h = text_draw.textsize(f"{i*5+j+offset}", font=font3)
#             x = (120-w)
#             if x < 0:
#                 x = 0
#             text_draw.text(((120-w)/2, (120-h)/2-5),
#                            f"{i*5+j+offset}",   font=font3)
#         else:
#             w, h = text_draw.textsize(f"{i*5+j+offset}", font=font2)
#             x = (120-w)
#             if x < 0:
#                 x = 0
#             text_draw.text(((120-w)/2, (120-h)/2-5),
#                            f"{i*5+j+offset}",   font=font2)

#         text_num_img = text_num_img.rotate(90, expand=True)
#         text_base_img.paste(text_num_img, (55, 0))

#         image.paste(text_base_img, (100+25+385*j+130, 120+25+170*i))

image.save(f'small.png')
