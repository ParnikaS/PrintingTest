import json
import requests
import unittest
from ddt import ddt, unpack, file_data
from Util import UtilClass
import os
from TestPrintingApi import Test_bPrintingApiClass

@ddt
class Test_aPrintMetaApiClass(unittest.TestCase):

    def setUp(self):
        self.util = UtilClass()
        self.test_data = self.util.json_read_data(os.path.abspath('TestData/testPrintMetaApi.json'))
        print(self.test_data)
        self.test_content = self.util.json_read_data(os.path.abspath('TestData/testPatientContent.json'))
        self.test_print_data = self.util.json_read_data('TestData/testPrintApi.json')

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
        input = value[3]["input"]
        contentKey = value[3]["input"]["content_key"]
        self.apiCall(input, contentKey, org)

    def apiCall(self, inp, existingKey, org):
        #print("in api call of metaapi")
        api_url = self.test_data["api_printmeta"]
        headers = self.test_data["headers"]
        data = requests.post(url=api_url, data=json.dumps(inp), headers=headers)
        status_code = data.status_code
        testPdfpath = os.path.abspath(self.test_data["pdfName"])

        if (status_code == 200):
            assert status_code == 200

            path, file = os.path.split(testPdfpath)
            #print(file)
            newName = existingKey+ "_testPDF.pdf"
            new_fullname = os.path.join(path, newName)
            os.rename(testPdfpath, new_fullname)
            #print("new full name---->" +new_fullname)
            self.test_data["pdfName"] = "TestData/"+newName
            self.util.json_write_data(os.path.abspath("TestData/testPrintMetaApi.json"), self.test_data)
            self.prepareDataForPrintApi(new_fullname, org)
        else:
            #print("Print Meta API-- "+data.reason)
            return data.reason


    def prepareDataForPrintApi(self, new_fullname, org):
        #print("in preparation data")
        initialUrl = self.test_print_data["api_printing"]
        self.test_print_data["api_printing"] = initialUrl+org
        self.test_print_data["testPdfPath"] = new_fullname
        self.util.json_write_data(os.path.abspath("TestData/testPrintApi.json"), self.test_print_data)
        self.suite()
        # api_url = initialUrl+org
        # print(api_url)
        # files = {'file': open(new_fullname, 'rb')}
        # data = requests.post(url=api_url, files=files)
        # # files.close()
        # if data.status_code == 200:
        #     print(data.status_code)
        #     assert data.status_code == 200
        # else:
            # print("Printing API-- " + data.text)
        #    return data.text
        # response = self.printapiCall()
        # assert response== 200
        self.suite()
        self.test_print_data["api_printing"] = initialUrl
        self.util.json_write_data(os.path.abspath("TestData/testPrintApi.json"), self.test_print_data)

    def suite(self):
        #from TestPrintingApi import Test_bPrintingApiClass
        suite_loader = unittest.TestLoader()
        suite1 = suite_loader.loadTestsFromTestCase(Test_bPrintingApiClass)
        suite = unittest.TestSuite(suite1)
        unittest.TextTestRunner(verbosity=2).run(suite)


    # def printapiCall(self):
    #     #print("in api call of print api")
    #     api_url = self.test_print_data["api_printing"]
    #     files = {'file': open(self.test_print_data["testPdfPath"] ,'rb')}
    #     data=requests.post(url=api_url,files=files)
    #     #files.close()
    #     if data.status_code == 200:
    #         print(data.status_code)
    #         return data.status_code
    #     else:
    #         print("Printing API-- "+data.text)
    #         return data.text

if __name__ == '__main__':
    unittest.main()
