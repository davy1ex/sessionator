import os
import random
from PIL import Image


images = os.listdir(os.path.join(os.getcwd(), 'imgs'))
random.shuffle(images)
result = []


for i in images:

    with Image.open(os.path.join('imgs', i)) as img:
        img.show()
        result.append(str(i) + ": " + input())
        img.close()
        print(result)
