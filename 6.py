# Построить систему классов для описания домашних животных.
# Предусмотреть методы для создания объектов, подачи голоса, реакции на ласку от хозяина.
class Pet(object):
    def voice(self):
        return self.v
    def caress(self):
        return self.c
class Hedgehog(Pet):
    v = 'фырк-фырк'
    c = 'xe-xe'
class Rabbit(Pet):
    v = 'Квик-квик'
    c = 'кнок-кнок'
class Parrot(Pet):
    v = 'Вовка - дурак'
    c = 'кеша доволен!'
class Pig(Pet):
    v = 'хрю-хрю'
    c = 'довольный хрюк'
pet = Hedgehog()
print('ёжик говорит: ', pet.voice())
print('когда ему хорошо: ', pet.caress())
pet = Rabbit()
print('кролик говорит', pet.voice())
print('когда хорошо; ', pet.caress())
pet = Parrot()
print('папугай говорит: ', pet.voice())
print('когда хорошо: ', pet.caress())
pet = Pig()
print('хрюшка говорит: ', pet.voice())
print('когда хорошо: ', pet.caress())
