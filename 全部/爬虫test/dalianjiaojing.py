from utils import post,get
import re,time
# b = {"requestType": "wei502_checkcarinfo", "para": {"CarType": "02", "CarNum": "辽B72XF2", "CarCode": "9397"}}
def dalianpachong():
    try:
        CarType = "02"
        CarNum = "BB22Y0"
        CarCode = "2853"
        url = 'http://weixin.dlutc.gov.cn/weixin_trunk/WeiXin/wei501.php?openid=oA2-lv6lIvhvzEn2YIISY_K14_cs&cartype=' + CarType + '&carnum=%E8%BE%BD' + CarNum + '&carcode=' + CarCode
        # print(url)
        time1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(time1)
        a = get(url)
        if a["code"] == 0:
            time2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            print(time2)
            a = get(url)
        # print(a["data"].decode())
        b = a["data"].decode().replace('\n', '').replace('\t', '').replace('\r', '')
        c = re.findall('<font color="#FF9900">(.*?)</font>  笔',b)
        L = []
        if int(c[0]) != 0 :
            d = re.findall('class="weui_cell_bd weui_cell_primary.*?<p>(.*?)</p>.*?扣(.*?)</p>.*?罚款金额.*?<p>¥(.*?)</p>.*?违法地点：(.*?)</p>.*?违法行为(.*?)</p>',b)
            # print(d)
            for i in d:
                dict = {}
                dict["jffakuan"] = "罚款%s元扣%s" % (i[2], i[1])  # 扣几分罚多少钱
                dict["time1"] = i[0]  # 违章时间
                dict["site"] = i[3]  # 违章地址
                dict["miaoshu"] = i[4]  # 违章描述
                L.append(dict)
            return L
        else:
            print(0)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    while True:
        print(dalianpachong())