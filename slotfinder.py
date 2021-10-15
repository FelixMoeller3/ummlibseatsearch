from time_utils import Date


def parse_table(table):
    table_rows = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')
        elements = []
        for column in columns:
            elements.append(column.get_text())
        table_rows.append(elements)
    table_rows.pop(0)
    return table_rows


def find_available_slots(res_slots):
    available_slots = []
    for slot in res_slots:
        if int(slot[3]) != 0:
            available_slots.append(Date(slot[0]))
    return available_slots


def find_wanted_slots(available_slots, bib_days):
    wanted_slots = []
    for slot in available_slots:
        slot_found = None
        for bibday in bib_days:
            if bibday.equals_date(slot):
                wanted_slots.append(bibday)
                slot_found = bibday
                break
        if slot_found is not None:
            bib_days.remove(slot_found)
    return wanted_slots
