import random
import os

from . import base

from ..classes.xmlib import XmlLib

def createuser(user):
    u = {}
    u["email"] = user["email"]
    u["phone"] = user["phone"]
    u["comment"] = user["comment"]
    u["name"] = user["name"]
    u["id"] = random.randint(1000000, 9999999)
    userxmlstr = XmlLib.object_to_xmlstr(u, "user")
    XmlLib.writefile(base.feedback + str(u["id"]) + ".xml", userxmlstr)
    return u

def getuser(email):    
    for file in os.listdir(base.feedback):
        if ".xml" in file:            
            xmlfile = XmlLib.xmlfile(base.feedback + file)            
            u = XmlLib.xml_to_dict(xmlfile, "user")
            if u["email"] == email:
                return u 
    return False     

def comments():
    users = []
    for file in os.listdir(base.feedback):
        if ".xml" in file:            
            xmlfile = XmlLib.xmlfile(base.feedback + file)            
            u = XmlLib.xml_to_dict(xmlfile, "user")
            users.append(u)

    res = []
    for u in users:
        comment = {"name": u["name"], "comment": u["comment"]}
        res.append(comment)
    return res         
