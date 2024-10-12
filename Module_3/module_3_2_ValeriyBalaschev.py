# Домашняя работа по уроку "Способы вызова функции"



def kontrol1(recipient, sender):
    sign = True
    if '@' in recipient and '@' in sender:
        sign = False
    return sign


def kontrol2(recipient, sender):
    sign = True
    for a in (".com", ".ru", ".net"):
        if recipient.endswith(a):
            sign = False
            break
    return sign


def kontrol3(recipient, sender):
    sign = True
    for a in (".com", ".ru", ".net"):
        if sender.endswith(a):
            sign = False
            break
    return sign

def send_email(message, recipient, *, sender="university.help@gmail.com"):

    if kontrol1(recipient, sender) is True or kontrol2(recipient, sender) is True or kontrol3(recipient, sender) is True:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != 'university.help@gmail.com':
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender}> на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.t
