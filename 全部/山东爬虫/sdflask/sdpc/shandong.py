from sdpc.utils import post,hpzldata
import json
def sdcx(hphm,hpzl,fdjh):
    try:
        url = "https://www.sdmsjw.gov.cn:666/h5-webapp/viosurveil/getclwzList.do"
        data = {
        "hphm":hphm,
        "hpzl":hpzldata[hpzl],
        "fdjh":fdjh,
        }
        a = post(url,data=data)
        if a["code"] != 0:
            a = post(url, data=data)
        b = a["data"].decode()
        c = json.loads(b)
        if  c["code"] == 1:
            jsonL = {
                "code": 2,
                "msg": "信息输入有误",
            }
            return json.dumps(jsonL, ensure_ascii=False)
        L = []
        try:
            for i in c["info"]:
                dict = {}
                # dict["cph"] = i[""]  # 车牌号
                dict["youwuwz"] = "有违章记录"
                dict["jffakuan"] = "罚款%s元扣%s" % (i["ysfkje"],i["wfjf"])  # 扣几分罚多少钱
                dict["time1"] = i["wfsj"]  # 违章时间
                dict["site"] = i["wfdz"]  # 违章地址
                dict["miaoshu"] = i["wfsm"]  # 违章描述
                L.append(dict)
            jsonL = {
                "code": 1,
                "msg": "查询成功",
                "data": L,
            }
            return json.dumps(jsonL, ensure_ascii=False)
        except Exception as e:
            dict = {}
            # dict["cph"] = i[""]  # 车牌号
            dict["youwuwz"] = "没有违章记录"
            L.append(dict)
            jsonL = {
                "code": 1,
                "msg": "查询成功",
                "data": L,
            }
            return json.dumps(jsonL, ensure_ascii=False)
    except Exception as e:
        jsonL = {
            "code": 0,
            "msg": "服务器错误",
        }
        return json.dumps(jsonL, ensure_ascii=False)

if __name__ == '__main__':
    hphm = "A8T865"
    hpzl = "小型汽车"
    fdjh = "040336"
    print(sdcx(hphm,hpzl,fdjh))