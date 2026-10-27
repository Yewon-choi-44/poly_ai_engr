###########################################
# 항수명: select_sort()
# input: in_data
# output/return: 약 300개의 selectsort 당한 리스트들일텐데
#                300개가 return으로 다 반환이 되는가?
#                반환하고 싶으면 쟤네를 또 길이 약 300짜리 리스트에 넣어야 되는 거임?
#                쟤네 뭔 특별한 cv2.cvtColor(파일명, cv2.COLOR_BGR2GRAY)로 변환된 np.array에 들어있는 애들 아님?
#                내가 막 임의로 그냥 보통 리스트에다 넣어버리면
#                이미지로서 기능을 할 수 없게 되는거 아님?
#                걍 숫자 많이 든 보통 리스트 되는 거잖아 색이 밝거나 어둡다는 정보 담고 있는 숫자들 모음집/이미지 어쩌구가 아니라...
#                리스트에다 넣고 또 다시 변환을 해줘야 하나
#                정보가 보존이 됨? 이미 내가 보통 숫자들로 만들어버렸던 애들인데? -> 된댄다. 딱히 상관 없댄다.
#
#                그럼 내가 걍 랜덤 돌려서 아무 숫자 300개 리스트에다 담아서
#                cv2 라이브러리로 어쩌구 어떻게 변환하면 그것도 이미지가 되나?
#                파이썬으로 그렇게 쉽게 이미지를 만들 수가 있다고??? 그럴 수 있나??? 아닐텐데...........? - > 맞댄다.
#
#                일단 cv2에 뭐 들었는지 좀 뜯어야겠습니다.
#                얘가 그 말로만 듣던 OpenCV라면서여?
#                어케 기능하는지 / 어떤 모듈 들었는지 / 뭘 할 수 있는지 / 뭐하는 lib인지 / 어디까지 해줄 수 있는 놈인지

#                얘로 이미지 변환시키면 np.array에 들어가던데(맞나) 걔는 내가 일반 리스트처럼 바꾸고 조건문에다 조건 걸고 사용이 안된다.
#                그거 왜 그러는지 찾고 / np.array는 보통 배열이랑 뭐가 다른지 / 왜 numpy에 소속되어서 다른 배열이랑 구분되는지
#                / cv에 왜 numpy 기능 들어가서 분탕치는지 -> 그럴만 하댄다.

#                / 왜 내가 맘대로 사용할 수 없는지 / 보호되는 중인 건지 / 왜 조건문에다 쓰려면 .all(), .any() <이거 걸어줘야 하는지...etc.
#
# 제미나이 안 쓰고 싶은데 난 지엽적인 것인 것만 궁금해해서 물어보려면 구글링으론 빡세다. 이렇게 하는 거 아닌 것 같은데
# 그래도 어캄; 궁금한데 이해를 해야 뭘 할 거 아님 그래도 일단 구글링부터 해보겟음0
# 이번에도 과제를 기한 안에 낼 수 없겠습니다.
# 아무튼
# nxn개씩 묶은 리스트들을 선택정렬해서
# 그 결과들을 기억하라고 시킬거임.
############################################
def select_sort(in_data):
    n = len(in_data)
    for i in range(n-1):
        for j in range(i+1, n):
            if in_data[j]<in_data[i]:
                in_data[i], in_data[j] = in_data[j], in_data[i]
        print(f"{i+1}회전 결과: {in_data}")

############################################
# 함수명: median_filter()
#
############################################
def median_filter(in_img):
    select_sort(in_img[0:3, 0:3])
    pass



#여기부터 main
import cv2
noise_img = cv2.imread("C:/Users/AI-00/Desktop/salt-pepper-noise.jpg")
input_img =cv2.cvtColor(noise_img, cv2.COLOR_BGR2GRAY)
print("\ninput_img\n",input_img)

size_ = int(input("몇 x 몇으로 걸러낼건가? 숫자만 입력하라.: "))


exit()
filter_img = median_filter(input_img)
print(type(input_img.shape))
cv2.imshow("noise_img", noise_img)
cv2.waitKey()