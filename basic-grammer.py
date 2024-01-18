# 29. try...except 文：JS と違って try...catch ではないらしい

try:
    initial_cash = int(input("最初の残高は?"))
except ValueError: # except のあとに例外（実行時エラー）の型を指定する
    print("入力が間違っているので終了します")
    # exit() # プログラムを強制終了する

# 28. 実行時エラー、すなわち例外

# ■ NameError：変数名タイポ
# -> NameError: name 'comman' is not defined. Did you mean: 'command' ?

# ■ TypeError：キャストし忘れ

# initial_cash = input("最初の残高は?") # int() キャストを忘れてる
# RATE = 1.1
# print(f"合計金額は {initial_cash * RATE:.0f} 円です")

# -> TypeError: can't multiply sequence by non-int of type 'float'
# sequence；文字列型のこと

# ■ ValueError：キャストできない入力を受け取ったとき

# initial_cash = int(input("最初の残高は?"))
# "Hello" と入力
# -> ValueError: invalid literal for int() with base 10: 'Hello'

# 27. コンパイルエラー：構文エラーと字下げエラー

# ■ SyntaxError：コロン書き忘れ、括弧閉じ忘れ、予約語スペルミスなど

#     match command
#                  ^
# SyntaxError: expected ':'

# ■ IndentationError：if, for, while などの後に字下げがないとき

#     print(f"Hello {}回目")
#     ^^^^^
# IndentationError: expected an indented block after 'for' statement on line 66

# 26. 真偽値 True False：JS と違って大文字なんだね

# False: 0 '' None など JS で言う falsy な値
# True: それ以外すべて。つまり `while 1 + 3` とかでも無限ループになる

# 24. while True で無限ループ
# 25. break でループ抜け、continue で途中抜けで次のループへ
command = None # JS の undefined で初期化

while 1 == 1:
    command = int(input("1, 2のどれかを入力、0で終了"))
    match command:
        case 0:
            # pass # 何もしない
            print("終了します")
            break # ループを抜ける
        case 1:
            print("画面1")
        case 2:
            print("画面2")
        case _: # どれにも当てはまらない場合は _ アンダースコア
            print("不正なコマンドです。再度入力してください")
            continue # それ以降の処理↓を実行せずに次のループへ
    print("メニューが表示されました")

# 23. while ループ
# for ループと違って回数が決まっていない場合に使う

command = int(input("1, 2のどれかを入力してください。0で終了します"))
while command != 0:
    match command:
        case 1:
            print("メニュー1")
        case 2:
            print("メニュー2")
    command = int(input("1, 2のどれかを入力してください。0で終了します"))
    
# 22. for の入れ子の for
initial_money = int(input("最初の残高は？"))
RATE = 1.1

# for year in range(3):
#     print(f"{year}年目：{initial_money * RATE ** year:,.2f}円")
# initial_money += 10_000
# for year in range(3):
#     print(f"{year}年目：{initial_money * RATE ** year:,.2f}円")
# initial_money += 10_000
# for year in range(3):
#     print(f"{year}年目：{initial_money * RATE ** year:,.2f}円")

for i in range(3):
    # 初回以降に残高追加する
    if i != 0:
        initial_money += 10_000
    for year in range(3):
        print(f"{year}年目:{initial_money * RATE ** year:,.2f}円")

# 20. for ループ
for i in range(3): # 0,1,2
    print(f"Hello {i}回目")
# range()
range(3, 9) # 3から9に満たない数(8)まで -> 345678
range(3, 9, 2) # 3から2刻みで -> 3579
range(8, 5, -1) # 逆順で -> 8765

# 21.
initial_cash = int(input("最初の残高は?"))
RATE = 1.1
for year in range(5):
    print(f"{year}年目:{initial_cash * RATE ** year:,.0f}円") # RATEのi乗、0年目は1

# 19. match の分岐条件に比較演算子を用いるとき
initial_cash = int(input("最初の残高は?"))

match initial_cash:
    # case >= 100_000 # これは文法エラー
    case n if n >= 100_000: # いったんinitial_cash を適当な変数で受けておいてから if で条件を付け足す
        RATE = 1.1
    case n if n >= 10_000:
        RATE = 1.05
    case _:
        RATE = 1.01
print(f"税率は {RATE:.2f} で、合計金額は {initial_cash * RATE:.0f} 円です！")

# 18. 三項演算子：値1 if ... else 値2
score = int(input("点数は？"))
print("合格！" if score >= 90 else "再テスト！")

