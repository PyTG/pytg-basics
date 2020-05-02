import telegram, logging

from datetime import datetime

from modules.pytg.ModulesLoader import ModulesLoader

def start_cmd_handler(update, context):
    bot = context.bot

    message = update.message
    chat_id = message.chat.id

    username = message.from_user.username
    user_id = message.from_user.id

    logging.info("Received start command update from {} ({}) in chat {}".format(username, user_id, chat_id))

    text_manager = ModulesLoader.load_manager("text")

    # Uncomment if username is needed to use the bot
    # if not username:
    #     logging.info("No username set")
    #
    #     phrases = text_manager.load_phrases("auth")
    #
    #     bot.sendMessage(
    #         chat_id = chat_id,
    #         text = phrases["no_username"]
    #     )

    #     return

    sqlite3_manager = ModulesLoader.load_manager("sqlite3")

    sqlite3_manager.connect()

    # Initialize user settings (if missing)
    user_settings_results = sqlite3_manager.select("Users", {'chat_id': chat_id}).fetchall()

    if len(user_settings_results) == 0:
        new_user_data = {}

        new_user_data["chat_id"] = chat_id
        new_user_data["username"] = username

        sqlite3_manager.insert("Users", new_user_data)
        sqlite3_manager.commit()

        user_data = sqlite3_manager.select("Users", {'chat_id': chat_id}).fetchone()
    else:
        user_data = user_settings_results[0]

        # Update username (if changed)
        if username != user_data["username"]:
            sqlite3_manager.update("Users", 
                key={'chat_id': user_data["chat_id"]}, 
                update_pairs={'username': username}
            )

            sqlite3_manager.commit()

    # Check user's authorization
    if user_data["authorized"] == 0:
        logging.info("User not authorized.")

        phrases = text_manager.load_phrases("auth")

        bot.sendMessage(
            chat_id = chat_id,
            text = phrases["no_auth"]
        )

        return

    sqlite3_manager.close()
    
    phrases = text_manager.load_phrases("welcome")

    menu_manager = ModulesLoader.load_manager("menu")

    bot.sendMessage(
        chat_id = chat_id,
        text = phrases["welcome"],
        reply_markup = menu_manager.create_reply_markup("main_menu")
    )