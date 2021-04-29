#我的練習
password = 'a123456'

i = 0
j = 3
while i < 3 :
    x = input('請輸入密碼:')
    if x == password:
        print('登入成功')
        break
    else:
        i = i + 1
        j = j - 1
        if i == 3:
            print('你已經輸入三次了,再見!')
        else:
            print('登入失敗!你還有',j,'次機會!')

