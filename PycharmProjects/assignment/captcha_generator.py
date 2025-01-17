from captcha.image import ImageCaptcha
import numpy as np
from PIL import Image
import random
import cv2

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

data_path = '/home/wlj/PycharmProjects/'


def random_captcha_text(char_set=number, captcha_size=4):  # 可以设置只用来生成数字
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text


def gen_capthcha_text_and_image(m):
    image = ImageCaptcha()
    captcha_text = random_captcha_text()
    captcha_text = ' '.join(captcha_text)
    captcha = image.generate(captcha_text)
    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    with open(data_path + "test_label.txt", "a") as f:
        f.write(captcha_text)
        f.writelines("\n")
    cv2.imwrite(data_path + 'test/' + '%s.jpg' %m, captcha_image)

if __name__ == '__main__':
    for m in range(0, 500):
        gen_capthcha_text_and_image(m)