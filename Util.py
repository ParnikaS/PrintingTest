import json
import datetime
import calendar
import os


class UtilClass():

    def json_read_data(self, jsonfile):
        with open(jsonfile, 'r') as file:
            dataset = json.load(file)
            file.close()
            return dataset

    def json_write_data(self, jsonfile, data):
        with open(jsonfile, 'w') as file:
            file.write(json.dumps(data))
            file.close()

    def generateKey(self,inpno,org,test_content):
        date = datetime.datetime.now()
        content_Key = calendar.timegm(date.utctimetuple())
        test_content[org][inpno]["input"]["content_key"] = str(content_Key)+org
        print("Content key---->   " + test_content[org][inpno]["input"]["content_key"])
        self.json_write_data(os.path.abspath("TestData/testPatientContent.json"), test_content)


