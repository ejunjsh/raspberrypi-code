# -*- coding: utf-8 -*-
import os
import requests
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

def getWeatherText():
    try:
        response = requests.get(
            "http://www.tuling123.com/openapi/api?key=652ae4a714794fe6b01faa990d7a981f&info=%s" % "广州今日天气")
        json = response.json()
        if json["code"] == 100000:
            return json["text"]
        else:
            return ""
    except:
        return ""


def text2voice(text):
    url = 'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_' \
          'demo&cod=2&lan=zh&ctp=1&pdt=1&spd=4&per=4&vol=5&pit=5'.format(text)
    # 直接播放语音
    os.system('mplayer "%s"' % url)


def playMusic(path):
    os.system('mplayer %s' % path)


if __name__ == '__main__':

    text = getWeatherText()
    if text != "":
        playMusic(os.path.join(os.path.dirname(__file__), 'music.mp3'))
        text2voice(text)
    else:
        playMusic(os.path.join(os.path.dirname(__file__), 'music.mp3'))
