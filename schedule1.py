#曜日入力
day = input('今日の曜日を入力してください :')

#スケジュール入力
if day == '月曜日' or day == '金曜日' :
    print(day + 'は特に予定はありません。')

elif day == '火曜日' or day == '水曜日' or day == '木曜日' :
    print(day + 'は予定が入っています。')
    
else :
    print('本日は' + day + 'です。ゆっくり休みましょう！')
