
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import urllib.request, json
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    profiles =  {
      "Ryan":       "76561198119457693",
      "Murr":       "76561198148333975",
      "Connie":     "76561198064816164",
      "Brendan":    "76561198015196091",
      "Sean":       "76561198067565856",
      "Paul":       "76561198037103618",
      "Darren":     "76561198106283508",
      "Aaron":      "76561198041512627",
      "Tommy":      "76561198119519194",
      "Dennis":     "76561197992177096",
      "Callum":     "76561198100508555",
      "Keane":      "76561198253331818"
    }
    listOfData=[]
    fullList=[]
    for k,v in profiles.items():
        url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?key=FD3CD0C6CE4594E95B645BFD740A0131&appid=730&steamid="+v
        url2 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=FD3CD0C6CE4594E95B645BFD740A0131&appid=730&steamids="+v
        try:
            response = urllib.request.urlopen(url)
            response2 = urllib.request.urlopen(url2)
            data = json.loads(response.read())
            data2 = json.loads(response2.read())
            total_kills = ""
            total_deaths = ""
            total_time_played = ""
            total_planted_bombs = ""
            total_defused_bombs = ""
            total_wins = ""
            total_kills_headshot = ""
            total_mvps = ""

            listOfData.append(data2['response']['players'][0]['avatarmedium'])
            listOfData.append(k)
            listOfData.append(data2['response']['players'][0]['personaname']) #profile name

            for d in data['playerstats']['stats']:
                if d['name'] == "total_kills":
                    total_kills = d['value']
                elif d['name'] == "total_deaths":
                    total_deaths = d['value']
                elif d['name'] == "total_time_played":
                    total_time_played = d['value']
                elif d['name'] == "total_planted_bombs":
                    total_planted_bombs = d['value']
                elif d['name'] == "total_defused_bombs":
                    total_defused_bombs = d['value']
                elif d['name'] == "total_kills_headshot":
                    total_kills_headshot = d['value']
                elif d['name'] == "total_mvps":
                    total_mvps = d['value']

            listOfData.append(total_kills)
            listOfData.append(total_deaths)
            listOfData.append(round(total_kills/total_deaths, 2))
            listOfData.append(round(total_time_played/60/60,2))
            listOfData.append(total_planted_bombs)
            listOfData.append(total_defused_bombs)
            listOfData.append(round(total_kills_headshot/total_kills,2))
            listOfData.append(total_mvps)

            fullList.append(listOfData)
            listOfData=[]
        except urllib.error.HTTPError as e:
            content = e.read()

    return render_template('index.html',result = fullList)
