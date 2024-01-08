from datetime import date
import xml.etree.ElementTree as ET
import requests


def parse_cbar_data():
    request_url = "https://cbar.az/currencies/{}.xml".format(date.today().strftime('%d.%m.%Y'))
    response = requests.get(request_url, timeout=30)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    result = {
        "date": root.attrib.get("Date"),
        "rates": []
    }
    for currency in root[1]:
        result["rates"].append(
            {
                "code": currency.get("Code"),
                "nominal": currency.find("Nominal").text,
                "value": currency.find("Value").text
            }
        )

    print(result)

    # for currency in root.findall("*/Valute"):
    #     print(currency.get("Code"))
    #     print(currency.find("Nominal").text)
    #     print(currency.find("Value").text)


parse_cbar_data()