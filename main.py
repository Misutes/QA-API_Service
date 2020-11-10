from flask import Flask, request, render_template
from QATree.treeGenerator import CTree
from handler import Handler
from QATree.Trees.sheme_1.globalBlock_3 import chooseNode
from config import setting

baseApp = Flask(__name__)

Tree = CTree(chooseNode)
handler = Handler(Tree=Tree)


@baseApp.route('/', methods=['GET', 'POST'])
def index():
    user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    handler.adduser(user_ip)
    if request.method == 'GET':
        if handler.usersPath[user_ip]:
            pos = handler.usersPath[user_ip].rfind('↓')
            current_node = handler.usersPath[user_ip][pos+1:]
        else:
            current_node = Tree.getBranchNamesList(Tree.tree)
    elif request.method == 'POST':
        route = int(request.form.get('route')) - 1
        if len(handler.users[user_ip]) > route:
            handler.usersPath[user_ip] += '<div style="font-size: 150%; color: green">|</div>' \
                                          '<div style="font-size: 150%; color: green">↓</div>' \
                                          + Tree.getBranchName(handler.users[user_ip][route])
            current_node = handler.stepDeep(ip=user_ip, path=route)
        else:
            print(Tree.getBranchList())
            Tree.visualiseTree(handler.users[user_ip])
            current_node = 'Error route. Choose right digit'
    return render_template('main_page.html', current_node=current_node, doin_path=handler.usersPath[user_ip])


@baseApp.route('/scheme')
def getScheme():
    if request.method == 'GET':
        scheme = 'Возможные схемы: \n'
        subStr = Tree.getBranchNamesList(Tree.tree)
        return scheme + subStr
    return


@baseApp.route('/scheme', methods=['POST'])
def updateScheme():
    user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if request.method == 'POST':
        handler.users[user_ip] = Tree.getBranchList(Tree.tree)
        return 'Ваш прогресс сброшен'


@baseApp.route('/back_<int:steps>', methods=['POST'])
def backRoute(steps):
    user_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    if request.method == 'POST':
        if steps == 1:
            handler.users[user_ip] = handler.usersPath[user_ip][0]
        elif steps < len(handler.usersPath[user_ip]):
            handler.usersPath[user_ip] = handler.usersPath[user_ip][:-(steps-1)]
            handler.users[user_ip] = handler.usersPath[user_ip]
        else:
            handler.usersPath[user_ip] = []
            handler.users[user_ip] = Tree.getBranchList(Tree.tree)
        return f'Успешно! Сделано шагов назад {steps}'.format(steps=steps)


if __name__ == '__main__':
    baseApp.run(**setting)
