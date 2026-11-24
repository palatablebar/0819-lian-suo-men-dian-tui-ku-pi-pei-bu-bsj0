from app.business import measured


def compute(data):
    receipts, returns, target = data
    balances = {r["record"]: r["quantity"] for r in receipts}
    unresolved = []
    matches = {}
    for row in returns:
        eligible = [
            r["record"]
            for r in receipts
            if r["lot"] == row["lot"]
            and r["expires"] == row["expires"]
            and r["day"] <= row["day"]
        ]
        amount = row["quantity"]
        if sum(balances[k] for k in eligible) < amount:
            unresolved.append(row["record"])
            continue
        for k in eligible:
            applied = min(balances[k], amount)
            if applied:
                balances[k] -= applied
                amount -= applied
                matches.setdefault(row["record"], {})[k] = applied
            if not amount:
                break
    return measured(
        sum(balances.values()),
        target,
        "件",
        {"matched": matches, "pending": unresolved, "remaining": balances},
        bool(unresolved),
    )
