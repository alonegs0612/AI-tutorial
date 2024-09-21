# -*- coding: utf-8 -*-
"""Random Num Game.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fu4AToZprswaW28aj9J-_AQb8oYaSEu3
"""

import random

def 숫자_맞추기_게임():
    정답 = random.randint(1, 100)
    시도_횟수 = 0

    print("1부터 100 사이의 숫자를 맞춰보세요.")

    while True:
        시도 = int(input("숫자를 입력하세요: "))  # 이 줄을 들여쓰기 했습니다.
        시도_횟수 += 1

        if 시도 < 정답:
            print("더 큰 숫자입니다.")
        elif 시도 > 정답:
            print("더 작은 숫자입니다.")
        else:
            print(f"축하합니다. {시도_횟수}번만에 맞추셨습니다.")
            break

숫자_맞추기_게임()  # 게임 실행