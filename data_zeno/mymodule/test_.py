import sys
import time

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_
import cv2
import numpy as np
from function import imgs_set_

def go_test():
    print("tst")

    from function import click_pos_2, click_pos_reg

    cla = "one"

    deadgold_find = False
    deadgold_find_count = 0
    while deadgold_find is False:
        deadgold_find_count += 1
        if deadgold_find_count > 10:
            deadgold_find = True

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_dya.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 720, 65, 785, cla, img, 0.88)
        if imgs_ is not None and imgs_ != False:
            print("dead_dya")
            click_pos_reg(imgs_.x + 60, imgs_.y, cla)
            time.sleep(0.2)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_gold.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 720, 65, 785, cla, img, 0.88)
        if imgs_ is not None and imgs_ != False:
            print("dead_gold")
            deadgold_find = True
            time.sleep(0.2)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(20, 720, 65, 785, cla, img, 0.88)
        if imgs_ is not None and imgs_ != False:
            print("dead_potion")
            click_pos_reg(imgs_.x + 60, imgs_.y, cla)
            time.sleep(0.2)
        time.sleep(0.3)




