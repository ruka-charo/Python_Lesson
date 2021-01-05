#規則的な計算

#規則設定
X = input('好きな数を入れてください。:')
x = int(X)

while x >=5 :

    if x % 2 == 0 :
        x = x - 1

    elif x % 3 == 0 :
        x = x - 2

    elif x % 5 == 0 :
        x = x - 2

    elif x % 5 == 2 :
        x = x - 4

    else :
        x = x - 3

    print(x)
