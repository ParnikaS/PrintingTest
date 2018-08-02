import json
import requests
import unittest
from ddt import ddt, unpack, file_data
from Util import UtilClass
import os
import shutil

@ddt
class Test_aPrintMetaApiClass(unittest.TestCase):

    util = UtilClass()
    test_data = util.json_read_data(os.path.abspath('TestData/testPrintMetaApi.json'))
    test_content = util.json_read_data(os.path.abspath('TestData/testPatientContent.json'))


    # @file_data('TestData/testPatientContent.json')
    # @unpack
    # def test_aBlankContent(self, value):
    #     self.generateKey(0,value[0]["input"]["org"])
    #     print(value)
    #     input = value[0]["input"]
    #     print(input)
    #     response =  self.apiCall(input)
    #     assert response == 400
    #
    # def test_bWrongformatcontent(self):
    #     self.generateKey(1)
    #     input = self.test_data["NANAVATI"][1]["input"]
    #     response = self.apiCall()
    #     assert response == 400
    #
    # def test_cCorrectformatWrongOrg(self):
    #     self.generateKey(2)
    #     input = self.test_data["NANAVATI"][2]["input"]
    #     response = self.apiCall()
    #     assert response == 400

    @file_data('TestData/testPatientContent.json')
    @unpack
    def test_dWithCorrectData(self,value):
        #print("in test of metaapi")
        org = value[3]["input"]["org"]
        self.util.generateKey(3,org, self.test_content)
        input = self.test_content[org][3]["input"]
        contentKey = self.test_content[org][3]["input"]["content_key"]
        print(contentKey)
        self.apiCall(input, contentKey, org)

    def apiCall(self, inp, existingKey, org):
        #print("in api call of metaapi")
        api_url = self.test_data["api_printmeta"]
        headers = self.test_data["headers"]
        data = requests.post(url=api_url, data=json.dumps(inp), headers=headers)
        status_code = data.status_code
        if (status_code == 200):
            assert status_code == 200
            testPdfpath = os.path.abspath("TestData/testPDF.pdf")
            if os.path.exists(testPdfpath):
                newName = existingKey+ "_testPDF.pdf"
                dst = os.path.join(os.path.abspath("TestData/files"), newName)
                shutil.copy(testPdfpath, dst)  #copy testpdf with content key to other folder
        else:
            #print("Print Meta API-- "+data.reason)
            return data.reason

if __name__ == '__main__':
    unittest.main()
