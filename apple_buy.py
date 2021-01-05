#初期条件
money = 1000
apple_price = 200

print('りんごは1個200円です。')
print('現在の所持金は1000円です。')

#個数入力
input_count = input('購入するリンゴの個数を入力して下さい: ')
count = int(input_count)

#計算
total_price = apple_price * count
r_money = money - total_price

#条件設定
if money > total_price :
    print('購入しました。残金は' + str(r_money) + '円です。')

elif money == total_price :
    print('購入しました。残金がありません。')

else :
    print('残金がありません。チャージしてください。')
