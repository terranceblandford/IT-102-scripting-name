#FindThePasswords
#By Terrance Blandford


import crypt
import sys
import os

def load_shadow(filename):
    users = {}
    with open(filename, "r", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            parts = line.split(":")
            user = parts[0]
            hashed = parts[1] if len(parts) > 1 else ""
            if hashed in ("", "*", "!"):
                continue
            users[user] = hashed
    return users

def load_wordlist(filename):
    with open(filename, "r", errors="ignore") as f:
        return [w.strip() for w in f if w.strip()]

def get_crypt_salt(full_hash):
    if not full_hash.startswith("$"):
        return None
    parts = full_hash.split("$")
    if len(parts) >= 4 and parts[2].startswith("rounds="):
        return f"${parts[1]}${parts[2]}${parts[3]}$"
    elif len(parts) >= 3:
        return f"${parts[1]}${parts[2]}$"
    else:
        return None

def crack(shadow_file, wordlist_file, out_file="cracked.txt"):
    users = load_shadow(shadow_file)
    words = load_wordlist(wordlist_file)

    if not users:
        print("No crackable passwords found in shadow file")
        return
    print(f"loaded {len(users)} user hashes and {len(words)} candidate passwords.")
    found = ()

    for user, full_hash in users.items():
        salt = get_crypt_salt(full_hash)
        if salt is None:
            print( f"[!] Could not parse salt for {user}.")
            continue

        matched = False
        for idx, word in enumerate(words, start=1):
            test = crypt.crypt(word, salt)
            if test == full_hash:
                print(f"[+] {user} -> {word}")
                found[user] = word
                matched = True
                with open( out_file, "a") as outf:
                    outf.write(f"{user}:{word}\n")
                    break

            if idx % 100 == 0:
                print(f"[+] {user}: tried {idx} words")

            if not matched:
                print(f"[-] No match for {user} in this wordlist.")
        
        print("Done. Matches written to", out_file)
        return found
    
    if __name__ == "__main__":
        if len(sys.argv) < 3:
            print("Usage: python3 crack_shadow.py shadow.txt passwords.txt")
            sys.exit(1)

        shadow_fn = sys.argv[1]
        wordlist_fn = sys.argv[2]

        if not os.path.exists(shadow_fn):
            print("Shadow file not found:". shadow_fn); sys.exit(1)
        if not os.path.exists(wordlist_fn):
            print("Wordlist not found:", wordlist_fn); sys.exit(1)

        crack(shadow_fn, wordlist_fn)
