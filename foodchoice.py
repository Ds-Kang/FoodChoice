import random
import tkinter as tk
from tkinter import messagebox

Kr=['김치찌개','비지찌개','부대찌개','삼겹살', '된장찌개', '김치찜', '김치볶음밥', '생선구이', '보쌈', '칼국수', '샤브샤브', '감자전' ,'김치전', '잔치국수', '계란찜', '소고기무국', '제육볶음', '계란말이', '미역국', '닭갈비', '돼지갈비', '냉면', '두루치기', '순두부찌개', '순대볶음', '파전', '육회', '비빔밥']
Ch=['마라탕','마라상궈','짜장면','짬뽕', '울면', '우육면', '탄탄면', '딤섬', '꿔바로우', '깐풍기', '볶음밥', '청경채 볶음', '양꼬치', '마파두부', '북경오리']
Jp=['우동','초밥','돈까스', '데리야끼 숙주볶음', '회', '라멘', '돈부리', '장어덮밥', '사케동', '오꼬노미야끼', '김치가츠나베', '타꼬야끼', '야끼소바', '나가사끼짬뽕', '카레라이스']
Bs=['라면','비빔삽겹','햄버거', '튀김', '떡볶이', '순대', '오뎅', '떡꼬치', '닭꼬치', '닭강정', '만두', '호떡', '크레이프', '붕어빵', '빵', '토스트', '샌드위치', '크레이프', '타르트']
Bd=['치킨','피자', '파스타', '씨리얼', '그라탕', '라자냐', '요거트', '햄버거', '리조또', '필라프', '스테이크', '피시앤칩스', '바베큐', '소세지', '슈바인학센', '빠에야', '슈니첼', '케밥', '프레첼', '타파스', '또띠아', '엠파나다']
Gt=['핫도그', '인도커리', '베트남 쌀국수', '팟타이', '분짜', '도너츠', '요거트', '러시아 음식', '할랄음식', '아랍음식', '멕시칸 음식', '아프리카 음식', '케밥', '덴마크 음식', '스위스 음식', '프랑스음식']

root=tk.Tk()
root.title('FoodFinder')
root.geometry('370x370')
root.resizable(0,0)

def eat_choice(type):
	food=random.choice(type)
	messagebox.showinfo("how about",food)

label1=tk.Label(root,text='음식 종류')
label1.grid(row=0,column=1)

Krbtn=tk.Button(root, text="한식",command=lambda: eat_choice(Kr),width=16,height=8)
Krbtn.grid(row=1,column=0)
Chbtn=tk.Button(root, text="중식",command=lambda: eat_choice(Ch),width=16,height=8)
Chbtn.grid(row=1,column=1)
Jpbtn=tk.Button(root, text="일식",command=lambda: eat_choice(Jp),width=16,height=8)
Jpbtn.grid(row=1,column=2)
Bsbtn=tk.Button(root, text="분식",command=lambda: eat_choice(Bs),width=16,height=8)
Bsbtn.grid(row=2,column=0)
Bdbtn=tk.Button(root, text="양식",command=lambda: eat_choice(Bd),width=16,height=8)
Bdbtn.grid(row=2,column=1)
Gtbtn=tk.Button(root, text="기타",command=lambda: eat_choice(Gt),width=16,height=8)
Gtbtn.grid(row=2,column=2)


root.mainloop()

