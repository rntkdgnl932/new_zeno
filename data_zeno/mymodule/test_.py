import sys
import time
import requests

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_
import cv2
import numpy as np
from function import imgs_set_

def go_test():
    print("tst")

    from function import click_pos_2, click_pos_reg, text_check_get, in_number_check, int_put_
    from jadong_zeno import jadong_start
    from action_zeno import gold_check_open, out_check, now_hunting
    from server import server_get_version, server_get_zeno
    cla = "three"
    v_.now_cla = cla

    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\zenonia_title_2.PNG"
    img_array = np.fromfile(full_path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    imgs_ = imgs_set_(0, 50, 960, 1030, v_.now_cla, img, 0.8)
    if imgs_ is not None and imgs_ != False:
        click_pos_reg(imgs_.x - 40, imgs_.y, cla)
        print("qhdu", imgs_)
    else:
        print("no look")

    # # 층수 클릭
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\one_step.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("one_step", imgs_)
    #     x1 = imgs_.x
    #     y1 = imgs_.y
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #     if imgs_ is not None and imgs_ != False:
    #         print("one_step1 : lock_step", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #         if imgs_ is not None and imgs_ != False:
    #             print("one_step2 : lock_step", imgs_)
    #         else:
    #             print("one_step : 클릭하자")
    # else:
    #     print("one_step 없", imgs_)
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\two_step.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("two_step", imgs_)
    #     x1 = imgs_.x
    #     y1 = imgs_.y
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #     if imgs_ is not None and imgs_ != False:
    #         print("two_step1 : lock_step", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #         if imgs_ is not None and imgs_ != False:
    #             print("two_step2 : lock_step", imgs_)
    #         else:
    #             print("two_step : 클릭하자")
    # else:
    #     print("two_step 없", imgs_)
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\three_step.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("three_step", imgs_)
    #     x1 = imgs_.x
    #     y1 = imgs_.y
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #     if imgs_ is not None and imgs_ != False:
    #         print("three_step1 : lock_step", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #         if imgs_ is not None and imgs_ != False:
    #             print("three_step2 : lock_step", imgs_)
    #         else:
    #             print("three_step : 클릭하자")
    # else:
    #     print("three_step 없", imgs_)
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\four_step.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("four_step", imgs_)
    #     x1 = imgs_.x
    #     y1 = imgs_.y
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #     if imgs_ is not None and imgs_ != False:
    #         print("four_step1 :lock_step", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #         if imgs_ is not None and imgs_ != False:
    #             print("four_step2 : lock_step", imgs_)
    #         else:
    #             print("four_step : 클릭하자")
    # else:
    #     print("four_step 없", imgs_)
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\five_step.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("five_step", imgs_)
    #     x1 = imgs_.x
    #     y1 = imgs_.y
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #     if imgs_ is not None and imgs_ != False:
    #         print("five_step1 : lock_step", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #         if imgs_ is not None and imgs_ != False:
    #             print("five_step2 : lock_step", imgs_)
    #         else:
    #             print("five_step : 클릭하자")
    # else:
    #     print("five_step 없", imgs_)
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\six_step.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("six_step", imgs_)
    #     x1 = imgs_.x
    #     y1 = imgs_.y
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #     if imgs_ is not None and imgs_ != False:
    #         print("six_step1 : lock_step", imgs_)
    #     else:
    #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
    #         img_array = np.fromfile(full_path, np.uint8)
    #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #         imgs_ = imgs_set_(x1, y1 - 50, x1 + 50, y1, cla, img, 0.85)
    #         if imgs_ is not None and imgs_ != False:
    #             print("six_step2 : lock_step", imgs_)
    #         else:
    #             print("six_step : 클릭하자")
    # else:
    #     print("six_step 없", imgs_)

    # jadong_start(cla, "사냥_미드가르드_로렐라이강_17갑옷")
    # jadong_start(cla, "사냥_미드가르드_엘라움계곡_30목걸이장갑")
    # gold_check_open(cla)




    # jadong_start(cla, "사냥_미드가르드_카나크협곡_34갑벨")
    # jadong_start(cla, "사냥_미드가르드_로쿠광산_37장벨귀")




