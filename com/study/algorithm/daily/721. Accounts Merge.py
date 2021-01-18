import collections

class UnionFind():
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            if self.rank[parent_y] < self.rank[parent_x]:
                self.parent[parent_y] = parent_x
            elif self.rank[parent_y] > self.rank[parent_x]:
                self.parent[parent_x] = parent_y
            else:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += 1


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_int = {}
        id_to_email = {}
        email_to_name = {}

        num = 0
        for account in accounts:
            name = account[:1][0]
            for email in account[1:]:
                if email not in email_to_int:
                    email_to_int[email] = num
                    id_to_email[num] = email
                    num += 1
                    email_to_name[email] = name

        uf = UnionFind(len(email_to_int))
        for account in accounts:
            first_email = account[1:2][0]
            for other in account[2:]:
                uf.union(email_to_int[first_email], email_to_int[other])

        name_emails = collections.defaultdict(list)
        for email,name in email_to_name.items():
            index = uf.find(email_to_int[email]) #根--》emails
            name_emails[index].append(email)

        res = []
        for index, emails in name_emails.items():
            emails.sort()
            res.append([email_to_name[id_to_email[index]]] + emails)

        return res


import collections

class UnionFind():
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            if self.rank[parent_y] < self.rank[parent_x]:
                self.parent[parent_y] = parent_x
            elif self.rank[parent_y] > self.rank[parent_x]:
                self.parent[parent_x] = parent_x


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_int = {}
        id_to_email = {}
        email_to_name = {}

        num = 0
        for account in accounts:
            name = account[:1][0]
            for email in account[1:]:
                if email not in email_to_int:
                    email_to_int[email] = num
                    id_to_email[num] = email
                    num += 1
                    email_to_name[email] = name

        uf = UnionFind(len(email_to_int))
        for account in accounts:
            first_email = account[1:2][0]
            for other in account[2:]:
                uf.union(email_to_int[first_email], email_to_int[other])

        name_emails = collections.defaultdict(list)
        for email,name in email_to_name.items():
            index = uf.find(email_to_int[email]) #根--》emails
            name_emails[index].append(email)

        res = []
        for index, emails in name_emails.items():
            emails.sort()
            res.append([email_to_name[id_to_email[index]]] + emails)

        return res

if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

    print(Solution().accountsMerge(accounts))


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

    print(Solution().accountsMerge(accounts))
