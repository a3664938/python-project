# conding:utf-8
import requests
import json
class RequestMethod:

    def post_main(self,url,header=None,data=None):
        res=requests.post(url=url,headers=header,json=data).text
        # print(type(res))
        return json.loads(res)
    def get_main(self,url,header=None,data=None):
        res=requests.get(url=url, headers=header,data=data).text
        # print(type(res))
        return json.loads(res) # 将字符串转换为json
    def run_main(self,method,url,header=None,data=None):
        res=None
        if method=='post':
            res=self.post_main(url,header,data)
        else:
            res=self.get_main(url,header,data)
        # print(res)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2) # 将json格式化为字符串


if __name__=='__main__':
    url = 'http://cd.sysdsoft.cn:7309/WorkflowRequest/GetTodoTaskAuthority?taskId=402880727211bdc101723a76d8b41086&userId=744f91cf-927c-4078-a23f-251a2dcea690'
    # data = {"current":1,"pageSize":20,"userID":"744f91cf-927c-4078-a23f-251a2dcea690","page":1}
    header = {
    "Custom-Agent":"WEB",
    "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJVc2VyTmFtZSI6InB0eWgwMyIsIlVzZXJPcmdEdXR5SWQiOiI5MTgwODIxNy05OGNjLTQ5YjUtODIxYi03Y2I1OTliMWM0ODkiLCJTZXNzaW9uS2V5IjoicHR5aDAzXzkxODA4MjE3LTk4Y2MtNDliNS04MjFiLTdjYjU5OWIxYzQ4OSIsIkxvZ2luVGltZSI6IjIwMjAtMDUtMjRUMTI6NDM6MDEuNzU1MjE4MiswODowMCIsIkN1c3RvbUFnZW50IjoiV0VCIiwiVHlwZSI6MH0.ActPN2IDUrjjc6HK5jOzqcvk8xVbgZ07LgZ7xt-AsoE"
}
    run=RequestMethod()
    res=run.run_main("get",url,header,data=None)
    # res1=run.run_main("get","https://www.baidu.com/s?ie=UTF-8&wd=https%E6%B5%8B%E8%AF%95")

    print(res)
