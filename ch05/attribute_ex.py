class Tag:
  # class attribute: 모든 instance에서 공유
  species = "Human"

  def setNameAge(self, n, a):
    # instance attribute: 각 instance마다 독립적
    self.name = n
    self.age = a

p1 = Tag()
p2 = Tag()
p3 = Tag()
p1.setNameAge("엘사", 30)
p2.setNameAge("모아나", 20)
p3.setNameAge("라푼젤", 25)

print(p1.species)  # "Human" (class attribute)
print(p2.species)  # "Human" (class attribute)
print(p3.species)  # "Human" (class attribute)

print(p1.name, p1.age)  # "엘사 30" (instance attribute)
print(p2.name, p2.age)  # "모아나 20" (instance attribute)
print(p3.name, p3.age)  # "라푼젤 25" (instance attribute)