# 17. match による条件分岐（スイッチ文）
signal = input("信号の色は？")

match signal:
    case "赤":
        print("止まれ！")
    case "黄":
        print("減速せよ。")
    case "青" | "緑": # | でor条件を表す
        print("行け！")
    case _: # アンダーバーで default ケース
        print("それは信号ではないよ。")

# 15. 論理演算子：and, or, not
eng_score = int(input("英語の点数は？"))
math_score = int(input("数学の点数は？"))

# and, or, not：JSと違って英語で書くんだね
if eng_score >= 90 and math_score >= 90:
    print("合格！")
# 16 elif で条件分岐を追加
elif not(eng_score <= 45) and not(math_score <= 45):
    print("及第点。")
else:
    print("落第！")

# 13. if による条件分岐
# 14. if else による条件分岐
score = int(input("テストは何点でしたか？"))
if score > 80: # コロンが必要
    print("合格！")
    print("よくできました！") # インデント中はずっと条件文と見なされる
else:
    print("失格！")
    print("次また頑張りや")
print("プログラム終了")
# 比較演算子 > >= < <= == !=

# 12. f文字列内の埋め込み変数のオプション
initial_cash = int(input("最初の残高は？"))
RATE = 1.1
# : の後に ,   で3桁ごとカンマ区切り
# : の後に .2f で小数点以下2桁まで表示
print(f"0年目：{initial_cash:,.2f} 円")
print(f"1年目:{initial_cash * RATE:,.2f} 円")
print(f"2年目:{initial_cash * RATE * RATE:,.2f} 円")

# 11. ユーザーからの入力を受け取る
num = input("数値を入力してください：")

# input された値は文字列型になる
print(num * 2) # "2424"
print(type(num)) # -> <class 'str'>

# 数字にキャストしてあげてから計算する
print(int(num) * 2) # 整数
print(float(num) * 2) # 小数

# 10. 文字列を埋め込む
age = 82
name = "kyonenya"
# str():数値はそのままだと文字列に埋め込めないので文字列にキャストする
print("私は" + str(age) + "歳です")
# print("私は" + age + "歳です") -> TypeError: can only concatenate str (not "int") to str

# {} と format()：値たちを自動で文字列にキャストして埋め込み
print("私は {} です。年齢は {} 歳です".format(name, age))
# f文字列：テンプレートリテラル。一番新しい書き方
print(f"私は {name} です。年齢は {age} 歳です") # 先頭に f と書いてからダブルクォート

# 9. 文字列の操作
# 連結：半角スペースでも区切れる（変数の場合は使えない）
print("Takashi" " " "Kyonenya")
print("Takashi" + " " +  "Kyonenya")
# 繰り返し *n
print("-" *16)

# 8. 文字列
print('It\'s a pen.\nI am kyonenya.') # バックスラッシュでエスケープ、改行は\n

# """ ダブルクォート三つで改行を直接反映できる（JSのテンプレートリテラルと同じ）
# """\ バックスラッシュで最初の行の改行を無視できる
print("""\
Your ID is:
kyonenya""")

# 7. 値の再代入
# 定数は慣習的に大文字にして目視で再代入を避けてもらう
RATE = 1.1
cash = 10000

# += -= *= 再代入演算子
cash += 5000 # cash = cash + 5000 と同じ
cash *= RATE
print(cash)

# 6. 変数の命名ルール
# a-z A-Z 0-9 _ のみしか使えない：- は使えない
    # initial-balance = 1 -> SyntaxError: cannot assign to expression here.
# 予約語は使えない：if else or and
# 大文字小文字は区別される（Case Sensitive）

# 変数を使わず値をベタ書きするのを「リテラル」という

# 5. 変数
initial_balance = 10000 # 最初の現金
rate = 1.1 # 利子率
print(initial_balance * rate * rate) # 2年後の残高

# 4. 数値の演算
print(10 ** 3) # ** べき乗 -> 1000
print(10 // 3) # // 割り算の商 -> 3
print(10 % 3) # % 割り算の余り -> 1

# 3. 数値
# e 10の何乗を掛ける
print(1.2e4)  # 1.2 に10の4乗を掛けたもの
print(1.2e-4) # 1.2 に10のマイナス4乗を掛けたもの

# _ アンダースコア 値に影響しない区切り文字
print(10_000_000)

# 1. 基礎文法編
# 基本データ型：数値、文字列
# 制御構造：順次処理、条件分岐、反復処理
# エラー処理：文法エラー、例外

