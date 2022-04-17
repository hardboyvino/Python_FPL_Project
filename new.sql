-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Get the table columnns for crime scene reports
.schema crime_scene_reports;



-- Check out all the crime reports in the area
SELECT * FROM crime_scene_reports;



-- Narrow down the search to the date of the crime (Down to 2 crimes on the day)
SELECT * FROM crime_scene_reports WHERE day = "28" AND month = "7" AND year = "2021" AND street = "Humphrey Street";



-- Get the table columnns for interviews
.schema interviews;

-- Get the Police interview transcripts for the 3 witnesses and the bakery owner
SELECT * FROM interviews WHERE day = "28" AND month = "7" AND year = "2021" AND transcript LIKE "%bakery%";



-- First check bakery security logs for who exited the parking lot. GIVES US 8 LICENSE PLATE NUMBERS
SELECT * FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "35";

-- Get passport number of all those on the 1st flight to Chicago

SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE destination_airport_id = "4" AND year = "2021" AND month = "7" AND day = "29");

-- Get the names of those passports
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE destination_airport_id = "4" AND year = "2021" AND month = "7" AND day = "29"));


-- Join people and phone_calls so as to find caller and receiver 1 time
SELECT * FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller;


SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25")
INTERSECT
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28" AND duration <= "60")
INTERSECT
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id IN (SELECT id FROM flights WHERE year = "2021" AND month = "7" AND day = "29" AND id = "36"));