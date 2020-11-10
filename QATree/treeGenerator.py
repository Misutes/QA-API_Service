from anytree import RenderTree
from copy import deepcopy


class CTree:

    def __init__(self, tree):
        self.tree = tree

    def visualiseTree(self, tree=None):
        for pre, fill, node in RenderTree(tree if tree else self.tree):
            print("%s%s" % (pre, node.name))

    def printTree(self):
        from anytree.exporter import DotExporter
        DotExporter(self.tree).to_picture('chooseNode.png')

    @staticmethod
    def getBranchName(branch):
        return str(branch.name)

    def getBranch(self, element):
        return '1: ' + self.getBranchList[element]

    @staticmethod
    def getBranchList(branch):
        rawList = [_branch for _branch in branch.children]
        return rawList

    def getBranchNamesList(self, branch):
        rawList = ['<div> {i}: '.format(i=i+1) + str(self.getBranchName(_branch))+'</div>' for i, _branch
                   in zip(range(len(branch.children)), self.getBranchList(branch))]
        strList = ''.join(rawList)
        return strList


def listTOnode(parent, massive):
    for element in massive:
        element.parent = parent


def multipleParents(parents, child):
    for parent in parents:
        copyChild = deepcopy(child)
        copyChild.parent = parent
