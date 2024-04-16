import time

# import os
import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def event_stop(cla):
    import numpy as np
    import cv2
    from function import click_pos_reg, click_pos_2, imgs_set_
    from action_zeno import menu_open
    try:
        print("event_stop")

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\event_18\\not_again_view.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(220, 650, 280, 710, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("not_again_view", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\event_18\\today_one.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(220, 650, 480, 750, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("today_one", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)


    except Exception as e:
        print(e)




