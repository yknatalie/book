# print("Give me the two numbers and I'll sum them")
# print("Enter the 'q' to quit ")
# while True:
#     one = input("First number: ")
#     if one == 'q':
#         break
#     second = input("Second number: ")
#     if second == 'q':
#         break
#     try:
#         answer = int(one)/int(second)
#     except ValueError:
#         print('Only integers are possible!')
#     else:
#         print(answer)

# cats = 'cats.txt'
# dogs = 'dogs.txt'
# try:
#     with open(dogs, encoding='utf-8') as f:
#         f = f.read()
# except FileNotFoundError:
#     pass
# else:
#     print(f)

file_path = 'C:\\Users\\Admin\\Desktop\\Tom_3.txt'
with open(file_path) as f:
    f = f.read()
    print(f.lower().count('the '))
