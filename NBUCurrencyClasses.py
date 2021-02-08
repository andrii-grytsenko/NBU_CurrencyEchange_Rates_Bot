import NBU_API as api


class CurrencyRateItem():
    def __init__(self):
        self.__index = 0
        self.__description = ""
        self.__rate = 0
        self.__currency_code = ""
        self.__exchange_date = ""

    def update(self, data):
        self.__index = data["r030"]
        self.__description = data["txt"]
        self.__currency_code = data["cc"]
        self.__rate = data["rate"]
        self.__exchange_date = data["exchangedate"]

    def to_string(self):
        return f"{self.__currency_code}: {self.__rate:.4f} ({self.__description})"

    def get_currency_code(self, currency_code):
        return self.__currency_code


class CurrencyRateList():
    def __init__(self):
        self.__rates_list = []
        self.__api = api.NBU_API()

    def __refresh(self, data):
        self.__rates_list.clear()
        for item in data:
            cr_item = CurrencyRateItem()
            cr_item.update(item)
            self.__rates_list.append(cr_item)

    def get_currency_rate(self, currency_code):
        for item in self.__rates_list:
            if item.get_currency_code(currency_code) == currency_code:
                return item.to_string()
        return f"Currency rate for {currency_code} was not defined"

    def update(self, currency=""):
        if currency != "":
            response = self.__api.get_specified_currency_rates_by_now(currency)
        else:
            response = self.__api.get_currency_rates_by_now()
        if response.status_code == 200:
            self.__refresh(response.json())
            return True
        else:
            return False

    def get_currencies_list(self):
        currencies_list = []
        for item in self.__rates_list:
            currencies_list.append(item.get_currency_code(self))
        return currencies_list
