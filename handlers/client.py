from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!\n'
                                                 f'Вот команды которые у нас есть: \n'
                                                 f'/info : Информация о менторстве и GeekCoin \n'
                                                 f'/mentors : список менторов которые могут вам помочь \n'
                                                 f'/techmentors : список тех-менторов которые могут вам помочь \n'
                                                 f'/help : помощь вам с дз \n'
                                                 f'/helpmentors : заполняете анкету и через некоторое время вам напишет ментор\n')


# async def mentors(message: types.message):
#     await bot.send_message(message.from_user.id, )
# async def teshmentors(message: types.Message):
#     await bot.send_message(message.from_user.id, )


async def help(message: types.Message):
    await bot.send_message(message.from_user.id,
                           "Понимаю, что иногда выполнение домашнего задания может быть сложным. "
                           "Важно следовать определенным шагам, чтобы успешно выполнить задание. "
                           "Вот несколько советов, которые могут помочь вам выполнить домашнее задание:\n"
                           "\n"
                           "Понимание задания: Внимательно прочитайте задание несколько раз, чтобы полностью понять, что от вас требуется. "
                           "Если есть непонятные моменты, не стесняйтесь спрашивать преподователей, менторов или одногруппников.\n"
                           "\n"
                           "Планирование: Разбейте задание на более мелкие части. Создайте план, в котором определите, какие шаги нужно предпринять, "
                           "чтобы выполнить задание. Это может включать в себя исследование, чтение, написание и проверку.\n"
                           "\n"
                           "Исследование и чтение: Если задание требует дополнительной информации или изучения, проведите небольшое исследование. "
                           "Воспользуйтесь учебниками, интернетом и другими ресурсами для получения необходимой информации.\n"
                           "\n"
                           "Самоконтроль: После завершения задания, не забудьте провести проверку на наличие ошибок и опечаток. "
                           "Это поможет улучшить качество вашей работы.\n"
                           "\n"
                           "Время для отдыха: Не забывайте делать перерывы во время работы над заданием."
                           " Отдых поможет вам сохранить концентрацию и эффективность.\n"
                           "\n"
                           "\n"
                           "Помните, что практика делает мастера. "
                           "Чем больше заданий вы будете выполнять, тем легче будет справляться с будущими заданиями.")


async def info(message: types.Message):
    await bot.send_message(message.from_user.id, "GeekCoin - это внутренняя валюта Geeks\n"
                                                 "🏻‍💻Каждому ученику выдается 4 гиккоина в начале каждого месяца. Ученик может воспользоваться коинами, когда ему понадобится помощь ментора.\n"
                                                 "\n"
                                                 "🖇Ментор же в свою очередь сможет обменять их на деньги в администрации.\n"
                                                 "\n"
                                                 "Каждый гиккоин имеет свою цену в зависимости от месяца обучения⏬⏬\n"
                                                 "\n"
                                                 "📌Frontend и Backend \n"
                                                 "1 месяц - 150сом\n"
                                                 "2 месяц - 200 сом\n"
                                                 "3 месяц - 250 сом\n"
                                                 "4 месяц - 300 сом\n"
                                                 "5месяц - 350сом\n"
                                                 "\n"
                                                 "📌Android, iOS\n"
                                                 "1 месяц - 150сом\n"
                                                 "2,3 месяц - 200сом\n"
                                                 "4 месяц - 250сом\n"
                                                 "5,6 месяц - 300сом\n"
                                                 "7 месяц - 350сом\n"
                                                 "\n"
                                                 "📌 UX/UI\n"
                                                 "1 месяц - 150 сом\n"
                                                 "2 месяц - 200 сом\n"
                                                 "3 месяц - 250 сом\n"
                                                 "\n"
                                                 "❗️Физические коины и онлайн коины взаимозаменяемы. Если вы не использовали свои GeekCoin, то в конце учебного месяца они сгорают!\n"
                                                 "\n"
                                                 "P.S Если в начале месяца вам не выдали GeekCoinы, обратитесь к старшему ментору своего направления")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(info, commands=['info'])
    dp.register_message_handler(help, commands=['help'])
