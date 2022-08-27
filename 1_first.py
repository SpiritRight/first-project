# 영어단어 저장하고 맞추는 프로그램
# 1. 영어단어와 한국어 한 번에 입력 or 영어단어, 한국어를 같은 줄에 입력
# 2. 입력 후 입력 한 것을 삭제
# 3. 삭제 한 단어들을 딕셔러니로 해서 묶어서 저장 후 밑에 표기
# 4. 시험보기 버튼을 누르면 랜덤으로 영어단어나 한국어를 보여주면서 테스트 보기
# 5. 다 푼 후 제출버튼을 누르면 몇점이고 뭐가 틀렸는지 창으로 보여주기.


import tkinter as tk

def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button")

    labelExample.pack()
    buttonExample.pack()

app = tk.Tk()
buttonExample = tk.Button(app, 
              text="Create new window",
              command=createNewWindow)
buttonExample.pack()

app.mainloop()