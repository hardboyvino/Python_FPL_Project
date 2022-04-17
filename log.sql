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
SELECT * FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25";



-- Compare the plate numbers with the peoples record. GIVES US NAMES OF THE 8 LICENSE PLATES HOLDERS - VANESSA, BARRY, IMAN, SOFIA, LUCA, DIANA, KELSEY, BRUCE
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");



-- Next, check who went to ATM to withdraw. GIVES US 8 ACCOUNT NUMBERS
SELECT * FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw";



-- Get names of the 8 account numbers withdrawing at Leggett Street. BRUCE, DIANA, LUCA, BROOKE, TAYLOR, BENISTA, IMAN, KENNY
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));



-- Check who overlaps with license plate and ATM withdrawals. BRUCE, DIANA, IMAN, LUCA
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");



-- Then, check the call logs (for a less than a minute call).
SELECT * FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28" AND duration <= "60";



-- Compare the callers, ATM withdrawal and License plate. BRUCE , DIANA
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28")
INTERSECT
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");



-- Compare the receivers, License plate. DIANA, LUCA
SELECT name FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28")
INTERSECT
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");



-- Compare the receiver, ATM withdrawal and License plate. DIANA, LUCA
SELECT name FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28")
INTERSECT
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "35");



-- Get the flight the next day 29th July 2021. ALL FLIGHTS LEAVE FROM FIFTYVILLE REGIONAL AIRPORT
SELECT full_name FROM airports WHERE id IN (SELECT origin_airport_id FROM flights WHERE year = "2021" AND month = "7" AND day = "29");



-- Get the earliest flight destination and city the next day 29th July 2021. O'HARE INTERNATIONAL AIRPORT, CHICAGO
SELECT * FROM flights WHERE year = "2021" AND month = "7" AND day = "29" ORDER BY hour, minute;
SELECT full_name FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE year = "2021" AND month = "7" AND day = "29" ORDER BY hour, minute);
SELECT city FROM airports WHERE id IN (SELECT destination_airport_id FROM flights WHERE year = "2021" AND month = "7" AND day = "29" ORDER BY hour, minute);



-- Passport number of BRUCE, DIANA AND LUCA. Compare with passport numbers on first flight
SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana" OR name = "Luca";

-- See if any of them where on that flight. BRUCE, LUCA
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE passport_number IN (SELECT passport_number FROM people WHERE name = "Bruce" OR name = "Diana" OR name = "Luca") AND flight_id IN (SELECT id FROM flights WHERE year = "2021" AND month = "7" AND day = "29" ORDER BY hour, minute LIMIT 1));





-- Check who overlaps with callers, license plate and ATM withdrawals. BRUCE AND DIANA
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE phone_number IN
(SELECT caller FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28" AND duration < "60")
INTERSECT
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");





-- Baker mentioned someone else talking on the phone for long without buying anything. Maybe they were calling the theif hence, theif not only caller but also receiver. DIANA IS THE THEIF!!!
SELECT name FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28")
INTERSECT
SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = "2021" AND month = "7" AND day = "28" AND atm_location = "Leggett Street" AND transaction_type = "withdraw"))
INTERSECT
SELECT name FROM people WHERE phone_number IN
(SELECT caller FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28" AND duration < "60")
INTERSECT
SELECT name FROM people WHERE license_plate IN
(SELECT license_plate FROM bakery_security_logs WHERE year = "2021" AND month = "7" AND day = "28" AND hour = "10" AND minute >= "15" AND minute <= "25");

-- BUt who was calling Diana? Just 1 person
SELECT caller FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28" AND receiver = (SELECT phone_number FROM people WHERE name = "Diana");

-- Their identity is ... MARGARET
SELECT name FROM people WHERE phone_number IN
(SELECT caller FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28" AND receiver = (SELECT phone_number FROM people WHERE name = "Diana"))
INTERSECT
SELECT name FROM people WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE year = "2021" AND month = "7" AND day = "28");