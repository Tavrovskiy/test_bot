from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import random

TOKEN = '7075523720:AAGIK3_imz_u7y9Y0sbJCGkroCzAKY2X-K8'

# Список советов
advice_list = [
    "Уделите время чтению каждый день.",
    "Начните утро с зарядки.",
    "Планируйте свой день заранее.",
    "Учите новое слово каждый день.",
    "Проводите время на природе.",
    "Изучайте новый навык или хобби.",
    "Практикуйте благодарность.",
    "Слушайте музыку, которая вас вдохновляет.",
    "Попробуйте медитацию или йогу.",
    "Пейте зеленый чай для улучшения здоровья.",
    "Ограничьте время, проведенное в социальных сетях.",
    "Путешествуйте, когда это возможно.",
    "Учите иностранные языки.",
    "Ведите дневник.",
    "Создавайте цели на короткий и долгий срок.",
    "Будьте активными и занимайтесь спортом.",
    "Помогайте другим.",
    "Смейтесь чаще.",
    "Учитесь готовить новые блюда.",
    "Сохраняйте позитивный настрой.",
    "Проводите качественное время с семьей и друзьями.",
    "Избегайте переедания.",
    "Спите не менее 7-8 часов в сутки.",
    "Учитесь быть терпеливыми.",
    "Практикуйте осознанность.",
    "Читайте книги по саморазвитию.",
    "Избавляйтесь от лишних вещей.",
    "Учитесь говорить 'нет'.",
    "Планируйте финансы и экономьте.",
    "Будьте открыты к новым возможностям."
]

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Получить совет", callback_data='get_advice')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Привет! Нажмите на кнопку, чтобы получить случайный совет.', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    advice = random.choice(advice_list)
    query.edit_message_text(text=f"Совет: {advice}")

def main() -> None:
    updater = Updater(TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
