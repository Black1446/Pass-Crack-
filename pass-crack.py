import hashlib
import itertools
import string
from colorama import init, Fore

# Initialize colorama
init(autoreset=True)

def crack_hash(password_hash):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    for length in range(1, 5):  # You can change the range based on password length
        for attempt in itertools.product(characters, repeat=length):
            attempt_str = ''.join(attempt)
            if hashlib.sha256(attempt_str.encode()).hexdigest() == password_hash:
                return attempt_str
    return None

def print_ascii_art():
    print(Fore.YELLOW + """
################################
       CRACK
################################
       CODED BY BLACK1446
################################
    EDUCATIONAL PURPOSE ONLY
################################
    """)

def main():
    print_ascii_art()
    print(Fore.YELLOW + "Xulo adeegga aad rabto:")
    print("1. TikTok")
    print("2. Facebook")
    print("3. YouTube")
    print("4. Instagram")
    print("5. PUBG")
    
    option = input("Dooro adeegga (1-5): ")
    
    if option in ['1', '2', '3', '4', '5']:
        username = input(Fore.YELLOW + "Gali username-ka: ")
        hashed_password = input(f"Gali sha256 password hash-ka ee {username}: ")
        password = crack_hash(hashed_password)
        
        if password:
            print(Fore.YELLOW + f"Password-ka {username} waa: {password}")
        else:
            print(Fore.YELLOW + "Password lama helin.")
    else:
        print(Fore.YELLOW + "Doorasho aan sax ahayn!")

if __name__ == "__main__":
    main()
