import time

# import os
import sys

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_



def jejak_ready(cla):
    import numpy as np
    import cv2
    from action_zeno import menu_open
    from function import click_pos_2, click_pos_reg, imgs_set_
    try:
        print("jejak_ready")


        jejak_ = False
        jejak_count = 0
        while jejak_ is False:
            jejak_count += 1
            if jejak_count > 7:
                jejak_ = True
            print("jejak_count", jejak_count)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_jaelyo_jangbi.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 70, 190, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    jejak_start(cla)
                    jejak_ = True
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jangbi_click.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(120, 120, 180, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jaelyo_click.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(5, 120, 70, 180, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_etc.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(500, 70, 720, 120, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
            else:
                menu_open(cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\menu_jejak.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 950, 530, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)
            time.sleep(0.5)
        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 50, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)


def jejak_start(cla):
    import numpy as np
    import cv2
    import os
    from action_zeno import menu_open
    from function import click_pos_2, click_pos_reg, imgs_set_
    try:
        print("jejak_ready")
        dir_path = "C:\\my_games\\zenonia"
        file_path1 = dir_path + "\\data_zeno\\imgs\\jejak\\jejak_list_1.txt"
        with open(file_path1, "r", encoding='utf-8-sig') as file:
            jejak_list_1 = file.read().splitlines()
        file_path2 = dir_path + "\\data_zeno\\imgs\\jejak\\jejak_list_2.txt"
        with open(file_path2, "r", encoding='utf-8-sig') as file:
            jejak_list_2 = file.read().splitlines()


        # 마법으로 전환
        for i in range(len(jejak_list_1)):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\" + jejak_list_1[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(110, 110, 420, 920, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                x_reg = imgs_.x
                y_reg = imgs_.y

                click_pos_reg(x_reg, y_reg, cla)
                time.sleep(0.5)

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 970, 900, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(760, 1000, cla)
                    time.sleep(0.1)
                    click_pos_2(760, 1000, cla)
                    time.sleep(0.5)
                    click_pos_2(860, 1000, cla)
                    time.sleep(0.5)


                    for k in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 970, 520, 1020, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for z in range(10):
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 970, 520, 1020, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(1)
                for y in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
                time.sleep(0.3)
            time.sleep(0.3)

        # 희귀로 전환전에 다시 재설정
        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_skillbook_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(120, 190, 190, 240, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for k in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_jaelyo_skillbook.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 120, 70, 190, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)

                break
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jaelyo_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 70, 170, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)

        # 다시 돌아오기
        for i in range(5):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jangbi_click.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(120, 120, 180, 180, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

                for k in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_jaelyo_jangbi.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 120, 70, 190, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.2)

                break
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jaelyo_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(10, 120, 70, 170, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)

        # 희귀로 전환
        for i in range(len(jejak_list_2)):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\" + jejak_list_2[i] + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(110, 110, 420, 920, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                x_reg = imgs_.x
                y_reg = imgs_.y

                click_pos_reg(x_reg, y_reg, cla)
                time.sleep(0.5)

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_click.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 970, 900, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(760, 1000, cla)
                    time.sleep(0.5)
                    click_pos_2(860, 1000, cla)
                    time.sleep(0.5)

                    for k in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\close.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 970, 520, 1020, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            for z in range(10):
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\close.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(440, 970, 520, 1020, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                                time.sleep(0.5)
                            break
                        time.sleep(1)
                for y in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)
                time.sleep(0.3)
            time.sleep(0.3)

        # 나가기
        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 50, cla)
            else:
                break

    except Exception as e:
        print(e)

