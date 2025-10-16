from telegram import Update
from telegram.ext import ContextTypes
from functions.color import color
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(f"\n{color("R")}{update.effective_user.first_name} {update.effective_user.last_name}{color("re")} used {color("R")}/start{color("re")}")
    print(f"With id: {update.effective_user.id} and Username: {update.effective_user.username}\n")
    await update.message.reply_text("Hello! I'm Taha bot.")
