# We take in the min amount for the requester and max amount for the responder

def pay(reqAmt, resAmt):
    if (reqAmt >= resAmt):
        return (reqAmt-resAmt)/reqAmt
    else:
        return 0
