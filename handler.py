

class Handler:

    def __init__(self, Tree):
        self.users = {}
        self.usersPath = {}
        self.Tree = Tree

    def adduser(self, ip: str):
        if ip not in self.users:
            self.users.setdefault(ip, self.Tree.getBranchList(self.Tree.tree))
            self.usersPath.setdefault(ip, '')

    def stepDeep(self, ip, path):
        currentPosition = self.Tree.getBranchList(self.users[ip][path])
        if currentPosition:
            variants = self.Tree.getBranchNamesList(self.users[ip][path])
            self.users[ip] = currentPosition
            return variants
        variants = self.Tree.getBranchName(self.users[ip][0])
        return variants


