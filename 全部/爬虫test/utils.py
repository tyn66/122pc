import requests

#todo  封装后的requests的get与post方法
#http是无状态的，封装的方法仅用于一次请求，无法保存cookie
def get(url, params=None, headers=None, cookies=None, proxies=None, verfiy=None, timeout=10):
    '''
    此方法用于get请求
    :param url: url地址
    :param params: ？&符号后面的参数，说白，url路由参数
    :param headers: 请求头信息
    :param cookies: 请求的cookie
    :param proxies: 请求的代理ip
    :param verfiy: 请求时是否认证https
    :param timeout: 请求网络超时
    :return:
    '''
    s = requests.session()
    ret = {}
    ret["code"] = 0
    try:
        if params != None:
            s.params = params
        if headers != None:
            s.headers = headers
        if cookies != None:
            s.cookies = cookies
        if verfiy != None:
            s.verfiy = verfiy
        if proxies != None:
            s.proxies = proxies
        r = s.get(url=url, timeout=timeout)
        if r != None:
            ret["code"] = 1
            ret["data"] = r.content
            return ret
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()
    return ret


def post(url, data, params=None, headers=None, cookies=None, proxies=None, verfiy=None, timeout=20):
    s = requests.session()
    ret = {}
    ret["code"] = 0
    try:
        if params != None:
            s.params = params
        if headers != None:
            s.headers = headers
        if cookies != None:
            s.cookies = cookies
        if verfiy != None:
            s.verfiy = verfiy
        if proxies != None:
            s.proxies = proxies

        r = s.post(url=url, data=data, timeout=timeout)
        if r != None:
            ret["code"] = 1
            ret["data"] = r.content
            return ret
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()
    return ret
