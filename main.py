import time
import datetime
from bs4 import BeautifulSoup
import requests
from mail_service import send_email
import time_utils
import slotfinder
from parser import get_args


username, password, receivers, bib_days = get_args()
print(username,password)
timeout = 300

while True:
    response = requests.get('https://www.umm.uni-heidelberg.de/bibliothek/s1/schulungen/arbeitsplatzreservierung_cms.php')
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table')

    res_slots = slotfinder.parse_table(table)
    available_slots = slotfinder.find_available_slots(res_slots)
    wanted_slots = slotfinder.find_wanted_slots(available_slots, bib_days)

    current_time = datetime.datetime.now()
    wanted_slots_found = len(wanted_slots)
    timeout = time_utils.set_timeout()
    if wanted_slots_found == 0:
        message = f"No slots found at {current_time}, sleeping until" \
                  f" {current_time + datetime.timedelta(seconds=timeout)} to search for the following" \
                  f" remaining slots: {time_utils.concatenate_dates(bib_days)}"
        print(message)
    else:
        dates_found = time_utils.concatenate_dates(wanted_slots)
        message = f"Found following slots at {current_time}: {dates_found}. Sleeping until" \
                  f" {current_time + datetime.timedelta(seconds=timeout)} to search for " \
                  f"the following remaining slots: {time_utils.concatenate_dates(bib_days)}"
        print(message)
        email_content = 'Für folgende Tage sind neue Reservierungsplätze verfügbar: ' + dates_found

        send_email(username, password, receivers, email_content, 'Neue Reservierungsplätze verfügbar')

    if len(bib_days) == 0:
        print("All desired slots found")
        break
    time.sleep(timeout)
