from classes.error import * 

def compErr(errData):
    return {"err":"The requested resource was not found."}

comp = errorClass(404, compErr)