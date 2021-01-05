#指定した数までの自然数から任意の倍数を取り除く

#%%
#要素の追加
n = 2
n_s = [1,2]

N = input('調べたい自然数の上限を入力してください。:')
N = int(N)

while n <= N :
    n = n + 1
    n_s.append(n)
    if n == N :
        break
#%%

#倍数を取り除く
a = input('取り除く倍数を入力してください。:')
a = int(a)

for m in n_s :
    if m % a == 0 :
        continue
    print(m)
