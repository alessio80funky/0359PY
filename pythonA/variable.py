#変数

#letを使わない

message = "Python メッセージ"
age = 20

#print(message) <-コメントアウト
print(age)

print(f"{message}と{age}")


#変数に関しての注意：

#変数に使えない変数名

# 1 - 数字で始まる変数名　ー＞　123name = "message"
# 2 -  アンダースコアで始まる変数名　ー＞　_name = "message"
# 3 -  予約語　　下記となります：

#False,class,is,none,continue,try,True,def,else,elif,for,if,whileなど

#False = 12

print(False)

  #File "C:\Users\xxxx\OneDrive\デスクトップ\python-3\variable.py", line OO
    #False = 12
   # ^^^^^
#SyntaxError: cannot assign to False