from app.business import decision


def policy(result):
    return decision(result, "INSUFFICIENT_RECEIPT" if result["flag"] else None)
