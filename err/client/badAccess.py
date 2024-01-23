from classes.error import errorClass

def compErr(errData):
    return {"err":"Your access was wrong or expired."}

comp = errorClass(403, compErr)