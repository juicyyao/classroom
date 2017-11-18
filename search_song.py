import requests
import pymongo
import re
client=pymongo.MongoClient()
db=client.music163
col_playlists=db.playlists
col_song_id=db.song_id
col_song_lyric=db.song_lyric
def get_playlists_song(id):
    print ('========================playlists:',id,'==========================')
    header={
        'Host':'music.163.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        'Cookie':'_ntes_nnid=2e27d7d29cbd41d9708396b29aa27af6,1503923367666; _ntes_nuid=2e27d7d29cbd41d9708396b29aa27af6; mail_psc_fingerprint=53fca94f3ec3156a90fbc4a5f8364d33; __s_=1; _ngd_tid=7GGHhJ5fiq4t5%2B0R1%2FlGeaAAzNAKromV; P_INFO=juicyyaoo@163.com|1510716887|0|other|00&99|shh&1510713567&carddav#shh&null#10#0#0|&0|urs&mail163|juicyyaoo@163.com; __utma=94650624.1112872772.1503923373.1503923373.1510810806.2; __utmc=94650624; __utmz=94650624.1503923373.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; JSESSIONID-WYYY=uytGJgvf%5Ctf%2B%2BNVrI26Eu7EIsNxodGu%2B7Je1eMHGN8R8EziNl0k7yB9BhH8NsfVwlct%5CW5GfaZldHWf%5C%2Fgmto5%2FWXQEyeht1v%5Cokp%5CWgar3xEKEflIUjdItTRN5Vn4vGNaEd%2BQJpNv7v7uMfo9MzZQ3dDlgsobc1T3nD1c6JlWsKY0%2F2%3A1510917712925; _iuqxldmzr_=32'
    }
    try:

        url_playlists = 'http://music.163.com/api/playlist/detail?id={}&updateTime=-1'.format(id)
        req = requests.get(url_playlists,headers=header)
        data= req.json()
        result_song=data['result']
        tracks=result_song['tracks']
        for j in tracks:
            col_song_id.insert_one(j)
    except Exception as e:
        print (e,id)



def get_lyric(song_id):
    try:
        url = 'http://music.163.com/api/song/lyric?os=pc&id={}&lv=-1&kv=-1&tv=-1'.format(song_id)
        req = requests.get(url)
        data = req.json()
        lrc = data['lrc']
        col_song_lyric.insert_one(lrc)
    except Exception as e:
        print (e,song_id)

headers = {
 'Cookie': 'appver=1.5.0.75771',
 'Referer':'http://music.163.com/'
}
keywords='彩虹'
url_search = 'http://music.163.com/api/search/pc'
data = {'s':keywords,'offset':1,'limit':10,'type':1000}
req = requests.post(url_search,data=data,headers=headers)
content = req.json()
result=content['result']
playlists=result['playlists']
for playlists_id in playlists:
    get_playlists_song(playlists_id['id'])
    for k in col_song_id.find():
        song_id=k['id']
        print('+++++song_name',k['name'],'+++++')
        get_lyric(song_id)









