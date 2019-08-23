import requests
import pandas as pd
from web_api import Crawl


def next(url, number, page):
    '''
    Make the request to access data from San Francisco Government's food truck
    And display current available food truck on Today
    '''
    url_query = Crawl(number, page).create_query()
    url += url_query
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        show_data_list(data)
    else:
        print("Url Invalid")
        quit()


def show_data_list(data):
    df = pd.DataFrame(data)
    if(df.empty):
        print("No data to display")
        quit()
    else:
        print(df.to_string(index=False, header=["Name", "Address"]))


def main():
    url = "http://data.sfgov.org/resource/bbb8-hzi6.json"
    page = 0
    number = 10
    next(url, number, page)
    while True:
        proceed = input("Print next 10 food trucks(y/n)?")
        if proceed.lower() == 'y':
            page += 1
            next(url, number, page)
        else:
            break


if __name__ == '__main__':
    main()




