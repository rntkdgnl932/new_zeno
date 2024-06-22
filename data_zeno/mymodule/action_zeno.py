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
    from function import click_pos_2, imgs_set, imgs_set_, random_int, drag_pos, text_check_get, click_pos_reg
    from massenger import line_to_me
    import numpy as np
    import cv2
    import os
    from event_18 import event_stop
    try:





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
                    # 이벤트 닫기
                    event_stop(cla)

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
        from potion_zeno import maul_dead_potion
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

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dead\\dead_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 920, 480, 990, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            is_dead_ready = True
            print("dead...", imgs_)
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
            imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                is_dead_ready = False
                is_dead = True
                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    is_dead_ready = False
                    is_dead = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        is_dead_ready = False
                        is_dead = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)



        if is_dead == True:

            # why = "제노니아..." + str(v_.dead_count) + "번 죽어버렸다...체크바람."
            # line_to_me(cla, why)

            result_schedule = myQuest_play_check(v_.now_cla, "check")
            print("dead_die : result_schedule", result_schedule)
            result_schedule_ = result_schedule[0][2]

            if result_schedule_ == "튜토육성" or "죄악" in result_schedule_:
                myQuest_play_add(cla, result_schedule_)

            if '_' in result_schedule_:
                sche_ = result_schedule_.split("_")
                if sche_[1] == "지옥" and v_.dead_count > 4:
                    myQuest_play_add(cla, result_schedule_)

            time.sleep(1)

            dead_click = False
            dead_click_count = 0
            while dead_click is False:
                dead_click_count += 1
                if dead_click_count > 5:
                    dead_click = True

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dead\\jaehwa_change.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(5, 720, 200, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    dead_click = True
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 28, 360, 90, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
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
                        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\zero.PNG"
                        # img_array = np.fromfile(full_path, np.uint8)
                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        # imgs_ = imgs_set_(115, 690, 155, 720, cla, img, 0.88)
                        # if imgs_ is not None and imgs_ != False:
                        #     exp_ = True
                        # else:

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 28, 360, 60, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
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
                                    x_reg = imgs_.x
                                    y_reg = imgs_.y

                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_gold.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(20, 720, 65, 785, cla, img, 0.88)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(x_reg, y_reg, cla)
                                        time.sleep(0.3)
                                        click_pos_2(235, 755, cla)
                                        time.sleep(0.3)
                                    else:
                                        dead_gold_change(cla)

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(480, 580, 660, 660, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            exp_ = True

                        # time.sleep(0.3)

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
                        # full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\zero.PNG"
                        # img_array = np.fromfile(full_path, np.uint8)
                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        # imgs_ = imgs_set_(115, 690, 155, 730, cla, img, 0.88)
                        # if imgs_ is not None and imgs_ != False:
                        #     jangbi_ = True
                        # else:

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_cross_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 28, 360, 60, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\0_30.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(180, 340, 120, 230, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("장비 0/30")
                                jangbi_ = True
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\tuto_grow\\dead\\dead_gold.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(20, 720, 65, 785, cla, img, 0.88)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(155, 410, cla)
                                    time.sleep(0.3)
                                    click_pos_2(235, 755, cla)
                                    time.sleep(0.3)
                                else:
                                    dead_gold_change(cla)

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\dead\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 580, 660, 660, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            jangbi_ = True


                        # time.sleep(0.3)
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

            maul_dead_potion(cla)
            time.sleep(0.5)

            if result_schedule_ == "튜토육성":
                v_.dead_count += 1
                myQuest_play_add(cla, result_schedule_)
            else:
                v_.dead_count += 1
                if v_.dead_count > 29:
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
        # 업적 수령
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_soolyung.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(415, 710, 540, 780, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 재료 부족
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\jejak_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(390, 590, 560, 660, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            go_ = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        # 제작 닫기
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jejak\\close.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(440, 970, 520, 1020, cla, img, 0.85)
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
        imgs_ = imgs_set_(290, 870, 340, 920, cla, img, 0.75)
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
                get_market_gyohwanso(cla)




    except Exception as e:
        print(e)
        return 0

def clean_screen_action(cla):
    try:
        import cv2
        import numpy as np
        import sys
        import os
        from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos, imgs_set
        from massenger import line_to_me
        print("clean_screen_action")

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\monitor\\jangsigan_zeno.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set(280, 490, 400, 540, cla, img)
        if imgs_ is not None:
            ms_ = str(v_.this_game) + str(": 장시간 보여...무슨 에러가 발생한듯...")
            line_to_me(cla, ms_)

            dir_path = "C:\\my_games\\load\\zenonia"
            file_path = dir_path + "\\start.txt"
            file_path2 = dir_path + "\\cla.txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = v_.now_cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)

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
            imgs_ = imgs_set_(0, 50, 960, 1030, cla, img, 0.8)
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
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\xx.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 10, 960, 1040, cla, img, 0.85)
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

        exit = False
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(900, 20, 960, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            exit = True

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_quest_exit.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(630, 20, 700, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
            exit = True
        if exit == True:
            confirm_all(cla)


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

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            click_pos_reg(imgs_.x, imgs_.y, cla)
        # 죽음 dead 관련
        dead_die(cla)

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
    import cv2
    import numpy as np
    from function import click_pos_2, click_pos_reg, imgs_set_, drag_pos
    from jadong_zeno import spot_arrive
    try:

        print("go_maul")
        quihwan_ = False
        quihwan_count = 0
        while quihwan_ is False:
            quihwan_count += 1
            if quihwan_count > 10:
                quihwan_ = True

            result_out = out_check(cla)

            if result_out == True:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    quihwan_ = True

                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\quickslot\\maul_quihwan.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 940, 410, 1010, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        quihwan_ = True
                        time.sleep(1)
                        where = "마을로 가즈아"
                        spot_arrive(cla, where)

                        is_maul = False
                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                is_maul = True
                                break
                            time.sleep(0.2)
                        if is_maul == False:
                            print("침공중이라 최초 마을로 가기")
                            go_maul_shade(cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\juljun\\juljun_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(380, 830, 580, 880, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(360, 460, 900, 460, cla)
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            break
                        time.sleep(0.5)
                else:
                    clean_screen(cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0
def go_maul_shade(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, click_pos_reg, imgs_set_
        from jadong_zeno import spot_arrive
        print("go_maul_shade")

        in_maul_ = False
        in_maul_count = 0
        while in_maul_ is False:
            in_maul_count += 1
            if in_maul_count > 10:
                in_maul_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\maul\\jabhwa.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(690, 940, 750, 1020, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_maul_ = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\map.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(20, 20, 100, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    # 쉐이드 숲
                    go_maul_shade_world(cla)
                    # 쉐이드 숲에 마을 클릭하기
                    click_pos_2(755, 430, cla)
                    # 최종 도착하기
                    go_maul_shade_maul_in(cla)
                else:
                    clean_screen(cla)
                    time.sleep(0.2)
                    click_pos_2(110, 130, cla)
            time.sleep(1)
    except Exception as e:
        print(e)
        return 0

def go_maul_shade_world(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, click_pos_reg, imgs_set_
        from jadong_zeno import spot_arrive
        print("go_maul_shade")

        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\midgard_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(130, 30, 250, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                in_map_ = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\map_midgard.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(390, 50, 535, 90, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\midgard_in_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(20, 100, 930, 1000, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("미드가르드로 고고고!!!")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\midgard_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(130, 30, 250, 70, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.3)
                    else:
                        print("미드가르드 맵인데 안 보인다. 오류다.")
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\midgard\\map_midgard.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(390, 50, 535, 90, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("okokok")
                            break
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\return_midgard\\map_return_midgard.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(390, 50, 535, 90, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(375, 85, cla)
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\userminer\\map_userminer.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(390, 50, 535, 90, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(375, 85, cla)
                                else:
                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\andra\\map_andra.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(390, 50, 535, 90, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(375, 85, cla)
                                    else:
                                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\map.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(20, 20, 100, 70, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_2(180, 50, cla)
                        time.sleep(0.3)


            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def go_maul_shade_maul_in(cla):
    import cv2
    import numpy as np
    from function import click_pos_2, click_pos_reg, imgs_set_
    from jadong_zeno import spot_arrive
    try:

        print("go_maul_shade_maul_in")

        in_map_ = False
        in_map_count = 0
        while in_map_ is False:
            in_map_count += 1
            if in_map_count > 10:
                in_map_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\dungeon\\confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(490, 610, 650, 650, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                confirm_all(cla)
                where = "마을로 가즈아"
                spot_arrive(cla, where)
                in_map_ = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\jadong\\teleport2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(310, 170, 950, 840, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("teleport2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
    except Exception as e:
        print(e)
        return 0

def menu_open(cla):
    try:
        import cv2
        import numpy as np
        from function import click_pos_2, imgs_set_, click_pos_reg
        print("menu_open")



        mno_ = False
        mno_count = 0
        while mno_ is False:
            mno_count += 1
            if mno_count > 7:
                mno_ = True

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

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
                imgs_ = imgs_set_(820, 420, 890, 520, cla, img, 0.85)
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
                        imgs_ = imgs_set_(820, 420, 890, 520, cla, img, 0.85)
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
        print("menu_open_check")
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
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\xx.PNG"
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
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\xx.PNG"
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
        from guild_zenonia import guild_check
        print("get_items")

        clean_screen(cla)

        # 이벤트 보상
        get_event(cla)

        # 마켓 소환
        get_market_sohwan_start(cla)

        # 마켓 교환소
        get_market_gyohwanso_start(cla)

        # 업적
        get_upjuk(cla)
        # 우편
        get_post(cla)
        # 시즌 패스
        get_season_pass(cla)

        guild_check(cla)


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
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\barobogi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 940, 1030, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
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
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\barobogi.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 0, 940, 1030, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
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
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\xx.PNG"
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
        from function import imgs_set_, click_pos_2, click_pos_reg, drag_pos
        print("get_event")
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\event_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 25, 750, 60, cla, img, 0.8)
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

                    y_reg = 370
                    for k in range(8):
                        y_reg = y_reg + 50
                        click_pos_2(320, y_reg, cla)
                        time.sleep(0.2)


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
                            else:
                                # 타이틀 포인트 부터 파악
                                title_point = False

                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_title_point.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(450, 460, 945, 495, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("e_title_point", imgs_)
                                    title_point = True
                                    click_pos_reg(imgs_.x - 70, imgs_.y + 15, cla)
                                else:
                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_title_point2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(450, 460, 945, 495, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("e_title_point2", imgs_)
                                        title_point = True
                                        click_pos_reg(imgs_.x - 70, imgs_.y + 15, cla)

                                if title_point == True:
                                    time.sleep(0.5)
                                    drag_pos(650, 550, 650, 870, cla)
                                    for c in range(5):
                                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_point2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(570, 500, 940, 765, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                                        else:
                                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_edge_point.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(595, 725, 945, 765, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("e_edge_point", imgs_)
                                                click_pos_reg(imgs_.x - 15, imgs_.y, cla)
                                            else:
                                                break
                                        time.sleep(0.5)


                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_point2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(570, 500, 940, 765, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x - 15, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_point2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(880, 380, 930, 430, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_reg(imgs_.x - 15, imgs_.y, cla)
                                    else:
                                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\get_event\\e_edge_point.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(595, 725, 945, 765, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("e_edge_point", imgs_)
                                            click_pos_reg(imgs_.x - 15, imgs_.y, cla)
                                        else:
                                            drag_pos(650, 720, 650, 400, cla)

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
                    imgs_ = imgs_set_(700, 25, 750, 60, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("event_check", imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                time.sleep(0.5)



    except Exception as e:
        print(e)
        return 0

def get_market_sohwan(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_market_sohwan")

        sohwan = False
        sohwan_count = 0
        while sohwan is False:
            sohwan_count += 1
            if sohwan_count > 10:
                sohwan = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 280, 450, 330, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                poomjul = False

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\1_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(555, 330, 600, 365, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(400, 710, cla)
                    poomjul = True
                    sohwan = True
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\poomjul.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(260, 390, 340, 435, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(400, 710, cla)
                        poomjul = True
                        sohwan = True

                if poomjul == False:
                    click_pos_2(560, 710, cla)
                    time.sleep(0.2)
                    sohwan = True

                    notfullyet_level = False

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\sohwan_exit.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 950, 530, 1030, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.2)
                            break
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\barobogi.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 940, 1030, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 280, 450, 330, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(560, 710, cla)
                                for k in range(10):
                                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\notfullyet_level.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(350, 130, 500, 200, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        sohwan = True
                                        notfullyet_level = True
                                        break
                                    else:
                                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\1_1.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(555, 330, 600, 365, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            sohwan = True
                                            notfullyet_level = True
                                            break
                                    time.sleep(0.1)
                        if notfullyet_level == True:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\sohwan_exit.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 950, 530, 1030, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            break
                        time.sleep(0.2)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\toichunjok_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 280, 450, 330, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    poomjul = False

                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\1_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(555, 330, 600, 365, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(400, 710, cla)
                        poomjul = True
                        sohwan = True
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\poomjul.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(260, 390, 340, 435, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(400, 710, cla)
                            poomjul = True
                            sohwan = True

                    if poomjul == False:
                        click_pos_2(560, 710, cla)
                        time.sleep(0.2)
                        sohwan = True

                        notfullyet_level = False

                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\barobogi.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 0, 940, 1030, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\sohwan_exit.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 950, 530, 1030, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.2)
                                break
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\toichunjok_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 280, 450, 330, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(560, 710, cla)
                                    for k in range(10):
                                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\notfullyet_level.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(350, 130, 500, 200, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            sohwan = True
                                            notfullyet_level = True
                                            break
                                        else:
                                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\1_1.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(555, 330, 600, 365, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                sohwan = True
                                                notfullyet_level = True
                                                break
                                        time.sleep(0.1)
                            if notfullyet_level == True:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\sohwan_exit.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 950, 530, 1030, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.2)
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                break
                            time.sleep(0.5)
            time.sleep(0.5)

        for i in range(10):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\barobogi.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 940, 1030, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(370, 280, 450, 330, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(400, 710, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\toichunjok_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 280, 450, 330, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(400, 710, cla)
                else:
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\sohwan_exit.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 950, 530, 1030, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def get_market_sohwan_start(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_market_sohwan_start")

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

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(165, 125, 225, 170, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    for i in range(4):
                        reg_x1 = 180 + (i * 200)
                        reg_x2 = 250 + (i * 200)
                        locked = False
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(reg_x1, 200, reg_x2, 250, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            locked = True
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(reg_x1, 200, reg_x2, 250, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                locked = True
                        if locked == False:
                            click_pos_2(reg_x1, 230, cla)
                            get_market_sohwan(cla)
                    # click_pos_2(235, 230, cla)
                    # get_market_sohwan(cla)
                    # click_pos_2(435, 230, cla)
                    # get_market_sohwan(cla)
                    # click_pos_2(630, 230, cla)
                    # get_market_sohwan(cla)
                    # click_pos_2(830, 230, cla)
                    # get_market_sohwan(cla)

                    for i in range(4):
                        reg_x1 = 180 + (i * 200)
                        reg_x2 = 250 + (i * 200)
                        locked = False
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(reg_x1, 410, reg_x2, 460, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            locked = True
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(reg_x1, 410, reg_x2, 460, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                locked = True
                        if locked == False:
                            click_pos_2(reg_x1, 440, cla)
                            get_market_sohwan(cla)

                    # click_pos_2(235, 440, cla)
                    # get_market_sohwan(cla)
                    # click_pos_2(435, 440, cla)
                    # get_market_sohwan(cla)
                    # click_pos_2(630, 440, cla)
                    # get_market_sohwan(cla)
                    # click_pos_2(830, 440, cla)
                    # get_market_sohwan(cla)

                    e_click = True

                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gold_sohwan.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 180, 60, 230, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(165, 125, 225, 170, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gold_sohwan.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 180, 60, 230, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\sohwan_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(160, 70, 360, 120, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
            else:
                clean_screen(cla)
                click_pos_2(765, 60, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

            time.sleep(0.5)

        # for i in range(10):
        #     result_out = out_check(cla)
        #     if result_out == False:
        #         full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\action\\clean_exit.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(900, 20, 960, 80, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             click_pos_reg(imgs_.x, imgs_.y, cla)
        #     else:
        #         break
        #     time.sleep(0.3)



    except Exception as e:
        print(e)
        return 0

def get_market_gyohwanso(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg
        print("get_market_gyohwanso")

        is_sohwan_ = False

        sohwan = False
        sohwan_count = 0
        while sohwan is False:
            sohwan_count += 1
            if sohwan_count > 10:
                sohwan = True

            poomjul = False

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\poomjul.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(430, 390, 515, 435, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(400, 710, cla)
                poomjul = True
                sohwan = True
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\poomjul.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(260, 390, 340, 435, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(400, 710, cla)
                    poomjul = True
                    sohwan = True

            if poomjul == False:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\bonginsuk_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 280, 540, 330, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(270, 645, cla)
                    time.sleep(0.4)
                    click_pos_2(560, 710, cla)
                    time.sleep(0.2)
                    is_sohwan_ = True
                    sohwan = True

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gaginsuk_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 280, 540, 330, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(270, 645, cla)
                    time.sleep(0.4)
                    click_pos_2(560, 710, cla)
                    time.sleep(0.2)
                    is_sohwan_ = True
                    sohwan = True

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok_title2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(370, 280, 460, 330, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(560, 710, cla)
                    time.sleep(0.2)
                    is_sohwan_ = True
                    sohwan = True

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\jaelyo_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 280, 500, 330, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(270, 645, cla)
                    time.sleep(0.1)
                    click_pos_2(270, 645, cla)
                    time.sleep(0.1)
                    click_pos_2(270, 645, cla)
                    time.sleep(0.4)
                    click_pos_2(560, 710, cla)
                    time.sleep(0.2)
                    is_sohwan_ = True
                    sohwan = True

                time.sleep(0.2)

                if is_sohwan_ == True:
                    for k in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\notfullyet_level.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(350, 130, 500, 200, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(400, 710, cla)
                            sohwan = True
                            break
                        time.sleep(0.1)

        for i in range(10):

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break

            time.sleep(0.5)

    except Exception as e:
        print(e)
        return 0

def get_market_gyohwanso_start(cla):
    try:
        import cv2
        import numpy as np
        from function import imgs_set_, click_pos_2, click_pos_reg, drag_pos
        print("get_market_gyohwanso")

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

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\bonginsuk.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(200, 125, 280, 170, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:

                    # 봉인석
                    locked = False
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 200, 230, 250, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        locked = True
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(170, 200, 230, 250, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            locked = True
                    if locked == False:
                        click_pos_2(235, 230, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\bonginsuk_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 280, 540, 330, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                        get_market_gyohwanso(cla)

                    # 각인석
                    locked = False
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(170, 410, 230, 460, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        locked = True
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(170, 410, 230, 460, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            locked = True
                    if locked == False:
                        click_pos_2(235, 440, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gaginsuk_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 280, 540, 330, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                        get_market_gyohwanso(cla)

                    # 마루족 상인 선물 상자자
                    locked = False
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 200, 450, 250, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        locked = True
                    else:
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 200, 450, 250, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            locked = True
                    if locked == False:
                        click_pos_2(435, 230, cla)
                        for i in range(10):
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\marujok_title2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 280, 460, 330, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)
                        get_market_gyohwanso(cla)

                    for z in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\pyungbumhan_jaelyo.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(380, 120, 500, 180, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:

                            locked = False
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(370, 200, 550, 250, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                locked = True
                            else:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\lock2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(370, 200, 550, 250, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    locked = True
                            if locked == False:
                                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\pyungbumhan_jaelyo.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(380, 120, 500, 180, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    for i in range(10):
                                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\jaelyo_title.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(420, 280, 500, 330, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(0.5)
                                    get_market_gyohwanso(cla)
                            break
                        else:
                            drag_pos(870, 350, 200, 350, cla)
                        time.sleep(0.5)

                    e_click = True

                else:

                    for i in range(10):

                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gold_gyohwanso.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 130, 60, 180, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\bonginsuk.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 125, 280, 170, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gold_gyohwanso.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 130, 60, 180, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\gyohwanso_click.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(430, 70, 600, 120, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)




            else:
                clean_screen(cla)
                click_pos_2(765, 60, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    time.sleep(0.5)

            time.sleep(0.5)

        for i in range(10):

            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\title\\market_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(930, 50, cla)
                else:
                    break
                time.sleep(0.5)

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
        imgs_ = imgs_set_(910, 110, 950, 150, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            isupjuk = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(910, 110, 950, 150, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                isupjuk = True
                click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)



        if isupjuk == True:

            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)


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
                        imgs_ = imgs_set_(415, 710, 540, 780, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            post2_ = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(880, 1000, cla)
                            time.sleep(0.5)

                time.sleep(0.5)
        for i in range(3):
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\upjuk_soolyung.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(415, 710, 540, 780, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
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
        imgs_ = imgs_set_(700, 420, 740, 470, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            is_post = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 420, 740, 470, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            is_post = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)



        if is_post == True:

            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\post_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 120, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)

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
                    imgs_ = imgs_set_(560, 30, 620, 70, cla, img, 0.8)
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
                    imgs_ = imgs_set_(360, 30, 540, 70, cla, img, 0.8)
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
        imgs_ = imgs_set_(700, 350, 740, 390, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            isseason = True
            click_pos_reg(imgs_.x - 20, imgs_.y + 15, cla)
        else:
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\check2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 350, 740, 390, cla, img, 0.8)
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

            for i in range(10):
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\item\\seasonpass_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 135, 70, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)

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
                    imgs_ = imgs_set_(90, 70, 150, 300, cla, img, 0.85)
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
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\cleanscreen\\xx.PNG"
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
        for i in range(30):
            gold_2 = gold_check_open(cla)
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
            gold_ = text_check_get(415, 70, 515, 90, cla)
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
                    # 퀘스트 수락 버튼 놓아두기

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
                        else:
                            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\market\\cancle.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 600, 500, 770, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)


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



def mine_check(cla):
    import numpy as np
    import cv2
    from function import imgs_set_, click_pos_reg, click_pos_2, text_check_get, in_number_check, int_put_
    from schedule import myQuest_play_add

    try:
        print("mine_check")

        if cla == "one":
            plus = 0
        elif cla == "two":
            plus = 960
        elif cla == "three":
            plus = 960 * 2
        elif cla == "four":
            plus = 960 * 3

        gold_ = 0
        dia_ = 0

        monster_in = False
        monster_in_count = 0
        while monster_in is False:
            monster_in_count += 1
            if monster_in_count > 7:
                monster_in = True
            full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 30, 150, 80, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                monster_in = True
                print("거래소 오픈")

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\property\\zen.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 30, 850, 70, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("zen", imgs_)

                    x_2 = imgs_.x



                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\property\\gold.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 30, 850, 70, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("gold", imgs_)
                    # 789
                    x_reg_1 = imgs_.x - plus
                    for i in range(4):
                        read_gold = text_check_get(x_reg_1 + 7 + i, 37, x_2 - 12, 63, cla)
                        if read_gold == "":
                            print("골드 못 읽음")
                        else:
                            print("read_gold", read_gold)
                            break

                    digit_ready = in_number_check(cla, read_gold)
                    print("digit_ready", digit_ready)
                    if digit_ready == True:
                        read_data_int = int(int_put_(read_gold))
                        print("read_data_int", read_data_int)
                        gold_ = read_data_int

                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\property\\dia.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 37, 850, 63, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("dia", imgs_)
                    x_reg_2 = imgs_.x - plus
                    # 741

                    for i in range(4):
                        read_dia = text_check_get(x_reg_2 + 7 + i, 39, x_reg_1 - 25, 63, cla)
                        if read_dia == "":
                            print("다이아 못 읽음")
                        else:
                            print("read_dia", read_dia)
                            break

                    digit_ready = in_number_check(cla, read_dia)
                    print("digit_ready", digit_ready)
                    if digit_ready == True:
                        read_data_int = int(int_put_(read_dia))
                        print("read_data_int", read_data_int)
                        dia_ = read_data_int


            else:
                menu_open(cla)
                time.sleep(0.2)
                full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\menu_auction.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(670, 100, 950, 530, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    for i in range(10):
                        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\auction\\auction_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(10, 10, 120, 80, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            break
                        time.sleep(0.5)






        return gold_, dia_

    except Exception as e:
        print(e)
        return 0


def system_check(cla):
    import numpy as np
    import cv2
    import os
    from function import imgs_set_
    from action_zeno import confirm_all
    from massenger import line_to_me
    try:
        print("system_check")

        full_path = "c:\\my_games\\zenonia\\data_zeno\\imgs\\check\\system_check.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(100, 200, 900, 860, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            confirm_all(cla)

            why = "제노는 현재 시스템 점검 중"
            print(why)
            line_to_me(cla, why)

            dir_path = "C:\\my_games\\load\\zenonia"
            file_path = dir_path + "\\start.txt"
            file_path2 = dir_path + "\\cla.txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)

    except Exception as e:
        print(e)
        return 0