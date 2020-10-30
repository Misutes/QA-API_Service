from flask import Flask, request
from QATree.treeGenerator import CTree
from handler import Handler
from QATree.Trees.firstScheme import level_0

baseApp = Flask(__name__)

schemeLevel = ['вопросы', ['вопрос 1.1', ['вопрос 1.2', [['вопрос 2.1', ['вопрос 2.2.1', 'вопрос 2.2.2']], 'вопрос 2.2']], 'вопрос 1.3', 'вопрос 1.4']]
Tree = CTree(['cхемы', [level_0]])
Tree.visualiseTree()
handler = Handler(Tree=Tree)


@baseApp.route('/<int:case>', methods=['POST', 'GET'])
def index(case):
    if request.method == 'POST':
        user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        handler.adduser(user_ip)
        if len(Tree.getBranchList(Tree.tree)) >= case-1:
            return handler.stepDeep(ip=user_ip, path=case-1)
        return 'error params'
    return 'Pre-base QA-service'


@baseApp.route('/scheme')
def getScheme():
    if request.method == 'GET':
        scheme = 'Возможные схемы: \n'
        subStr = Tree.getBranchNamesList(Tree.tree)
        return scheme + subStr
    return


@baseApp.route('/scheme', methods=['POST'])
def updateScheme():
    if request.method == 'POST':
        return 'Ваш прогресс сброшен'


@baseApp.route('/back_<int:steps>', methods=['POST'])
def backRoute(steps):
    if request.method == 'POST':
        user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        print(handler.usersPath[user_ip])
        handler.usersPath[user_ip] = handler.usersPath[user_ip][:-(steps-1)]
        print(handler.usersPath[user_ip])
        handler.users[user_ip] = handler.usersPath[user_ip]
        return f'Успешно! Сделано шагов назад {steps}'.format(steps=steps)


if __name__ == '__main__':
    baseApp.run(debug=True)
