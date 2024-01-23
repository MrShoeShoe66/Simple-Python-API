from classes.error import * 

def compErr(errData):
    return {"err":"Your access was wrong or expired."}

comp = errorClass(502, compErr)