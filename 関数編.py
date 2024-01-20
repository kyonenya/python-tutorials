# 17. 関数式 lambda：JS のアロー関数の醜い形
def calc(n, func):
    return func(n) # 引数として渡された関数のスイッチをポチッ()と押せる

# lambda 引数: 返り値
print(calc(10, lambda n: n * 2))

# 16. 関数を引数として渡す
def calc(n, func):
    return func(n) # 引数として渡された関数のスイッチをポチッ()と押せる

def double(n):
    return n * 2

print(calc(10, double)) # 関数を引数として渡す
# 引数として渡すときその場でに関数定義もしてしまうにはどうするのだろう→無名関数

# 15. 関数を丸括弧なしで使うと関数そのものが渡せる(当然だろ)
def triple(n):
    return n * 3

print(triple(10))

sanbai = triple # 関数を丸ごとコピー
print(sanbai(10)) # -> 30

# 14. globalキーワードは使うな、引数で渡せ
def get_price(a, b, rate):
    if a + b >= 3000:
        rate = 1.2
    return (a + b) * rate

rate = 1.1
# グローバル変数は呼び出すときに引数として渡そうね
# (当たり前だろ。全部 let しかない世界なんだからやむを得ないだろ)
get_price(3000, 7000, rate)
get_price(300, 700, rate)

# 13. (非推奨) globalキーワードで関数内でグローバル変数を明示的に参照
def get_summed_price(a, b):
    global rate # else の場合はグローバル変数のほうが参照される
    if a + b >= 3000:
        rate = 1.2
    return (a + b) * rate

rate = 1.1

print(get_summed_price(3000, 7000)) # -> 1.2
print(get_summed_price(300, 700)) # -> 1.1

# 関数内でグローバル変数である rate に代入したので値が変わってしまう
print(rate) # -> 1.2

# 12. ローカル変数になる条件
def get_summed_price2(a, b):
    # if 文の片方の条件でしか rate は定義されていないので、もう片方の条件では rate は未定義扱いになる
    # Python では関数内に変数定義があれば、条件分岐内でしか初期化されなかろうが問答無用でローカル変数扱いになる
    if a + b >= 3000:
        rate = 1.2
    return (a + b) * rate

# get_summed_price2(1000, 500) # -> UnboundLocalError: local variable 'rate' referenced before assignment

# 11. 関数内に定義されていない変数は関数の外を探しに行く
def get_taxed_price(raw):
    result = raw * rate # 値が代入されていないのでスコープの外を探しに行く
    return result

rate = 1.1 # は？ 関数定義より下に書いてある変数が関数から参照されるのヤバすぎだろ
print(get_taxed_price(100)) # -> 110

# 10. 関数のスコープ：スコープがインデントで一目瞭然なの Python のいいところね
def get_taxed_price2(raw):
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

