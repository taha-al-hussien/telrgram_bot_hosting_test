import os, logging, dotenv
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
    ConversationHandler
)
# Importin functions
from functions.color import color
from functions.start import start
from functions.count import count
from functions.remove_member import remove_member



dotenv.load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


logging.basicConfig(
    format=f'{color("Bl")}%(asctime)s{color("re")} - {color("R")}%(name)s{color("re")} - {color("R")}%(levelname)s\n{color("C")}%(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)













def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("count", count))
    application.add_handler(CommandHandler("remove", remove_member))

    logger.info(f"{color("G")}Bot started successfully!{color("re")}")
    application.run_polling()

if __name__ == '__main__':
    main()