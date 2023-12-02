
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

