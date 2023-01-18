import json
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

def ToBase64(file):
    with open(file,'rb') as fileObj:
        audio_data = fileObj.read()
        base64_data = base64.b64encode(audio_data)
        result = base64_data.decode()
    return result

# 从文件读取秘钥
def getSecret(Path):
    file = open(Path,'r')
    ID = file.readline().strip()
    Key = file.readline()
    file.close()
    return ID,Key

secretPath = "./CloudKey.txt"
SecretID, SecretKey = getSecret(secretPath)

import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models

def run(file64):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential(SecretID, SecretKey)
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "ocr.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = ocr_client.OcrClient(cred, "ap-beijing", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.GeneralFastOCRRequest()
        params = {
            "ImageBase64":file64
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个GeneralFastOCRResponse的实例，与请求对象对应
        resp = client.GeneralFastOCR(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())
        resultString = resp.to_json_string()
        resultDict = json.loads(resultString)
        content = ''
        for i in resultDict['TextDetections']:
            temp = i['DetectedText']
            content = content+ temp
        print(content)
        fout = open("./res.txt",'w')
        fout.write(content+"\n")
        fout.close()
        

    except TencentCloudSDKException as err:
        print(err)

file = "./ocrTarget.jpg"

file64 = ToBase64(file)
run(file64)
