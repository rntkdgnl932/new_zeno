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

def go_test(cla):
    print('hi test!', cla)


# 이미지 특정 색상 제외함
def image_processing(src, min_color, max_color):
    import cv2
    import numpy
    try:
        img_ = cv2.cvtColor(numpy.array(src), cv2.COLOR_RGB2BGR)
        exception_img = cv2.inRange(img_, min_color, max_color)
        return exception_img
    except Exception as e:
        print(e)
        return 0

def random_int():
    try:
        import random
        result = random.randint(1, 4)
        return int(result)
    except Exception as e:
        print(e)

def random_int_2():
    try:
        import random
        result = random.randint(100, 200)
        return result
    except Exception as e:
        print(e)

def random_int_3():
    try:
        import random
        result = random.randint(50, 100)
        return result
    except Exception as e:
        print(e)

def isNumber_(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def change_number(many_potion):
    try:

        potion_ = many_potion

        if " " in potion_:
            potion_ = potion_.replace(' ', '')
            print("!!!!!! ['   '] !!!!!!!", potion_)
        if "고" in potion_:
            potion_ = potion_.replace('고', '2')
            print("!!!!!! [' 고 => 2 '] !!!!!!!", potion_)
        if "ㄷ" in potion_:
            potion_ = potion_.replace('ㄷ', '5')
            print("!!!!!! [' ㄷ => 5 '] !!!!!!!", potion_)
        if "요" in potion_:
            potion_ = potion_.replace('요', '8')
            print("!!!!!! [' 요 => 8 '] !!!!!!!", potion_)
        if "°" in potion_:
            potion_ = potion_.replace('°', '0')
            print("!!!!!! [   ° => 0   ] !!!!!!!", potion_)
        if ")" in potion_:
            potion_ = potion_.replace(')', '1')
            print("!!!!!! [   ) => 1   ] !!!!!!!", potion_)
        if "‘" in potion_:
            potion_ = potion_.replace('‘', '1')
            print("!!!!!! [   ‘ => 1   ] !!!!!!!", potion_)
        if "?" in potion_:
            potion_ = potion_.replace('?', '2')
            print("!!!!!! [   ? => 2  ] !!!!!!!", potion_)
        if "L" in potion_:
            potion_ = potion_.replace('L', '1')
            print("!!!!!! [   L => 1  ] !!!!!!!", potion_)
        if "|" in potion_:
            potion_ = potion_.replace('|', '1')
            print("!!!!!!![   | => 1  ]!!!!!!!!!!!", potion_)
        if "A" in potion_:
            potion_ = potion_.replace('A', '4')
            print("!!!!!!!!![  A => 4 ]!!!!!!!!!!!!!", potion_)
        if "D" in potion_:
            potion_ = potion_.replace('D', '2')
            print("!!!!!!!!![  D => 2 ]!!!!!!!!!!!!!", potion_)
        if "G" in potion_:
            potion_ = potion_.replace('G', '6')
            print("!!!!!!!!![  G => 6 ]!!!!!!!!!!!!!", potion_)
        if "B" in potion_:
            potion_ = potion_.replace('B', '8')
            print("!!!!!!!!![  B => 8  ]!!!!!!!!!!!!!", potion_)
        if "T" in potion_:
            potion_ = potion_.replace('T', '7')
            print("!!!!!!!!![  T => 7  ]!!!!!!!!!!!!!", potion_)
        if "S" in potion_:
            potion_ = potion_.replace('S', '5')
            print("!!!!!!!!![  S => 5  ]!!!!!!!!!!!!!", potion_)
        if "Q" in potion_:
            potion_ = potion_.replace('Q', '9')
            print("!!!!!!!!![  Q => 9  ]!!!!!!!!!!!!!", potion_)
        if "F" in potion_:
            potion_ = potion_.replace('F', '9')
            print("!!!!!!!!![  F => 9  ]!!!!!!!!!!!!!", potion_)
        if "R" in potion_:
            potion_ = potion_.replace('R', '8')
            print("!!!!!!!!![  R => 8  ]!!!!!!!!!!!!!", potion_)
        if "a" in potion_:
            potion_ = potion_.replace('a', '4')
            print("!!!!!!!!![  a => 4  ]!!!!!!!!!!!!!", potion_)
        if "g" in potion_:
            potion_ = potion_.replace('g', '9')
            print("!!!!!!!!![  g => 9  ]!!!!!!!!!!!!!", potion_)

        potion_ = int_put_(potion_)

        if potion_[0] == "0":
            potion_ = "1" + potion_
            print("potion_ = '1' + potion_", potion_)

        return potion_
    except Exception as e:
        print(e)


def int_put_(data):
    try:
        import re
        data_ = data.replace(',', '').strip()
        data_2 = data_.replace('.', '').strip()
        data_3 = data_2.replace(' ', '').strip()
        data_4 = data_3.replace('/', '').strip()

        # data_2 = data_.strip().replace('.', '')
        # data_3 = data_2.strip().replace(' ', '')
        # data_4 = data_3.strip().replace('/', '')
        result = re.sub(r'[^0-9]', '', data_4)
        return result
    except ValueError:
        return False

def in_number_check(cla, data):
    try:
        import cv2
        import numpy as np
        from function import text_check_get, int_put_

        isNumber = False
        # print("들어온 데이타?", data)
        # print("len potion", len(data))
        if len(data) > 0:
            # print("길이가 0 보다 크다", len(data))
            for i in range(len(data)):
                result_num_bool = data[i].isdigit()
                if result_num_bool == True:
                    isNumber = True
        else:
            print("데이터가 길이가 없고 비어있다")

        return isNumber
    except Exception as e:
        print(e)

def imgs_set(a, b, c, d, cla, img):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
        
        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        if cla == 'four':
            plus = 960 + 960 + 960
        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10 , d - b + 10),
                                               confidence=0.7)
        return result
    except ValueError:
        return False

