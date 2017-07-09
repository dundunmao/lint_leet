# -*- encoding: utf-8 -*-
# Last Modified Date: 2/16/2015
# Add supported of Yahoo Japan Search with English Phrase
# Add supported of Yahoo Japan Search with Japanese Phrase
# Fixed bug in Google Hong Kong Search

import mechanize, pprint
from mechanize._html import MechanizeBs
import pprint
import sys,getopt
import time, datetime
import pdb
import string
import urllib, os, pprint
import urllib2
from bs4 import BeautifulSoup
import html5lib
import codecs

# ################################################################
# return -1, not found
def BD_index(keyword):

    print keyword
    keyword_replace_spaces = string.replace(keyword, ' ', '%20')#####??????????

    url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd='+keyword_replace_spaces+'&rsv_enter=1&rsv_sug3=5&rsv_sug4=745&rsv_sug1=1&rsv_sug2=0&inputT=811'
    url = url.encode('utf8')
    print 'url = ',url

    try:
        response = urllib2.urlopen(url, timeout = 10)
        html = response.read()
    except:
        print 'Bd_index cannot open website, keyword %s'%(keyword)
        return -1

    step = 0

    try:
        # print 'html =', html

        soup = BeautifulSoup(html,'html5lib')
        step = 1
        soup.encode('utf8','ignore')
        # print soup.prettify(encoding = 'utf8')
        div_b = soup.find(id = 'container')
        step = 2
        # print 'div = ', div_b
        result = div_b.find(attrs={'class':'nums'})
        # print 'result = ', result
        step = 3

        num_str = result.contents[1].encode('utf8')
        # print 'num_str = ', num_str
        pre_num =  num_str.split('百度为您找到相关结果约')[1]
        step = 4
        num = pre_num.split('个')[0].replace(',','')
        print 'num = ', num
        return long(num)

    except:
        print 'parsing error, step = %d'%(step)
        return -1

# ################################################################
# return -1, not found
def BD_news(keyword):

    keyword_replace_spaces = string.replace(keyword, ' ', '%20')

    url = 'http://news.baidu.com/ns?cl=2&rn=20&tn=news&word='+keyword_replace_spaces+'&ie=utf-8'
    url = url.encode('utf8')
    print 'url = ',url
    try:
        response = urllib2.urlopen(url, timeout = 10)
        html = response.read()
    except:
		print 'cannot open website'
		return -1

    step = 0
    try:
        #print 'html =', html

        soup = BeautifulSoup(html,'html5lib')
        step = 1
        soup.encode('utf8','ignore')

        # print soup.prettify(encoding = 'utf8')
        #div_g = soup.find(id = 'resultStats')
        div_b = soup.find(id = 'header_top_bar')
        step = 2
        #print 'div = ', div_b
        result = div_b.find(attrs={'class':'nums'})
        #print 'result = ', result
        step = 3

        num_str = result.contents[0].encode('utf8')
        #print 'num_str = ', num_str

        # first try to search '找到相关新闻约',
        # for those with not many news, the search phrase shall be '找到相关新闻'
        parse_str = '找到相关新闻约'

        pre_num_tmp =  num_str.split(parse_str)
        step = 4

        # if len(pre_num_tmp) == 1), it means that it did not find  '找到相关新闻约', try new phrase
        if (len(pre_num_tmp) == 1):
            parse_str = '找到相关新闻'
            pre_num_tmp =  num_str.split(parse_str)

        #print 'pre_num[1]', pre_num_tmp[1]

        step = 5
        pre_num = pre_num_tmp[1]
        num = pre_num.split('篇')[0].replace(',','')
        step = 6
        print 'num = ', num
        return long(num)

    except:
		print 'parsing error, step = %d'%(step)
		return -1

