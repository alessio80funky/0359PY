#データ型

#基本型：str（ストリング型）/int（数値型）/float（少数数値型）/bool（ブリアン）

name = "山田" #str（ストリング型
age = 21 #int（数値型）
height = 170.5 #float（少数数値型）
is_student = True #bool（ブリアン）=> (javascript => 小文字になります　=> true)

print(type(name)) #<class 'str'>
print(type(age)) #<class 'int'>
print(type(height)) #<class 'float'>
print(type(is_student)) #<class 'bool'>


#注意点：

age = 20

print(age + 5)#25

name = "alessio"

print( "hello " + name)

#エラー：　ストリング型と数値型が同時に使えない

#print( "hello " + 5)

 # File "C:\Users\kazuo\OneDrive\デスクトップ\python-3\data.py", line 26, in <module>
  
  #  print( "hello " + 5)
   #        ~~~~~~~~~^~~
#TypeError: can only concatenate str (not "int") to str >>テンプレート文字列使ったほうが安全



#参照型： list(配列)/tuple(固定配列）/dict（オブジェクト）

