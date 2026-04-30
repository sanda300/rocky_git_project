
food = ["김밥", "만두", "양념치킨", "족발", "피자", "쫄면", "라면"]


it_food = iter(food)
print(type(it_food))

for food in it_food:
    print(food)

print(next(it_food))    #STtopIteration

# 소스 코드 추가 버전

print(next(it_food))
