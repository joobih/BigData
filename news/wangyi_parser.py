#!/usr/bin/env python
# coding=utf-8

from datetime import datetime
from bs4 import BeautifulSoup

#解析网易新闻网页
class WangYiParser(object):
    def __init__(self):
        pass

    #解析新闻正文页面，返回字典：
    """
        #解析新闻页面
        {
            "time":"2017-01-11 15:02:52",                               #发表时间
            "title":"沪指震荡走低重心下挫跌0.79% 石油板块尾盘下行",     #标题
            "from":"网易财经",                                          #来源
            "text":"网易财经1月11日讯 股指早盘小幅低开......",          #正文部分
            "pictures":{
                "1":"http://quotes.money.163.com/0000001.html#13a03",   #正文中的图片地址
                "2":"second_pic url"
            }
            "editor":"王宏贵_NF7326",                                   #责任编辑
            "parser_time":"2017-01-11 20:57:00"                           #解析时间
        }
    """
    def news_page_parser(self, html):
        bs = BeautifulSoup(html, "html.parser")
        div = bs.find_all("div", id="epContentLeft")[0]

        #清楚div中的style,script标签和不需要的广告div 标签等
        style_div = div.find_all("style")
        for items in style_div:
            items.decompose()
        script_div = div.find_all("script")
        for items in script_div:
            items.decompose()
        div_b = div.find_all("div", id="js_qrcode_btm")
        if div_b:
            div_b[0].decompose()
        caijing_bq_div = div.find_all("div", attrs={"class":"caijing_bq"})[0]
        caijing_bq_div.decompose()
        other_div = div.find_all("div", attrs={"class":"gg200x300"})[0]
        other_div.decompose()
        result = {}
        #获取新闻标题
        h1_div = div.find_all("h1")[0]
        title = h1_div.text
        result["title"] = title

        #获取新闻来源
        time_div = div.find_all("div", attrs={"class":"post_time_source"})[0]
        from_div = time_div.find_all("a", id="ne_article_source")
        from_text = from_div[0].text
        result["from"] = from_text
        for items in from_div:
            items.decompose()
        print time_div,"time_div"

        #获取新闻发表时间
        time_div_text = time_div.text
        time_text = time_div_text.strip()
        a = time_text.find(u"来源")
        time_text = time_text[:a]
        print time_div_text,"time_div_text"
        result["time"] = time_text

        #获取新闻正文内容
        p_divs = div.find_all("p")
        text = ""
        for p in p_divs:
            p_text = p.text
            text += p_text.strip()
        result["text"] = text

        #获取新闻中的图片地址
        pic_div = div.find_all("img")
        pic_dict = {}
        for i, p in enumerate(pic_div):
            src = p.attrs["src"]
            pic_dict[str(i)] = src
        result["pictures"] = pic_dict

        #获取新闻的编辑者
        div_a = div.find_all("div",attrs = {"class":"ep-source cDGray"})[0]
        span_a = div_a.find_all("span",attrs = {"class":"ep-editor"})[0]
        editor = span_a.text.strip()
        b = editor.find(u"：")
        editor = editor[b+1:]
        result["editor"] = editor

        #取得系统当前时间
        make_time = datetime.now()
        make_time = str(make_time)
        result["make_time"] = make_time

        return result

