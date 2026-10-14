import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from pyswip import Prolog
from pyswip.prolog import PrologError

CARPETA = os.path.dirname(os.path.abspath(__file__))


# Lee el token desde el archivo .env
def leer_token():
    with open(os.path.join(CARPETA, ".env"), encoding="utf-8") as f:
        for linea in f:
            if linea.startswith("TELEGRAM_TOKEN="):
                return linea.split("=", 1)[1].strip()
    raise SystemExit("Falta TELEGRAM_TOKEN en el archivo .env")


# Carga las reglas y hechos de Prolog
prolog = Prolog()
prolog.consult(os.path.join(CARPETA, "deportes.pl").replace("\\", "/"))


# Solo acepta letras, números y guion bajo (evita romper la consulta de Prolog)
def valido(texto):
    return texto.replace("_", "").isalnum()


# Hace una pregunta a Prolog y devuelve la lista de respuestas
def consultar(pregunta, variable):
    try:
        return [r[variable] for r in prolog.query(pregunta)]
    except PrologError:
        # Si la pregunta no es válida para Prolog, no hay respuesta
        return []


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = """
BOT DE DEPORTES

/modalidades futbol
/jugadores futsal
/recomendar alta exterior
/intensidad futsal
/lugar agua
"""
    await update.message.reply_text(mensaje)


# /modalidades futbol
async def modalidades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not valido(context.args[0]):
        await update.message.reply_text("Escribe así: /modalidades futbol")
        return

    deporte = context.args[0].lower()
    lista = consultar(f"modalidades_de('{deporte}', M).", "M")

    if lista:
        msg = f"Modalidades de {deporte}:\n\n"
        for m in lista:
            msg += f"• {m}\n"
    else:
        msg = "No encontré ese deporte."

    await update.message.reply_text(msg)


# /jugadores futsal
async def jugadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not valido(context.args[0]):
        await update.message.reply_text("Escribe así: /jugadores futsal")
        return

    modalidad = context.args[0].lower()
    lista = consultar(f"obtener_jugadores('{modalidad}', N).", "N")

    if lista:
        msg = f"{modalidad} se juega con {lista[0]} jugadores por equipo."
    else:
        msg = "No encontré esa modalidad."

    await update.message.reply_text(msg)


# /recomendar alta exterior
async def recomendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 2 or not valido(context.args[0]) or not valido(context.args[1]):
        await update.message.reply_text("Escribe así: /recomendar alta exterior")
        return

    intensidad = context.args[0].lower()
    lugar = context.args[1].lower()
    lista = consultar(f"recomendar_modalidad('{intensidad}', '{lugar}', M).", "M")

    if lista:
        msg = "Modalidades recomendadas:\n\n"
        for m in lista:
            msg += f"• {m}\n"
    else:
        msg = "No encontré recomendaciones."

    await update.message.reply_text(msg)


# /intensidad futsal
async def intensidad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not valido(context.args[0]):
        await update.message.reply_text("Escribe así: /intensidad futsal")
        return

    modalidad = context.args[0].lower()
    lista = consultar(f"obtener_intensidad('{modalidad}', I).", "I")

    if lista:
        msg = f"La intensidad de {modalidad} es {lista[0]}."
    else:
        msg = "No encontré esa modalidad."

    await update.message.reply_text(msg)


# /lugar agua
async def lugar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not valido(context.args[0]):
        await update.message.reply_text("Escribe así: /lugar agua")
        return

    sitio = context.args[0].lower()
    lista = consultar(f"modalidades_por_lugar('{sitio}', M).", "M")

    if lista:
        msg = f"Modalidades que se practican en {sitio}:\n\n"
        for m in lista:
            msg += f"• {m}\n"
    else:
        msg = "No encontré ese lugar. Prueba: interior, exterior o agua."

    await update.message.reply_text(msg)


# APP
app = ApplicationBuilder().token(leer_token()).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("modalidades", modalidades))
app.add_handler(CommandHandler("jugadores", jugadores))
app.add_handler(CommandHandler("recomendar", recomendar))
app.add_handler(CommandHandler("intensidad", intensidad))
app.add_handler(CommandHandler("lugar", lugar))

app.run_polling()