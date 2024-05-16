import random
import os

from . import base

from ..classes.xmlaxmllib import XmlaXmlLib

def createuser(user):
    u = {}
    u["email"] = user["email"]
    u["id"] = random.randint(1000000, 9999999)
    userxmlstr = XmlaXmlLib.object_to_xmlstr(u, "user")
    XmlaXmlLib.writefile(base.userspath + str(u["id"]) + ".xml", userxmlstr)
    return u

def getuser(email):    
    for file in os.listdir(base.userspath):
        if ".xml" in file:            
            xmlfile = XmlaXmlLib.xmlfile(base.userspath + file)            
            u = XmlaXmlLib.xml_to_dict(xmlfile, "user")
            if u["email"] == email:
                return u 
    return False           
