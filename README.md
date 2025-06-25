🤖 Night Companion Bot
Night Companion is a simple yet supportive Telegram bot built with pyTelegramBotAPI. It’s designed to check in on users regularly, offer reassurance, and provide quick emergency options—making it especially useful during night walks or when feeling unsafe.

🛠 Features
⏰ Auto Check-In: Periodic prompts asking the user if they are safe.

🚨 Emergency SOS: Sends an emergency alert to predefined contacts.

📍 Location Sharing: Prompts the user to share their location.

💬 Reassurance Responses: Comforting replies to emotional messages like "scared", "lost", or "thank you".

📘 Help Command: Lists all available commands.

📦 Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/night-companion-bot.git
cd night-companion-bot
Install dependencies:

bash
Copy code
pip install pyTelegramBotAPI
Add your bot token:
Replace the TOKEN variable in the script with your actual Telegram bot token.

🚀 Usage
Run the bot using:

bash
Copy code
python bot.py
Once running, you can interact with the bot on Telegram.

💬 Bot Commands
Command	Description
/start	Starts the bot and auto check-in
/help	Lists all available commands
/sos	Sends an emergency alert
/location	Requests location sharing
/stop	Stops auto check-in

📞 Emergency Contact Setup
Edit this line in the script to add or modify emergency contact numbers:

python
Copy code
emergency_contact = "9677945201", "9944738020"
⚠️ These contacts are only placeholders. Integrate with SMS or external services (e.g., Twilio) for real emergency notifications.

🛡 Disclaimer
This bot is a supportive tool and not a substitute for professional emergency services. Always contact local authorities in real emergencies.
