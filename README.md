# ummlibseatsearch

This project allows you to search for seats in the library of Umm (https://www.umm.de/start/) for specific days and get notified via Email when seats for a given day are available.

## Usage
-- usr 
The username of the Email-Account which is used to send the notification Emails. Preferably a Gmail-Account.

--pw
The password of the Email-Account whose username is specified as the "--usr"-argument

--r
A list of Email-Addresses which receive the notification, separated by a comma. Example: --r max.mustermann@gmx.de,maria.mustermann@gmail.com

--d
The days which should be searched for, also separated by a comma. Example: --d 10.05.2021,20.6.2021
