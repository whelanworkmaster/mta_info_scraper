import time
from threading import Thread
from selenium import webdriver

from status_manager import parse_statuses, get_new_delayed_trains_and_update_times
from constants import get_mta_line_delay_times_dict
from timer import Timer


class ScrapeUrl(Thread):

    def __init__(self, info_url):
        Thread.__init__(self)
        self.daemon = True
        self.info_url = info_url
        self.web_driver = webdriver.Firefox()
        self.delayed_trains = set()
        self.train_delay_times = get_mta_line_delay_times_dict()
        self.total_time = Timer()
        self.start()

    def run(self):
        self.total_time.start()
        while True:
            self.web_driver.get(self.info_url)
            statuses = self.web_driver.find_element_by_id('tab-subway')

            statuses = parse_statuses(statuses.text)
            self.delayed_trains = get_new_delayed_trains_and_update_times(statuses, self.delayed_trains, self.train_delay_times)
            time.sleep(5.0)

    def get_delayed_trains(self, line):
        if line in self.delayed_trains:
            return f'Line {line} is delayed'
        else:
            return f'Line {line} is not delayed'

    def get_line_uptime(self, line):
        uptime = 1 - (self.train_delay_times[line].get_time() / self.total_time.get_time())
        uptime = '{:.1%}'.format(uptime)
        return f'Line {line} has been up: {uptime}'
