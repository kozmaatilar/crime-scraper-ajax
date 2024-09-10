import httpx
import time
import asyncio
import json
import csv
from fake_useragent import UserAgent
import argparse
import os
from datetime import datetime
import csv

parser = argparse.ArgumentParser()

target_url = 'https://communitycrimemap.com/'

agent = UserAgent()

# Define header to write data into csv file
header = [ 'Class', 'Incident', 'Crime', 'Date/Time', 'Location_Name', 'Address', 'Accuracy', 'Agency', 'latitude', 'longitude', 'keyword' ]

# Define all global variables to use in this scraper
from_date = last_date = last_date_temp = search_keyword = east = north = west = south = lat = lng = ''
EXTRA_DATA = False # variable for extra data 

##### data to use for post request #####

async def getLocationCoordinates(endDate):
    post_data = {
        "buffer": {
            "enabled": False,
            "restrictArea": False,
            "value": []
        },
        "date": {
            "start": from_date,
            "end": endDate,
            "quick": ""
        },
        "agencies": [],
        "layers": {
            "selection": [
                None,
                None,
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                {
                    "selected": False
                },
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                },
                {
                    "selected": True
                }
            ]
        },
        "location": {
            "bounds": {
                "east": east,
                "north": north,
                "south": south,
                "west": west
            },
            "lat": lat,
            "lng": lng,
            "zoom": 13
        },
        "analyticLayers": {
            "density": {
                "selected": False,
                "transparency": 60
            }
        }
    }
    return post_data

##### request to get token #####

async def getAuthenticationToken():
    url = f'{target_url}api/v1/auth/newToken'
    async with httpx.AsyncClient() as client:
        request = await client.get(url)
        if request.status_code == 200:
            responseData = request.json()
            return responseData['data']['jwt']

##### function to write data #####

async def write_info(data):
    try: 
        with open("results/" + search_keyword + ".csv", mode = 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    except Exception as e:     
        print("Error: while writing data \n", e)

# convert date into specific format 2024-04-23 => 04/23/2024

async def convertDate(date):
    newDate = date.split('-')
    return newDate[1] + '/' + newDate[2] + '/' + newDate[0]


# post request to get data from server

async def getLocationData():
    url = f'{target_url}api/v1/search/load-data'
    global last_date_temp, EXTRA_DATA, last_date
    EXTRA_DATA = False
    async with httpx.AsyncClient() as client:        
        while True:
            try:
                print("Start")
                await asyncio.sleep(1)
                request = await client.post(url, data=json.dumps(await getLocationCoordinates(await convertDate(last_date_temp))), headers={"Content-Type": "application/json", "Authorization": f"Bearer {await getAuthenticationToken()}"})
                print(request)   
                break
            except Exception as e:
                print("An error occurred:", e) 
                continue
        try:
            if request.status_code == 200:
                print("Request successful.")
                responseData= request.json()
                i = 0
                length = len(responseData['data']['grid']['eve'])
                print(length)
                if(length == 0): return
                last_date_temp = responseData['data']['grid']['eve'][length-1]["DateTime"].split(" ")[0]
                print(last_date_temp)
                for item in responseData['data']['grid']['eve']:   
                    i += 1
                    Class = item['Class']
                    Incident = item['IRNumber']
                    Crime = item['Crime']
                    DateTime = item['DateTime'].split(':')[0] + ':' + item['DateTime'].split(':')[1]
                    LocationName = ''
                    try:
                        LocationName = item['LocationType']
                    except Exception as e:                  
                        LocationName = ''
                    try:
                        Address = item["AddressOfCrime"]
                    except Exception as e:
                        Address = ""
                    Accuracy = item['Accuracy']
                    Agency = item['Agency']
                    latitude = item['YCoordinate']
                    longitude = item['XCoordinate']
                    keyword = search_keyword
                    data = [Class, Incident, Crime, DateTime, LocationName, Address, Accuracy, Agency, latitude, longitude, keyword]
                    if i == 500:
                        EXTRA_DATA = True
                    if(data[3].split(" ")[0] != last_date_temp):
                        await write_info(data)
                if (last_date_temp != from_date) and EXTRA_DATA:
                    print('Got data to ' + last_date_temp)
                    await asyncio.create_task(getLocationData())                
                else: return
        except Exception as e:
            print("An error occurred:", e) 

# write hearder into csv file

async def write_header():
    try:
        with open("results/" + search_keyword + ".csv", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            
    except: print('Error while writing hearder')

# main function to run first

async def main():
    print('please input range of date')
    global from_date, last_date_temp, last_date, search_keyword, east, north, west, south, lat, lng

    fromdate = input("From: (01/01/2000): ")
    last_date_temp = input("To: (2024-04-15):(if you want current date, enter) ")
    if not last_date_temp: 
        last_date_temp = datetime.now().strftime("%Y-%m-%d")

    with open('cities.csv', 'r') as file:
        try:
            csv_reader = csv.DictReader(file)
            from_date = fromdate
            last_date = last_date_temp
            for row in csv_reader:
                last_date_temp = last_date                
                if row['city'].split(",")[0]:
                    search_keyword = row['city']
                    try: 
                        east = float(row['east'])
                        west =float(row['west'])
                        south = float(row['south'])
                        north = float(row['north'])
                        lat = float(row['lat'])
                        lng = float(row['lng'])
                    except: 
                        await write_header()
                        continue

                    if not os.path.exists('results/' + search_keyword + '.csv'):
                        await write_header()
                    print(search_keyword + ' scraping start from', from_date, 'to', last_date_temp)
                    await asyncio.create_task(getLocationData())
        except: pass

start_time = time.perf_counter()
print(asyncio.run(main()))
end_time = time.perf_counter()
