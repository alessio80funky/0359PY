student = {
    "name":"佐藤",
    "age":20,
    "score":85
}

print(student["name"])#佐藤


car = {
    "brand":"Nissan",
    "model":"carola",
    "year":2004
}

print(car)#{'brand': 'Nissan', 'model': 'carola', 'year': 2004}

print(car["brand"])#Nissan
car.update({"brand":"Madza"})#置き換え専用のメソッド
print(car)#{'brand': 'Madza', 'model': 'carola', 'year': 2004}


# メソッド一覧：　https://qiita.com/FujiedaTaro/items/40d2dd907ccf24194f5f