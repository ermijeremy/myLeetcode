class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = [''.join(sorted(strs[i])) for i in range(len(strs))]
        ans = {}
        for i in range(len(s)):
            ans[s[i]] = ans.get(s[i],[]) + [i]
        for i in ans.values():
            for k in range(len(i)):
                i[k] = strs[i[k]]
        return [i for i in ans.values()]