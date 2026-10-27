def calculate_bmi(weight, height_cm):
   bmi = float(weight/((height_cm*0.01)**2))
   return bmi
    
def get_bmi_status(bmi):
    if bmi < 18.5:
        print("건강 상태: 저체중")
    elif 18.5 <= bmi < 23:
        print("건강 상태: 정상")
    elif 23 <= bmi < 25:
        print("건강 상태: 과체중")
    elif bmi >= 25:
        print("건강 상태: 비만")

    #딕셔너리로도 만들면 좋을듯