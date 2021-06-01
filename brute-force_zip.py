from tqdm import tqdm

import zipfile
import sys

# Choose the zip file to crack
zip_file = sys.argv[1]
# path of the dictionary/wordlist
wordlist = sys.argv[2]

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
x_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", x_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=x_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found in this wordlist.")
