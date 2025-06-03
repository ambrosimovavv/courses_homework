import re
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
import json


def get_href(address:str) -> dict:
    """

    :param address:
    :return: словарь, где ключи 'other_inner_links' -- остальны внутренние ссылки
                                'articles_links' -- ссылки на статьи хабра
                                'outer_links' -- ссылки, ведущие на сторонние сайты
    """
    # 1. будет отправлять запрос на этот сайт
    res = requests.get(address)
    if res.ok:
        # print(res.json())
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.find_all('a')
        other_inner_links = []
        outer_links = []
        articles_links = []
        pattern = re.compile(r'^/ru/articles/\d+/?$') # регулярка, чтобы выделить
        for link in links:
            href = link.get('href')
            link_text = link.get_text()
            # 2. получать с него все ссылки на другие сайты (которые находятся в href-атрибуте html-тэга а)
            if href is not None and href.startswith('http') and 'habr.com' not in urlparse(href).netloc:
                outer_links.append({
                    "href_text": link_text,
                    "href": href
                })
            elif href is not None and pattern.match(href):
                articles_links.append({
                    "href_text": link_text,
                    "href": href
                })
            else:
                other_inner_links.append({
                    "href_text": link_text,
                    "href": href
                })
        #print(inner_link)
        # output_json = json.dumps({'other_inner_links': other_inner_links,
        #                           'articles_links': articles_links,
        #                           'outer_links': outer_links},
        #                          ensure_ascii=False, indent=2)
        output_json = {'other_inner_links': other_inner_links,
                                   'articles_links': articles_links,
                                   'outer_links': outer_links}
    else:
        output_json = json.dumps({"message": "null"})
        print("Error: ", res.text)
    return output_json

if __name__ == '__main__':
    query ='django'
    # 0. Выбрать любой сайт на котором есть хотя бы одна ссылка на другие сайты (html-тэг a)
    address = f'https://habr.com/ru/search/?q={query}'
    input_json = get_href(address)
    # 3. выводить полученные ссылки в терминал
    print(f"Внешние ссылки: \n{json.dumps(input_json['outer_links'], ensure_ascii=False, indent=2)}")
    print("ссылки на статьи")
    main_addr = 'https://habr.com'
    for link in input_json['articles_links']:
        address = main_addr+link['href']
        new_links = get_href(address)
        print(f"Внешние ссылки: \n{json.dumps(new_links['outer_links'], ensure_ascii=False, indent=2)}")


