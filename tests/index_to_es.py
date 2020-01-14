import datetime
import json
import os
import re

from elasticsearch import Elasticsearch as ES
from elasticsearch import helpers

programs = ["Luna Goff", "Coby Hopper", "Ayman Hodgson", "Veer Wheeler", "Kester Singh", "Faith Read", "Ria Bass", "Rui Huynh", "Nikita Sierra", "Elina Hogg"]


def parse_date(date_str, tz) -> datetime.datetime:
    try:
        date = datetime.datetime.strptime(date_str, "%B %d, %Y %X")
    except ValueError:
        try:
            date = datetime.datetime.strptime(date_str, "%d %B %Y %X.%f")
        except ValueError:
            try:
                date = datetime.datetime.strptime(date_str, "%B %d, %Y %X.%f")
            except ValueError:
                try:
                    date = datetime.datetime.strptime(date_str, "%B %d %Y %X.%f")
                except ValueError:
                    try:
                        date = datetime.datetime.strptime(date_str, "%B %d, %Y %H:%M:??")
                    except ValueError:
                        try:
                            date = datetime.datetime.strptime(date_str, "%d %B %Y %H:%M:??")
                        except ValueError:
                            try:
                                date = datetime.datetime.strptime(date_str, "%B %d, %Y")
                            except ValueError:
                                try:
                                    date = datetime.datetime.strptime(date_str, "%B %Y")
                                except ValueError:
                                    try:
                                        date = datetime.datetime.strptime(date_str, "(original intended date) %B %Y")
                                    except ValueError:
                                        print(date_str)
    return date.replace(microsecond=0).replace(tzinfo=tz)


def parse_tz(tz_str):
    tz_str = tz_str.replace('−', '-')
    offset = float(re.search(r'([0-9-.]+)', tz_str).groups()[0])
    tzname = tz_str.split()[0]
    return datetime.timezone(datetime.timedelta(hours=offset), tzname)


def convert_tons(ton_str):
    try:
        num, unit = ton_str.split()[-2:]
        num = float(num.replace(",", ""))
        unit = unit.lower()
        if unit == "mt":
            num = num * 1000000
        elif unit == "kt":
            num = num * 1000
        return num
    except ValueError:
        return None


def parse_coordinates(loc_str):
    try:
        coord = re.search(r'([0-9.]+°N) ([0-9.]+°[WE])', loc_str).groups()
        lat = float(coord[0][:-2])
        lon = float(coord[1][:-2])
        if coord[1][-1] == "W":
            lon = -1 * lon
        location = {"lat": lat, "lon": lon}
    except AttributeError:
        location = None
    return location


def parse_yield(yield_str):
    if isinstance(yield_str, int):
        y = yield_str * 1000
    elif yield_str.lower() in ["no yield", "unknown yield", 'unknown']:
        y = None
    elif yield_str.lower().endswith('t'):
        y = convert_tons(yield_str)
    elif yield_str.lower().endswith('kg'):
        y = convert_grams(yield_str)
    else:
        y = convert_tons(yield_str.split('[')[0])
    return y


def convert_grams(gram_str):
    num, unit = gram_str.split()
    num = float(num.replace(",", ""))
    unit = unit.lower()
    if unit == "kg":
        num = num * 0.001
    return num


def init_es_index(index_name):
    ES_HOST = 'http://tarski.cs-i.brandeis.edu:9200'
    es = ES(ES_HOST, timeout=30, max_retries=10, retry_on_timeout=True)
    es.indices.delete(index=index_name, ignore=[400, 404])
    mappings = json.load(open(f"{index_name}.mappings"))
    es.indices.create(index_name, body=mappings)
    return es


def read_bombs(datadir):
    for program in os.listdir(datadir):
        for bomb in json.load(open(os.path.join(datadir, program))):
            for key in bomb.keys():
                tz = None
                if 'timezone' in key.replace(' ', '').lower():
                    tz = parse_tz(bomb[key])
                if "date" in key.lower():
                    date = parse_date(bomb[key], tz)
                if "location" in key.lower():
                    location = parse_coordinates(bomb[key])
                if "yield" in key.lower():
                    y = parse_yield(bomb[key])
                if "name" in key.lower():
                    name = bomb[key]
                # program = random.sample(programs, 1)[0]
            yield {'_type': '_doc', '_source': {'year': date.isoformat(),
                                               'location': location,
                                               'yield': y,
                                               'name': name,
                                               'program': program.split('.')[0]
                                               }}


if __name__ == '__main__':
    index_name = 'nuke_tests'
    es = init_es_index(index_name)
    helpers.bulk(es, read_bombs('nuclear_operations_json'), index=index_name)

