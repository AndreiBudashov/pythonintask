#Задача N8. Вариант 8
#Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка.
#Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений.
#Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
#Будашов Андрей
#05.04.2016
import random
words=("питон","анаграмма","простая","сложная","ответ","подстаканник")
word=random.choice(words)
correct=word
jumple=""
hint=""
ball=100
while word:
	position=random.randrange(len(word))
	jumple+=word[position]
	word=word[:position]+word[(position+1):]
	
print(
"""
Добро пожаловать в игру 'Анаграммы'!
Надо переставить буквы так. чтобы получилось осмысленное слово.
(Для выхода нажмите Enter. не вводя своей версии.) 
"""
)
print("Вот анаграмма:",jumple)
guess=input("")
while guess !=correct and guess!="":
	guess=input("Попробуйте отгадать исходное слово: ")
	if guess=="подсказка":
		hint= (correct[position+1])
		print (hint)
		ball-=15
		position+=1
	elif guess==correct:
		print("Да, именно так! Вы отгадали!/n")
		print("Ваши баллы",ball)
	elif guess!=correct:
		print("Неправильно,попробуй еще")
print("Спасибо за игру")
input("Нажмите Enter для выхода")