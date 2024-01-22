x = None

# 17. 辞書
scores = {"math": 41, "english": 87, "physics": 61}

scores["math"] = 100 # 要素を上書き
scores["chemistry"] = 83 # 要素を追加
# scores = {'math': 100, 'english': 87, 'physics': 61, 'chemistry': 83}

del scores["english"] # del：要素を削除
popped_value = scores.pop("chemistry") # .pop()：削除した値を再利用したいなら
# -> 83
# scores = {'math': 100, 'physics': 61}

# 16. 文字列 split <-> join リスト

birthday = '1994-06-15'
birthday.split('-')
# -> ['1994', '06', '15']

date_parts = ['1994', '06', '15']
"-".join(date_parts) # .join() の順番キモっ！
# -> '1994-06-15'

date_parts = [1994, 6, 15]
"-".join(str(part) for part in date_parts) # 文字列にキャストしてから join

# 15. シーケンスとしての文字列
# シーケンス：連続した値。JSでいう配列のこと

# 文字列もそう、これもJSと同じ。もちろん破壊的変更はできない
name = "kyonenya"
name[:5]
# -> 'kyone'
len(name)
# -> 8

# 文字列用のメソッド (非破壊的)
name.replace("kyonen", "kotoshi")
# -> 'kotoshiya'
name.upper()
# -> 'KYONENYA'

# 14. タプルのアンパック：JS のスプレッド構文
age, country, _ = (29, "JPN", "male")

age, *rest = (29, "JPN", "male") # *hoge：JS のレスト構文
print(rest) # 残りをリストとして受け取る
# -> ['JPN', 'male']

# 13. タプル：後から変更できない配列
kyonenya = ("JPN", 29)
kyonenya = "JPN", 29 # () は省略できる

kyonenya[1] # インデックスアクセスもできる
# -> 29

# 中の要素を後から変更することはできない
# kyonenya[1] = 30
# -> TypeError: 'tuple' object does not support item assignment

# 　使える：in, len(), index(), count()
# 使えない：.append(), .insert(), .pop()

# タプルとリストの変換
list(kyonenya) # これで変更可能になるよ
# -> ['JPN', 29]
tuple(['JPN', 29])
# -> ('JPN', 29)

# 12. リスト内包表記に if 文を組み合わせる
prices = [10, 400, 30, 200]

# 最後に if を書き加える
taxed_prices = [price * 1.1 for price in prices if price > 100] # 100円以下は取り扱わず除外する
print(taxed_prices)

# 11. リスト内包表記：.map と同じようなもの
prices = [100, 300, 200]

# リストから新しいリストを作る
# 通常版
taxed_prices = []

for price in prices:
    taxed_prices.append(price * 1.1)

# ワンライナー版：要素を受けての処理 for 要素 in 配列：倒置法！
prices_with_tax = [price * 1.1 for price in prices]
# -> [110, 330, 220]

# 10. リストをループさせる
prices = [100, 300, 200]

for price in prices: # for 要素 in 配列／range
    print(price * 1.1)

# enumerate()：配列からインデックス付きで要素を取り出す関数
for index, price in enumerate(prices):
    print(f"{index}番目：{price * 1.1:.0f}円")

# 9. スライス記法で非破壊的変更
nums = [0, 1, 2, 3, 4, 5]
sliced_list = nums[2:5]

print(sliced_list) # -> [2, 3, 4]
print(nums) # -> [0, 1, 2, 3, 4, 5]：元配列に変更なし！

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums[2:8:2] # 2以上8未満までを2飛ばしで
# -> [2, 4, 6]
nums[8:2:-2] # 8以下2より大きいまでを後ろから2飛ばしで：後ろから指定
# -> [8, 6, 4]
nums[::-1] # 最初から最後まで後ろから1つづつ：.reverse() の非破壊版
# -> [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# 8. スライス記法で破壊的変更
nums = [0, 1, 2, 3, 4, 5]

nums[2:5] # インデックス2番目以降5番目未満
# -> [2, 3, 4]

nums[2:5] = [200, 300, 400]
# nums = [0, 1, 200, 300, 400, 5]

nums[2:2] = [1.5] # インデックス2番目から始まるところ、つまり2番目の手前に挿入
# nums = [0, 1, 1.5, 2...]

nums = [0, 1, 2, 3, 4, 5]

nums[:3] # nums[0:3]：インデックス0番目から3番目未満
# -> [0, 1, 2]

nums[2:] # nums[2:♾️]：インデックス2番目から最後まで
# -> [2, 3, 4, 5]

# 7. リストの要素の並べ替え
scores = [20, 10, 30]

scores.reverse()
# scores = [30, 10, 20] 

scores.sort() # 破壊的ソート
# scores = [10, 20, 30]

# scores.sort().reverse()
scores.sort(reverse=True) # 逆順ソート
# scores = [30, 20, 10]

# sorted()：非破壊的ソート。元データを変更せず関数の実行結果として返す
scores_sorted = sorted(scores, reverse=True)
# -> [30, 20, 10]

# 6. リストの集計
scores = [20, 40, 30, 20]

len(scores) # len()：長さを取得。リスト以外にも使えるのでメソッドではなく関数
# -> 3

min(scores) # -> 20
max(scores) # -> 40
sum(scores) # -> 110

scores.count(20) # .count()：特定の値が何回登場するか
# -> 2

scores.index(20) # .index()：特定の値が最初に登場するインデックス
# -> 0

35 in scores # in：特定の値が含まれているかどうか真偽値を返す
# -> False

# 5. 要素を削除するメソッドたち
scores = [10, 20, 40, 20]

scores.remove(20) # .remove()：最初の 20 だけが削除される
# scores = [10, 40, 20]

# 20 を全て削除したい場合 -> 後述

popped_score = scores.pop(0) # .pop()：指定したインデックスの要素を削除して返す
# -> 10

del scores[0] # del：pop() と同じ。ただし値を返さない

scores.clear() # .clear()：全削除
# scores = []

# 4. extend：複数要素追加, insert：間に挿入
scores = [60]

scores.extend([78, 71]) # .extend()：複数要素追加
scores = scores + [66, 98] # + で複数要素追加できる:JSと違う!
# -> [60, 78, 71, 66, 98]

scores = [10, 20] * 3 # * で3回繰り返すを表現できる：JSと違う！
# -> [10, 20, 10, 20, 10, 20]

scores = [10, 20]
scores.insert(1, 15) # 1番目(2つ目)の後に 15 を代入 
# scores = [10, 15, 20]

# 3. append：リストに要素を追加するメソッド
scores = [60, 78]
scores.append(71) # メソッド：値の後に直接 . を繋げて呼べる関数
# scores = [60, 78, 71]

# 2. リスト型：JS でいう配列
scores = [60, 78, 71]
sum(scores) # sum(リスト型) という組み込み関数
# -> 209

scores[2] # インデックス：リストの各要素にアクセス。JSと同じ
# -> 71

scores[1] = 100 # リストの要素に再代入
# scores = [60, 100, 71]

# 初期化された要素数以上の要素にはアクセスできない
# scores[100] = 100 # -> IndexError: list assignment index out of range

# 1. データ構造編でやること

# 数値
# 文字列
# 真偽値
# None

# リスト [1, 4, 3, 7]
# タプル ("JPY", 37, 140)
# 辞書 {"math": 82, "english": 70}
# 集合 {"Taro", "Jiro", "Saburo"}

print(x)

