import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 أهلاً بيك في B4xBot!\n\n"
        "🔥 البوت الشامل للمجموعات\n"
        "🛡️ حماية وإدارة\n"
        "🎮 ألعاب وتحديات\n"
        "⭐ نقاط ومستويات\n\n"
        "اكتب /help حتى تشوف الأوامر."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 أوامر B4xBot:\n\n"
        "/start - تشغيل البوت\n"
        "/help - المساعدة\n"
        "/id - معرفة الـ ID\n"
        "/rules - قوانين المجموعة"
    )


async def user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🆔 ID مالك هو:\n`{update.effective_user.id}`",
        parse_mode="Markdown"
    )


async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📜 قوانين المجموعة:\n\n"
        "1️⃣ الاحترام بين الأعضاء\n"
        "2️⃣ ممنوع السبام\n"
        "3️⃣ ممنوع نشر الروابط بدون إذن\n"
        "4️⃣ ممنوع الإساءة للأعضاء\n\n"
        "❤️ نتمنى للجميع وقت ممتع!"
    )


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN غير موجود")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("id", user_id))
    app.add_handler(CommandHandler("rules", rules))

    print("B4xBot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
