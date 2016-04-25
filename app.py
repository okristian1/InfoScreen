    # -*- coding: utf-8 -*-
import os
from flask import Flask, session, render_template
import requests
import json
import sys
from urllib.request import urlopen
import time
import datetime
from datetime import datetime
import codecs




app = Flask(__name__)


@app.route('/')
def tables():
    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {1: 'Amfiet', 2: 'Jacob Roll', 3: 'Olav Tryggvasson', 4: 'Cicignon',
                  5: 'Tordenskjold', 8: 'Thomas Angell', 10: 'Lars Tiller',
                  12: 'Madame Beyer', 13: 'Fru Schøller'}

    meeting = []
    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H.%M', time.gmtime(json_to_standard_start+7200))
                end = time.strftime('%H.%M', time.gmtime(json_to_standard_end+7200))
                if company == "":
                    company = (data[row]['CustomerName'])
                meeting.append({'room':room, 'company':company,'start': start, 'end': end})
            else:
                break

    return render_template('oversikt.html', meeting = meeting[::-1])

@app.route('/cicignon')
def cicignon():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {4: 'Cicignon'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])


                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('cicignon.html', meeting = meetings[::-1])


@app.route('/tordenskjold')
def tordenskjold():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {5: 'Tordenskjold'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])

                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('tordenskjold.html', meeting = meetings[::-1])



@app.route('/jacobroll')
def jacobroll():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {2: 'Jacob Roll'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])

                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('jacobroll.html', meeting = meetings[::-1])


@app.route('/olavtryggvasson')
def olavtryggvasson():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {3: 'Olav Tryggvasson'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])


                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('olavtryggvasson.html', meeting = meetings[::-1])

@app.route('/amfiet')
def amfiet():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {1: 'Amfiet'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])


                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('amfiet.html', meeting = meetings[::-1])

@app.route('/larstiller')
def larstiller():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {10: 'Lars Tiller'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])


                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('larstiller.html', meeting = meetings[::-1])


@app.route('/thomasangell')
def thomasangell():

    meetings = []

    current_time = datetime.now().strftime('%H%M')

    response = urlopen(
    'https://sparbank1.2book.se/simpleIntegration/GetCreaJson?RestaurantId=4&dateTime=' + (
    time.strftime("%Y-%m-%d")))
    reader = codecs.getreader("utf-8")
    data = json.load(reader(response))
    table_dict = {8: 'Thomas Angell'}


    row = -1
    for i in data:
        row += 1
        for i in data[row]['TableNrs']:
            if i in table_dict:
                room = (table_dict.get(i))
                json_to_standard_start = int(data[row]['StartDateTime'][6:16])
                json_to_standard_end = int(data[row]['EndDateTime'][6:16])
                company = (data[row]['Company'])
                start = time.strftime('%H%M', time.localtime(json_to_standard_start))
                starth = time.strftime('%H', time.localtime(json_to_standard_start))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end))
                starth = time.strftime('%H', time.localtime(json_to_standard_start+7200))
                startm = time.strftime('%M', time.localtime(json_to_standard_start))
                startstr = starth + '.' + startm
                end = time.strftime('%H%M', time.localtime(json_to_standard_end))
                endh = time.strftime('%H', time.localtime(json_to_standard_end+7200))
                endm = time.strftime('%M', time.localtime(json_to_standard_end))
                endstr = endh + '.' + endm
                if company == "":
                    company = (data[row]['CustomerName'])


                if int(current_time) > int(start) and int(current_time) < int(end):
                    meetings.append({'company':company,'start': startstr, 'end': endstr})
                else:
                    break
            else:
                break

    return render_template('thomasangell.html', meeting = meetings[::-1])


@app.route('/forside')
def forside():
        return render_template('frontpage.html')



if __name__ == '__main__':

	app.run(host="127.0.0.1", port = 5000, debug = True)
	app.run(host="127.0.0.1", port = 5000)
