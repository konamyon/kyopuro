# 複数の整数の入力を一つの変数ずつ受け取る
n,m = map(int,input().split())
print(n,m)

# 複数の整数の入力をリストで受け取る
a = list(map(int,input().split()))
print(a)

# 辞書
from collections import defaultdict
d = defaultdict(int) # 辞書の値に初めからゼロが入っている
d = {}
d["name"] = "こな" # 辞書名["キー"]　= 値
d["age"] = 21
print(d) # {'name': 'こな', 'age': 21}
print(d["age"]) # 21
sorted_d_values = dict(sorted(d.items(), key=lambda x: x[1], reverse=True)) # 辞書の値によって降順ソート
sorted_d_desc_keys = dict(sorted(d.items(), key=lambda x: x[0], reverse=True)) # 辞書のキーによって降順ソート


# 配列の中身を空白区切りで出力
a = []
print(" ".join(map(str, a)))

# 空白無しの縦n横任意のグリッドを二次元配列で受け取る
a = []
for i in range(n):
    a.append(list(input())) # 空白区切りで与えられてる場合は input().split()

# 空の二次元配列を作成
b = [['' for _ in range(n)] for _ in range(n)]

# 二次元配列のグリッドを90°回転する関数
def roted(a):
    b = [['' for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            b[j][n-i-1] = a[i][j]
    return b

# 整数iの各桁の総和
s = sum(list(map(int,str(i))))

#nの各桁の総和を求める関数
def calc_sum_digit(n):
    sum_digit = 0
    while n > 0:
        sum_digit += n%10
        n //= 10
    return sum_digit

# 数字が格納された配列を与えるとその配列のi番目の数字が何番目に大きいか順位付けしてくれる関数
def rank(a):
    rank = []
    for i in range(n):
        r = 1
        for j in range(n):
            if a[i] < a[j]:
                r += 1
        rank.append(r)
    return rank

# 数字を格納する配列(何個でもいい)を与えるとフルハウスかどうか判定してくれる関数
def fullhouse(a):
    d = {}
    count2 = 0
    count3 = 0
    for i in range(len(a)):
        d[a[i]] = 0
    for i in range(len(a)):
        d[a[i]] += 1
    set_a = set(a)
    for i in set_a:
        if d[i] >= 2:
            count2 += 1
        if d[i] >= 3:
            count3 += 1
    if count2 >= 2 and count3 >=1:
        print("Yes")
    else:
        print("No")

# グリッドsの中にあるグリッドｔと同じパターンを探し、s中のtパターンの左上の座標を表示
def gridSerch(s,t):
    n = len(s)
    m = len(t)
    for a in range(n-m+1):
        for b in range(n-m+1):
            f = True
            for i in range(m):
                for j in range(m):
                    if s[a+i][b+j] != t[i][j]:
                        f = False
            if f:
                print(a+1,b+1)

# 文字列またはリストaの中に"00"が何個含まれているか
a.count("00") 

# sの文字列をn回先にずらすシーザー暗号
s = "ABC"
n = 2
ans = []
for i in s:
    shift = (ord(i) - ord("A") + n) % 26
    ans.append(chr(ord("A")+shift))
print("".join(ans))

# 累積和
a = [1,2,3,4,5]
ruiseki = [0]*len(a)
for i in range(len(a)):
    ruiseki[i] = ruiseki[i-1] + a[i]
print(ruiseki)

# aabccを(a,2)(b,1)(c,2)みたいに表す（連超圧縮）
n = 5
s = "aabcc"
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    print(s[i],j-i)
    i = j
    
# 大文字小文字判定
s = "a"
if s.isupper():
    print("大文字")
if s.islower():
    print("小文字")

# i番目の辺を結ぶ頂点のペアがi行目に与えられるタイプのグラフの受け取り方
g = [[] for i in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)
print(g)


# 深さ優先探索（ABC138-D）
from collections import deque
n,q = map(int,input().split())
g = [[] for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
print(g)

que = deque()

visited = [False]*(n+1)

counter = [0]*(n+1)

for i in range(q):
    p,x = map(int,input().split())
    counter[p] += x
    
print(counter)

que.append(1)

visited[1] = True

while len(que) > 0:
    now = que.popleft()
    now_number = counter[now]
    for i in g[now]:
        if visited[i] == False:
            counter[i] += now_number
            visited[i] = True
            que.append(i)
print(*counter[1:])