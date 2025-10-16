from telegram import Update
from telegram.ext import ContextTypes
from functions.color import color


async def count(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    print(f"\n{color("R")}{update.effective_user.first_name} {update.effective_user.last_name}{color("re")} used {color("R")}/count{color("re")} {" ".join(context.args)}")
    print(f"With id: {update.effective_user.id} and Username: {update.effective_user.username}\n")
    if not context.args:
        await update.message.reply_text("Give a number after the command to count to it.")
        return
    num = context.args[0].strip()
    if not num.isdigit():
        await update.message.reply_text("Error: the argument must be a number.")
        return
    num = int(num)
    if num <= 0:
        await update.message.reply_text("Give a number greater than 0 after the command to count to it.")
        return
    text = ''
    for i in range(1, num + 1):
        text += f'{i}\n'
    await update.message.reply_text(text)
        
