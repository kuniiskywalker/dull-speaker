import shlex
import subprocess
 
from datetime import datetime
 
import urllib2
import json
 
CMD_SAY = 'jsay'
 
def main():
    say_datetime()
    say_weather()
    return
 
def say_datetime():
    d = datetime.now()
    text = '%s月%s日、%s時%s分%s秒' % (d.month, d.day, d.hour, d.minute, d.second)
    text = CMD_SAY + ' ' + text
    print(text)
    proc = subprocess.Popen(shlex.split(text))
    proc.communicate()
    return
 
def say_weather():
    city = '130010'; # Tokyo 
    json_url = 'http://weather.livedoor.com/forecast/webservice/json/v1' #API URL
 
    weather_text = u'%sの天気は%sです。'
    temperature_text = u'%sの予想最高気温、%s度、予想最低気温、%s度です。' 
 
    try:
        r = urllib2.urlopen('%s?city=%s' % (json_url, city) )
        obj = json.loads( unicode(r.read()) )
 
        title = obj['title']
        forecasts = obj['forecasts']
      
        # TODAY
        cast = forecasts[0]
        today_w_txt = weather_text % (cast['dateLabel'], cast['telop'])
 
        # TOMMOROW
        cast = forecasts[1]
        temperature = cast['temperature']
        tommorow_w_txt = weather_text % (cast['dateLabel'], cast['telop'])
        tommorow_t_txt = temperature_text % (cast['dateLabel'], temperature['max']['celsius'], temperature['min']['celsius'])
         
        # SAY
        weather_str = title + ' ' + today_w_txt + ' ' + tommorow_w_txt + ' ' + tommorow_t_txt
        weather_str = weather_str.encode('utf-8')
         
        text = '''%s '%s' ''' % (CMD_SAY, weather_str)
        print(text)
        proc = subprocess.Popen(shlex.split(text))
        proc.communicate()
    finally:
        r.close()
 
    return
 
 
### Execute
if __name__ == "__main__":
    main()

