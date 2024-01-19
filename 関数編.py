# 10. 関数のスコープ：スコープがインデントで一目瞭然なの Python のいいところね
def get_taxed_price(raw):
    result = raw * 1.1
    return result
    # result はインデント内でスコープが閉じているローカル変数

# print(result) # -> NameError: name 'result' is not defined
result = 110 # グローバル変数

# 9. 関数で処理をまとめる
def show_content(content):
    print(f"{content}\n-----")
def show_ad():
    print(f"全品50%オフ！\n-----")

show_ad()
show_content("初めてのツイートです")
show_ad()

# 8. 早期リターン
def print_username(name):
#    if name != "admin" and name != "root":
#        print(name)
    if name == "admin" or name == "root":
        return
    print(name)

print_username("隆史") # -> 隆史
print_username("root") # -> (None)

# 7. 引数にデフォルト値を設定する
def show_time(h, m, s=0): # 秒は指定しなくてもいい、指定されなければ0を代入
    print(f"{h:02}:{m:02}:{s:02}") # :02：満たない場合は0を2桁埋める

show_time(6, 28, 40) # -> 06:28:40
show_time(6, 28) # 06:28:00
# デフォルト値を設定するということは引数を省略可能にするということでもある
# 第2引数を省略可能にした後に第3引数は必須にする、みたいなことはできない

# 6. キーワード引数：オブジェクト引数みたいに引数に名前をつけて呼べる
def greet_with_name(name, by):
    print(f"こんにちは{name}さん、と{by}さんが言ってました")

greet_with_name("太郎", "二郎") # 位置引数：どっちがどっちか判りづらい
greet_with_name(by="二郎", name="太郎") # キーワード引数：順番を入れ替えてもいい

# 4. 何も返さない関数：JS でいう void 関数的な
def print_sum(a, b):
    print(a + b)
    # return None

print_sum(100, 200)

# 5. 何も返さない関数は内部的にはNoneを返している
print(print_sum(100, 200)) # -> None

# 3. 処理の順序
# 関数定義しただけでは何も実行されない
# 関数は呼び出されて初めて、実引数が仮引数に渡されて返り値として呼び出し元に返る

# 2. 関数定義
# def 丸括弧仮引数 コロン
def double(n): # 関数名には a-z A-Z 0-9 _ のみが使える
    return n * 2

print(double(10)) # -> 20

# 1. 組み込み関数とユーザー定義関数
#    実引数      戻り値
len("Hello") # -> 5
max(3, 6, 5) # -> 6
min(5, 2, 7) # -> 2
