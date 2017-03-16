# Yelp Deals Bot (CLI)

## The Inspiration
Yelp is one of my most used app.
Whenever I need advice on where to eat or what to order, I consult yelp.
As a college student,  I am also interested in not paying a lot for food,
which can be difficult in Palo Alto.

Earlier this year, I was meeting up with a friend in downtown Palo Alto.
After a while, we decided to eat at Cream.
When I opened the Yelp App, I discovered that there was a deal.
To ensure that I will be aware of future deals and not just stumble upon them,
I wrote a bot using the Yelp 2.0 API to determine help me locate deals.

## How it Works
This is a bot that runs from the command line.
Input a location as an argument to find out which restaurants nearby are offerning vouchers or deals.

For this to work, you will need a config.py with your Yelp keys
please create a config.py file including the following:

### config.py

  key = "YOUR CONSUMER KEY"

  secret = "YOUR SECRET KEY"

  token = "YOUR TOKEN"

  secret_token = "YOUR SECRET TOKEN"

## Conclusions

The deals section for the few cities I tested (San Francisco or Palo Alto) seem a little lackluster. It is mostly just vouchers. I saw that there was also a cashback program where you get 10% cashback if you use a registered credit card.
