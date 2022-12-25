# Prank Bot for Discord
A Discord bot that allows users to prank other users in a Discord server. The bot has two commands: /prank and /stopprank.

## **Command Overview**
### **/prank** - Takes in a Discord user as an argument and adds them to a list of users that will be pranked. The bot will then move the user to a designated prank channel and play a audio file called "prank_2.mp3" in the channel. If the prank function has not yet been started, it will also start a loop that will continue to move the user to the prank channel every 10 seconds.
### **/stopprank** - Takes in a Discord user as an argument and removes them from the list of users being pranked. This will stop the bot from moving the user to the prank channel and playing the audio file.
## **Requirements**
### Discord API token in a .env file as the DISCORD_TOKEN variable
discord.py and dotenv Python modules
### FFmpeg installed with the path to the ffmpeg.exe file specified in the code
## Running the Bot
To run the bot, simply execute the Python script on your machine. The bot will automatically connect to Discord and start listening for commands. You can then use the /prank and /stopprank commands in a Discord server where the bot is a member to prank other users.
