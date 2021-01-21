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

#思路:邮箱是独一无二的。相同的邮箱代表着相同的人
# 思路：1.同一账户下，不用邮箱合并 2.不用账户下，邮箱合并 3.因为之前合并了邮箱，所有此刻 各个连通分量已经确定。仅需要输出就行

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
        #建立邮箱的唯一标识
        #邮箱与人名的对应。主要是解决后期按照人名输出邮箱
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
                #合并邮箱。如果该账户下仅有一个邮箱，不会进入这里因为邮箱的唯一标识已经确认完毕。
                #技术遇到 name1:[e@e, a@a] name2:[e@e], name3:[a@a], name4:[e@e, d@d].已经进行了连通处理
                uf.union(email_to_int[first_email], email_to_int[other])

        name_emails = collections.defaultdict(list)
        for email,name in email_to_name.items():
            index = uf.find(email_to_int[email]) #根-->emails
            name_emails[index].append(email)

        res = []
        for index, emails in name_emails.items():
            emails.sort()
            res.append([email_to_name[id_to_email[index]]] + emails)

        return res


import collections


class Solution(object):

    def buildGraph(self, accounts):
        graph = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            for other in account[2:]:
                graph[master].append(other)
                graph[other].append(master)
        return graph

    def dfs(self, graph, emails, visited, master):
        if master not in visited:
            visited.add(master)
            emails.append(master)
            for other in graph[master]:
                self.dfs(graph, emails, visited, other)


    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = self.buildGraph(accounts)
        visited = set()

        res = []
        for account in accounts:
            name = account[0]
            master = account[1]
            emails = []
            self.dfs(graph, emails, visited, master)
            if emails:
                res.append([name] + sorted(emails))

        return res

#bfs,dfs
import collections


class Solution(object):

    def buildGraph(self, accounts):
        graph = collections.defaultdict(list)
        for account in accounts:
            master = account[1]
            for other in account[2:]:
                graph[master].append(other)
                graph[other].append(master)
        return graph

    def dfs(self, graph, emails, visited, master):
        if master not in visited:
            visited.add(master)
            emails.append(master)
            for other in graph[master]:
                self.dfs(graph, emails, visited, other)

    def bfs(self, graph, emails, visited, master):
        if master not in visited:
            queue = collections.deque()
            emails.append(master)
            queue.append(master)
            visited.add(master)

            while queue:
                node = queue.popleft()
                for other in graph[node]:
                    if other not in visited:
                        queue.append(other)
                        emails.append(other)
                        visited.add(other)



    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        graph = self.buildGraph(accounts)
        visited = set()

        res = []
        for account in accounts:
            name = account[0]
            master = account[1]
            emails = []
            self.bfs(graph, emails, visited, master)
            if emails:
                res.append([name] + sorted(emails))

        return res













if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]

    print(Solution().accountsMerge(accounts))
