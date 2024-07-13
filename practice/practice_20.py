class Family:
    lastname = "김" # 클래스 변수

a = Family()
b = Family()
c = Family()

a.lastname = "박"

print(a.lastname)
print(b.lastname)
print(c.lastname)