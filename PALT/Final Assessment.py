# 1: guessing a secret number
# import random
#
# ans = random.randint(0, 10)
# max_attempt = 3
# print('Guess a number in the range of 0 to 10')
#
# while max_attempt > 0:
#     guess = int(input(f'Attempt left ({max_attempt}) : '))
#
#     # Conditions
#     if 0 > guess or 11 <= guess:
#         print(f"You're kidding, right?")
#     elif guess < ans:
#         print(f'The number is greater than your guess, {guess}.')
#     elif guess > ans:
#         print(f'The number is smaller than your guess, {guess}.')
#     elif guess is ans:
#         print(f'\nCongratulation! Your guess is a right number!')
#         break
#
#     # Decrement attempt
#     max_attempt -= 1
#
#     # output after attempt reach 0
#     if max_attempt == 0:
#         print('\nyou lost the game')


# 2:class: Time
# import time
#
#
# class Time:
#     def __init__(self, sec):
#         self.sec = sec
#
#     def convert_to_minutes(self):
#         minutes, self.sec = divmod(self.sec, 60)
#         return "%d:%d" % (minutes, self.sec)
#
#     def convert_to_hours(self):
#         #  sec convert to HHMMSS
#         hhmmss = time.gmtime(self.sec)
#         str_hhmmss = f'{hhmmss.tm_hour}:{hhmmss.tm_min}:{hhmmss.tm_sec}'
#         return str_hhmmss
#
#
# # sample
# tr = 3680
#
# # object for convert to minutes
# obj_minute = Time(tr)
# print(obj_minute.convert_to_minutes())
#
# # object for convert to hours
# obj_hour = Time(tr)
# print(obj_hour.convert_to_hours())


# 3:
# with open('myLine.txt', 'w') as fw:
#     fw.write("""This is the 1st Line
# This is the 2nd Line
# This is the 3rd Line
# This is the 4th Line
# This is the 5th Line
# This is the 6th Line
# This is the 7th Line
# This is the 8th Line
# This is the 9th Line
# This is the 10th Line""")
#
#
# def first_5_lines():
#     with open('myLine.txt', 'r') as fr:
#         record = fr.readlines()
#
#         # line target at 0 to 5, start with line 1
#         line_target = 1
#         line_end = 5
#
#         # condition for line
#         while line_target <= line_end:
#             print(record[line_target-1].rstrip())
#             line_target += 1
#
#
# def last_5_lines():
#     with open('myLine.txt', 'r') as fr:
#         record = fr.readlines()
#
#         # line target at 6 to 10, start with line 6
#         line_target = 6
#         line_end = 10
#
#         # condition for line
#         while line_target <= line_end:
#             print(record[line_target-1].rstrip())
#             line_target += 1
#
#
# first_5_lines()
# last_5_lines()


# 4:
# from tkinter import *
#
# root = Tk()
# root.title('GUI Example')
# root.geometry('250x100')
#
#
# # function copy text
# def copy_text():
#     text = txt_box.get()
#     lbl_text.config(text=text)
#
#
# txt_box = Entry(root)
# txt_box.pack(pady=(20, 0))
#
# btn_copy = Button(root, text='Copy Text', command=copy_text)
# btn_copy.pack()
#
# lbl_text = Label(root, text='Text is displayed here')
# lbl_text.pack()
#
# mainloop()

