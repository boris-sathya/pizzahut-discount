# pizzahut-sweden-discount

## Description
If you're someone that eats at pizzahut sweden twice or more a week, you probably know that you can get a 20% discount coupon if you fill up
an online feedback survey. The goal of this script is to automate the feedback process by POSTING pre-defined answers to the survey. 

## Survey Rules
The rules of the survey are that, you should give your feedback within 3 days of your visit to Pizzahut, write down the discount code on your old receipt
and present it to the cashier the next time you visit, which cannot be farther than 3 months.

## Sample Usage
```
sathya@kuttisevuru:~/pizzahut-discount$ python pizzaforever.py -h
usage: pizzaforever.py [-h] [-g]

optional arguments:
  -h, --help  show this help message and exit
  -g          God mode. Fetch Coupons without a receipt

sathya@kuttisevuru:~/pizzahut-discount$ python pizzaforever.py 
Date of your visit YYMMDD:171205
Time of your visit HHMM:1151
Restaurant Number:206
Receipt Number:125121
Submitting Form: 0 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=173703
Submitting Form: 1 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=363703
Submitting Form: 2 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=363703
Submitting Form: 3 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=373703
Submitting Form: 4 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=373703
Submitting Form: 5 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=383703
Submitting Form: 6 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=393703
Submitting Form: 7 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=403703
Submitting Form: 8 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=413703
Submitting Form: 9 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=413703
Submitting Form: 10 -- URL: https://u.pizzahutsurvey.com/Survey.aspx?c=423703
Valideringskod: 80442
``` 
## God Mode
It happens that the webapplication doesn't actually validate the receipt number, so it is possible to generate discount coupons
without a valid receipt (and its associated data) and social engineer your way in or write down the *god mode* generated coupon code 
on a previously expired receipt.
