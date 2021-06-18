import time
import sys
import pygame


class Fighter:  # Боец
    def __init__(self, hp, stamina, strength, defence, dmg):
        self.hp = hp    # Максимум - 1000.
        self.dmg = dmg  # Максимум - 100000
        self.stamina = stamina  # Максимум - 100.
        self.strength = strength    # Максимум - 10000.
        self.defence = defence  # Максимум - 1000.

    def calculate_dmg(self):
        pass

    def attack(self, target):   # target - цель, противник
        current_dmg = self.calculate_dmg()
        target.hp -= current_dmg
        print(target.hp)


class Player(Fighter):
    def __init__(self, hp, stamina, strength, defence, dmg):
        Fighter.__init__(self, hp, stamina, strength, defence, dmg)
        self.inventory = []
        self.money = {"бронзовые":23, "серебряные":12}

    def calculate_dmg(self):
        current_dmg = self.dmg
        if 'Murasame' in self.inventory:
            current_dmg += 100
        return current_dmg


class Mob(Fighter):
    def calculate_dmg(self):
        return self.dmg


# Создаём функцию викторины
def hokage_quiz():
    print5000('Вы слышите голос.\nОн говорит:')
    print5000('Имя седьмого хокаге')
    hoho = input('Что вы ответите? ')
    if hoho == 'Наруто':
        print5000('Возможно, ты прав...')
        time.sleep(3)
        dattebae.play()
        print5000('ТЫ ПРАВ ДАТТЕБАЁЁ.')
        time.sleep(2)

        print5000('Стенд Джотаро. In English please.')
        jojo_pose = input('Ответь мне. ')
        if jojo_pose == 'Star Platinum':
            time.sleep(3)
            yare_yare_daze.play()
            print5000('Yare yare daze.')
            return True
    return False


# Создаём функцию супер принта
def print5000(sentence):
    print(sentence)
    input()


pygame.mixer.init()
# Создаём аудиофайл
minecraft_music = pygame.mixer.Sound('music/1.mp3')
# Устанавливаем громкость
minecraft_music.set_volume(0.1)
# Запускаем
minecraft_music.play()

dattebae = pygame.mixer.Sound('music/даттебаё.mp3')
yare_yare_daze = pygame.mixer.Sound('music/yare-yare-daze.mp3')

player = Player(100, 3, 1, 1, 5)

# name = input('Добро пожаловать, странник. Как твоё имя?\n')
# print5000('Ты попал в мир под названием...')
# time.sleep(2)
# world_name = input('Как же он назывался... ')
# print5000('Точно,', world_name)
print5000('Вы проснулись посреди леса.')
print5000('Вы не знаете где вы, но помните своё имя.')
print5000('Вы встаёте и видите 1) горы и 2) город')
choice = int(input('Куда отправитесь? '))
if choice == 1:
    print5000('Вы не можете пойти в горы, вам нужна экипировка.')
if choice == 2:
    print5000('Вы отправились в город.')

print5000('Вы встретили повозку. Возница предлагает вам подъехать.')
choice = int(input('1) согласиться 2) не соглашаться. Ваш выбор: '))
if choice == 1:
    print5000('Вы подъехали до города.\nВыносливость + 7')
    stamina += 7

if choice == 2:
    print5000('Выносливость - 3\nСила + 10 ')
    stamina -= 3
    strength += 10
    print5000('По пути в город вы сильно утoмились. Слева от дороги вы заметили тропинку.')
    choice = int(input('1) Пойти или 2) нет? '))
    if choice == 1:
        print5000('Вы пошли по тропинке и увидели алтарь, в который вкована катана.')
        time.sleep(2)
        print5000('На алтаре надпись: "ТОЛЬКО ДОСТОЙНЕЙШИЙ СМОЖЕТ ОБЛАДАТЬ ЭТИМ МЕЧЁМ."')
        result = hokage_quiz()
        if result == True:
            print5000('ТЫ ДОСТОЙНЕЙШИЙ, ТАК ВОЗЬМИ ЭТОТ МЕЧ.')
            print5000('Имя ему Murasame')
            time.sleep(2)
            print5000('Получено: Murasame')
            inventory.append('Murasame')
            time.sleep(2)
            print5000('Здоровье + 7\nСила + 99\nЗащита + 7\nВыносливость + 32')
            hp += 7
            strength += 99
            defence += 7
            stamina += 32
        if result == False:
            print5000('Ну прости ты не достоин. Второго шанса не будет. ')
            print5000('*Появляются стражи*')
            the_world = time.time()
            tikat = int(input('1) Тикать/ 2) не тикать\nУ вас 1 секундa\n'))
            time_taken = time.time()
            if tikat == 1 and time_taken - the_world < 10:
                print5000('*Вы успешно удираете*')
            else:
                print5000('ZA WARUDOOOOO!')
                print5000('RIP')
                print5000('GAME OVER')
                sys.exit()
    if choice == 2:
        print5000('Вы отказываетесь идти по тропе. ')
        print5000('На вас напали РАЗБИЙНИКИ. ')
        print5000('GAME OVER')
        sys.exit()


time.sleep(2)

print5000('Глава 2. Город.')
time.sleep(2)
print5000('Я вхожу в город.')
print5000('Я прогуливаюсь по нему, пытаясь понять куда я попал.')
print5000('В метре от меня есть большое построение и надпись "Гильдия авантюристов"')
print5000('Ну была не была, пойду туда.')
print5000('Я вошёл в здание и увидел столики, за которыми сидят авантюристы и торгаши')
print5000('Человек у входа говорит: "Хочешь вступить в гильдию?"')
print5000('Стартовый взнос составляет 2 серебряные монеты')
time.sleep(1)
sous = int(input('Я думаю 1)согласиться или 2)нет'))
sous == 2

print5000('Ну ладно, соглашусь.')
print5000('Незнакомый человек: "Отлично! Пойдём со мной."')
print5000('Незнакомец: *ведёт вас в комнату. На двери весит табличка "Главная комната"*')
print5000('Незнакомец: *Достаёт документ и протягивает мне*')
print5000('Незнакомец: Вот эти бумаги надо заполнить.')
print5000('Я осматриваю документ. На бумаге написано "Ваше имя"')
print5000('*Я подписываю документы и отдаю их незнакомцу*')
print5000('Незнакомец: Отлично, теперь ты официально член гильдии.')
print5000('*Я спрашиваю незнакомца как тебя зовут?*')
print5000('Незнакомец: Зовут меня Альберт будем знакомы!')
print5000('Альберт: *протягивает вам руку*')
print5000('*Я пожал руку*')
print5000('Альберт: Хорошо, сначала начнём с лёгкой мисии.')
print5000('Адьберт: Ты готов?')
print5000('Да готов.')
print5000('Альберт: Так первая мисия, сопроводить торговца в страну "Волн"')
print5000('Альберт: С тобой пойдут ещё 3 человека. Торговец придёт через 1 час.')
print5000('Альберт: Остальные уже здесь.')
print5000('*Из двери выходят 3 человека и говорят мы пришли*')
print5000('*Они заметили меня и спросили* о это ты тот новенький?')
print5000('*Я отвечаю* да это я')
print5000('Мы познакомились, и пришёл торговец.')
print5000('Мы отправились в путь.')
print5000('Вы идёте по равнине')
print5000('На вас напали!')
slime = Mob(50, 5, 2, 1, 5)
print5000('На вас напал слайм!')
print5000(f'HP: {slime.hp}')
# player.attack(goblin)
# goblin.attack(player)
#вывести защиту слайма, атаку и защиту игрока
