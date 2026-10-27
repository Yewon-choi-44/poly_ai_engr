# 1. 사용자로부터 키(cm)와 몸무게를(kg) 입력받아 BMI를 계산하고 비만여부를 알려주는 프로그램을 모듈을 활용하여 작성하시오.
# (파일명: bmi_main.py)
# 모듈명: bmi_module.py

import bmi_module as bm

kg = float(input("키(cm): "))
cm = float(input("몸무게(kg): "))

aa=bm.calculate_bmi(kg,cm) 
bm.get_bmi_status(aa)