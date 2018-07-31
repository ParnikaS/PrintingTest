import requests
import unittest
from Util import UtilClass
#from TestPrintMetaApi import Test_aPrintMetaApiClass

class Test_bPrintingApiClass(unittest.TestCase):


    #test_data = Test_aPrintMetaApiClass.test_print_data
    def setUp(self):
        self.util = UtilClass()
        self.test_data = self.util.json_read_data('TestData/testPrintApi.json')
        print(self.test_data)

    # def test_aNoFileSent(self):
    #     response = self.apiCall(0)
    #     assert response == 500

    def test_bCorrectFileSent(self):
        response = self.apiCall()
        assert response == 200


    def apiCall(self):
        api_url = self.test_data["api_printing"]
        #file = open(self.test_data["testPdfPath"] ,'rb')
        print("printing PDF Path------>>>   "+ self.test_data["testPdfPath"])

        files = {'file': open(self.test_data["testPdfPath"] ,'rb')}
        data=requests.post(url=api_url,files=files)
        #files.close()

        if data.status_code == 200:
            print(data.status_code)
            return data.status_code
        else:
            print("Printing API-- "+data.text)
            return data.text