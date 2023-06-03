import sqlite3
import requests
import time

while True:
    time.sleep(1800)
    connection = sqlite3.connect("itstep_B.sl3", 5)
    cur = connection.cursor()
    cur.execute("CREATE TABLE w_table (name TEXT);")

    response = requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D1%81%D1%82%D0%B0%D1%80%D1%8B%D0%B9-%D0%BE%D1%81%D0%BA%D0%BE%D0%BB")
    response_text = response.text

    response_parse = response_text.split("<p>")
    for parse_elem_1 in response_parse:
        if parse_elem_1.endswith("°C"):
            for parse_elem_2 in parse_elem_1.split("</p>"):
                if parse_elem_2.endswith("°C") and parse_elem_2[1].isdigit():
                    cur.execute("INSERT INTO w_table (name) VALUES ()", (parse_elem_2))

    response_parse = response_text.split("<p>")
    for parse_elem_1 in response_parse:
       if parse_elem_1.startswith(">"):
            for parse_elem_2 in parse_elem_1.split("</p>"):
                if parse_elem_2.startswith(">") and parse_elem_2[1].isdigit():
                   cur.execute("INSERT INTO w_table (name) VALUES ()", (parse_elem_2))


    connection.commit()
    cur.execute("SELECT rowid, name FROM w_table WHERE rowid=1;")
    cur.execute("SELECT rowid, name FROM w_table WHERE rowid=2;")
    connection.commit()
    res = cur.fetchall()
    print(res)
    connection.close()