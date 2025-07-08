from telegram.ext import Updater, CommandHandler
from telegram import ParseMode

TOKEN = "7616030256:AAES5uS_oTTYifktwQzNZ53fe05uVBSIYns"

def check(update, context):
    if not context.args:
        update.message.reply_text("❌ Please enter a TikTok username.\n\nExample:\n/check charlidamelio", parse_mode=ParseMode.MARKDOWN)
        return

    username = context.args[0].lstrip("@").lower()

    fake_data = {
        "charlidamelio": {
            "google": True,
            "email": True,
            "phone": False,
            "passkey": False
        },
        "kala.chan1526": {
            "google": False,
            "email": True,
            "phone": True,
            "passkey": False
        }
    }

    info = fake_data.get(username)
    if not info:
        update.message.reply_text(f"❌ No login info found for @{username}.")
        return

    msg = (
        f"🔍 *TikTok Account Check:* @{username}\n\n"
        f"{'✅' if info['google'] else '❌'} Google Linked\n"
        f"{'✅' if info['email'] else '❌'} Email Login Available\n"
        f"{'✅' if info['phone'] else '❌'} Phone Linked\n"
        f"{'✅' if info['passkey'] else '❌'} Passkey Enabled"
    )

    update.message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)

def start(update, context):
    update.message.reply_text("👋 Welcome! Use /check <username>")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("check", check))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
  
