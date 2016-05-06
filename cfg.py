
# Config file

# Twitch server configurations. DON'T CHANGE !!
HOST = "irc.twitch.tv"
PORT = 6667
RATE = 20/30

# Your twitch username
NICK = "test_banana"

# Your twitch OAuth token (Can be found here: twitchapps.com/tmi/)
# To change OAuth token:
# 1) Replaces the whole text, apart from the quotes
PASS = "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Your twitch chat to look at (Twitch default is just your username)
# To change chat:
# 1) Type in your chat name in the text underneath keeping the # in front
CHAN = "#test_banana"

# Notification sound file.
# To change audio clip:
# 1) Put a .wav file inside the 'sounds' folder
# 2) Replace 'sound1.wav' in the text underneath to your sound files full name.
#		NOTE: Don't remove the 'sounds/' part of the test !!
SOUND = "sounds/sound1.wav"

# Cool down before a sound can be played again (unit in seconds)
COOL = 60