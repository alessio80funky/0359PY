class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def result(self):
        print(f"{self.name}さんは{self.score}点です。")



studentA = Student("佐藤",80)
studentB = Student("橋本",60)
studentC = Student("鈴木",75)

#print(studentA.name, studentB.name, studentC.name)
#print(studentA.score, studentB.score, studentC.score)

studentA.result()
studentB.result()
studentC.result()