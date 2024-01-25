# 12. @staticmethod：関数をまとめておくだけのクラス

def to_h1(str):
    return f"<h1>{str}</h1>"
def to_p(str):
    return f"<p>{str}</p>"

class HTMLHelper:
    @staticmethod
    def to_h1(str): # インスタンス化しないので self が要らない
        return f"<h1>{str}</h1>"
    @staticmethod
    def to_p(str):
        return f"<p>{str}</p>"    

HTMLHelper.to_h1("はじめに")
# -> <h1>はじめに</h1>

# 9. @classmethod：インスタンスではなくクラスに紐づく変数とメソッド
class Tweet:
    # クラス定義の直下に変数を作ればクラスに紐づいた属性になる
    _count = 0

    def __init__(self, text):
        # インスタンスに紐づくメソッド内でクラスに紐づく属性を呼び出すときはクラス名を付けて呼び出す必要がある
        self._text = text
        Tweet._count += 1

    @classmethod # クラスに紐づくメソッド
    def show_count(cls): # class だと予約語で被るので
        return cls._count

for i in range(5):
    Tweet(i)

Tweet.show_count()
# -> 5

# 5–8. 属性は直接アクセスせずにメソッドを介してアクセスしよう
class Post:

    def __init__(self, text):
        # 6. プライベートな属性には慣習上 _ をつけておく(カプセル化)
        self._text = text
        self._likes = 0 # いいねの初期値は0にする

    def show(self):
        print(f"{self._text} - {self._likes}いいね")

    # 5. メソッドを介して属性を書き換える
    def like(self):
        self._likes += 1

    # 8. @property：getter の簡単な記法
    @property
    def likes(self):
        return self._likes # post.likes でアクセスできるようになる
    # 8. @{propertyName}.setter：setter の簡単な記法
    @likes.setter
    def likes(self, num):
        self._likes = num # # post.likes = 123 で書き換えできるようになる

    # 7. setter, getter
    def set_likes(self, num):
        self._likes = num
    def get_likes(self):
        return self._likes

# 10–11. 継承
class AdPost(Post): # これだけで継承完了、子クラスができる
    # pass # 何も書かないと文法エラーになるので
    
    # 11. メソッドのオーバーライド：メソッドを同名で再定義して独自機能を実装する
    def __init__(self, text, sponsor):
        self._sponsor = sponsor
        # あとは同じ
        # self._text = text
        # self._likes = 0
        super().__init__(text) # super() で親クラスのインスタンスを参照できる
    def show(self):
        super().show()
        print(f"--- sponsored by {self._sponsor} ---")

posts = [
    Post("こんにちは"),
    Post("いい天気ですね"),
    AdPost("おい 聞いてるか", "コカコーラ")
]

# メソッドを介した属性の書き換え (5–6.)
# posts[0].likes += 1 # 属性を直接書き換えるな!
posts[0].like()

# setter, getter (7.)
posts[1].set_likes(100)
posts[1].get_likes()
# -> 100

# @property (8.)
posts[2].likes = 1000
posts[2].likes
# -> 1000

# 継承 (10.)
posts[2].show()

for post in posts:
    post.show()

# 2–4. クラスのリテラル表現
class Entry:
    # 3. コンストラクタ
    # __init__(self, 引数1, 引数2, ...)：コンストラクタ
    def __init__(self, text, likes):
        self.text = text # self で自身のインスタンスを指す
        self.likes = likes

    # 4. メソッド：同じく self を引数にとる
    def show(self):
        print(f"{self.text} - {self.likes}いいね")

entries = [
    Entry("こんにちは", 9), # インスタンスを生成：JS と違って new しない
    Entry("いい天気ですね", 2)
]

entries[0].text # -> 'こんにちは'
entries[1].likes # -> 2
entries[1].show() # 'いい天気ですね - 2いいね'

# 1. クラス：データ型を自作すること
# Pythonには型がないのでオブジェクトに型をつけるにはクラスに頼るしかない

# 定義：class Post:
# インスタンス化：post = Post()
# 属性：post.text= "Hello"
# メソッド：post.show()

