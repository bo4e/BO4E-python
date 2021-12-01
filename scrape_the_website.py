from os.path import exists
from typing import List

import requests as requests
from bs4 import BeautifulSoup

ENUM_CODE_TEMPLATE = f'''
# pylint: disable=missing-module-docstring
from bo4e.enum.strenum import StrEnum
class {{enum_class_name}}(StrEnum):
    """
    {{enum_class_docstring}}
    """
{{enum_members}}
'''

doc_main_html = requests.get("https://www.bo4e.de/dokumentation").text
doc_main_soup = BeautifulSoup(doc_main_html, "html.parser")
enum_urls: List[str] = [a.attrs["href"] for a in doc_main_soup.find_all("a") if a.text.startswith("ENUM")]
for enum_url in enum_urls:
    html_doc = requests.get(enum_url).text
    soup = BeautifulSoup(html_doc, "html.parser")
    enum_class_name = soup.find("h2").text.split(" ")[-1]
    relevant_div = soup.find("div", attrs={"class": "large-12 column"})
    python_file_path = "src/bo4e/enum/" + enum_class_name.lower() + ".py"
    if exists(python_file_path):
        continue
    try:
        enum_class_docstring = relevant_div.find("p").text
    except AttributeError:
        # bdew artikelnummer, arithmetische operation
        # scheiss CMS, es gibt nicht immer nen paragraph
        enum_class_docstring = relevant_div.text.split(".")[0].strip()
    table_rows = relevant_div.find("tbody").findAll("tr")
    enum_member_codes: List[str] = []
    for table_row in table_rows:
        row_cells = list(table_row.find_all("td"))
        if len(row_cells) == 0:
            continue  # probably the <th> row
        enum_member_name = row_cells[0].text
        enum_member_doc = row_cells[-1].text
        enum_member_codes.append(f"    {enum_member_name} #: {enum_member_doc}")
    replacement_dict = {
        "enum_class_name": enum_class_name,
        "enum_class_docstring": enum_class_docstring,
        "enum_members": "\n".join(enum_member_codes),
    }
    enum_code = ENUM_CODE_TEMPLATE.format(**replacement_dict)
    with open(python_file_path, "w", encoding="utf-8") as enum_code_file:
        enum_code_file.write(enum_code)