def imgs_set_(a, b, c, d, cla, img, data):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui

        ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

        if cla == 'one':
            plus = 0
        if cla == 'two':
            plus = 960
        if cla == 'three':
            plus = 960 + 960
        if cla == 'four':
            plus = 960 + 960 + 960

        pos = (a + plus, b, c - a, d - b)
        pyautogui.screenshot("asd.png", region=pos)

        result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10, d - b + 10),
                                               confidence=data)
        return result
    except ValueError:
        return False


def click_with_image(image_path):
    try:
        from PIL import ImageGrab
        from functools import partial
        import pyautogui
        isClick = False
        data_count = 0
        while isClick is False:
            data_count += 1
            if data_count > 7:
                isClick = True
            location = pyautogui.locateOnScreen(image_path)
            if location is not None:
                pyautogui.click(location)
                isClick = True
    except Exception as e:
        print(e)

def get_region(start_x, start_y, end_x, end_y, cla):
    coordinate = 0
    if cla == 'one':
        coordinate = 0
    if cla == 'two':
        coordinate = 960
    if cla == 'three':
        coordinate = 960 + 960
    if cla == 'four':
        coordinate = 960 + 960 + 960

    value = (start_x + random_int() + coordinate, start_y, end_x - start_x + random_int(), end_y - start_y)
    return value

def click_pos(pos):
    try:
        import pyautogui
        pyautogui.moveTo(pos[0] + random_int(), pos[1] + random_int())
        time.sleep(random_int())
        pyautogui.click()
    except Exception as e:
        print(e)



def mouse_move(x, y):
    import pydirectinput
    try:
        reg_x = x + random_int()
        reg_y = y + random_int()
        pydirectinput.moveTo(reg_x, reg_y)
        print("mouse_move", reg_x, reg_y)

    except Exception as e:
        print(e)
        return 0


def win_left_move(cla):
    try:
        import serial

        arduino_port = v_.COM_
        baudrate = v_.speed_

        print("win_left_move", cla)

        ser = serial.Serial(arduino_port, baudrate)

        moveX = 0
        moveY = 0
        moveZ = 7

        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()

    except Exception as e:
        print(e)
        return 0


def win_right_move(cla):
    try:
        import serial

        arduino_port = v_.COM_
        baudrate = v_.speed_

        print("win_right_move", cla)

        ser = serial.Serial(arduino_port, baudrate)

        moveX = 0
        moveY = 0
        moveZ = 6

        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()

    except Exception as e:
        print(e)
        return 0


