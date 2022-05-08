from email.policy import default

import numpy as np
import cv2
from PIL import ImageGrab
import time

count = 0
while 1:
    count = count + 1
    # 坐标
    # img = ImageGrab.grab(bbox=(430, 160, 1750, 920))
    img = ImageGrab.grab(bbox=None)
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('s', frame)

    if count == 20:
        t = time.time() * 1000
        cv2.imwrite('./data/test/' + str(int(t)) + '.png', frame)
        count = 0

    cv2.waitKey(5)
