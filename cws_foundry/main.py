from services.google_sheet import GSM
from time import sleep

def main():
    # Initialize the GSM (Google Sheets Manager)
    gsm = GSM()
    gsm.fetch()

    while True:
        # Find the next available task
        # Prioritize "Ready to publish"
        task = gsm.get_next_task()

        if not task:
            print("No tasks found...")
            continue

        print("Executing task...")
        sleep(5)
        gsm.update_task({
            "ID": task["ID"],
            "Status": "Published"
        })


if __name__ == "__main__":
    main()