COLUMNS = ("lot", "day", "expires", "quantity")
KINDS = ("receive", "return", "balance")
PROJECT = {
    "name": "连锁门店退库匹配簿",
    "actor": "门店库存对账员",
    "stages": [
        ("intake", "样例采信"),
        ("prepare", "批号编排"),
        ("calculate", "退货冲配"),
        ("policy", "数量平衡"),
        ("balance", "运行对账"),
    ],
    "chart": "余量分布",
}
