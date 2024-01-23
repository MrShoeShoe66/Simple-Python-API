from classes.error import * 

def compErr(errData):
    return {"err":"Server failed to execute your request, please try again later."}

comp = errorClass(500, compErr)