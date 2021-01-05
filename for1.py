#初期条件
money = 1000
apple_price = 200

#個数リスト
counts = [0,1,2,3,4,5,6]

#計算 & 繰り返し条件設定
for count in counts :

    total_price = apple_price * count
    r_money = money - total_price

    if money > total_price :
        print(str(count) + '個購入しました。残金は' + str(r_money) + '円です。')

    elif money == total_price :
        print(str(count) + '個購入しました。残金がありません。')

    else :
        print(str(count) + '個購入しようとしましたが、残金がありません。チャージしてください。')
