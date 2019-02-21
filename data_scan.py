# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:52:18 2019

@author: Dell
"""

import json
import re
import time 
from jieba.analyse import *
from jieba.analyse import extract_tags

with open("issues_parsed.json",'r',encoding='utf-8') as f:
    for line in f:
        content=json.loads(line)
        docnum=content['docNum']
        caseType=content['caseType']
        trialLevel=content['trialLevel']
        docType=content['docType']
        url=content['url']
        fact=content['fact']
        defender=content['defender']
        issues=content['issues']
        defender_s= ''.join(defender)
        if(len(defender_s)!=0):
            fw=open("defender_notnull.txt",'a',encoding='utf-8')
            fw.write(defender_s)
            fw.close()
    f.close()