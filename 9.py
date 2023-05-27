import requests
import logging
logging.basicConfig(level=logging.DEBUG,
filename="logs.log", filemode="a",
format="We have next logging message: "
"%(asctime)s:%(levelname)s-%(message)s"
)
choose = input("Номер нужной крипто валюты - ")
logging.info("first choose")
value = float(input("Количевство криптовалюты - "))
logging.info("second choose")
b = 0
c = 0
for i in range (1):
    def m(*args):
        for choose in args:
            if type(choose) == int:
                logging.warning("check syntax")
                if choose >= 0:
                    logging.warning("check type")
                    if choose < 10:
                       logging.warning("check type")
                       pass
                    else:
                        print(TypeError, "Число должно быть меньше 11")
                        logging.error("error")
                        break
                    pass
                else:
                    print(TypeError, "Число должно быть больше 0")
                    logging.error("error")
                    break
                pass
            else:
                print(SyntaxError, "Это должно быть число")
                logging.error("error")
                break
                b = 1

    if b == 1:
        break
    else:
        pass

    a = int(choose)-1
    logging.info("set number of list")
    res_parse_list = []
    logging.info("start list")
    response = requests.get("https://coinmarketcap.com/")
    logging.info("check website")
    response_text = response.text
    response_parse = response_text.split("<span>")
    logging.info("delete class")
    for parse_elem_1 in response_parse:
       if parse_elem_1.startswith("$"):
           logging.info("search")
           for parse_elem_2 in parse_elem_1.split("</span>"):
               logging.info("delete class")
               if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                  logging.info("search")
                  res_parse_list.append(parse_elem_2)

    exchange_rate = res_parse_list[a]
    logging.info("search number of list")
    exchange_rate = exchange_rate.replace("$", "").replace(",", "")
    logging.info("clear")
    exchange_rate_1 = float(exchange_rate)
    logging.debug("debug")
    print(exchange_rate_1*value)
    logging.info("result")
