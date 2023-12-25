from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return 'π'.join(strs)
        

    def decode(self, s: str) -> List[str]:
        return s.split('π')
