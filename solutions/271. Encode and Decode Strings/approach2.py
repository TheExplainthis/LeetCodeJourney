from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_result = ''
        for string in strs:
            encoded_result += string.replace('/', '//') + '/:'
        return encoded_result

    def decode(self, s) -> List[str]:
        decoded_list = []
        current_buffer = ""

        index = 0

        while index < len(s):
            if s[index:index + 2] == '/:':
                decoded_list.append(current_buffer)
                current_buffer = ""
                index += 2
            elif s[index:index + 2] == '//':
                current_buffer += '/'
                index += 2
            else:
                current_buffer += s[index]
                index += 1

        return decoded_list
