import turtle as t
import time
import random

def start():
    restart="y"
    while restart=="y":

        count=0        
        num_list=[]
        user_list=[]

        t.bgcolor("pink")
        t.ht()
        t.up()
        t.goto(0,0)
        t.write("START", False, "center", ("", 30))
        time.sleep(2)
        t.clear()

        
        num_input=t.textinput("Remember Numbers", "몇 개로 도전하나요?")
        for _ in range(int(num_input)):
            rand_num=random.randint(1, 50)
            t.write(rand_num, False, "center",("",70))
            num_list.append(rand_num)
            time.sleep(1)
            t.clear()


        user_input=t.textinput("Remember Numbers", "정답은? (예시: 2 14 31)").split()
        user_list=[int(i) for i in user_input]
     
       
        for i in range(int(num_input)):
            if num_list[i]==user_list[i]:
                count+=1


        t.write(f"{num_input}개 중에 맞힌 갯수 : {count}", False, "center", ("",30))
        t.goto(0,-50)

        if count==int(num_input):
            t.write("당신은 천재! 도전 갯수를 올려봐요!",False,"center",("",30))
        else:
            t.write(f"정답은 {num_list}",False,"center",("",30))
            t.goto(0,-100)
            t.write(f"당신 답은 {user_list}",False,"center",("",30))
            t.goto(0,-150)
            t.write("연습이 필요하네요ㅎㅎ",False,"center",("",30))

        
        time.sleep(3)
        t.clear()
        restart=t.textinput("Remember Numbers","다시도전하시나요? y or n")
        if restart=="n":
            t.goto(0,0)
            t.write("Bye Bye~",False,"center",("",30))



    t.done()


start()