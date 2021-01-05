#曜日
days = ['月曜日','火曜日','水曜日','木曜日','金曜日','土曜日','日曜日']

#スケジュール入力
for day in days :

    if day == '月曜日' or day == '金曜日' :
        print(day + 'は特に予定はありません。')

    elif day == '火曜日' or day == '水曜日' or day == '木曜日' :
        print(day + 'は予定が入っています。')

    else :
        print('本日は' + day + 'です。ゆっくり休みましょう！')
