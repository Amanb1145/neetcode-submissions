class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = {}

        for i in strs:
            f = {}

            for item in i:
                if item in f:
                    f[item] = f.get(item, 0) + 1
                else:
                    f[item] = 1

            a = tuple(sorted(f.items()))

            if a in l:
                l[a].append(i)
            else:
                l[a] = [i]

        return list(l.values())