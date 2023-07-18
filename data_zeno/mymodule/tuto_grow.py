# import random
# import pyautogui
# import pytesseract
# import numpy as np
# import numpy
# from PIL import Image
# import re
# import cv2
import time
import sys
sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_

def tuto_grow_start(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_2, click_pos_reg
    from action_zeno import dead_die, bag_open, get_items, quickslot_check, in_maul_check
    from potion_zeno import potion_check_tuto
    try:

        result_dead = dead_die(cla)

        result_maul = in_maul_check(cla)
        if result_maul == True:
            potion_check_tuto(cla)

        if result_dead == True:
            print("장비와 스킬을 다시 갖추자")

            # 장비 입기
            bag_open(cla)
            click_pos_2(730, 350, cla)
            time.sleep(0.2)
            for i in range(5):
                jangbi = 'jangbi_' + str(i)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\tuto_jangbi\\" + jangbi + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    x_reg = imgs_.x
                    y_reg = imgs_.y
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\e.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg - 50, y_reg - 50, x_reg, y_reg, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        time.sleep(0.2)
                    else:
                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(0.2)
                        click_pos_reg(x_reg, y_reg, cla)
                        time.sleep(0.5)
                else:
                    pass

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            get_items(cla)

            quickslot_check(cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("가방 열려있다. 10초 뒤 닫겠당.")

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\tuto_jangbi\\jangbi_0.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                x_reg = imgs_.x
                y_reg = imgs_.y
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\e.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_reg - 50, y_reg - 50, x_reg, y_reg, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    time.sleep(0.2)
                else:
                    click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.2)
                    click_pos_reg(x_reg, y_reg, cla)
                    time.sleep(0.5)

            for i in range(11):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("가방 오픈중", i)
                    if i > 9:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        break
                else:
                    break
                time.sleep(1)
        else:
            level_up_point(cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_ing_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 740, 940, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("quest_ing_1...퀘스트 진행중", imgs_)
            potion_check_tuto(cla)
        else:
            print("퀘스트 클릭하자")
            # 스킵
            tuto_skip(cla)

            # m 및 퀘스트 수락
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\m.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 820, 550, 860, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                move_ = True
                while move_ is True:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\m.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 820, 550, 860, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("m...이동중", imgs_)
                    else:
                        move_ = False
                    time.sleep(3)
            else:

                skip_ready = False
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\gabang_skip_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 460, 420, 610, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    skip_ready = True
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skill_skip_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 460, 420, 610, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    skip_ready = True
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\menu_skip_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 460, 420, 610, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    skip_ready = True
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\wichi_skip_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 500, 840, 590, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    skip_ready = True
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\mystatus_skip_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 500, 840, 590, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    skip_ready = True
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\mohumga_skip_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(560, 500, 840, 590, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    skip_ready = True


                if skip_ready == True:
                    ready_ = False
                    ready_count = 0
                    while ready_ is False:
                        ready_count += 1
                        if ready_count > 10:
                            ready_ = True
                            tuto_quest(cla)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_3.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 30, 960, 120, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("gabang_ready : skip_3", imgs_)
                            ready_ = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_4.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(800, 30, 960, 120, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("gabang_ready : skip_4", imgs_)
                                ready_ = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                else:
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
                            dead_die(cla)
                            tuto_quest(cla)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quest_look\\quest_look.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(880, 100, 960, 170, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)



        print('hi tuto_grow_start!', cla)
    except Exception as e:
        print(e)
        return 0


def tuto_1(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_2
    try:
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\joystick.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 960, 500, 1050, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("joystick", imgs_)
            click_pos_2(900, 115, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\attack_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 960, 700, 1050, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("attack_1", imgs_)
            click_pos_2(820, 920, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 30, 960, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("attack_1", imgs_)
            click_pos_2(820, 920, cla)

    except Exception as e:
        print(e)
        return 0

def level_up_point(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    try:
        print("level_up_point")
        # 체크 후 스텟 업

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\levelup_check\\levelup_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(40, 25, 80, 60, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("level_up_check", imgs_)
            reg_x = imgs_.x - 20
            reg_y = imgs_.y + 8

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_soolock_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 600, 700, 700, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest_soolock_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_soolock_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 600, 700, 700, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("quest_soolock_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

            click_pos_reg(reg_x, reg_y, cla)
            time.sleep(1)

            str_look = False
            str_look_count = 0
            while str_look is False:
                str_look_count += 1
                if str_look_count > 10:
                    str_look = True
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\levelup_check\\str.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 360, 120, 390, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\levelup_check\\zero.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 370, 550, 410, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        # 스탯 업 스톱
                        str_look = True
                        click_pos_2(530, 760, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\levelup_check\\str.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(60, 360, 120, 390, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(285, 345, cla)
                            time.sleep(0.5)
                    else:
                        # dex 클릭
                        click_pos_2(390, 555, cla)
                        time.sleep(0.2)
                else:
                    click_pos_reg(reg_x, reg_y, cla)
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def tuto_skip(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_zeno import menu_open_check
    try:
        print('skip!', cla)



        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("skip_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("skip_3", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\skip_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 30, 960, 120, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("skip_4", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\no_look.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 580, 480, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("no_look", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\level_up_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 420, 520, 460, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("level_up_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\contents_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(415, 115, 525, 180, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("contents_open", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 600, 640, 640, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        result_memu = menu_open_check(cla)
        if result_memu == True:
            click_pos_2(915, 55, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_quest(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2
    from action_zeno import bag_open
    try:
        print('tuto_quest!', cla)
        boho_ = False

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\boho\\quest_boho.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            boho_ = True

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\boho\\seline.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            boho_ = True
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\boho\\marujok.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            boho_ = True
        if boho_ == True:
            click_pos_2(905, 790, cla)
            for i in range(100):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_click_00.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 80, 890, 150, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_quest_exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 20, 700, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        time.sleep(2)
                time.sleep(2)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_click_0.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_click_00.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 80, 890, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest_click_00", imgs_)
                click_pos_2(865, 110, cla)

                quest_confirm_ready = False
                quest_confirm_ready_count = 0
                while quest_confirm_ready is False:
                    quest_confirm_ready_count += 1
                    if quest_confirm_ready_count > 10:
                        quest_confirm_ready = True
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 500, 740, 740, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_confirm", imgs_)
                        quest_confirm_ready = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        for i in range(20):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\auto_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(850, 740, 940, 820, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("이동중", i)
                            else:
                                break
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_ing_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(850, 740, 940, 820, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)

                    time.sleep(0.2)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_click_0.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("quest_click_0", imgs_)
                    click_pos_reg(imgs_.x + 100, imgs_.y + 15, cla)
        else:

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_click_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(650, 80, 880, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest_click_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_soolock_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 600, 700, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("quest_soolock_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_soolock_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(480, 600, 700, 700, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest_soolock_2", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\quest\\quest_bosang_get_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 600, 550, 730, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("quest_bosang_get_1", imgs_)

            reg_x = imgs_.x
            reg_y = imgs_.y

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 600, 520, 700, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("select_3", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(1)
                click_pos_reg(reg_x, reg_y, cla)
                bag_open(cla)
                click_pos_2(730, 750, cla)
                selected = False
                selected_count = 0
                while selected is False:
                    selected_count += 1
                    if selected_count > 5:
                        selected = True
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 350, 950, 750, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
            else:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(430, 600, 520, 700, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("select_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(1)
                    click_pos_reg(reg_x, reg_y, cla)
                    bag_open(cla)
                    click_pos_2(730, 750, cla)
                    selected = False
                    selected_count = 0
                    while selected is False:
                        selected_count += 1
                        if selected_count > 5:
                            selected = True
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(640, 350, 950, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(430, 600, 520, 700, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("select_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                        click_pos_reg(reg_x, reg_y, cla)
                        time.sleep(0.5)
                        click_pos_reg(reg_x, reg_y, cla)
                        # 추후에 스킬 장착하기
            # 마무리
            click_pos_reg(reg_x, reg_y, cla)

    except Exception as e:
        print(e)
        return 0

def tuto_select(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg
    try:

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 600, 520, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("select_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0


def tuto_select(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg
    try:

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\select_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 600, 520, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("select_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0

