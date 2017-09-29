# We take in the min amount for the requester and max amount for the responder

def payment(reqAmt, resAmt):
    if (reqAmt >= resAmt):
        return (reqAmt-resAmt)/reqAmt
    else:
        return 0
