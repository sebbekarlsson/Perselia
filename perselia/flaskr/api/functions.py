def ok(bool):
    return {"ok":bool}

def errors(errors):
    if errors is None:
        return {"errors" : "null"}
    else:
        return {"errors" : [{"error": open(error).read().encode('utf-8')} for error in errors]}