#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    # Finds the root of a node in this data structure
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)

        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        emailToAccount = {}  # emails => index of account

        # Create disjoint sets
        for i, account in enumerate(accounts):
            for email in account[1:]:  # skip first param which is email
                if email in emailToAccount:
                    # they both have an email in common so they belong to the same person
                    uf.union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i

        emailGroup = defaultdict(list)  # index of account => list of emails
        for email, i in emailToAccount.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)

        result = []
        for i, emails, in emailGroup.items():
            name = accounts[i][0]
            # array concatenation
            result.append([name] + sorted(emailGroup[i]))

        return result
# @lc code=end
