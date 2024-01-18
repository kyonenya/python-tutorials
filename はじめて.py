import random # 7. 乱数モジュール

# 8. while
answer2 = random.randint(1, 10)
count = 0 # 何回推測したか

while True: # 追加。Trueは大文字なんだね
    print("あなたの推測は? ", end="")
    guess2 = int(input())
    # 9. 正解までの回数を表示する
    count += 1 # count = count + 1

    if answer2 == guess2:
        print("当たり! あなたは%i回で正解しました" %count)
        break # 追加。ループを抜ける条件
    elif answer2 > guess2:
        print("もっと大きい!")
    else:
        print("もっと小さい!")

# 6-7. if文
# answer = 6
answer = random.randint(1, 10)

print("あなたの推測は? ", end="")
guess = int(input())

# if/elif/else のあとにコロン:
if answer == guess: # 比較は ==, 代入は =
    print("当たり！")
elif answer > guess: # elseif じゃないんだね
    print("もっと大きい！")
else:
    print("もっと小さい！")

print("答え：%i" %answer) # 数字を埋め込むときは %i

# 5. 数値の入力を受け取る
print("Your number? ", end="")
num = int(input()) # inputが受け取れるのは数値だけ、なので数値型にキャストする
print(num + 3)

# 4. ユーザーからの入力を受け取る
print("Your name? ", end="") # 末尾にデフォルトでは改行が入ってしまうのでunset
name2 = input()
print("Hello %s" %name2)

# 3. 変数
name = "kyonenya" # var とかないんだね
# 埋め込みたい変数を%s そのあと半角スペースを空けて%変数名
print("Hello %s!" %name) # %s は文字列の場合

# 2. 文字列の表示とコメント
# print("Hello kyonenya!")
# コメント行は # で

