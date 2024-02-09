# assignment: programming assignment 1
# author: Jooho Lee
# date: 1/15/2024
# file: hello.py is a program that asks the user to enter user's name,
# major, and age and outputs a greeting message that
# include the information about the user
# input: string data
# output: string data
name = input('Hello! What is your name?\n')
major = input('What is your major?\n')
age = int(input('What is your age?\n'))
print(f'Nice to meet you, ' + name + '.\n')
print(f'Your major is ' + major + '.\n')
print(f'You will be ' + str(age + 1) + ' years old next year.')