def click_pos_2(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui
        # print("test")
        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        if cla == 'four':
            coordinate = 960 + 960 + 960

        ser = serial.Serial(arduino_port, baudrate)

        moveZ = 1
        k_reg = v_.mouse_speed
        c_reg = v_.mouse_pm

        move_ = False
        move_count = 0
        while move_ is False:
            move_count += 1
            if move_count > 300:
                print("move_count", move_count)
                move_ = True

            # 이동 시킬 포인트 계산
            x_reg = pos_1 + coordinate - pyautogui.position()[0]
            y_reg = pos_2 - pyautogui.position()[1]
            # if move_count > 280:
            #     print("이동 시킬 포인트 계산 y_reg", y_reg)

            if -c_reg < x_reg < c_reg:
                moveX = x_reg
            elif x_reg > 0:
                if x_reg == k_reg:
                    moveX = x_reg
                else:
                    moveX = min(k_reg, x_reg)
            else:
                if x_reg == -k_reg:
                    moveX = x_reg
                else:
                    moveX = max(-k_reg, x_reg)

            if -c_reg < y_reg < c_reg:
                moveY = y_reg
            elif y_reg > 0:
                if y_reg == k_reg:
                    moveY = y_reg
                else:
                    moveY = min(k_reg, y_reg)
            else:
                if y_reg == -k_reg:
                    moveY = y_reg
                else:
                    moveY = max(-k_reg, y_reg)

            # # 이동 시킬 포인트 결과값
            # print("이동 시킬 포인트 결과값 moveY", moveY)

            data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
            ser.write(data.encode())
            received_data = ser.readline().decode().strip()

            if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]
                if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg:
                    # print("move_count", move_count)
                    # print("moveX", moveX)
                    # print("moveY", moveY)
                    # print("x_reg", x_reg)
                    # print("y_reg", y_reg)
                    moveZ = 2
                    move_ = True
                    data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                    ser.write(data.encode())
                # else:
                #     print("아직 오차 범위 밖이다...", move_count)
                #     print("x_reg", x_reg)
                #     print("y_reg", y_reg)





        ser.close()

    except Exception as e:
        print("error:", e)


def click_pos_reg(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 0
        if cla == 'three':
            coordinate = 0
        if cla == 'four':
            coordinate = 0

        ser = serial.Serial(arduino_port, baudrate)

        moveZ = 1
        k_reg = v_.mouse_speed
        c_reg = v_.mouse_pm

        move_ = False
        move_count = 0
        while move_ is False:
            move_count += 1
            if move_count > 300:
                move_ = True



            # 이동 시킬 포인트 계산
            x_reg = pos_1 + coordinate - pyautogui.position()[0]
            y_reg = pos_2 - pyautogui.position()[1]

            if -c_reg < x_reg < c_reg:
                moveX = x_reg
            elif x_reg > 0:
                if x_reg == k_reg:
                    moveX = x_reg
                else:
                    moveX = min(k_reg, x_reg)
            else:
                if x_reg == -k_reg:
                    moveX = x_reg
                else:
                    moveX = max(-k_reg, x_reg)

            if -c_reg < y_reg < c_reg:
                moveY = y_reg
            elif y_reg > 0:
                if y_reg == k_reg:
                    moveY = y_reg
                else:
                    moveY = min(k_reg, y_reg)
            else:
                if y_reg == -k_reg:
                    moveY = y_reg
                else:
                    moveY = max(-k_reg, y_reg)


            data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
            ser.write(data.encode())
            received_data = ser.readline().decode().strip()

            if received_data == '0' or (-c_reg < moveX < c_reg and -c_reg < moveY < c_reg):
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]
                if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg:
                    moveZ = 2
                    move_ = True
                    data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                    ser.write(data.encode())


        ser.close()

    except Exception as e:
        print("error:", e)

# def mouse_move_cpp(pos_1, pos_2, cla):
#     try:
#         import serial
#         import pyautogui
#
#         arduino_port = v_.COM_
#         baudrate = v_.speed_
#
#         coordinate = 0
#         if cla == 'one':
#             coordinate = 0
#         if cla == 'two':
#             coordinate = 0
#         if cla == 'three':
#             coordinate = 0
#         if cla == 'four':
#             coordinate = 0
#
#         ser = serial.Serial(arduino_port, baudrate)
#
#         x_current, y_current = pyautogui.position()
#
#         x_reg = pos_1 + coordinate - x_current
#         y_reg = pos_2 - y_current
#
#         moveZ = 1
#
#         move_ = False
#         move_count = 0
#         while move_ is False:
#             move_count += 1
#             if move_count > 200:
#                 move_ = True
#
#             k_reg = v_.mouse_speed
#             c_reg = v_.mouse_pm
#
#             if -c_reg < x_reg < c_reg:
#                 moveX = x_reg
#             elif x_reg > 0:
#                 moveX = min(k_reg, x_reg)
#             else:
#                 moveX = max(-k_reg, x_reg)
#
#             if -c_reg < y_reg < c_reg:
#                 moveY = y_reg
#             elif y_reg > 0:
#                 moveY = min(k_reg, y_reg)
#             else:
#                 moveY = max(-k_reg, y_reg)
#
#             data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
#             ser.write(data.encode())
#             received_data = ser.readline().decode().strip()
#
#             if received_data == '0' or (-c_reg < moveX < c_reg and -c_reg < moveY < c_reg):
#                 move_ = True
#                 data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
#                 ser.write(data.encode())
#             x_reg = pos_1 + coordinate - pyautogui.position()[0]
#             y_reg = pos_2 - pyautogui.position()[1]
#
#         ser.close()
#
#     except Exception as e:
#         print("error:", e)

