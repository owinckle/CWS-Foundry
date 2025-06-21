from services.google_sheet import GSM

def main():
    # Initialize the GSM (Google Sheets Manager)
    gsm = GSM()
    print(gsm.url)


if __name__ == "__main__":
    main()