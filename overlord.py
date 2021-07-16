import time
import sys
import pygame
import random


class Fighter:  # Боец
    def __init__(self, name, hp, stamina, dmg):
        self.name = name
        self.hp = hp    # Максимум - 1000.
        self.dmg = dmg  # Максимум - 100000
        self.stamina = stamina  # Максимум - 100.
        self.dmg_blocked = False

    def attack(self, target, ultimate=False):   # target - цель, противник
        current_dmg = self.calculate_dmg()
        if self.dmg_blocked == True:
            current_dmg //= 2
            self.dmg_blocked = False

        if self.stamina > 0:
            if ultimate == True:
                target.hp -= current_dmg * 7
                print5000('ORA ORA ORA!')
                ora.play()
                self.stamina -= 7
            else:
                target.hp -= current_dmg
                self.stamina -= 2
            self.stamina += 1
            print(f'{target.name} HP: {target.hp}')
        else:
            print('Вы выдохлись. У вас не хватает выносливости, чтобы атаковать.')

    def block(self, target):
        target.dmg_blocked = True
        print5000('Урон противника уменьшен.')


class Player(Fighter):
    def __init__(self, name, hp, stamina, dmg):
        Fighter.__init__(self, name, hp, stamina, dmg)
        self.inventory = []
        self.money = {"бронзовые":23, "серебряные":12}

    def calculate_dmg(self):
        current_dmg = self.dmg
        if 'Murasame' in self.inventory:
            current_dmg += 100
        current_dmg += random.randint(-20, 20)
        return current_dmg


class Mob(Fighter):
    def calculate_dmg(self):
        current_dmg = self.dmg
        current_dmg += random.randint(-20, 20)
        return current_dmg


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
    print(sentence, end='')
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
ora = pygame.mixer.Sound('music/ora.mp3')

player = Player('Вася', 100, 3, 32)
def story_before_battle():
    name = input('Добро пожаловать, странник. Как твоё имя?\n')
    print5000('Ты попал в мир под названием...')
    time.sleep(2)
    world_name = input('Как же он назывался... ')
    print5000('Точно,', world_name)
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
    print5000('Незнакомец: Зовут меня Ахмед будем знакомы!')
    print5000('Ахмед: *протягивает вам руку*')
    print5000('*Я пожал руку*')
    print5000('Ахмед: Хорошо, сначала начнём с лёгкой мисии.')
    print5000('Ахмед: Ты готов?')
    print5000('Да готов.')
    print5000('Ахмед: Так первая мисия, сопроводить торговца в страну "Волн"')
    print5000('Ахмед: Торговец придёт через 1 час.')
    print5000('Пришёл торговец.')
    print5000('Мы отправились в путь.')
    print5000('Вы идёте по равнине')
    print5000('На вас напали!')

def battle(mob):
    print5000('На вас напали!')
    print5000(f'Противник: {mob.name}')
    print5000(f'HP: {mob.hp}')
    print5000('-----------')
    print5000(f'Ваше HP: {player.hp}')
    while True:
        battle = input('1) Бой 2) Посмотреть инвентарь 3) Убежать ')
        if battle != '1' and battle != '2' and battle != '3':
            continue    # Начинаем цикл заново

        battle = int(battle)
        if battle == 1:
            punch = input('1) Aтака 2) ORA ORA ORA 3) Защита ')
            if punch == '1':
                player.attack(mob)
            if punch == '2':
                player.attack(mob, ultimate=True)
            if punch == '3':
                player.block(mob)
            mob.attack(player)
        if battle == 2:
            print5000(player.inventory)
        if battle == 3:
            print5000('Вы успешно убежали')
            break   # Вырубаем цикл
        if player.hp <= 0:
            print5000('Поражение')
            sys.exit()
        if mob.hp <= 0:
            print5000('Бой окончен')
            print5000(f'Вы успешно отбились от противника {mob.name}')
            break

mob = Mob(name='Слайм', hp=50, stamina=5, dmg=20)
battle(mob)
print5000('Я с торговцем иду по тропе и на встречу нам выбегают разбойники')
mob = Mob(name='Разбийник', hp=100, stamina=5, dmg=32)
battle(mob)
