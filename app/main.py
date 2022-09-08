from whois import WhoIs

if __name__ == "__main__":
    whoIs = WhoIs()
    print(whoIs.host("google.com"))