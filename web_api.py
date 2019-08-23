import datetime


class Crawl:
    def __init__(self, number, page):
        self.number = number
        self.page = page

    # get current time
    def get_current_time(self):
        return datetime.datetime.now().strftime("%H:%M")

    # get current day of week
    def get_day_of_week(self):
        return datetime.datetime.now().isoweekday()

    #create SoQl query to make api call
    def create_query(self):
        select_col = "applicant, location"
        current_time = self.get_current_time()
        current_day = self.get_day_of_week()
        limit = self.number
        offset = self.number * self.page

        soql = "?$select={0}" \
               "&$where='{1}' Between start24 AND end24 AND dayorder={2}" \
               "&$limit={3}" \
               "&$offset={4}" \
               "&$order=applicant ASC".format(select_col, current_time, current_day, limit, offset)
        return soql
