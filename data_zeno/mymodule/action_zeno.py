import time

import requests
import json
# import os
import sys


sys.path.append('C:/my_games/zenonia/data_zeno/mymodule')

import variable as v_

def character_schedule_select(cla, character_id):
    import os
    try:
        # 현재 진입한 캐릭터 번호(id)

        dir_path = "C:\\my_games\\zenonia"
        if cla == 'one':
            file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
        if cla == 'two':
            file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
        if cla == 'three':
            file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
        if cla == 'four':
            file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

        change_now = False

        is_select_ = False
        is_select_count = 0
        while is_select_ is False:
            is_select_count += 1
            if is_select_count > 15:
                is_select_ = True

            if os.path.isfile(file_path) == True:

                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_id = file.read()

                if str(character_id) == str(read_id):
                    is_select_ = True
                else:
                    change_now = True
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(str(character_id))
                time.sleep(0.3)
            else:
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(str("none"))
            time.sleep(0.3)

        return change_now
    except Exception as e:
        print(e)
        return 0

def character_change(cla, character_id):
    try:

        from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
        from massenger import line_to_me
        import numpy as np
        import cv2
        import os



        result_now_select = character_schedule_select(cla, character_id)

        if result_now_select == True:
            print("캐릭터 체인지")
            cha_select = False
            cha_select_count = 0
            while cha_select is False:
                cha_select_count += 1
                if cha_select_count > 10:
                    cha_select = True
                    line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

                # 캐릭터 선택 화면
                print("# 캐릭터 선택 화면1")
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    # 좌표
                    x_reg = imgs_.x
                    y_reg = imgs_.y

                    last_change = False
                    last_change_count = 0
                    while last_change is False:
                        last_change_count += 1
                        if last_change_count > 10:
                            last_change = True
                        print("진입")
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
                        if imgs_ is None:
                            # 진입여부 파악
                            in_game = False
                            in_game_count = 0
                            while in_game is False:
                                in_game_count += 1
                                if in_game_count > 40:
                                    in_game = True
                                    line_to_me(cla, "게임화면 진입에 문제가 있다.")
                                result_out = out_check(cla)
                                if result_out == True:
                                    last_change = True
                                    cha_select = True
                                    in_game = True
                                else:
                                    print("진입중")
                                time.sleep(1)
                        else:

                            for i in range(10):
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    y_ = 50 + (int(character_id) * 90)
                                    click_pos_2(55, y_, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(x_reg, y_reg, cla)
                                else:
                                    break
                                time.sleep(5)
                        time.sleep(0.5)



                else:
                    # 추후 대기중 화면 설정하기
                    # 대기중 화면이 아닐때
                    menu_open(cla)
                    time.sleep(0.1)
                    click_pos_2(910, 410, cla)
                    time.sleep(1)
                    for i in range(20):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            confirm_all(cla)
                        time.sleep(1)
                time.sleep(1)
        else:
            # 캐릭터 선택 화면
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                # 좌표
                x_reg = imgs_.x
                y_reg = imgs_.y

                last_change = False
                last_change_count = 0
                while last_change is False:
                    last_change_count += 1
                    if last_change_count > 10:
                        last_change = True
                    print("진입")
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
                    if imgs_ is None:
                        # 진입여부 파악
                        in_game = False
                        in_game_count = 0
                        while in_game is False:
                            in_game_count += 1
                            if in_game_count > 40:
                                in_game = True
                                line_to_me(cla, "게임화면 진입에 문제가 있다.")
                            result_out = out_check(cla)
                            if result_out == True:
                                last_change = True
                                in_game = True




                            else:
                                print("진입중")
                            time.sleep(1)
                    else:

                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                y_ = 50 + (int(character_id) * 90)
                                click_pos_2(55, y_, cla)
                                time.sleep(0.2)
                                click_pos_reg(x_reg, y_reg, cla)
                            else:
                                break
                            time.sleep(5)
                    time.sleep(0.5)
    except Exception as e:
        print(e)

def dead_die(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, click_pos_reg, imgs_set_
        from schedule import myQuest_play_check, myQuest_play_add
        from massenger import line_to_me
        print("deae_die")

        is_dead = False
        is_dead_ready = False

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\boohwal_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 800, 700, 1030, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            is_dead_ready = True
            print("boohwal_click...퀘스트 진행중", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 935, 480, 990, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            is_dead_ready = True
            print("dead...퀘스트 진행중", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)

        if is_dead_ready == True:
            is_out_ = False
            is_out_count = 0
            while is_out_ is False:
                is_out_count += 1
                if is_out_count > 20:
                    is_out_ = True
                result_out = out_check(cla)
                if result_out == True:
                    is_out_ = True
                else:
                    print("부활 대기 중")
                    clean_screen(cla)
                time.sleep(2)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                is_dead = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    is_dead = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
        time.sleep(0.5)

        is_dead_ready_count = 0
        while is_dead_ready is True:
            is_dead_ready_count += 1
            if is_dead_ready_count > 10:
                is_dead_ready = False
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                is_dead_ready = False
                is_dead = True
                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    is_dead_ready = False
                    is_dead = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        is_dead_ready = False
                        is_dead = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)



        if is_dead == True:

            why = "제노니아...죽어버렸다...체크바람."
            line_to_me(cla, why)

            result_schedule = myQuest_play_check(v_.now_cla, "check")
            print("dead_die : result_schedule", result_schedule)
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성":
                myQuest_play_add(cla, result_schedule_)

            time.sleep(1)

            dead_click = False

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                dead_click = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    dead_click = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

            if dead_click == True:
                dead_gold_change(cla)
                # 경험치 복구
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\0_30.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(75, 340, 125, 370, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print("경험치 0/30")
                else:
                    click_pos_2(75, 355, cla)
                    time.sleep(0.3)

                    exp_ = False
                    exp_count = 0
                    while exp_ is False:
                        exp_count += 1
                        if exp_count > 10:
                            exp_ = True
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\zero.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(115, 690, 155, 720, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            exp_ = True
                        else:

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 28, 360, 60, cla, img, 0.85)
                            if imgs_ is None:
                                exp_ = True

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\0_30.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(75, 340, 125, 370, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("경험치 0/30..")
                                exp_ = True
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\exp.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 375, 80, 440, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.3)
                                    click_pos_2(235, 755, cla)
                                    time.sleep(0.3)
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 660, 660, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)

                time.sleep(0.5)

            dead_click = False

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                dead_click = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    dead_click = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

            if dead_click == True:
                dead_gold_change(cla)
                # 장비 복구
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\0_30.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 340, 120, 230, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print("장비 0/30")
                else:
                    click_pos_2(195, 355, cla)
                    time.sleep(0.5)

                    jangbi_ = False
                    jangbi_count = 0
                    while jangbi_ is False:
                        jangbi_count += 1
                        if jangbi_count > 10:
                            jangbi_ = True
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\zero.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(115, 690, 155, 730, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            jangbi_ = True
                        else:

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(280, 28, 360, 60, cla, img, 0.85)
                            if imgs_ is None:
                                jangbi_ = True

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\0_30.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(180, 340, 120, 230, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("장비 0/30")
                                jangbi_ = True
                            else:
                                click_pos_2(55, 410, cla)
                                time.sleep(0.3)
                                click_pos_2(235, 755, cla)
                                time.sleep(0.3)
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 580, 660, 660, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                time.sleep(0.5)


        for i in range(2):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\dead_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(245, 330, 300, 380, cla, img, 0.88)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y ,cla)
                break

        if is_dead == True:
            print("v_.dead_count : ", v_.dead_count + 1)
            result_schedule = myQuest_play_check(v_.now_cla, "check")
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성":
                v_.dead_count += 1
                myQuest_play_add(cla, result_schedule_)
            else:
                v_.dead_count += 1

                if v_.dead_count > 4:
                    why = "제노 튜노...심하게 " + str(v_.dead_count) + "번 죽었으니 주인님 오실때 까지 기다리겠습니다."
                    line_to_me(cla, why)
                    loop_ = True
                    while loop_ is True:
                        time.sleep(30)



        return is_dead
    except Exception as e:
        print(e)
        return 0

def dead_gold_change(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg
        print("dead_gold_change")
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
    except Exception as e:
        print(e)
        return 0


def confirm_all(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg, click_pos_2

        go_ = False

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 610, 650, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 580, 660, 660, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 935, 480, 990, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(480, 580, 630, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\umsik_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 710, 570, 770, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\potion\\confirm_sangjum_potion.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 650, 600, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(490, 615, 620, 660, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\code_406.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 470, 600, 530, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_2(480, 625)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\code_406_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(400, 590, 570, 660, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)


        return go_
    except Exception as e:
        print(e)
        return 0

def out_check(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_
        print("out_check")



        go_ = False
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\out\\out_talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(290, 870, 340, 920, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            go_ = True
        return go_
    except Exception as e:
        print(e)
        return 0

def clean_screen(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("clean_screen")

        clean = False
        clean_count = 0
        while clean is False:

            clean_screen_action(cla)

            clean_count += 1
            if clean_count > 10:
                clean = True
            result_out = out_check(cla)
            if result_out == True:
                clean = True
            else:
                clean_screen_action(cla)




    except Exception as e:
        print(e)
        return 0

def clean_screen_action(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
        print("clean_screen_action")

        # 플 내리기
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\zenonia_start_ready.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\zenonia_title_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            # 제노는 3클라 고정
            imgs_ = imgs_set_(0, 50, 960, 1030, "three", img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x - 40, imgs_.y, v_.now_cla)

        # 절전
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            drag_pos(360, 460, 600, 460, cla)
            time.sleep(1)

        confirm_all(cla)

        # x 관련
        for i in range(4):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\x.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(250, 310, 960, 390, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.3)

        # 지도 관련
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\spot_click_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 340, 520, 390, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_2(635, 365, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 20, 960, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_quest_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 20, 700, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)

        mr_ = menu_open_check(cla)
        if mr_ == True:
            click_pos_2(915, 55, cla)
        # 튜토 관련 클린
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\level_up_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(430, 420, 520, 460, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("clean : level_up_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\skip\\contents_open.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(415, 115, 525, 180, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("clean : contents_open", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
        # 튜토 관련 클린
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

        if skip_ready == True:
            ready_ = False
            ready_count = 0
            while ready_ is False:
                ready_count += 1
                if ready_count > 10:
                    ready_ = True
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
        # 소환 관련 클린
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\sohwan\\exit_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
    except Exception as e:
        print(e)
        return 0

def in_maul_check(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_
        go_ = False
        print("in_maul_check")
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
        return go_
    except Exception as e:
        print(e)
        return 0

def go_maul(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, click_pos_reg, imgs_set_
        from jadong_zeno import spot_arrive
        print("go_maul")

        in_maul_ = False
        in_maul_count = 0
        while in_maul_ is False:
            in_maul_count += 1
            if in_maul_count > 10:
                in_maul_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\map.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 20, 100, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\is_dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 550, 250, 620, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("is_dungeon", imgs_)

                    quihwan_ = False
                    quihwan_count = 0
                    while quihwan_ is False:
                        quihwan_count += 1
                        if quihwan_count > 10:
                            quihwan_ = True
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\maul_quihwan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(340, 940, 410, 1010, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            quihwan_ = True
                            time.sleep(2)
                            where = "마을로 가즈아"
                            spot_arrive(cla, where)
                        else:
                            click_pos_2(930, 50, cla)
                        time.sleep(1)
                else:
                    time.sleep(0.2)
                    click_pos_2(840, 100, cla)
                    time.sleep(0.5)
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\maul.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(740, 120, 870, 1020, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x + 50, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_2(240, 100, cla)
                    potal_ = False
                    potal_count = 0
                    while potal_ is False:
                        potal_count += 1
                        if potal_count > 7:
                            potal_ = True

                        in_ = in_maul_check(cla)
                        if in_ == False:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\teleport.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(240, 160, 300, 230, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(270, 200, cla)
                                time.sleep(0.5)
                            confirm_all(cla)

                        else:
                            in_maul_ = True
                            potal_ = True
                        time.sleep(0.3)
            else:
                clean_screen(cla)
                time.sleep(0.2)
                click_pos_2(110, 130, cla)
                # # 마을이동서 있으면 클릭...없으면 map으로 이동
                # # map으로 이동 후 던전인지 확인...
                # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\maul_quihwan.PNG"
                # img_array = np.fromfile(full_path, np.uint8)
                # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                # imgs_ = imgs_set_(340, 940, 410, 1010, cla, img, 0.85)
                # if imgs_ is not None and imgs_ != False:
                #     click_pos_reg(imgs_.x, imgs_.y, cla)
                #     in_maul_ = True
                # else:
                #     click_pos_2(110, 130, cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0


def menu_open(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, imgs_set_
        print("menu_open")



        mno_ = False
        mno_count = 0
        while mno_ is False:
            mno_count += 1
            if mno_count > 7:
                mno_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\game_start.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, 970, 940, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                mno_ = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\menu_setting.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(820, 380, 890, 450, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    mno_ = True
                else:
                    clean_screen(cla)
                    time.sleep(0.3)
                    click_pos_2(915, 55, cla)

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\menu_setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(820, 380, 890, 450, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.2)

            time.sleep(0.5)
        time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def menu_open_check(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_
        print("menu_open")
        go_ = False
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\menu_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 380, 890, 450, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0

def bag_open(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, imgs_set_
        print("menu_open")
        mno_ = False
        mno_count = 0
        while mno_ is False:
            mno_count += 1
            if mno_count > 7:
                mno_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 300, 960, 380, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                mno_ = True
            else:
                clean_screen(cla)
                time.sleep(0.3)
                click_pos_2(865, 55, cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0


def bag_open_check(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_
        print("menu_open")
        go_ = False
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 310, 950, 370, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True

        return go_
    except Exception as e:
        print(e)
        return 0


def get_items(cla):
    try:
        import cv2
        import os
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_items")

        clean_screen(cla)

        # 이벤트 보상
        get_event(cla)

        # 업적
        get_upjuk(cla)
        # 우편
        get_post(cla)
        # 시즌 패스
        get_season_pass(cla)


        # 가방 열고 아이템 클릭
        bag_open(cla)
        click_pos_2(775, 350, cla)
        time.sleep(0.2)

        # 페어리
        for i in range(3):
            peari = 'peari' + str(i)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\sohwan\\" + peari + ".PNG"

            if os.path.isfile(full_path) == True:

                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    exit_1 = False
                    exit_1_count = 0
                    while exit_1 is False:
                        exit_1_count += 1
                        if exit_1_count > 10:
                            exit_1 = True
                            click_pos_2(480, 980, cla)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\sohwan\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            exit_1 = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                pass
        # 코스튬
        for i in range(3):
            costum = 'costum' + str(i)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\sohwan\\" + costum + ".PNG"

            if os.path.isfile(full_path) == True:

                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    exit_1 = False
                    exit_1_count = 0
                    while exit_1 is False:
                        exit_1_count += 1
                        if exit_1_count > 10:
                            exit_1 = True
                            click_pos_2(480, 980, cla)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\sohwan\\exit_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            exit_1 = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                pass

        # 스킬북
        for i in range(3):
            book = 'book_' + str(i)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\skillbook\\" + book + ".PNG"
            if os.path.isfile(full_path) == True:
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                pass
        # 음식상자
        umsik_ = False
        umsik_count = 0
        while umsik_ is False:
            umsik_count += 1
            if umsik_count > 5:
                umsik_ = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\umsik.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(650, 360, 940, 740, cla, img, 0.97)
            if imgs_ is not None and imgs_ != False:

                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.2)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                for i in range(3):
                    confirm_all(cla)
                    time.sleep(0.5)
            else:
                umsik_ = True
            time.sleep(0.5)
        for i in range(2):
            confirm_all(cla)
            time.sleep(0.5)
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 310, 950, 370, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                break


    except Exception as e:
        print(e)
        return 0

def get_event(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_event")
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\event_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 25, 750, 60, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("event_check", imgs_)
            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)

            e_click = False
            e_click_count = 0
            while e_click is False:
                e_click_count += 1
                if e_click_count > 10:
                    e_click = True
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 20, 960, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.3)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\event_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_point.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(320, 340, 350, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("e_point", imgs_)
                            click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                            time.sleep(0.7)

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\get_event.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 690, 940, 770, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_exit.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(900, 20, 960, 80, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                e_click = True
                                time.sleep(0.3)
                                break
                        time.sleep(0.7)


                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\event_check.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 25, 750, 60, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("event_check", imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0



def get_upjuk(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_upjuk")

        isupjuk = False

        menu_open(cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(910, 110, 950, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            isupjuk = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(910, 110, 950, 150, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            isupjuk = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

        for i in range(10):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(0.5)

        if isupjuk == True:
            post_ = False
            post_count = 0
            while post_ is False:
                post_count += 1
                if post_count > 10:
                    post_ = True
                    click_pos_2(930, 50, cla)

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    post_ = True

                    post2_ = False
                    post2_count = 0
                    while post2_ is False:
                        post2_count += 1
                        if post2_count > 10:
                            post2_ = True
                            click_pos_2(480, 750, cla)

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_soolyung.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(415, 730, 540, 770, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            post2_ = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(880, 1000, cla)
                            time.sleep(0.5)

                time.sleep(0.5)
        for i in range(2):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(930, 50, cla)
                time.sleep(0.5)
                break
    except Exception as e:
        print(e)
        return 0



def get_post(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_post")

        is_post = False

        menu_open(cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 370, 740, 410, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            is_post = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 370, 740, 410, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            is_post = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

        for i in range(10):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\post_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(0.5)

        if is_post == True:
            post_ = False
            post_count = 0
            while post_ is False:
                post_count += 1
                if post_count > 10:
                    post_ = True
                    click_pos_2(930, 50, cla)

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\post_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("1")
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\p_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(560, 30, 620, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("2")
                        click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)

                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\p_point2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(900, 130, 960, 180, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\p_point2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(900, 130, 960, 180, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(890, 190, cla)
                                time.sleep(0.5)

                            else:
                                break
                            confirm_all(cla)
                            time.sleep(0.2)


                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\p_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(360, 30, 540, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("3")
                        click_pos_reg(imgs_.x - 30, imgs_.y + 10, cla)
                        time.sleep(0.5)
                        post2_ = False
                        post2_count = 0
                        while post2_ is False:
                            post2_count += 1
                            if post2_count > 10:
                                post2_ = True
                                click_pos_2(480, 750, cla)

                            result = confirm_all(cla)
                            if result == True:
                                post2_ = True
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_post_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(840, 140, 960, 240, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(900, 1000, cla)
                            time.sleep(0.2)
                    else:
                        post_ = True
                        click_pos_2(930, 50, cla)
                time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0



def get_season_pass(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg, click_pos_2
        print("get_season_pass")

        isseason = False

        menu_open(cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 300, 740, 340, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            isseason = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 300, 740, 340, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            isseason = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)

        for i in range(10):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\seasonpass_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 135, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                break
            time.sleep(0.5)

        if isseason == True:
            season_pass_ = False
            season_pass_count = 0
            while season_pass_ is False:
                season_pass_count += 1
                if season_pass_count > 10:
                    season_pass_ = True
                    click_pos_2(930, 50, cla)

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\seasonpass_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 135, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\sp_point.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 70, 150, 180, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x - 30, imgs_.y + 15, cla)

                        season_pass2_ = False
                        season_pass2_count = 0
                        while season_pass2_ is False:
                            season_pass2_count += 1
                            if season_pass2_count > 10:
                                season_pass2_ = True
                                click_pos_2(480, 750, cla)

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                season_pass2_ = True
                                time.sleep(0.5)
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\season_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    season_pass2_ = True
                                    time.sleep(0.5)
                                else:
                                    click_pos_2(900, 1000, cla)
                            time.sleep(0.3)
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\select\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.75)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\season_confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(415, 730, 545, 770, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                            else:
                                season_pass_ = True
                                click_pos_2(930, 50, cla)
                        time.sleep(0.5)
                time.sleep(0.5)
            for i in range(4):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\seasonpass_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 135, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 50, cla)
                    time.sleep(0.1)
                    break
                time.sleep(0.2)
    except Exception as e:
        print(e)
        return 0




def quickslot_check(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg, drag_pos
        # 퀵슬롯 체크
        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\maul_quihwan.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(340, 940, 410, 1010, cla, img, 0.85)
        # if imgs_ is None:
        #     bag_open(cla)
        #     click_pos_2(775, 350, cla)
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\maul_quihwan2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(650, 350, 940, 740, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(0.5)
        #         click_pos_2(375, 980, cla)
        #         time.sleep(0.5)
        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\random_move.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(400, 940, 460, 1010, cla, img, 0.85)
        # if imgs_ is None:
        #     bag_open(cla)
        #     click_pos_2(775, 350, cla)
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\random_move.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(650, 350, 940, 740, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(0.5)
        #         click_pos_2(430, 980, cla)
        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
        # if imgs_ is None:
        #     bag_open(cla)
        #     click_pos_2(775, 350, cla)
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(650, 350, 940, 740, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(0.5)
        #         click_pos_2(585, 980, cla)
        #         time.sleep(0.5)
        #=======================================================================
        # is_potion = False
        # is_potion_count = 0
        # while is_potion is False:
        #     is_potion_count += 1
        #     if is_potion_count > 10:
        #         is_potion = True
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         drag_pos(585, 980, 430, 980, cla)
        #     else:
        #         is_potion = True
        #     time.sleep(1)
        #
        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\ccochi.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(450, 940, 510, 1010, cla, img, 0.85)
        # if imgs_ is None:
        #     bag_open(cla)
        #     click_pos_2(775, 350, cla)
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\ccochi2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(650, 350, 940, 740, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(0.5)
        #         click_pos_2(480, 980, cla)
        #         time.sleep(0.5)
        #         drag_pos(480, 980, 480, 1030, cla)
        #         time.sleep(0.5)
        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\salad.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(500, 940, 560, 1010, cla, img, 0.85)
        # if imgs_ is None:
        #     bag_open(cla)
        #     click_pos_2(775, 350, cla)
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\salad2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(650, 350, 940, 740, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(0.5)
        #         click_pos_2(530, 980, cla)
        #         time.sleep(0.5)
        #         drag_pos(530, 980, 530, 1030, cla)
        #         time.sleep(0.5)
        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\steak.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
        # if imgs_ is None:
        #     bag_open(cla)
        #     click_pos_2(775, 350, cla)
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\steak2.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(650, 350, 940, 740, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         click_pos_reg(imgs_.x, imgs_.y, cla)
        #         time.sleep(0.5)
        #         click_pos_2(585, 980, cla)
        #         time.sleep(0.5)
        #         drag_pos(585, 980, 585, 1030, cla)
        #         time.sleep(0.5)
        #
        # is_potion = False
        # is_potion_count = 0
        # while is_potion is False:
        #     is_potion_count += 1
        #     if is_potion_count > 10:
        #         is_potion = True
        #     full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\potion.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(555, 940, 610, 1010, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         is_potion = True
        #     else:
        #         drag_pos(375, 980, 530, 980, cla)
        #     time.sleep(1)

        for i in range(2):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\bag\\bag_exit.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 310, 950, 370, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                break

    except Exception as e:
        print(e)
        return 0


def now_hunting(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg
        print("now_hunting")

        dead_die(cla)

        go_ = False

        gold_1 = gold_check_open(cla)
        for i in range(15):
            gold_2= gold_check_open(cla)
            if int(gold_1) != int(gold_2):
                go_ = True
                break
            time.sleep(1)
        return go_
    except Exception as e:
        print(e)
        return 0

def gold_check_open(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_reg, in_number_check, text_check_get, int_put_
        print("gold_check")

        many_gold = 0

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\hunting\\gold.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 50, 380, 110, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            gold_ = text_check_get(415, 70, 500, 90, cla)
            print("gold", gold_)
            is_number = in_number_check(cla, gold_)
            if is_number == True:
                result_num = int_put_(gold_)
                many_gold = result_num
            else:
                print("숫자가 아니다.")
        else:
            hunt_ = False
            hunt_count = 0
            while hunt_ is False:
                hunt_count += 1
                if hunt_count > 5:
                    hunt_ = True
                result_out = out_check(cla)
                if result_out == True:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\hunting\\hunt_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(480, 30, 570, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\hunting\\gold.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 50, 380, 110, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            hunt_ = True
                else:
                    clean_screen(cla)
                time.sleep(1)

        return many_gold
    except Exception as e:
        print(e)
        return 0


def zeno_moving(cla):
    import numpy as np
    import cv2
    from function import imgs_set_
    try:
        print("moving")

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
    except Exception as e:
        print(e)
        return 0




