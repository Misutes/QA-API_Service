from anytree import Node, RenderTree

class CTree:

    def __init__(self, preTree):
        self.__preTree = preTree
        self.tree = self.__createTree()

    def __prepareBranch(self):
        self.name = self.__preTree[0]
        self.children = self.__preTree[1]

    def __createTree(self):
        self.__prepareBranch()
        Tree = Node(self.name)
        for child in self.children:
            if isinstance(child, list) and len(child) >= 2:
                subTree = CTree(child)
                subTree.tree.parent = Tree
                continue
            Node(child, parent=Tree)
        return Tree

    def visualiseTree(self):
        for pre, fill, node in RenderTree(self.tree):
            print("%s%s" % (pre, node.name))

    @staticmethod
    def getBranchName(branch):
        return str(branch.name)

    def getBranch(self, element):
        return self.getBranchList[element]

    @staticmethod
    def getBranchList(branch):
        rawList = [_branch for _branch in branch.children]
        return rawList

    def getBranchNamesList(self, branch):
        rawList = ['{i}: '.format(i=i+1) + str(self.getBranchName(_branch)) for i, _branch
                   in zip(range(len(branch.children)), self.getBranchList(branch))]
        strList = '\n'.join(rawList)
        return strList

