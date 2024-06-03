class Tag:
  # class method: 모든 instance에서 공유되는 attribute 정의
  @classmethod
  def species(cls):
    return "Human"

  def __init__(self, n, a):
    # instance attribute: 각 instance마다 독립적
    self.name = n
    self.age = a

  # instance method: instance마다 고유한 정보 출력
  def introduce(self):
    print(f"Hello, my name is {self.name}\nMy age is {self.age}")

# class method 호출
print(Tag.species())  # Human

# instance 생성 및 method 호출
p1 = Tag("엘사", 30)
p2 = Tag("모아나", 20)
p3 = Tag("라푼젤", 25)
p1.introduce()  # Hello, my name is 엘사
                # My age is 30
p2.introduce()  # Hello, my name is 모아나
                # My age is 20
p3.introduce()  # Hello, my name is 라푼젤
                # My age is 25