# ################################################################
# Using mechanize to search Google website and Yahoo Japan
# At this moment, it seems that Yahoo Japan does not have news functions.
# supported media:
# mediachannel = 1: www.google.com
# mediachannel = 2: news.google.com
# mediachannel = 3: google.com.hk
# mediachannel = 4: search.yahoo.co.jp
# ################################################################
def gg_yj_search_mechanize(keyword, mediachannel):

    assert((mediachannel <=4) and (mediachannel >= 1))

    br = mechanize.Browser()
    # br.set_all_readonly(False)    # allow everything to be written to
    br.set_handle_robots(False)     # ignore robots
    br.set_handle_refresh(False)    # can sometimes hang without this
    br.set_handle_redirect(True)
    br.set_handle_referer(True)

    # _BL_WARNING_, the following agent is really too old, we shall replace with a newer agent
    # br.addheaders =[('User-agent', 'Firefox')]
    br.addheaders = [('user-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.3) Gecko/20100423 Ubuntu/10.04 (lucid) Firefox/3.6.3')]

    # google search
    if(mediachannel == 1):
        url = "http://www.google.com"
        search_box='q'

    # google news search
    if(mediachannel == 2):
        url = "http://news.google.com"
        search_box='q'

    # google Hong Kong
    if(mediachannel == 3):
        url = "http://www.google.com.hk"
        search_box='q'

    # Yahoo Japan
    if(mediachannel == 4):
        url = "http://search.yahoo.co.jp"
        search_box='p'

    try:
        # response = br.open(url)
        br.open(url)
        # html = response.read() # the text of the page
        # print 'html =', html
        htmll1 = br.response() # get the response again  ###################?????????????????
        # # print 'html1 =', html1 # can apply lxml.html.fromstring()
        # print '======================================================='
        # br.select_form("q") # works when form has a name
        br.select_form(nr=0)
        br.form[search_box] = keyword

        # _BL_DELETE_, for debugging only
        #if (mediachannel == 4):
        #    br.form[search_box] = 'メンター·グラフィックス社'

        response = br.submit()
        response_html = response.get_data()
        #print response_html

        ## In Google search results, the portion will show the number of search results
        ## For some strange reason, I found that the results can be display in two different ways
        ## <div id="resultStats">About 604,000,000 results<nobr>  (0.24 seconds)
        ## or
        ## <div id="resultStats">About 562,000,000 results</div>
        ## Here, we use the 2nd way
        if ((mediachannel == 1) or (mediachannel == 2) or (mediachannel == 3)):
            start_0 = string.find(response_html, 'id=\"resultStats\">')

        if (mediachannel == 4):
            # start_0 = string.find(response_html, 'class=\"resultNum\">')
            start_0 = string.find(response_html, 'で検索した結果')

        #start_1 = string.find(response_html, 'results<nobr>')
        # print '=============== start_0 + 100 %d'%(start_0+100)
        tmp_str = response_html[start_0:(start_0+100)]
        print tmp_str

        if((mediachannel == 1) or (mediachannel == 2)):
            start_2= string.rfind(tmp_str, 'result')

        if(mediachannel == 3):
            start_2 = string.rfind(tmp_str, '項結果')

        if(mediachannel == 4):
            start_2 = string.rfind(tmp_str, '件')


        print "============== start_2 %d"%(start_2)

        num_of_search_results_str = tmp_str[len('id=\"resultStats\">'):start_2]

        # At this step, above string will look "About 4,310"
        if((mediachannel == 1) or (mediachannel == 2)):
            checkAbout = string.find(num_of_search_results_str, 'About')

        # The following code is not reliable, because it is not always same leading characters '約有'
        # _BL_WARNING_
        if(mediachannel == 3):
            checkAbout = string.find(num_of_search_results_str, '約有')

        if(mediachannel == 4):
            checkAbout = string.find(num_of_search_results_str, '約')

        if(checkAbout == -1):
            # Could not find 'About' related word
            print 'WARNING, Can not find About word, %s'%(checkAbout)

        # is there an error ?
        if((mediachannel == 1) or (mediachannel == 2)):

            if(checkAbout != -1):
                # with 'About'
                num_of_search_results_only = num_of_search_results_str[len('About'):len(num_of_search_results_str)]
            else:
                # no 'About'
                num_of_search_results_only = num_of_search_results_str[0:len(num_of_search_results_str)]

        # The following code is not reliable, because it is not always same leading characters '約有'
        # _BL_WARNING_
        if(mediachannel == 3):
            num_of_search_results_only = num_of_search_results_str[len('約有'):len(num_of_search_results_str)]

        # The following code is not reliable, because it is not always same leading characters '約有'
        # _BL_WARNING_
        if(mediachannel == 4):
            num_of_search_results_only = num_of_search_results_str[checkAbout + len('約'):len(num_of_search_results_str)]

        print num_of_search_results_only

        num_of_search_results = num_of_search_results_only.replace(',','')

        print num_of_search_results
        return long(num_of_search_results)

    except:
        print 'Data Error: keyword %s, mediachannel %d'%(keyword, mediachannel)
        return -1


