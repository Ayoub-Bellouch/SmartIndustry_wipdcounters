# SmartIndustry_wipdcounters
The file vEnv is an instance of the envirennement created with => conda env create -f "..Directory\vEnv.yml"
You can create your venv using the file.yml => conda env create -f environment_name.yml



* Telegram Automation Part1 - bot for individual chat :
    On Telegram, search @ BotFather, send him a “/start” message
    Send another “/newbot” message, then follow the instructions to setup a name and a username - Call it "NotifCall"
    Choose a username of my bot -> "NotifCall_bot"
    On Telegram, search your bot (by the username you just created), press the “Start” button or send a “/start” message
    Use this token to access the HTTP API:

              5121400289:AAHRZKx2voyY3HSfHJi2bgsLdHqnKB_WpcY
              Keep your token secure and store it safely, it can be used by anyone to control your bot.

    Open a new tab with your browser, enter https://api.telegram.org/bot/getUpdates , replace with your API token, press enter to run https://api.telegram.org/bot5121400289:AAHRZKx2voyY3HSfHJi2bgsLdHqnKB_WpcY/getUpdates
    Done! Congratulations on your new bot. You will find it at t.me/NotifCall_bot. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

* Telegram Automation Part2 - bot for groupe chat - Simulation Caractère Stocker en temp réel :

    After creating the bot using instruction in the top of this page, then:
    Add the bot to the group: Go to the group, click on group name, click on Add members, in the searchbox search for your bot like this: @my_bot, select your bot and click add.
    open the group chat in a browser, you will see an URL in this format: "https://web.telegram.org/z/#-783940739" a negative number occurs in the link, that is the chat_ID of the groupe that we can use to send our messages:
    we consider chat_id = -783940739, then we can use the telegram_bot_sendtext method to do the necessary to send notifs.

* Executive Files are: 
        1- Telegramautomation.py => is a python code that asks for 20 integer values, groups them in a list and then test the  decrease of the list, if it is the case it generates an alert message for objective to send it to a telegrame group identified with a chat_id.
the message sent contains the date of the summary, hours+minutes and the seconds remaining before the stackers is empty ...

        2- ProductionLigneState.py => is a python code that takes part counters in each production phase, integrates this data to an array: production phase name, counters value, and sends the message via telegram

Install requarements using :
	pip install -r requirements.txt
