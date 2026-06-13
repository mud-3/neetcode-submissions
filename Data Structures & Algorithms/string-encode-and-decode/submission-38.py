class Solution:
    # 基於 ASCII 路線的「零漏洞、硬內存裝甲優化版」

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "EMPTY_ARRAY"  # 1. 戰術隔離：用唯一的特殊簽名代表「真正的空列表 []」

        # 每個單詞轉成 ASCII 數字後，即便它是空字串 ""，我們也保持其路由通道不變。
        # 空字串會生成一個空字串，夾在分號之間。
        return ";".join(
            ",".join(str(ord(char)) for char in string) for string in strs
        )

    def decode(self, s: str) -> List[str]:
        if s == "EMPTY_ARRAY":
            return []  # 2. 完美接應：解碼端識別出簽名，精準還原空列表

        decoded = []
        # 🛠️ 核心修正：利用 Python 的 split(';')。
        # 如果 s 是 "" (代表 [""] 轉出來的結果)，split(';') 會精準返回 ['']。
        for word_ascii in s.split(";"):
            if word_ascii == "":
                decoded.append("")  # 3. 邊界解鎖：完美接住 [""] 或者 ["", ""] 等地獄場景！
            else:
                decoded.append(
                    "".join(chr(int(char_code)) for char_code in word_ascii.split(","))
                )

        return decoded