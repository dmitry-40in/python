import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
import random


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


sweets_total = 221 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Привет, {update.effective_user.first_name}!\nЭто игра с конфетами человек против глупого бота.\nПравила:\nВы и бот делаете ход друг после друга.\nПервый ход определяет бот.\nЗа один ход можно забрать не более чем 28 конфет.\nТот, кто берет последнюю конфету - проиграл.')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/start - напомнить правила игры.\n/help - показать варианты действий.\n/sweets + число конфет (указывать без +) - начать играть с заданным количеством конфет.\n/take + число конфет (указывать без +) - взять несколько конфет.')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def sweets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global sweets_total

    sum = ''
    for i in context.args:
        sum += i
    sweets_total = int(sum)

    turn = random.randint(0,1)
    if turn == 0:
        bot_take_sweets = random.randint(1, min([28, sweets_total]))
        sweets_total -= bot_take_sweets
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Задано начальное количество конфет: {sum}шт.\nБот решил ходить первым и взял конфет: {bot_take_sweets} шт.\nОсталось конфет: {sweets_total} шт.')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Задано начальное количество конфет: {sweets_total} шт.\n{update.effective_user.first_name}, ходишь первым!')


async def take_sweets(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global sweets_total

    turn = ''
    for i in context.args:
        turn += i
    turn = int(turn)

    if turn <= 28 and turn >= 1:
        if turn > sweets_total:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Осталось конфет меньше, чем Вы хотите взять.')
        else:
            sweets_total -= turn
            
            if sweets_total == 0:
                await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{update.effective_user.first_name}, Вы выиграли!')
            else:
                if sweets_total > 28:
                    bot_take_sweets = random.randint(1, 28)
                    sweets_total -= bot_take_sweets
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Вы взяли конфет: {turn} шт.\nБот взял конфет: {bot_take_sweets} шт.\nОсталось конфет: {sweets_total} шт.')
                else:
                    bot_take_sweets = random.randint(1, sweets_total)
                    sweets_total -= bot_take_sweets
                    if sweets_total == 0:
                        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Бот взял конфет: {bot_take_sweets} шт.\nБот выиграл!')
                    else:
                        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Вы взяли конфет: {turn} шт.\nБот взял конфет: {bot_take_sweets} шт.\nОсталось конфет: {sweets_total} шт.')
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'Можно брать от 1 до 28 конфет')


if __name__ == '__main__':
    application = ApplicationBuilder().token('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX').build()

    start_handler = CommandHandler('start', start)   
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    sweets_handler = CommandHandler('sweets', sweets)
    take_sweets_handler = CommandHandler('take', take_sweets)
    
    help_handler = CommandHandler('help', help_command)


    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(sweets_handler)
    application.add_handler(take_sweets_handler)
    application.add_handler(help_handler)
    application.run_polling()
