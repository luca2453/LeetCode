class Solution:
    def isValid(self, s: str) -> bool:
        lista = []

        openKeys = ["(", "[", "{"]
        closeKeys = [")", "]", "}"]

        for i in s:
            if i in closeKeys and lista == []:
                return False

            if i in openKeys:
                lista.append(i)
            
            if i in closeKeys:
                if openKeys[closeKeys.index(i)] != lista.pop():
                    return False

        return lista == []