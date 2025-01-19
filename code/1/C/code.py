#AtcoderC問題→回答としては正しそうだが、実行速度が遅いためC++で書き直し
q = int(input()) #クエリ数
list = [] #各蛇の長さを保持する配列(配列数q)
head = 0 #l-1 番目の蛇の頭の座標

for i in range(q):
    query = input()
    # 標準入力に空白を含む場合
    if " " in query :
        k,l = map(int, query.split())
    # 標準入力に空白を含まない場合
    else :
        k = int(query)
    if k == 1:
        #蛇の値を保持
        list.append(l)
    elif k == 2:
        #先頭の蛇は離脱
        del list[0]
    elif k == 3:
        #l番目の蛇の頭の座標を出力する
        for j in range(l-1):
            head += list[j]
        print(head)
        head = 0 #表示のたびに初期化が必要