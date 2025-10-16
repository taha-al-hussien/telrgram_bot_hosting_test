from telegram import Update
from telegram.ext import ContextTypes
from functions.color import color


async def remove_member(update: Update, context: ContextTypes.DEFAULT_TYPE, user = None):
    # debugging
    print(f"\n{color("R")}{update.effective_user.first_name} {update.effective_user.last_name}{color("re")} used {color("R")}/remove{color("re")} {" ".join(context.args)}")
    print(f"With id: {update.effective_user.id} and Username: {update.effective_user.username}\n")
    
    if context.args:
        chat_member = await context.bot.get_chat_member(chat_id=update.effective_chat.id, user_id=int(context.args[0]))
        user = chat_member.user
    if user is None:
        user = update.message.reply_to_message.from_user
    
    chat_type = update.message.chat.type
    
    if not (chat_type == "group" or chat_type == "supergroup"):
        await update.message.reply_text("This command can only be used in groups.")
        return
    
    chat_id = update.message.chat_id
    await context.bot.ban_chat_member(chat_id=chat_id, user_id=user.id)
    await update.message.reply_text(f"{user.first_name}{" " + user.last_name if not user.last_name == None else ""} has been removed from the group.")


