import requests
import unittest
import os
from ddt import ddt, unpack, file_data
from Util import UtilClass

@ddt
class Test_bPrintingApiClass(unittest.TestCase):


    util = UtilClass()
    files_with_contentKey = os.listdir(os.path.abspath("TestData/files/"))
    base_url = "http://go-lb-843065005.us-west-2.elb.amazonaws.com/pattern_overlay?token=823a4022952a4bf0b6531ba7f0b8163a43fac451&format=PDF&org_name="

    # @file_data('TestData/testPrintApiContent.json')
    # @unpack
    # def test_bNoFileSent(self,value):
    #     print(value[0])
    #     response = self.apiCall(value,0)
    #     assert response == 500

    @file_data('TestData/testPrintApiContent.json')
    @unpack
    def test_awrongFileSent(self, value):
        org = value[1]["org"]
        filePath = value[1]["filePath"]
        #print(filePath)
        response = self.apiCall(org,filePath)
        assert response == 400

    @file_data('TestData/testPrintApiContent.json')
    @unpack
    def test_cCorrectFileSent(self,value):
        #print(self.files_with_contentKey)
        if self.files_with_contentKey[0].__contains__("NANAVATI") and self.files_with_contentKey[1].__contains__("BLK"):
            test_data = self.util.json_read_data('TestData/testPrintApiContent.json')
            test_data["NANAVATI"][2]["filePath"] = os.path.abspath("TestData/files/")+'/'+self.files_with_contentKey[0]
            test_data["BLK"][2]["filePath"]= os.path.abspath("TestData/files/")+'/'+self.files_with_contentKey[1]
            self.util.json_write_data(os.path.abspath("TestData/testPrintApiContent.json"), test_data)
            # print(test_data)
        org = value[2]["org"]
        filePath = test_data[org][2]["filePath"]
        response = self.apiCall(org,filePath)
        assert response == 200

    def apiCall(self,org,filepath):

        api_url = self.base_url + org
        files = {'file': open(filepath, 'rb')}
        #files = {'file': open(value[inpno]["filePath"], 'rb')}
        #print(api_url)
        data = requests.post(url=api_url, files=files)
        if data.status_code == 200:
            print(data.status_code)
            return data.status_code
        else:
            print(data.text)
            return data.status_code

    @classmethod
    def tearDownClass(cls):
        filelist = cls.files_with_contentKey
        for file in filelist:
            os.remove(os.path.abspath("TestData/files") + "/" + file)

if __name__ == '__main__':
    unittest.main()
