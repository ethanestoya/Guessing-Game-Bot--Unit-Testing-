import socket

host = "192.168.1.214"
port = 7777

s = socket.socket()
s.connect((host, port))

data = s.recv(1024)
print(data.decode().strip())

# --- Bot Player ---
use_bot = input("Play as bot? (y/n): ").lower() == 'y'
low = 1
high = 100
# -----------------------

while True:
    if use_bot:
        guess = (low + high) // 2
        user_input = str(guess)  # Convert guess to string
        print(f"Bot guesses: {guess}")
    else:
        user_input = input("Choose Difficulty: ").strip()

    try:
        s.sendall(user_input.encode())
        reply = s.recv(1024).decode().strip()
        print(reply)

        if "CORRECT!" in reply:
            break

        if use_bot:
            if "Guess Lower" in reply:
                high = guess - 1
            elif "Guess Higher" in reply:
                low = guess + 1
    except ConnectionAbortedError as e:
        reply = s.recv(1024).decode().strip()
        print(reply)
        break

s.close()
