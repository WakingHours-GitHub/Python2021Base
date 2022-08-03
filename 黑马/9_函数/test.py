import os
import shutil
import datetime


# from jsonToWxid  import JsonToWxid
# from wxidToQrcode import WxidToQrcode

class Run():
    def __init__(self, jsonFile, wxidFile, qrcodePath):

        self.jsonFile = jsonFile
    self.wxidFile = wxidFile
    self.qrcodePath = qrcodePath

    def main(self):

        jtw = JsonToWxid(self.jsonFile, self.wxidFile)
        coding = jtw.get_encoding(self.jsonFile)
        print(coding)
        wxlist = jtw.loadJsonFile(coding)
        jtw.wxidsToFile(wxlist)
        wti = WxidToQrcode(self.wxidFile, self.qrcodePath)
        wti.createQrcode()

jf = "原始的文件"
sf = "完成的文件"
wf = "提取的wxid"
qf = "生成的二维码"

current_url = os.getcwd()
fileList = os.listdir(current_url + "/" + jf)
for jsonfile in fileList:
    now_time = datetime.datetime.now()
time = datetime.datetime.strftime(now_time, '%Y%m%d')
print("================================" + jsonfile + "==================================")
jsonFile = current_url + '/' + jf + '/' + jsonfile
filename = os.path.splitext(jsonfile)
wxidFile = current_url + '/' + wf + '/' + filename[0] + '__' + time + '.txt'
qrcodePath = current_url + '/' + qf + '/' + filename[0] + '__' + time + '/'
isexit = os.path.exists(qrcodePath)
if (not isexit):
    os.mkdir(qrcodePath)
run = Run(jsonFile, wxidFile, qrcodePath)
run.main()
success_url = current_url + '/' + sf + '/' + filename[0] + '__' + time + '.json'
shutil.move(jsonFile, success_url)
