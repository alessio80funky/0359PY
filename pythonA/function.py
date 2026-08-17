#関数

def say_Hello():
    print("こんにちは！")
    print("Pythonは楽しい")
#関数を呼び出す    
say_Hello()


def add(a,b):
    return a + b

result = add(10,5)

print(result)

######################################

#変数代入する場合

def greet(name):
    return f"{name}さん、こんにちは！"


name = greet("田中")#固定データ

name = greet("田中")


print(name)

#######################################

#直接関数を実行する場合

def greet(name):
    return f"{name}さん、こんにちは！"

print(greet("田中"))#固定データ

print(greet("田中"))


