from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, Application


def log(update):
    file = open('telelog.csv', 'a')
    file.write(
        f'{update.effective_user.first_name},{update.effective_user.id},{update.message.text}\n')
    file.close()


def log_2(update):
    file = open('telelog.csv', 'a')
    file.write(
        f'{update.effective_user.first_name},{update.effective_user.id},{variant}\n')
    file.close()


async def start(update, _):
    log(update)
    keyboard = [
        [
            InlineKeyboardButton("Рациональные", callback_data='1'),
            InlineKeyboardButton("Комплексные", callback_data='2'),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('С какими числами работаем?', reply_markup=reply_markup)


async def button(update, _):
    query = update.callback_query
    global variant

    variant = query.data

    log_2(update)

    await query.answer()
    if variant == '1':
        variant_text = 'рациональными'
        await query.edit_message_text(text=f'Итак, работаем с {variant_text} числами.\nВведите значение А: `/a`.')
    elif variant == '2':
        variant_text = 'комплексными'
        await query.edit_message_text(text=f'Итак, работаем с {variant_text} числами.\nВведите значение А: `/a`.')
    elif variant == '+':
        await query.edit_message_text(text=f'{a} {variant} {b} = {a+b}')
    elif variant == '-':
        await query.edit_message_text(text=f'{a} {variant} {b} = {a-b}')
    elif variant == '*':
        await query.edit_message_text(text=f'{a} {variant} {b} = {a*b}')
    elif variant == '/':
        await query.edit_message_text(text=f'{a} {variant} {b} = {a/b}')
    elif variant == '%':
        await query.edit_message_text(text=f'{a} {variant} {b} = {a%b}')
    else:
        await query.edit_message_text(text=f'{a} {variant} {b} = {a//b}')


async def a(update, context):
    log(update)
    global a
    sum = ''
    a = ''
    for i in context.args:
        sum += i
    if variant == '1':
        a = int(sum)
    else:
        a = complex(sum)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'A = {a}\nВведите значение B: `/b`')


async def b(update, context):
    log(update)
    global b
    sum = ''
    b = ''
    for i in context.args:
        sum += i
    if variant == '1':
        b = int(sum)
    else:
        b = complex(sum)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f'B = {b}\nВыберите действие: `/action`')


async def action(update, _):
    log(update)

    if variant == '1':
        keyboard = [
            [
                InlineKeyboardButton("+", callback_data='+'),
                InlineKeyboardButton("-", callback_data='-'),
                InlineKeyboardButton("*", callback_data='*'),
                InlineKeyboardButton("/", callback_data='/'),
            ],
            [
                InlineKeyboardButton("%", callback_data='%'),
                InlineKeyboardButton("//", callback_data='//'),
            ],
        ]
    else:
        keyboard = [
            [
                InlineKeyboardButton("+", callback_data='+'),
                InlineKeyboardButton("-", callback_data='-'),
                InlineKeyboardButton("*", callback_data='*'),
                InlineKeyboardButton("/", callback_data='/'),
            ],
        ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выбери действие:', reply_markup=reply_markup)


async def help_command(update, _):
    log(update)
    await update.message.reply_text("Используйте `/start` для начала работы с калькулятором.")


if __name__ == '__main__':

    app = Application.builder().token("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(CommandHandler('A', a))
    app.add_handler(CommandHandler('B', b))
    app.add_handler(CommandHandler('action', action))
    app.add_handler(CommandHandler('help', help_command))

    app.run_polling()