def mouse_move_cpp(pos_1, pos_2, cla):
    try:
        import serial
        import pyautogui

        arduino_port = v_.COM_
        baudrate = v_.speed_

        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        if cla == 'four':
            coordinate = 960 + 960 + 960

        ser = serial.Serial(arduino_port, baudrate)

        moveZ = 1
        k_reg = v_.mouse_speed
        c_reg = v_.mouse_pm

        move_ = False
        move_count = 0
        while move_ is False:
            move_count += 1
            if move_count > 300:
                move_ = True



            # 이동 시킬 포인트 계산
            x_reg = pos_1 + coordinate - pyautogui.position()[0]
            y_reg = pos_2 - pyautogui.position()[1]

            if -c_reg < x_reg < c_reg:
                moveX = x_reg
            elif x_reg > 0:
                if x_reg == k_reg:
                    moveX = x_reg
                else:
                    moveX = min(k_reg, x_reg)
            else:
                if x_reg == -k_reg:
                    moveX = x_reg
                else:
                    moveX = max(-k_reg, x_reg)

            if -c_reg < y_reg < c_reg:
                moveY = y_reg
            elif y_reg > 0:
                if y_reg == k_reg:
                    moveY = y_reg
                else:
                    moveY = min(k_reg, y_reg)
            else:
                if y_reg == -k_reg:
                    moveY = y_reg
                else:
                    moveY = max(-k_reg, y_reg)

            data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
            ser.write(data.encode())
            received_data = ser.readline().decode().strip()

            if -c_reg < moveX < c_reg and -c_reg < moveY < c_reg:
                x_reg = pos_1 + coordinate - pyautogui.position()[0]
                y_reg = pos_2 - pyautogui.position()[1]
                if -c_reg < x_reg < c_reg and -c_reg < y_reg < c_reg:
                    move_ = True
                    data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
                    ser.write(data.encode())


        ser.close()

    except Exception as e:
        print("error:", e)

def drag_pos_Press():
    try:
        import serial
        import pyautogui

        arduino_port = v_.COM_
        baudrate = v_.speed_

        ser = serial.Serial(arduino_port, baudrate)

        # 마우스 누르기
        moveX = 0
        moveY = 0
        moveZ = 3
        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())



        ser.close()

    except Exception as e:
        print("error:", e)

def drag_pos_Release():
    try:
        import serial
        import pyautogui

        arduino_port = v_.COM_
        baudrate = v_.speed_

        ser = serial.Serial(arduino_port, baudrate)
        # 마우스 떼기
        moveX = 0
        moveY = 0
        moveZ = 4
        data = f'x = {moveX}, y = {moveY}, z = {moveZ}\n'
        ser.write(data.encode())

        ser.close()

    except Exception as e:
        print("error:", e)