# baidu search unit test, to test a few special combination
def Baidu_Search_unitTest():

    # Test 1: to search something that will NOT be found
    BD_index('somestrangethingsnottofind')

    # Test 2: try double quotation and product name
    BD_index('\"mentor graphics\" pcb')
    BD_index('\"cadence design\" pcb')

    # Test 3: no double quotation, news search
    BD_news('Mentor Graphics')
    BD_news('Glogou')

    # Test 4: test with no product name
    BD_news('\"Mentor Graphics\"')

    #Test 5: news search with double quotation
    BD_news('\"mentor graphics\" pcb')
    BD_news('\"cadence design\" pcb')

# For each vendor in input_file_name, search product_name in supported asia media, and output to output_file_name
# Example: product_name can be 'pcb'
# Note: At this moment, product_name do not include Asian characters, only Alphabet
def Index_Search_All(input_file_name, product_name, output_file_name):

    try:
        in_f = codecs.open(input_file_name, 'r', 'utf-8')
    except:
        print 'read input file error: %s'%(input_file_name)
        sys.exit(0)

    try:
        out_f = codecs.open(output_file_name, 'w', 'utf-8')
    except:
        print 'file creation error: %s'%(output_file_name)
        sys.exit(0)

    # put the title line 1st
    out_str = u'%s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s \t %s\t %s\n'%('english_phrase',
                'chinese_phrase',
                'bd_index_common',
                'bd_index_chinese',
                'bd_news_common',
                'bd_news_chinese',
                'gg_index_common',
                'gg_new',
                'gg_hk',
                'gg_site',
                'bd_site',
                'yj_index_eng',
                'yj_index_jp')

    out_f.write(out_str)
    out_f.flush()

    cnt = 0

    for line in in_f:

        # Try to handle each line
        try:
            # strip off '\r\n' at the end
            line = line.rstrip()

            columns = string.split(line, '\t')

            print '=======before ===='
            print columns
            print '=======after ====='

            english_phrase = columns[1]
            chinese_phrase = columns[2]
            domain_name = columns[3]
            japanese_phrase = columns[4]

            # For most search, we will add product name, add double quotation \" \"
            # For domain search, we will not need do this
            english_phrase = '\"%s\" %s'%(english_phrase, product_name)
            # For Chinese, we will not use double quotation
            chinese_phrase ='%s %s'%(chinese_phrase, product_name)
            #chinese_phrase ='\"%s\" pcb'%(chinese_phrase)

            #site domain search, example: site:mentor.com
            site_domain = 'site:%s'%(domain_name)

            bd_index_common = BD_index(english_phrase)
            bd_index_chinese = BD_index(chinese_phrase)
            bd_news_common = BD_news(english_phrase)
            bd_news_chinese = BD_news(chinese_phrase)
            gg_index_common = gg_yj_search_mechanize(english_phrase, 1)
            gg_new = gg_yj_search_mechanize(english_phrase, 2)
            gg_hk = gg_yj_search_mechanize(english_phrase, 3)
            gg_site = gg_yj_search_mechanize(site_domain, 1)
            bd_site = BD_index(site_domain)

            # For Yahoo Japan search, English phase search
            yj_index_eng = gg_yj_search_mechanize(english_phrase, 4)

            # For Yahoo Japan search, Japanese phase search
            print 'japanese phase: %s'%(japanese_phrase)

            # For the reason, I still do not understand, we have to encode the Japanese phrase,
            # maybe because the file format of Japanese phrases we got
            japanese_phrase_encoded = japanese_phrase.encode('utf-8')
            yj_index_jp = gg_yj_search_mechanize(japanese_phrase_encoded, 4)

            out_str = u'%s \t %s \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %d \t %d\t %d\n' % (english_phrase,
                        chinese_phrase,
                        bd_index_common,
                        bd_index_chinese,
                        bd_news_common,
                        bd_news_chinese,
                        gg_index_common,
                        gg_new,
                        gg_hk,
                        gg_site,
                        bd_site,
                        yj_index_eng,
                        yj_index_jp)

            print out_str

            out_f.write(out_str)
            out_f.flush()

            cnt = cnt + 1

            print 'cnt %d'%(cnt)

        except:
            error_str = 'cnt %d, english_phrase %s'%(cnt, english_phrase)
            print error_str
            continue

    in_f.close()
    out_f.close()

