import time

import cv2
import numpy as np
# import os
import sys

sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_

def dungeon_start(cla, where):
    from action_zeno import dead_die
    from jadong_zeno import jadong_arrive_check, jadong_juljun_attack_dead
    from potion_zeno import juljun_potion_check, juljun_maul_potion
    from function import imgs_set_
    try:
        print("dungeon_start")
        # 절전 자동 모드 아니라면 진입하기
        dead_die(cla)
        result_arrived = jadong_arrive_check(cla, where)
        if result_arrived == True:
            result_potion = juljun_potion_check(cla)
            if result_potion == False:
                juljun_maul_potion(cla)
                dungeon_ready(cla, where)


        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\dead_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(380, 830, 580, 920, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                jadong_juljun_attack_dead(cla, where)


            dead_die(cla)
            dungeon_ready(cla, where)
        time.sleep(3)
    except Exception as e:
        print(e)
        return 0

def dungeon_ready(cla, where):
    from schedule import myQuest_play_add
    from jadong_zeno import spot_arrive, juljun_arrive
    try:
        print("dungeon_ready")
        # 던전 진입하기
        dungeon_menu_in(cla, where)
        # 해당 던전 클릭하기
        result_open = dungeon_click(cla, where)

        # 열려 있을때 층수 클릭
        if result_open == False:
            print("던전이 안 열려 있어서 끝...add")
            myQuest_play_add(cla, where)
        else:
            # 층수 클릭
            result_lock = dungeon_step_click(cla, where)
            if result_lock == True:
                print("lock 걸려 있어서 끝...add")
                myQuest_play_add(cla, where)
            else:
                print("마지막 입장하기")
                result_havetime = dungeon_in(cla, where)
                if result_havetime == True:
                    spot_arrive(cla, where)
                    juljun_arrive(cla, where)
                else:
                    print("시간 없어 스케쥴 완료")
                    myQuest_play_add(cla, where)

    except Exception as e:
        print(e)
        return 0

def dungeon_menu_in(cla, where):
    from action_zeno import menu_open
    from function import imgs_set_, click_pos_reg, click_pos_2
    try:
        print("dungeon_menu_in")

        in_dun_ = False
        in_dun_count = 0
        while in_dun_ is False:
            in_dun_count += 1
            if in_dun_count > 10:
                in_dun_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\dungeon_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 110, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_dun_ = True
            else:
                menu_open(cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\menu_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(660, 90, 950, 480, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    # 처음엔 new 글자...
                    click_pos_2(705, 260, cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

def dungeon_click(cla, where):
    from function import imgs_set_, click_pos_reg, click_pos_2
    try:
        print("dungeon_click")

        opened = True

        if '_' in where:
            dungeon_spl_ = where.split("_")
            # 일반_업보_4
        if dungeon_spl_[1] == "업보":
            dun_title = "upbo_title"
        if dungeon_spl_[1] == "지옥":
            dun_title = "hell_title"
        if dungeon_spl_[1] == "죄악":
            dun_title = "crime_title"
        if dungeon_spl_[1] == "저주":
            dun_title = "curse_title"
        if dungeon_spl_[1] == "마족":
            dun_title = "devil_title"
        if dungeon_spl_[1] == "아르카스":
            dun_title = "arcas_title"
        # if dungeon_spl_[1] == "묘지":
        #     dun_title = "tomb_title"


        in_dun_ = False
        in_dun_count = 0
        while in_dun_ is False:
            in_dun_count += 1
            if in_dun_count > 10:
                in_dun_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\" + dun_title + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(550, 100, 750, 150, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_dun_ = True

                if dungeon_spl_[1] == "업보" or dungeon_spl_[1] == "마족":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 140, 200, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        opened = False
                if dungeon_spl_[1] == "지옥" or dungeon_spl_[1] == "아르카스":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 220, 200, 260, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        opened = False
                if dungeon_spl_[1] == "죄악":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 290, 200, 340, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        opened = False
                if dungeon_spl_[1] == "저주":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 370, 200, 410, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        opened = False

            else:
                if dungeon_spl_[0] == "일반":
                    click_pos_2(365, 65, cla)
                if dungeon_spl_[0] == "특수":
                    click_pos_2(440, 65, cla)
                # if dungeon_spl_[0] == "파티":
                #     click_pos_2(560, 65, cla)
                time.sleep(1)
                if dungeon_spl_[1] == "업보" or dungeon_spl_[1] == "마족":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 140, 200, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("not_open1", imgs_)
                        in_dun_ = True
                        opened = False
                    else:
                        click_pos_2(150, 150, cla)
                if dungeon_spl_[1] == "지옥" or dungeon_spl_[1] == "아르카스":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 220, 200, 260, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("not_open2", imgs_)
                        in_dun_ = True
                        opened = False
                    else:
                        click_pos_2(150, 220, cla)
                if dungeon_spl_[1] == "죄악":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 290, 200, 340, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("not_open3", imgs_)
                        in_dun_ = True
                        opened = False
                    else:
                        click_pos_2(150, 300, cla)
                if dungeon_spl_[1] == "저주":
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\not_open.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 370, 200, 410, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("not_open4", imgs_)
                        in_dun_ = True
                        opened = False
                    else:
                        click_pos_2(150, 370, cla)

            time.sleep(0.5)
        time.sleep(0.5)
        return opened
    except Exception as e:
        print(e)
        return 0

def dungeon_step_click(cla, where):
    from function import imgs_set_, click_pos_reg, click_pos_2, drag_pos
    try:
        print("dungeon_step_click")

        step = 1
        locked = False

        if '_' in where:
            dungeon_spl_ = where.split("_")
            # 일반_업보_4
            step = int(dungeon_spl_[2])

            if dungeon_spl_[1] == "업보":
                if step > 4:
                    drag_pos(880, 480, 580, 480, cla)
                else:
                    drag_pos(580, 480, 880, 480, cla)
            if dungeon_spl_[1] == "지옥":
                if step > 4:
                    step = 4
            if dungeon_spl_[1] == "죄악":
                if step > 3:
                    step = 3
            if dungeon_spl_[1] == "저주":
                if step > 2:
                    step = 2
            if dungeon_spl_[1] == "마족":
                if step > 4:
                    drag_pos(880, 480, 580, 480, cla)
                else:
                    drag_pos(580, 480, 880, 480, cla)
                if step > 5:
                    step = 5
            if dungeon_spl_[1] == "아르카스":
                if step > 4:
                    drag_pos(880, 480, 580, 480, cla)
                else:
                    drag_pos(580, 480, 880, 480, cla)
                if step > 5:
                    step = 5
            time.sleep(0.5)
        in_dun_ = False
        in_dun_count = 0
        while in_dun_ is False:
            in_dun_count += 1
            if in_dun_count > 10:
                in_dun_ = True

            if step == 1:
                step_ = "one_step"
            if step == 2:
                step_ = "two_step"
            if step == 3:
                step_ = "three_step"
            if step == 4:
                step_ = "four_step"
            if step == 5:
                step_ = "five_step"
            if step == 6:
                step_ = "six_step"

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\" + step_ + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(560, 460, 915, 510, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print(step_, imgs_)
                x1 = imgs_.x

                if cla == "one":
                    x_ = x1
                if cla == "two":
                    x_ = x1 - 960
                if cla == "three":
                    x_ = x1 - 960 - 960
                if cla == "four":
                    x_ = x1 - 960 - 960 - 960

                y1 = imgs_.y
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(x_, y1 - 50, x_ + 50, y1, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("lock_step1", imgs_)

                    if step == 1:
                        in_dun_ = True
                        locked = True
                    elif step > 1:
                        step -= 1
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\lock_step2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_, y1 - 50, x_ + 50, y1, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("lock_step2", imgs_)
                        if step == 1:
                            in_dun_ = True
                            locked = True
                        elif step > 1:
                            step -= 1
                    else:
                        print("클릭하자")
                        in_dun_ = True
                        click_pos_reg(x1, y1, cla)
            else:
                print(step_, "없다")
                if step > 4:
                    drag_pos(880, 480, 580, 480, cla)
                else:
                    drag_pos(580, 480, 880, 480, cla)

            time.sleep(0.5)
        return locked
    except Exception as e:
        print(e)
        return 0


def dungeon_in(cla, where):
    from function import imgs_set_, click_pos_reg, text_check_get
    from action_zeno import confirm_all
    try:
        print("dungeon_in")

        havetime = True

        in_dun_ = False
        in_dun_count = 0
        while in_dun_ is False:
            in_dun_count += 1
            if in_dun_count > 10:
                in_dun_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 610, 650, 650, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_dun_ = True
                confirm_all(cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\dungeon_in_ready.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(840, 970, 880, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dungeon_in_ready", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(0.1)

                    click_before = "이용시간부족"
                    click_after = text_check_get(320, 140, 450, 170, cla)
                    print("click_after", click_after)

                    equal = 0
                    for i in range(len(click_after)):
                        for z in range(len(click_before)):
                            if click_after[i] == click_before[z]:
                                equal += 1
                                print("equal", click_after[i], click_before[z])
                                if equal > 4:
                                    havetime = False
                                    in_dun_ = True
                                    break

                    time.sleep(1)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\dungeon_in.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(720, 970, 850, 1020, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("dungeon_in", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        time.sleep(0.1)

                        click_before = "이용시간부족"
                        click_after = text_check_get(320, 140, 450, 170, cla)
                        print("click_after", click_after)

                        equal = 0
                        for i in range(len(click_after)):
                            for z in range(len(click_before)):
                                if click_after[i] == click_before[z]:
                                    equal += 1
                                    print("equal", click_after[i], click_before[z])
                                    if equal > 3:
                                        havetime = False
                                        in_dun_ = True
                                        break
                        time.sleep(1)
                    else:
                        print("안 보여")

            time.sleep(0.5)

        return havetime
    except Exception as e:
        print(e)
        return 0

def dungeon_check(cla, where):
    from function import imgs_set_, click_pos_reg, text_check_get
    from action_zeno import confirm_all
    try:
        print("dungeon_check")

        # 특수_마족_1
        # 일반_xx_3
        where_split = where.split("_")

        if where_split[1] == "마족":
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\devil_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 90, 110, 140, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("절전")
        if where_split[1] == "아르카스":
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\arcas_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 90, 150, 140, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("절전")
        if where_split[1] == "업보":
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\juljun_title\\upbo_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 90, 110, 140, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("절전")

        # 절전모드인지 먼저 체크하기기
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("절전")


    except Exception as e:
        print(e)
        return 0

