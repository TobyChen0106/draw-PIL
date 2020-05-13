import pyqrcode
for i in range(300):
    code = pyqrcode.create(f'{i}', error='H')
    code.png(f'codes/{i}.png', scale=6)