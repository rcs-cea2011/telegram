from telegram import bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import telegram


def start(update, context):
    update.message.reply_text('Hola humano')


def process_message(update, context):

    print(update)

    text = update.channel_post.caption
    print (text)

    # bot.deleteMessage(chat_id=update.channel_post.chat.id, message_id=update.channel_post.message_id)

    # text2 = update.message.text
    print ('00000')

    if update.channel_post['photo'] == []:
        print (1)
        fileID = update.channel_post['document']['file_id']
        fileName = update.channel_post['document']['file_name']
        context.bot.sendDocument(chat_id='@canalprincipa',
                                 caption=text,
                                 channel_post=text,
                                 document=fileID)

    elif update.channel_post['photo'] != []:
        print (2)
        fileID = update.channel_post['photo'][-1]['file_id']
        context.bot.sendPhoto(chat_id='@canalprincipa',
                              caption=text,
                              photo=fileID)
    else:
        print (3)
        text = update.channel_post.text
        context.bot.send_message(
            chat_id='@canalprincipa',
            channel_post=text
        )

    pass
# print(update)

#  text = update.channel_post.text
#  print (text)

# context.bot.send_message(
#    chat_id='@canalprincipa',
#    channel_post=text
# )


def process_message2(update, context):
    print (3)
    text = update.message.text
    context.bot.send_message(
        chat_id='@canalprincipa',
        text=text
    )
    pass


if __name__ == '__main__':
    token = os.environ['TOKEN']

    bot = telegram.Bot(token=token)

    updater = Updater(token=token, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.document | Filters.photo, process_message))

   # dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message2))

    updater.start_polling()

    print('Bot is polling')
    updater.idle()
