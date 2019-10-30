import time
import json
from selenium import webdriver
from scrapy.selector import Selector
from collections import OrderedDict
from multiprocessing import Pool
import time
# 테서렉트에서 받은 이미지 인식 결과 Json형태의 String을 받는 변수


def searchWord(keywordData):
    start_time = time.time()
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1920x1080')
    # options.add_argument("disable-gpu")

    searchKeyword=[]
    #searchKeyword=keywordData.split("\n")
    searchKeyword.append(keywordData.replace("\n"," "))
    driver = webdriver.Chrome(chrome_options=options)

    meanList = []
    keywordData = OrderedDict()
    print(searchKeyword)
    for n in searchKeyword:
        try:

            driver.get("https://translate.google.co.kr/?hl=ko#view=home&op=translate&sl=auto&tl=ko&text=")

            driver.find_element_by_xpath('//*[@id="source"]').send_keys(n)
            time.sleep(0.5)

            html = driver.page_source
            # 페이지의 elements모두 가져오기
            selector = Selector(text=html)

            wordMean = " ".join(selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/*/text()').extract())
            keywordData[n]=wordMean
            meanList.append(wordMean)

        except IndexError:
            try:
                wordMean = " ".join( selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/*/text()')[0].extract())
                keywordData[n] = wordMean
                meanList.append(wordMean)
            except IndexError:
                keywordData[n] = "검색된 결과 없음"

    driver.close()
    print("--- %s seconds ---" % (time.time() - start_time))
    return json.dumps(keywordData, ensure_ascii=False, indent="\t").encode("utf-8")



