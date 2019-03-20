# # prompt user to input a number
# x = int(input('Enter a number: '))

# add try and except to help error handling
# try:
#     x = int(input('Enter a number: '))
# except:
#     print('That\'s not a valid number!')

# # keep running until a proper input in recieved 
# while True:
#     try:
#         x = int(input('Enter a number: '))
#         break
#     except:
#         print('That\'s not a valid number!')

# print everytime input is attempted
# while True:
#     try:
#         x = int(input('Enter a number: '))
#         break
#     except:
#         print('That\'s not a valid number!')
#     print('\nAttempted Input\n')

# # print everytime input is attempted fixed
# while True:
#     try:
#         x = int(input('Enter a number: '))
#         break
#     except:
#         print('That\'s not a valid number!')
#     finally:
#         print('\nAttempted Input\n')

# # example of else and finally 
# q = 0
# while q < 2:
#     try:
#         x = int(input('Enter a number: '))     
#     except Exception as e:
#         print('That\'s not a valid number!')
#         print('An error occured: ', e)
#     else:
#         print('Number is Valid')
#     finally:
#         print('\nAttempted Input\n')
#     q +=1