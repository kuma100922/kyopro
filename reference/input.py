# コンソールから取得する標準出力方式のリファレンス

s = input()  # 標準入力から文字列を受け取る
a, b = map(int, s.split('x'))  # 文字列を'x'で分割し、int型に変換してaとbに代入

print(a * b)  # aとbを掛け算して結果を出力