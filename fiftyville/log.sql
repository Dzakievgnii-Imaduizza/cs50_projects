-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Get the description of crimes on the same time and location as specified.
SELECT description FROM crime_scene_reports
WHERE street = "Humphrey Street" AND day = 28 AND month = 7 AND year = 2021;
-- Bakery, 10:15am
-- Get testimonies from interviews
SELECT transcript FROM interviews
WHERE day = 28 AND month = 7 AND year = 2021
AND transcript LIKE "%Bakery%";
-- TESTIMONY 1 = Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.
-- TESTIMONY 2 = I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
-- TESTIMONY 3 = As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket.
SELECT * FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute >=15 AND minute <=25;
-- CURRENT SUSPECTS = Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey
-- ELIMINATE SUSPECTS USING TESTIMONY 2
SELECT name FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_location = "Leggett Street"
AND transaction_type = "withdraw"
AND day = 28 AND month = 7 AND year = 2021;
-- CURRENT SUSPECTS = Bruce, Iman, Luca
-- USE THE THIRD TESTIMONY
SELECT name, phone_number, caller, receiver FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE day = 28 AND month = 7 AND year = 2021
AND duration < 60;
-- CURRENT SUSPECT = BRUCE
-- FIND OUT WHO WAS THE ONE WHO BRUCE CALLED
-- RECEIVER NUMBER = (375) 555-8161
SELECT * FROM people
WHERE phone_number = "(375) 555-8161";
-- DUDE'S NAME WAS ROBIN
-- FIND OUT WHERE BRUCE WAS HEADING TO THAT DAY
SELECT * FROM people
WHERE name = "Bruce";
-- BRUCE'S PASSPORT NUMBER = 5773159633
SELECT origin_airport_id, destination_airport_id FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN flights ON flights.id = passengers.flight_id
WHERE name = "Bruce"
AND day = 29 AND month = 7 AND year = 2021;
-- ORIGIN = 8, DESTINATION = 4
-- FIND DESTINATION
SELECT * from airports WHERE id = 4 OR id = 8;
-- BRO WENT TO NYC