import time

# import os
import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def guild_check(cla):
    import numpy as np
    import cv2
    from function import click_pos_reg, click_pos_2, imgs_set_
    from action_zeno import menu_open
    try:
        print("guild_check")

        guild_ = False
        guild_count = 0
        while guild_ is False:
            guild_count += 1
            if guild_count > 10:
                guild_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(220, 990, cla)
                time.sleep(0.1)
                click_pos_2(220, 990, cla)
                time.sleep(0.1)

                guild_ = True

                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\guild\\giboo_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 680, 280, 735, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\guild\\giboo_zero.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 660, 525, 690, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(830, 340, cla)
                            time.sleep(0.2)
                            break
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\guild\\giboo_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 680, 280, 735, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.3)
                    else:
                        click_pos_2(80, 990, cla)
                        time.sleep(0.1)
                        click_pos_2(80, 990, cla)
                    time.sleep(0.5)

                for i in range(5):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\guild\\giboo_zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 660, 525, 690, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(830, 340, cla)
                        time.sleep(0.2)
                        break
                    time.sleep(0.3)

            else:
                menu_open(cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\guild\\menu_guild.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 960, 360, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\guild_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.3)

        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\guild_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 130, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 50, cla)
                time.sleep(0.5)
                break


    except Exception as e:
        print(e)




