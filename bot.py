from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# O token virá do Railway (variável de ambiente)
TOKEN = os.getenv("BOT_TOKEN")

texto_apresentacao = (
    "Oi amorzinho, bem-vindo! Tenho 22 aninhos, criada no interior. "
    "Posso parecer inocente, mas por trás do jeitinho meigo escondo uma safadeza "
    "que você nem imagina 😈\n\n"
    "Olha só o que te espera ⤵️💖\n\n"
    "🫦 Meu lado mais safadinho\n"
    "🎬 Acesso aos meus vídeos\n"
    "🔞 Fetiches, POVs\n"
    "🔞 Vídeo chamadas\n"
    "🔞 Sorteios pra gravar comigo\n"
    "🔞 Solo e acompanhada, do jeitinho que você gosta\n\n"
    "Basta um clique e uma atitude pra se divertir comigo.\n"
    "Te espero no VIP! 👇🏻"
)

# /start → mostra texto + botão "OBTER OFERTA"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🔹 OBTER OFERTA 🔹", callback_data="oferta")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        texto_apresentacao,
        reply_markup=reply_markup
    )

# Quando clica em OBTER OFERTA → mostra planos
async def mostrar_ofertas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("VIP 7 dias - R$23,90", callback_data="plano_7")],
        [InlineKeyboardButton("VIP 15 dias - R$28,90", callback_data="plano_15")],
        [InlineKeyboardButton("VIP 30 dias - R$38,90", callback_data="plano_30")],
        [InlineKeyboardButton("VIP Anual - R$93,90", callback_data="plano_anual")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.message.reply_text(
        "Escolha uma das ofertas abaixo 👇",
        reply_markup=reply_markup
    )

# Quando escolhe um plano
async def escolher_plano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    plano = query.data
    await query.answer()

    mensagens = {
        "plano_7": "Você escolheu o Plano VIP 7 dias - R$23,90",
        "plano_15": "Você escolheu o Plano VIP 15 dias - R$28,90",
        "plano_30": "Você escolheu o Plano VIP 30 dias - R$38,90",
        "plano_anual": "Você escolheu o Plano VIP Anual - R$93,90"
    }

    await query.message.reply_text(
        text=f"{mensagens.get(plano, 'Plano inválido')}\n\n"
             f"✅ Em breve vou te enviar o PIX para pagamento!"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(mostrar_ofertas, pattern="^oferta$"))
    app.add_handler(CallbackQueryHandler(escolher_plano, pattern="^plano_"))

    print("🤖 Bot rodando no Railway...")
    app.run_polling()

if __name__ == "__main__":
    main()
