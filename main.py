# 1-misol
roy = [1, 2, 3, 4, 5, 6, 7, 8]
print(roy)

res = list(filter(lambda x: x % 2 == 0, roy))
print(res)

# 2-misol
roy = [10, 15, 20, 25, 30]
print(roy)

res = list(filter(lambda x: x % 2 != 0, roy))
print(res)

# 3-misol
roy = [-5, 3, -2, 7, -1, 0, 9]
print(roy)

res = list(filter(lambda x: x > 0, roy))
print(res)

# 4-misol
roy = [4, -3, 0, -7, 8, -1]
print(roy)

res = list(filter(lambda x: x < 0, roy))
print(res)

# 5-misol:
roy = [-2, 0, 5, 8, -1]
print(roy)

res = list(filter(lambda x: x > 0, roy))
print(res)

# 6-misol
roy = [1, 6, 3, 8, 2, 10]
print(roy)

res = list(filter(lambda x: x > 5, roy))
print(res)

# 7-misol
roy =  [12, 5, 7, 20, 3, 15]
print(roy)

res = list(filter(lambda x: x < 10, roy))
print(res)

# 8-misol
roy = [3, 5, 9, 10, 12, 14]
print(roy)

res = list(filter(lambda x: x % 3 == 0, roy))
print(res)

# 9-misol
roy = [6, 8, 12, 15, 18, 20]
print(roy)

res = list(filter(lambda x: x % 2 == 0 and x % 3 == 0, roy))
print(res)


# 10-misol
roy = [0, 1, 2, 0, 3, 0, 4]
print(roy)

res = list(filter(lambda x: x != 0, roy))
print(res)


# 11-misol
roy = [-2, -1, 0, 2, 4, 5, 7]
print(roy)

res = list(filter(lambda x: x % 2 == 0 and x > 0, roy))
print(res)

# 12-misol
roy = [-5, -4, -3, -2, -1, 0]
print(roy)

res = list(filter(lambda x: x % 2 != 0 and x < 0, roy))
print(res)


# 13-misol
roy = [-5, 1, 5, 10, 15, 20]
print(roy)

res = list(filter(lambda x:1 <= x <= 10, roy))
print(res)

# 14-misol
roy = [2, 5, 8, 10]
print(roy)

res = list(filter(lambda x: (x ** 2) < 50, roy))
print((res))

# 15-misol
roy = [15, 23, 35, 42, 55]
print(roy)

res = list(filter(lambda x: x % 10 == 5, roy))
print(res)

# 16-misol
roy = ["apple", "banana", "kiwi", "strawberry"]
print(roy)

res = list(filter(lambda x: len(x) > 5, roy))
print(res)

# 17-misol
roy = ["apple", "pear", "grape", "plum"]
print(roy)

res = list(filter(lambda x: "a" in x, roy))
print(res)

# 18-misol
roy = ["Ali", "vali", "Sardor", "john"]
print(roy)

res = list(filter(lambda x: x[0].isupper(), roy))
print(res)


# 19-misol
roy = ["123", "abc", "456", "78a"]
print(roy)

res = list(filter(lambda x: x.isdigit(), roy))
print(res)

# 20-misol
roy = ["", "hello", "", "world"]
print(roy)

res = list(filter(lambda x: x != "", roy))
print(res)

# 21-misol
roy = ["hi", "hello", "world", "python"]
print(roy)

res = list(filter(lambda x: len(x) % 2 == 0, roy))
print(res)

# 22-misol
roy = ["java", "python", "javascript", "c++"]
print(roy)

res = list(filter(lambda x: len(x) > len("python"),  roy))
print(res)

# 23-misol
roy = ["python", "java", "kotlin", "go"]
print(roy)

res = list(filter(lambda x: x.endswith("n"), roy))
print(res)

# 25-misol
roy = ["abc", "123", "hello1", "world"]
print(roy)

res = list(filter(lambda x: x.isalpha(), roy))
print(res)
