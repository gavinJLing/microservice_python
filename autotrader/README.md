## AutoTrader Scraper

A code sample to scrape online web site ([AutoTrader]() ) for car details to act as a data sample.A
Written in Python, using [BeautifulSoup4]() as the website DOM model api, and [Requests]() to handle the Http web services protocol.A

### Goal
To create AWS serverless app. with a console display UI. [Inspiration](https://medium.com/i-like-big-data-and-i-cannot-lie/serverless-data-engineering-aws-glue-lambda-athena-quicksight-de3ef177884f)
and associated [code](https://github.com/pbegle/scrape-craigslist-rentals/blob/master/handler.py)

This project requests details of []Audi R8's](https://www.autotrader.co.uk/car-search?sort=price-asc&radius=200&postcode=tn278eh&onesearchad=Used&make=AUDI&model=R8&transmission=Automatic)


## Get the code
```
git clone
cd /xxx/autotrader
```


**Dependancies**
```
pip install BeautifulSoup4
pip install requests

```

## Scrape the page
This will look to recover a long list of Audi R8 summaries from Autotrader, de-dup'g the list as it goes.
For each advert search summary it will then recover the detail page to further scrape some details. Autotrader uses iframes
a lot to contain the data. Will my limited knowledge and caring of the site I felt that it was sufficient to grab some text, where a down stream NLP process would attenpt to recover the spec. of each vehicle, based on the test description.


**Sample output from the search summary phase**
```
https://www.autotrader.co.uk/car-search?sort=price-asc&radius=200&postcode=tn278eh&onesearchad=Used&make=AUDI&model=R8&year-from=2007&year-to=2019&body-type=Coupe&transmission=Automatic&page=1
Processing Ad's from page 1 of 10. For total of Car count: 99
https://www.autotrader.co.uk/car-search?sort=price-asc&radius=200&postcode=tn278eh&onesearchad=Used&make=AUDI&model=R8&year-from=2007&year-to=2019&body-type=Coupe&transmission=Automatic&page=2
Processing Ad's from page 2 of 10. For total of Car count: 99
skipping duplicate add for ad_id 201910213547933
skipping duplicate add for ad_id 201910213547933
https://www.autotrader.co.uk/car-search?sort=price-asc&radius=200&postcode=tn278eh&onesearchad=Used&make=AUDI&model=R8&year-from=2007&year-to=2019&body-type=Coupe&transmission=Automatic&page=3
Processing Ad's from page 3 of 10. For total of Car count: 99
skipping duplicate add for ad_id 201906259388565
skipping duplicate add for ad_id 201909182373026
skipping duplicate add for ad_id 201907260477164
```

**Sample output from the detail phase**
```
inspection of Advert 1 of 99 for more details
url: https://www.autotrader.co.uk/classified/advert/201907260477164
Meta detail: # 1  id: 201907260477164   desc: Price: £54,995. Four wheel-drive, Audi parking system plus with rear camera, Contrast stitching - Titanium grey, Cruise control, Metallic - Suzuka grey, Metallic paint REF:C3CGC. Grey, Stunning low mileage example equipped with £5945 in options costing £99845 new in Suzuka grey metallic. Just serviced by Audi, the car has been serviced at 3664 miles, 5175 and 6336 miles. The car features LED headlights, advanced parking system with rear view camera, heated seats, Audi Music Interface, Nappa leather sports seats, bluetooth phone interface, cruise control, sat nav, front and rear parking sensors, voice control, LED daytime running lamps, Quattro 4WD, Sport mode, climate control and more. All keys and bookpack present. PROMOTORS WERE AWARDED A TOP 10 RANKING IN THE 2018 AUTOTRADER RETAILER AWARDS OUT OF OVER 6,500 NATIONAL RETAILERS. PLEASE SEE OUR WEBSITE FOR 60+PHOTOS HIGH QUALITY PHOTOS, HD VIDEO AND ONLINE FINANCE CALCULATOR. ZERO DEPOSITS AVAILABLE, SUBJECT TO STATUS. MOST OF OUR VEHICLES ARE READY TO DRIVE AWAY TODAY., £54,995
...
inspection of Advert 44 of 99 for more details
url: https://www.autotrader.co.uk/classified/advert/201908100994942
Meta detail: # 44  id: 201908100994942   desc: Price: £49,999. Key Information:

- List Price When New £100,145
- Capristo Sports Exhaust
- Full Audi Service History
- S Tronic

Factory Fitted Optional Extras:

LED Headlights - £2,860
Sideblade Carbon Sigma - £1,800
Metallic Paint - £715
19" '5-arm double spoke' Design Alloy Wheels in Titanium Finish - £570
Heated Front Seats	- £280
Coloured Stitching for Fine Nappa Leather - £275
Tyre Pressure Monitoring System - £275
Audi Music Interface - £255
Cruise Control - £225
Audi Hill Hold Assist - £90
Samao Orange, Metallic (Quartz grey sideblade)

Total Price of Optional Equipment	£7,345

Interior:

Full Leather Seats
Satellite Navigation
Heated Seats
Flat Bottom Leather Steering Wheel
Multi-Function Steering Wheel
Air Conditioning
Electric Windows
FM Radio
Bluetooth Connectivity

Exterior:

19" Alloy Wheels
LED Daylight Running Lights
Auto Lights
Body Coloured Callipers
```

## Output file contents

```
$ jq . car_science_autodtrader_20191028.json
{
  "source": "autotrader",
  "timestamp": "20191028",
  "ads": [
    {
      "id": "201907260477164",
      "title": "Audi R8 4.2 V8 QUATTRO 2d AUTO",
      "price": 54995,
      "reg": "2013/63",
      "body_type": "coupe",
      "miles": 6360,
      "cc": 4.2,
      "tran": "automatic",
      "fuel": "petrol",
      "url": "https://www.autotrader.co.uk/classified/advert/201907260477164",
      "description_raw": "Price: £54,995. Four wheel-drive, Audi parking system plus with rear camera, Contrast stitching - Titanium grey, Cruise control, Metallic - Suzuka grey, Metallic paint REF:C3CGC. Grey, Stunning low mileage example equipped with £5945 in options costing £99845 new in Suzuka grey metallic. Just serviced by Audi, the car has been serviced at 3664 miles, 5175 and 6336 miles. The car features LED headlights, advanced parking system with rear view camera, heated seats, Audi Music Interface, Nappa leather sports seats, bluetooth phone interface, cruise control, sat nav, front and rear parking sensors, voice control, LED daytime running lamps, Quattro 4WD, Sport mode, climate control and more. All keys and bookpack present. PROMOTORS WERE AWARDED A TOP 10 RANKING IN THE 2018 AUTOTRADER RETAILER AWARDS OUT OF OVER 6,500 NATIONAL RETAILERS. PLEASE SEE OUR WEBSITE FOR 60+PHOTOS HIGH QUALITY PHOTOS, HD VIDEO AND ONLINE FINANCE CALCULATOR. ZERO DEPOSITS AVAILABLE, SUBJECT TO STATUS. MOST OF OUR VEHICLES ARE READY TO DRIVE AWAY TODAY., £54,995",
      "other1": "",
      "other2": "",
      "other3": ""
    }...
```
and
```
...{
      "id": "201908100994942",
      "title": "Audi R8 4.2 V8 QUATTRO 2d AUTO 424 BHP",
      "price": 49999,
      "reg": "2013/62",
      "body_type": "coupe",
      "miles": 33000,
      "cc": 4.2,
      "tran": "automatic",
      "fuel": "petrol",
      "url": "https://www.autotrader.co.uk/classified/advert/201908100994942",
      "description_raw": "Price: £49,999. Key Information:\n\n- List Price When New £100,145\n- Capristo Sports Exhaust\n- Full Audi Service History \n- S Tronic\n\nFactory Fitted Optional Extras:\n\nLED Headlights - £2,860\nSideblade Carbon Sigma - £1,800\nMetallic Paint - £715\n19\" '5-arm double spoke' Design Alloy Wheels in Titanium Finish - £570\nHeated Front Seats\t- £280\nColoured Stitching for Fine Nappa Leather - £275\nTyre Pressure Monitoring System - £275\nAudi Music Interface - £255\nCruise Control - £225\nAudi Hill Hold Assist - £90\nSamao Orange, Metallic (Quartz grey sideblade)\t\n\nTotal Price of Optional Equipment\t£7,345\n\nInterior: \n\nFull Leather Seats \nSatellite Navigation \nHeated Seats \nFlat Bottom Leather Steering Wheel \nMulti-Function Steering Wheel \nAir Conditioning \nElectric Windows \nFM Radio \nBluetooth Connectivity \n\nExterior:\n\n19\" Alloy Wheels \nLED Daylight Running Lights \nAuto Lights \nBody Coloured Callipers ",
      "other1": "",
      "other2": "",
      "other3": ""
    },

```





