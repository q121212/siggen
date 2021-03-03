import requests
import numpy as np


class Api:
    def __init__(self, url=None):
        self.url = url
        self.page = None
        self.page_text = None
        self.signalType = {'int_page_signal_256': '_get_page_signal', 'sum_int_signal': '_get_int_signal'}
        self.exportFormat = {'xlsx': 'xlsx', 'csv': 'csv'}

    def _get_page(self):
        response = {'ok': None}
        try:
            response = requests.get(self.url)
            if response.ok:
                self.page = response.content
                self.page_text = response.text
        except (requests.exceptions.MissingSchema,
                requests.exceptions.InvalidURL,
                requests.exceptions.ConnectionError) as e:
            print(e)

    def _get_int_signal(self):
        if self.page:
            self.int_page_signal_256 = list(self.page)
            self.sum_int_signal = [sum(list(i.encode())) for i in self.page_text]
