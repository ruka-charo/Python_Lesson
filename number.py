#要素の追加(下限と上限を設定)

a = input('調べたい自然数の下限を入力してください。:')
a = int(a)

n = a
n_s = [n]

N = input('調べたい自然数の上限を入力してください。:')
N = int(N)

while n <= N :
    n = n + 1
    n_s.append(n)
    if n == N :
        break

print(n_s)
