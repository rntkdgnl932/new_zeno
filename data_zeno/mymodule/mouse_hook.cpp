#include <Mouse.h>
#include <Keyboard.h>

// 윈도우 키와 왼쪽 표시 버튼의 HID 키 코드
#define KEY_LEFT_GUI 0x08
#define KEY_LEFT_BRACE 0x2F

void moveMouse(int x, int y) {
  Mouse.move(x, y);
}

void clickMouse() {
  Mouse.click();
}

void dragMousePress() {
  Mouse.press();
}

void dragMouseRelease() {
  Mouse.release();
}

void left_win() {
  // 윈도우 키를 누른 상태로 왼쪽 표시 버튼을 누르기
  Keyboard.press(KEY_LEFT_GUI);
  delay(100); // 버튼을 누르는 시간(100밀리초)
  Keyboard.press(KEY_LEFT_ARROW);
  delay(100); // 버튼을 누르는 시간(100밀리초)
  Keyboard.releaseAll();

  delay(1000); // 다음 동작까지의 대기 시간(1초)
}

void right_win() {
  // 윈도우 키를 누른 상태로 왼쪽 표시 버튼을 누르기
  Keyboard.press(KEY_LEFT_GUI);
  delay(100); // 버튼을 누르는 시간(100밀리초)
  Keyboard.press(KEY_RIGHT_ARROW);
  delay(100); // 버튼을 누르는 시간(100밀리초)
  Keyboard.releaseAll();

  delay(1000); // 다음 동작까지의 대기 시간(1초)
}

void click_win() {
  // 윈도우 키를 누른 상태로 왼쪽 표시 버튼을 누르기
  Keyboard.press(KEY_LEFT_GUI);
  delay(100); // 버튼을 누르는 시간(100밀리초)
  Keyboard.releaseAll();

  delay(1000); // 다음 동작까지의 대기 시간(1초)
}

void setup() {
  Serial.begin(9600); // 시리얼 통신 시작
  Mouse.begin(); // 마우스 초기화
  Keyboard.begin(); // 키보드 초기화
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n'); // 시리얼에서 데이터 읽기
    int x, y, z;
    sscanf(data.c_str(), "x = %d, y = %d, z = %d", &x, &y, &z);


    if (z == 1) {
        // x, y 좌표에 마우스 이동 수행
        moveMouse(x, y);
    } else if (z == 2) {
        // 마우스 클릭 수행
        clickMouse();
    } else if (z == 3) {
        // 마우스 누르기
        dragMousePress();
    } else if (z == 4) {
        // 마우스 떼기
        dragMouseRelease();
    } else if (z == 5) {
        // 마우스 떼기
        left_win();
    } else if (z == 6) {
        // 마우스 떼기
        right_win();
    } else if (z == 7) {
        // 마우스 떼기
        click_win();
    }

    // 숫자 0 값을 파이썬으로 전송
    if (-3 < x && x < 3 && -3 < y && y < 3) {
        Serial.println(0);
    } else {
        Serial.println(1);
    }
  }
}