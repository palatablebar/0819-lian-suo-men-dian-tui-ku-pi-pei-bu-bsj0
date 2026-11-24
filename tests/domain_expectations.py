EXPECTED = {
    "0001": (2, 3, "READY"),
    "0002": (1, 0, "READY"),
    "0003": (0, None, "EXPIRED_RETURN"),
    "0004": (2, 36, "INSUFFICIENT_RECEIPT"),
}
EVIDENCE = {
    "0001": {
        "matched": {"000103": {"000101": 6, "000102": 4}},
        "pending": [],
        "remaining": {"000101": 0, "000102": 3},
    },
    "0004": {
        "matched": {},
        "pending": ["000403"],
        "remaining": {"000401": 6, "000402": 30},
    },
}
