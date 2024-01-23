from classes.error import * 

def compErr(errData):
    return {"err":"You are not allowed to do this."}

comp = errorClass(403, compErr)