def drag_pos(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        # 마우스 이동
        mouse_move_cpp(pos_1, pos_2, cla)

        # 0.2초
        time.sleep(0.2)
        # 마우스 누르기
        drag_pos_Press()
        # 0.2초
        time.sleep(0.2)
        # 마우스 이동
        mouse_move_cpp(pos_3, pos_4, cla)
        # 0.2초
        time.sleep(0.2)
        # 마우스 떼기
        drag_pos_Release()


    except Exception as e:
        print("error:", e)

def drag_pos_reg(pos_1, pos_2, pos_3, pos_4, cla):
    try:
        cla = "one"
        # 마우스 이동
        mouse_move_cpp(pos_1, pos_2, cla)

        # 0.2초
        time.sleep(0.2)
        # 마우스 누르기
        drag_pos_Press()
        # 0.2초
        time.sleep(0.2)
        # 마우스 이동
        mouse_move_cpp(pos_3, pos_4, cla)
        # 0.2초
        time.sleep(0.2)
        # 마우스 떼기
        drag_pos_Release()

    except Exception as e:
        print("error:", e)


# def text_check(posX1, posY1, posX2, posY2, text, method, method_pos):
#     try:
#         isClick = False
#         pos = (posX1, posY1, posX2 - posX1, posY2 - posY1)
#         while isClick is False:
#             pic = pyautogui.screenshot("asd.png", region=pos)
#             pic_ = numpy.array(pic)
#             # result = reader.readtext(pic_)
#             for txt in result:
#                 if txt is not None:
#                     print(txt[1])
#                     for text_ in text:
#                         if txt[1] == text_:
#                             print("aaa!!")
#                             method(method_pos)
#                             isClick = True
#     except Exception as e:
#         print(e)

def text_check_potion(posX1, posY1, posX2, posY2, cla):
    try:
        # from PIL import ImageGrab
        # from functools import partial
        import pyautogui
        import pytesseract

        potion = 0

        # result = pyautogui.locateCenterOnScreen(img, region=(a + plus, b, c - a + 10, d - b + 10),
        #                                         confidence=0.7)

        img = pyautogui.screenshot('asd.png', region=(get_region(posX1, posY1, posX2, posY2, cla)))
        white_img = image_processing(img, (148, 148, 148), (255, 255, 255))
        potion_count_ = pytesseract.image_to_string(white_img, lang=None)
        # print("text_check_potion", potion_count_)

        result_num_in = in_number_check(cla, potion_count_)
        if result_num_in == True:
            potion = change_number(potion_count_)
            potion_bloon = potion.isdigit()
            if potion_bloon == True:
                potion = int(potion)
            else:
                print("potion => 숫자 아님")

        return potion
    except Exception as e:
        print(e)
        return 0
def text_check_get(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        if cla == 'four':
            coordinate = 960 + 960 + 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        pic_ = numpy.array(pic)
        result = pytesseract.image_to_string(pic_, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_2(posX1, posY1, posX2, posY2, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        if cla == 'four':
            coordinate = 960 + 960 + 960
        isClick = False
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_3(posX1, posY1, posX2, posY2, color, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import cv2
        import pytesseract
        import numpy
        from PIL import Image
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        if cla == 'four':
            coordinate = 960 + 960 + 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png", cv2.IMREAD_COLOR)  # 사진을 컬러로 읽어오기
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)
        if color == 0:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 1:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2GRAY)
        if color == 2:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)
        if color == 3:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2YUV)
        if color == 4:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 5:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        if color == 6:
            rgb_image = cv2.cvtColor(pic_, cv2.COLOR_BGR2RGB)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        ##
        return result
    except Exception as e:
        print(e)
        return 0

def text_check_get_4(posX1, posY1, posX2, posY2, color, cla):
    try:
        from PIL import ImageGrab
        from functools import partial
        import numpy as np
        import cv2
        import pytesseract
        import numpy
        import pyautogui
        # color change
        coordinate = 0
        if cla == 'one':
            coordinate = 0
        if cla == 'two':
            coordinate = 960
        if cla == 'three':
            coordinate = 960 + 960
        if cla == 'four':
            coordinate = 960 + 960 + 960
        pos = (posX1 + coordinate, posY1, posX2 - posX1, posY2 - posY1)
        pyautogui.screenshot("asd.png", region=pos)
        pic = cv2.imread("asd.png")
        cv2.imwrite("asd.png", pic)
        ##
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        # path = Image.open(r'asd.png')
        pic_ = numpy.array(pic)

        rgb_image_ = cv2.cvtColor(pic_, cv2.COLOR_BGR2HSV)

        lower_yellow = np.array([60, 100, 100])
        upper_yellow = np.array([90, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        if color == 0:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_yellow, upper_yellow)
            rgb_image = cv2.bitwise_and(pic, pic, mask = rgb_image_ready)
        if color == 1:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_green, upper_green)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        if color == 2:
            rgb_image_ready = cv2.inRange(rgb_image_, lower_red, upper_red)
            rgb_image = cv2.bitwise_and(pic, pic, mask=rgb_image_ready)
        result = pytesseract.image_to_string(rgb_image, lang='kor+eng')

        cv2.imshow('img_color', pic)

        ##
        return result
    except Exception as e:
        print(e)
        return 0





