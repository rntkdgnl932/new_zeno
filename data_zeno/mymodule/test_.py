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

    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\out\\out_talk.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(290, 870, 340, 920, cla, img, 0.85)
    if imgs_ is not None and imgs_ != False:
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_click_0.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("퀘스트 클릭")
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quest_look\\quest_look.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(880, 100, 960, 170, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)




