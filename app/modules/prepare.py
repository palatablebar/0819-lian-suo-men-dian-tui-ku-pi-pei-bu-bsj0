from app.business import DomainIssue, by_kind, prepared, single


def prepare(rows):
    receives = sorted(by_kind(rows, "receive"), key=lambda r: (r["day"], r["record"]))
    returns = sorted(by_kind(rows, "return"), key=lambda r: (r["day"], r["record"]))
    if any(r["day"] >= r["expires"] for r in returns):
        raise DomainIssue("EXPIRED_RETURN")
    if any(r["day"] >= r["expires"] or not r["quantity"] for r in receives):
        raise DomainIssue("RECEIPT_CONTRACT")
    return prepared(
        len(receives),
        {"return_lines": len(returns)},
        (receives, returns, single(rows, "balance")["quantity"]),
    )
