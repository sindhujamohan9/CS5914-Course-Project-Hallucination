import os
import json


"""
IO Utils
"""


class PlainTextLoader():
    """
    Load plain text in "./data/wiki_plaintext"
    """
    def __init__(self, plainTextDir):
        self.plainTextDir = plainTextDir
        self.fileNameList = self.getFileNameList(plainTextDir)

    def getFileNameList(self, plainTextDir):
        """
        Get file name list
        """
        fileNameList = []
        for file in os.listdir(plainTextDir):
            if file.endswith('.json'):
                fileNameList.append(file)
        return fileNameList

    def loadJson(self, filePath):
        """
        Load json file
        """
        with open(filePath, 'r') as f:
            plainText = json.load(f)['text']

            return plainText


class GroundTruthLoader():
    """
    Load plain text in "./outputs/wiki_qa"
    """
    def __init__(self, groundTruthDir):
        self.groundTruthDir = groundTruthDir
        self.fileNameList = self.getFileNameList(groundTruthDir)

    def getFileNameList(self, groundTruthDir):
        """
        Get file name list
        """
        fileNameList = []
        for file in os.listdir(groundTruthDir):
            if file.endswith('.json'):
                fileNameList.append(file)
        return fileNameList

    def loadJson(self, filePath):
        """
        Load json file
        """
        with open(filePath, 'r') as f:
            data = json.load(f)
            return data


class QAPairLoader():
    """
    Load plain text in "./outputs/wiki_response"
    """
    def __init__(self, QADataDir):
        self.QADataDir = QADataDir
        self.fileNameList = self.getFileNameList(QADataDir)

    def getFileNameList(self, QADataDir):
        """
        Get file name list
        """
        fileNameList = []
        for file in os.listdir(QADataDir):
            if file.endswith('.json'):
                fileNameList.append(file)
        return fileNameList

    def loadJson(self, filePath):
        """
        Load json file
        """
        with open(filePath, 'r') as f:
            data = json.load(f)
            return data


