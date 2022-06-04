#виталя
from msilib.schema import Class
from multiprocessing.connection import answer_challenge
from unicodedata import name


class Human: 
    def __init__(self, name):
        self.name = name
    
    def answer_question(self, question):
        
        print(f'Очень интересный вопрос! Не знаю')

#Тимофей
class Student(Human): 
    def ask_question(self, someone, question):
        
        print(f'{someone.name}, {question}')

        someone.ananswer_question()

        print(' ')                                              

#Марина
class Curator(Human):
    def answer_question(self, question): 
        if question == curator.question :
            print(f'Держись, всё получится. Хочешь видео с котиками?') 
        else:
            Human.answer_question()

#Ира                                                               
class Mentor(Human): 
    def answer_question(self, question):
        if question == mentor.question :
            print(f'Отдохни и возвращайся с вопросами по теории.')
            
        elif question == 'как устроиться работать питонистом?':
            print(f'Сейчас расскажу.')
        
        else:
            Human.answer_question()

#Евгений
class CodeReviewer(Human): 
    def answer_question(self, question):
        if question == reviewer.question :
            print(f'О, вопрос про проект, это я люблю.')
        
        else:
            Human.answer_question()
                                                                

student1 = Student('Тимофей')

curator = Curator('Марина')

mentor = Mentor('Ира')

reviewer = CodeReviewer('Евгений')

friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
