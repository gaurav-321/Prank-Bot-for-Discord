# Prank-Bot-for-Discord

🚀 **Project Title:** Prank-Bot-for-Discord 🎉

✨ **Description:** Prank-Bot-for-Discord is a Python-based Discord bot designed to allow users to prank others within a Discord server using two commands: `/prank` and `/stopprank`. This bot provides an engaging way for members to interact in a fun and controlled manner, promoting camaraderie and creativity.

🚀 **Features:**
- 🎉 `/prank`: Adds a user to the prank list, moves them to a designated channel, and plays an audio file.
- 🏃‍♂️ `/stopprank`: Removes a user from the prank list and stops the pranking process.
- 🔧 Easy setup and configuration using environment variables.
- 🎶 Plays audio files during pranks.

🛠️ **Installation:**
To get started with Prank-Bot-for-Discord, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/gag3301v/Prank-Bot-for-Discord.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd Prank-Bot-for-Discord
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    Create a `.env` file in the root directory and add your Discord bot token:
    ```
    DISCORD_TOKEN=your_discord_bot_token_here
    AUDIO_FILE_PATH=path_to_your_audio_file.mp3
    ```

📦 **Usage:**
Here’s how to use Prank-Bot-for-Discord:

- **To start pranking a user:**
  ```bash
  /prank @username
  ```
  This command will move the specified user to a designated channel and play an audio file.

- **To stop pranking a user:**
  ```bash
  /stopprank @username
  ```
  This command will remove the user from the prank list and stop the pranking process.

🔧 **Configuration:**
Ensure that you have FFmpeg installed on your system as it is required for playing audio files. You can download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html).

🧪 **Tests:**
Prank-Bot-for-Discord does not include automated tests at the moment, but you can manually test the bot by running it and using the provided commands.

📁 **Project Structure:**
```
Prank-Bot-for-Discord/
├── .env
├── main.py
├── requirements.txt
└── README.md
```

🙌 **Contributing:**
Contributions are welcome! Please read our [CONTRIBUTING.md](https://github.com/gag3301v/Prank-Bot-for-Discord/blob/main/CONTRIBUTING.md) for details on how to contribute.

📄 **License:**
This project is licensed under the MIT License - see the [LICENSE](https://github.com/gag3301v/Prank-Bot-for-Discord/blob/main/LICENSE) file for more information.