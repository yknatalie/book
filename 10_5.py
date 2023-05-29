# name = input("What is your name? ")
# file_path = 'C:/Users/Admin/Desktop/guest.txt'

# with open('guest290.txt', 'w') as file_object:
#     file_object.write(name)

i = 4
# while True:
#     name = input("What is your name? ")
#     print(f'Hello, {name}!')
#     with open('greetings.txt', 'a') as file_object:
#         file_object.write(f'Hello {name}!\n')
#     i -= 1
#     if i == 0:
#         break
while i > 0:
    with open('answer.txt', 'a') as file_object:
        answer = input('Why do love programming? ')
        file_object.write(f'{answer}\n')
    i -= 1
