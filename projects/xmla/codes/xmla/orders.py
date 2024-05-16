import os.path
import os
import shutil
import random

from . import base

def do(opts):
    if 'orderid' in opts:
        return decline(opts["ids"], opts["userid"], opts["orderid"])
    else:
        return make(opts["ids"], opts["userid"])

def make(ids, userId):
    opts = {}
    opts["userid"] = userId
    products = ids.split("-")
    opts["orderid"] = str(random.sample(range(100000, 999999), 1)[0])
    full = True
    for product in products:
        full = full and orderProduct(product, opts)
    if (full):
        return opts["orderid"]
    else:
        return False

def decline(ids, userId, orderId):
    opts = {}
    opts["userid"] = userId
    opts["orderid"] = orderId
    opts["products"] = []
    pathorder = base.orderspath + str(opts["userid"]) + "/" + str(opts["orderid"]) + "/"
    for file in os.listdir(pathorder):
        opts["products"].append(os.path.basename(file))
    cancelOrder(opts)
    return opts["orderid"]

def orderProduct(id, opts):
    file = id + ".xml"
    if (os.path.isfile(base.productspath + file)):
        moveToOrder(file, opts)
        return True
    else:
        return False

def cancelOrder(opts):
    pathorder = base.orderspath + str(opts["userid"]) + "/" + str(opts["orderid"]) + "/"

    for file in opts["products"]:
        if os.path.isfile(pathorder + file):
            moveBack(pathorder, file)

def moveToOrder(file, opts):
    pathuser = base.orderspath + str(opts["userid"]) + "/"
    pathorder = base.orderspath + str(opts["userid"]) + "/" + str(opts["orderid"]) + "/"

    if (os.path.isdir(pathuser)):
        if (os.path.isdir(pathorder)):
            moveToOrderOs(file, pathorder)
        else:
            os.mkdir(pathorder)
            moveToOrderOs(file, pathorder)
    else:
        os.mkdir(pathuser)
        os.mkdir(pathorder)
        moveToOrderOs(file, pathorder)

def moveToOrderOs(file, pathorder):
    shutil.move(base.productspath + file, pathorder + file)

def moveBack(pathorder, file):
    pathproduct = base.productspath + file
    pathorder = pathorder + file
    shutil.move(pathorder, pathproduct)
