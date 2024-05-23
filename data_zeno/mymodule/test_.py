import sys
import time
import requests
import random

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_
import cv2
import numpy as np
from function import imgs_set_

def go_test():
    print("tst")
    import pyautogui
    from function import click_pos_2, click_pos_reg, text_check_get, in_number_check, int_put_, imgs_set_num, imgs_set_for
    from jadong_zeno import jadong_start, jadong_juljun_attack_check, map_list_open_ready, map_list_open, map_list_click, map_junlipoom_open, map_junlipoom_click
    from action_zeno import go_maul, out_check, mine_check, get_market_sohwan_start, get_items, get_event, get_upjuk, confirm_all, dead_die, menu_open
    from potion_zeno import juljun_potion_check, juljun_maul_potion, maul_dead_potion
    from realtime import collection, boonhae, chango_in, all_realtime
    from settings import chago_setting, chago_drag
    from potion_zeno import maul_potion
    from jejak_zenonia import jejak_start, jejak_ready
    from auction_zenonia import auction_ready, auction_start, auction_start2
    from property_zeno import my_property_upload
    from guild_zenonia import guild_check


    cla = "one"

    if cla == "one":
        plus = 0
    elif cla == " two":
        plus = 960
    elif cla == " three":
        plus = 960 * 2
    elif cla == " four":
        plus = 960 * 3

    # v_.now_cla = cla

    maul_dead_potion(cla)
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\realtime\\boonhae\\boonhae_confirm.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(740, 740, 850, 780, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("boonhae_confirm", imgs_)


    # for i in range(10):
    #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\potion\\" + str(i) + ".PNG"
    #     img_array = np.fromfile(full_path, np.uint8)
    #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    #     imgs_ = imgs_set_(380, 980, 402, 1005, cla, img, 0.9)
    #     if imgs_ is not None and imgs_ != False:
    #         print("num ? ", i)

    # print("result", result)
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\property\\zen.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(480, 30, 850, 70, cla, img, 0.8)
    # if imgs_ is not None and imgs_ != False:
    #     print("zen", imgs_)

    # auction_ready(cla)
    # jadong_start(cla, "사냥_미드가르드_고대유적지_43활투")

    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\confirm.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_(490, 610, 650, 650, cla, img, 0.85)
    # if imgs_ is not None and imgs_ != False:
    #     print("confirm", imgs_)

    # chango_in(cla)

    # x_1 = 255
    # x_2 = 270
    # y_1 = 495
    # y_2 = 515
    # #
    # # x_1 = 269
    # # x_2 = 284
    # # 490
    # # 515
    # #
    # # 279
    # # 294
    # # 490
    # # 515
    # #
    # # 289
    # # 304
    # # 490
    # # 515
    #
    # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\number\\vacant.PNG"
    # img_array = np.fromfile(full_path, np.uint8)
    # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    # imgs_ = imgs_set_num(x_1, y_1, x_2, y_2, cla, img, 0.9)
    # if imgs_ is not None and imgs_ != False:
    #     print("숫자 없다", x_1, y_1, x_2, y_2)



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




