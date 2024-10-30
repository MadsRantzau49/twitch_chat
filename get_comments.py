import socket
import requests
from rocket_league import *
import threading

# Twitch IRC settings
SERVER = "irc.chat.twitch.tv"
PORT = 6667
NICKNAME = "rantzau49"  # Replace with your Twitch username
CHANNEL = "#rantzau49"           # Replace with the channel you want to connect to (start with #)
CLIENT_ID = "fu1cpr526f2qz27e4uldf8csj89c7a"        # Replace with your Client ID
CLIENT_SECRET = "7rlwrlu0fzrctqdvcpapf61qeyqpcf" # Replace with your Client Secret

# Establish connection to Twitch IRC
def connect_to_twitch():
    token = "oauth:c5o5hlmkfwwjvgjrkb8co702jolcr2"
    irc = socket.socket()
    irc.connect((SERVER, PORT))
    irc.send(f"PASS {token}\n".encode("utf-8"))
    irc.send(f"NICK {NICKNAME}\n".encode("utf-8"))
    irc.send(f"JOIN {CHANNEL}\n".encode("utf-8"))
    
    while True:
        response = irc.recv(2048).decode("utf-8")
        print("Server response:", response)  # Print server responses for debugging
        if "End of /NAMES list" in response:
            print("Successfully joined channel!")
            break
    return irc

# Main loop to print chat messages
def receive_messages(irc):
    rl = Rocket_League()
    threading.Thread(target=rl.controller).start()

    while True:
        response = irc.recv(2048).decode("utf-8")
        if response.startswith("PING"):
            irc.send("PONG :tmi.twitch.tv\n".encode("utf-8"))
        elif "PRIVMSG" in response:
            # username = response.split("!", 1)[0][1:]
            message = response.split("PRIVMSG", 1)[1].split(":", 1)[1].strip().lower()
            rl.new_input(message)
if __name__ == "__main__":
    irc_connection = connect_to_twitch()
    print(irc_connection)
    receive_messages(irc_connection)
