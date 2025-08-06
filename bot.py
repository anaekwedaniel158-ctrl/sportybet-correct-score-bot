
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

BOT_TOKEN = "8045355459:AAF0Dbli97VZ-9b6St8XTbpPag2uxO5uQLQ"

# Replace this with real odds-to-score data
odds_map = {
    23: ["1-1", "2-1"],
    42.61: ["0-0", "2-2"],
    34.75: ["1-0"],
    21.61: ["3-1"],
    41.73: ["2-3"],
    26.51: ["3-2"],
    41.31: ["1-2"],
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Send me an odds (e.g. 23), and I’ll show you possible correct scores.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        text = update.message.text.strip()
        odds = float(text)
        scores = odds_map.get(odds, [])
        if scores:
            reply = f"Possible correct scores for odds {odds}:
" + "\n".join(scores)
        else:
            reply = "No matching correct scores found for this odds."
        await update.message.reply_text(reply)
    except ValueError:
        await update.message.reply_text("Please send a valid number (e.g. 23)")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("odds", handle_message))
    app.add_handler(CommandHandler("score", handle_message))
    app.add_handler(CommandHandler("search", handle_message))
    app.add_handler(CommandHandler("find", handle_message))
    app.add_handler(CommandHandler("get", handle_message))
    app.add_handler(CommandHandler("show", handle_message))
    app.add_handler(CommandHandler("check", handle_message))
    app.add_handler(CommandHandler("match", handle_message))
    app.add_handler(CommandHandler("result", handle_message))
    app.add_handler(CommandHandler("predict", handle_message))
    app.add_handler(CommandHandler("info", start))
    app.add_handler(CommandHandler("help", start))
    app.add_handler(CommandHandler("", handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