def eda_vendor_data_collection():

    # no japaness
    #input_file_name  ='eda_companies_utf8_v2.txt'
    #output_file_name ='eda_companies_out_pcb_v2.txt'

    #with japaness
    input_file_name  ='eda_companies_with_japanese_utf8.txt'
    output_file_name ='eda_companies_with_japanese_out_pcb_utf8.txt'
    product_name ='pcb'

    Index_Search_All(input_file_name,  product_name, output_file_name )

def csu_mba_data_collection():

    # no japanese
    input_file_name  ='csu_school_utf8.txt'
    output_file_name ='csu_school_out_mba.txt'

    #with japanese
    input_file_name  ='csu_with_japanese_utf8.txt'
    output_file_name ='csu_with_japanese_out_mba_utf8.txt'
    product_name ='mba'

    Index_Search_All(input_file_name,  product_name, output_file_name )

def destination_site_data_collection():

    #no japanese
    #input_file_name  ='travel_destination_utf8.txt'
    #output_file_name ='travel_destination_out_travel.txt'

    #with japanese
    input_file_name  ='travel_destination_with_Japanese_utf8.txt'
    output_file_name ='travel_destination_with_Japanese_out_travel_utf8.txt'
    product_name ='travel'

    Index_Search_All(input_file_name,  product_name, output_file_name )

def earphone_vendor_data_collection():

    #no japanese
    input_file_name  ='earphone_vendors_utf8.txt'
    output_file_name ='earphone_vendors_out_earphone_utf8.txt'

    product_name ='earphone'

    Index_Search_All(input_file_name,  product_name, output_file_name )


def csu_mba_data_collection():

    # no japanese
    input_file_name  ='csu_school_utf8.txt'
    output_file_name ='csu_school_out_mba.txt'

    #with japanese
    input_file_name  ='csu_with_japanese_utf8.txt'
    output_file_name ='csu_with_japanese_out_mba_utf8.txt'
    product_name ='mba'

    Index_Search_All(input_file_name,  product_name, output_file_name )

if __name__ == "__main__":

    # eda_vendor_data_collection()
    # csu_mba_data_collection()
    # destination_site_data_collection()
    earphone_vendor_data_collection()

    #gg_yj_search_mechanize("Mentor Graphics", 1)
    #gg_yj_search_mechanize("Mentor Graphics", 2)
    #gg_yj_search_mechanize("Mentor Graphics", 4)
    #gg_yj_search_mechanize("site:mentor.com", 1)

    #gg_yj_search_mechanize("\"PDF Solutions\" pcb", 2)
    #bd_site = BD_index("site:zuken.com")