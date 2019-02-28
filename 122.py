from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PIL import Image
from utils.utils import hpzl,city
import time,re,os,json

def pachong(cph,fdj,cllx):
    dict = {}
    driver = webdriver.Chrome()
    try:
        cph1 = cph[1:]
        city1 = cph[0]
        city2 = city[city1]
        url = "https://%s.122.gov.cn/views/inquiry.html" % city2
        hpzl1 = hpzl[cllx]
        driver.get(url=url)
        driver.find_element_by_xpath(hpzl1).click()
        driver.find_element_by_id("hphm1-b").send_keys(cph1)
        driver.find_element_by_id("wffdjh").send_keys(fdj)
        time.sleep(2)
        driver.find_element_by_name("captcha").click()
        time.sleep(1)
        if jietu(driver,cph) == 0:
            driver.close()
            dict["cph"] = cph
            dict["msg"] = "服务器错误"
            jsonL = {
                "code": 0,
                "data": dict,
            }
            return json.dumps(jsonL, ensure_ascii=False)
        else:
            captcha = input("请输入验证码:")
            driver.find_element_by_name("captcha").send_keys(captcha)
            driver.find_element_by_name("captcha").send_keys(Keys.ENTER)
            handles = driver.window_handles
            driver.switch_to.window(driver.window_handles[len(handles) - 1])
            time.sleep(1)
            c = driver.page_source.replace('\n', '').replace('\r', '').replace('\t', '')
            # print(c)
            d = re.findall('class="bluedi".*?该(.*?)</div>',c)
            if d == "机动车没有非现场违法未处理记录。 ":
                os.remove("%s.png" % (cph))
                driver.close()
                dict["cph"] = cph
                dict["msg"] = d
                jsonL = {
                    "code": 1,
                    "data": dict,
                }
                return json.dumps(jsonL, ensure_ascii=False)
            else:
                d = re.findall('class="bluedi".*?该(.*?)查看本人',c)
                os.remove("%s.png" % (cph))
                driver.close()
                dict["cph"] = cph
                dict["msg"] = d
                jsonL = {
                    "code": 1,
                    "data": dict,
                }
                return json.dumps(jsonL, ensure_ascii=False)
    except Exception as e:
        try:
            a1 = driver.switch_to.alert
            # print(a1.text)
            if a1.text == "图片验证码输入错误":
                driver.close()
                dict["cph"] = cph
                dict["msg"] = "图片验证码输入错误"
                jsonL = {
                    "code": -1,
                    "data": dict,
                }
                return json.dumps(jsonL, ensure_ascii=False)
            else:
                os.remove("%s.png" % (cph))
                driver.close()
                dict["cph"] = cph
                dict["msg"] = "根据您提交的信息，无法查询到违法记录。请核实您提交的信息是否准确。"
                jsonL = {
                    "code": -1,
                    "data": dict,
                }
                return json.dumps(jsonL, ensure_ascii=False)
        except Exception as e:
            os.remove("%s.png" % (cph))
            dict["cph"] = cph
            dict["msg"] = "服务器错误"
            jsonL = {
                "code": 0,
                "data": dict,
            }
            return json.dumps(jsonL, ensure_ascii=False)


def jietu(driver,cph):
    try:
        b = "%s.png"%(cph)
        handles = driver.window_handles
        driver.switch_to.window(driver.window_handles[len(handles)-1])
        driver.save_screenshot(b)
        imgelement = driver.find_element_by_xpath('//*[@id="queryWF"]/div[4]/div/span/img')  # 定位验证码
        location = imgelement.location  # 获取验证码x,y轴坐标
        size = imgelement.size  # 获取验证码的长宽
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y'] + size['height']))  # 写成我们需要截取的位置坐标
        i = Image.open(b)  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(b) # 保存我们接下来的验证码图片 进行打码
        code = 1
        return code
        # print(cph)
    except Exception as e:
        # print(e)
        code = 0
        return code

if __name__ == '__main__':
    while True:
        cph = "鲁A8T865"
        fdj = "040336"
        # cph = "鲁FD015J"
        # fdj = "319864"
        cllx = "小型汽车"
        print(pachong(cph,fdj,cllx))
        time.sleep(10)
