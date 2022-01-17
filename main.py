import os
import random
from PIL import Image


images = os.listdir()
random.shuffle(images)
result = []


for i in images:

    with Image.open(i) as img:
        img.show()
        result.append(str(i) + ": " + input())
        img.close()
        print(result)
