# 마트 주문 시스템
# 마트에서 파는 물품들을 추가해 놓고
# 선택할 때 마다 밑에 창에 추가가 되게끔
# 물품들의 가격은 시세 변동에 따라 킬 때 마다 +- 10% 안으로 바뀌게 끔 만들 예정

from tkinter import *
from tkinter.ttk import Labelframe
import random
import tkinter.messagebox as msgbox

root = Tk()
root.title("S마트 구매 시스템")
root.geometry("400x300")

my_money = 100000
# 장바구니 등록
def btn_check(cnt, text, price):
    # print(btn_drink1['text'])
    # label1_drink1 = Label(frame_bag, text=Text).grid(row=1, column=1)
    # label1_price1 = Label(frame_bag, text=price).grid(row=2, column=1)
    # label1_cnt1 = Label(frame_bag, text=cnt).grid(row=3, column=1)
    global my_money
    response = msgbox.askokcancel("확인 / 취소", "구매 하시겠습니까?")
    if response == 1:
        msgbox.showinfo("안내창", "{} 가 구매 되었습니다!".format(text))
        my_money -= price
        frame_my_money.config(text=my_money)
        cnt += 1
        print(cnt)
        return cnt


# 물품 카테고리
frame_drink = LabelFrame(root, text="음료")
# frame_drink.pack(side="right", fill="both", expand=True)
frame_drink.grid(row=0, column=0)

frame_veg = LabelFrame(root, text="채소")
# frame_veg.pack(side="right", fill="both", expand=True)
frame_veg.grid(row=0, column=1)

frame_snack = LabelFrame(root, text="과자")
# frame_snack.pack(side="right", fill="both", expand=True)
frame_snack.grid(row=0, column=2)

frame_ice = LabelFrame(root, text="아이스크림")
# frame_ice.pack(side="right", fill="both", expand=True)
frame_ice.grid(row=0, column=3)

frame_bag = LabelFrame(root, text="남은 돈")
frame_bag.grid(row=1, column=0)

frame_my_money = Label(frame_bag, text=my_money)
frame_my_money.pack()


# 물품 버튼
#음료 물품

btn_drink1 = Button(frame_drink, text="사이다" , width=5, height=2)
btn_drink1.config(command= lambda GetText=btn_drink1['text'] : btn_check(cnt_drink1, GetText, price_drink1))
cnt_drink1 = 0

btn_drink2 = Button(frame_drink, width=5, height=2, text="콜라")
btn_drink2.config(command= lambda GetText=btn_drink2['text'] : btn_check(GetText,price_drink2))

btn_drink3 = Button(frame_drink, width=5, height=2, text="포카리")
btn_drink3.config(command= lambda GetText=btn_drink3['text'] : btn_check(GetText,price_drink3))

btn_drink4 = Button(frame_drink, width=5, height=2, text="웰치스")
btn_drink4.config(command= lambda GetText=btn_drink4['text'] : btn_check(GetText,price_drink4))

btn_drink1.grid(row=1, column=0,  padx=3, pady=3)
btn_drink2.grid(row=2, column=0,  padx=3, pady=3)
btn_drink3.grid(row=3, column=0,  padx=3, pady=3)
btn_drink4.grid(row=4, column=0,  padx=3, pady=3)

price_drink1 = random.randrange(900,1100)
price_drink2 = random.randrange(900,1100)
price_drink3 = random.randrange(900,1100)
price_drink4 = random.randrange(900,1100)

Label_drink1 = Label(frame_drink, text=price_drink1).grid(row=1, column=1)
Label_drink2 = Label(frame_drink, text=price_drink2).grid(row=2, column=1)
Label_drink3 = Label(frame_drink, text=price_drink3).grid(row=3, column=1)
Label_drink4 = Label(frame_drink, text=price_drink4).grid(row=4, column=1)

#채소 물품
btn_veg1 = Button(frame_veg, width=5, height=2, text="당근")
btn_veg2 = Button(frame_veg, width=5, height=2, text="양배추")
btn_veg3 = Button(frame_veg, width=5, height=2, text="상추")
btn_veg4 = Button(frame_veg, width=5, height=2, text="버섯")

btn_veg1.grid(row=1, column=0,  padx=3, pady=3)
btn_veg2.grid(row=2, column=0,  padx=3, pady=3)
btn_veg3.grid(row=3, column=0,  padx=3, pady=3)
btn_veg4.grid(row=4, column=0,  padx=3, pady=3)

price_veg1 = random.randrange(900,1100)
price_veg2 = random.randrange(1700,2000)
price_veg3 = random.randrange(20000,30000)
price_veg4 = random.randrange(900,1100)

Label_veg1 = Label(frame_veg, text=price_veg1).grid(row=1, column=1)
Label_veg2 = Label(frame_veg, text=price_veg2).grid(row=2, column=1)
Label_veg3 = Label(frame_veg, text=price_veg3).grid(row=3, column=1)
Label_veg4 = Label(frame_veg, text=price_veg4).grid(row=4, column=1)

# 과자 물품
btn_snack1 = Button(frame_snack, width=5, height=2, text="빼빼로")
btn_snack2 = Button(frame_snack, width=5, height=2, text="프링글스")
btn_snack3 = Button(frame_snack, width=5, height=2, text="포카칩")
btn_snack4 = Button(frame_snack, width=5, height=2, text="칸쵸")

btn_snack1.grid(row=1, column=0,  padx=3, pady=3)
btn_snack2.grid(row=2, column=0,  padx=3, pady=3)
btn_snack3.grid(row=3, column=0,  padx=3, pady=3)
btn_snack4.grid(row=4, column=0,  padx=3, pady=3)

price_snack1 = random.randrange(1000,1200)
price_snack2 = random.randrange(2000,2500)
price_snack3 = random.randrange(1500,1800)
price_snack4 = random.randrange(900,1000)

Label_snack1 = Label(frame_snack, text= price_snack1).grid(row=1, column=1)
Label_snack2 = Label(frame_snack, text= price_snack2).grid(row=2, column=1)
Label_snack3 = Label(frame_snack, text= price_snack3).grid(row=3, column=1)
Label_snack4 = Label(frame_snack, text= price_snack4).grid(row=4, column=1)


# 아이스크림 물품
btn_ice1 = Button(frame_ice, width=5, height=2, text="비비빅")
btn_ice2 = Button(frame_ice, width=5, height=2, text="바밤바")
btn_ice3 = Button(frame_ice, width=5, height=2, text="죠스바")
btn_ice4 = Button(frame_ice, width=5, height=2, text="월드콘")

btn_ice1.grid(row=1, column=0,  padx=3, pady=3)
btn_ice2.grid(row=2, column=0,  padx=3, pady=3)
btn_ice3.grid(row=3, column=0,  padx=3, pady=3)
btn_ice4.grid(row=4, column=0,  padx=3, pady=3)

price_ice1 = random.randrange(400,500)
price_ice2 = random.randrange(400,500)
price_ice3 = random.randrange(400,500)
price_ice4 = random.randrange(600,800)

Label_ice1 = Label(frame_ice, text=price_ice1).grid(row=1, column=1)
Label_ice2 = Label(frame_ice, text=price_ice2).grid(row=2, column=1)
Label_ice3 = Label(frame_ice, text=price_ice3).grid(row=3, column=1)
Label_ice4 = Label(frame_ice, text=price_ice4).grid(row=4, column=1)


# 장바구니




root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()
