import requests


class NBU_API():
    '''
    Інформація про офіційно установлені курси на поточну дату
    https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json
    '''

    def get_currency_rates_by_now(self):
        return requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json")

    '''
    Інформація про офіційно установлені курси на поточну дату
    https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json
    '''

    def get_specified_currency_rates_by_now(self, currency):
        return requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?json&valcode=" + currency)
