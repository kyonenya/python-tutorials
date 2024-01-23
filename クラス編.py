x = None

# 5. 


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
    Entry("こんにちは", 9), # インスタンスを生成
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

print(x)

