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
    import pyautogui
    from function import click_pos_2, click_pos_reg, text_check_get, in_number_check, int_put_, imgs_set_num
    from jadong_zeno import jadong_start, jadong_juljun_attack_check
    from action_zeno import go_maul, out_check, mine_check
    from potion_zeno import juljun_potion_check, juljun_maul_potion
    from realtime import collection, boonhae, chango_in, all_realtime
    from settings import chago_setting, chago_drag
    from potion_zeno import maul_potion
    from jejak_zenonia import jejak_start, jejak_ready
    from auction_zenonia import auction_ready, auction_start, auction_start2
    from property_zeno import my_property_upload


    cla = "one"
    # v_.now_cla = cla

    # chago_setting(cla)

    # auction_ready(cla)
    my_property_upload(cla)

    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(200, 200, 250, 250, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("lock", imgs_)




    # result_low = auction_start(cla)
    # print("result_low", result_low)
    # result_many = auction_start2(cla)
    # print("result_many", result_many)

    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\4.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_num(269, 460, 283, 480, cla, img, 0.99)
    # if imgs_ is not None and imgs_ != False:
    #     print("4", imgs_)
    # else:
    #     print("없다..")

    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\vacant.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_num(256, 485, 267, 500, cla, img, 0.99)
    # if imgs_ is not None and imgs_ != False:
    #     print("숫자 없다", imgs_)
    # else:
    #     print("숫자 있다")

    # red_hwangya_1
    # jadong_juljun_attack_check(cla, "특수_마족_1")
    #
    # title_ = text_check_get(42, 90, 140, 160, cla)
    # print("title_", title_)

    # get_season_pass(cla)

    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\zenonia_title_2.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # # 제노는 4클라 고정
    # imgs_ = imgs_set_(0, 50, 960, 1030, v_.now_cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("보여", imgs_)
    # else:
    #     print("아보여")

    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\zenonia_start_ready.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(0, 200, 960, 350, v_.now_cla, img, 0.7)
    # if imgs_ is not None and imgs_ != False:
    #     print("매크로를 내려야 실행됨...10초", imgs_)
    # else:
    #     print("매크로 제목 안 보여")
    #
    #(50, 370, 320, 730, cla, img, 0.85)
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\chango\\guisok.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # for i in pyautogui.locateAllOnScreen(img, region=(50, 370, 270, 360), confidence=0.8):
    #     # for i in pyautogui.locateAllOnScreen(img, region=(810 + plus, 110, 945 + plus, 985),
    #     #                                      confidence=0.7):
    #     last_x = i.left
    #     last_y = i.top
    #     print("last_x", last_x)
    #     print("last_y", last_y)




