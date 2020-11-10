from anytree import Node

from QATree.Trees.sheme_1.globalBlock_1 import UpNBlock
from QATree.Trees.sheme_1.globalBlock_2 import parentsBlock_2
from QATree.treeGenerator import listTOnode, multipleParents

# ____________________ Global Block No_3 ____________________ #
# UBlock_0
block_0 = 'Покупка недвижимости'
NBlock_0 = Node(block_0)
under_blocks_0 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_0, massive=under_blocks_0)
Node('Лист Р1', parent=under_blocks_0[0])

# UBlock_1
block_1 = 'Покупка недвижемости'
NBlock_1 = Node(block_1)
under_blocks_1 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_1, massive=under_blocks_1)
Node('Лист Р2', parent=under_blocks_1[0])

# UBlock_2
block_2 = 'Покупка энергии'
NBlock_2 = Node(block_2)
under_blocks_2 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_2, massive=under_blocks_2)
Node('Лист Р3', parent=under_blocks_2[0])

# UBlock_3
block_3 = 'Сельскохозяйственная продукция'
NBlock_3 = Node(block_3)
under_blocks_3 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_3, massive=under_blocks_3)
Node('Лист Р4', parent=under_blocks_3[0])

# UBlock_4
block_4 = 'Товар для государственных нужд'
NBlock_4 = Node(block_4)
under_blocks_4 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_4, massive=under_blocks_4)
Node('Лист Р5', parent=under_blocks_4[0])

# UBlock_5
block_5 = 'Договор поставки'
NBlock_5 = Node(block_5)
under_blocks_5 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.531 ГК --> 507 ГК')
]
listTOnode(parent=NBlock_5, massive=under_blocks_5)
Node('Лист Р6', parent=under_blocks_5[0])

# UBlock_6
block_6 = 'Договор розничной купли-продажи'
NBlock_6 = Node(block_6)
under_blocks_6 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.507 ГК')
]
listTOnode(parent=NBlock_6, massive=under_blocks_6)
Node('Лист Р7', parent=under_blocks_6[0])

# UBlock_7
block_7 = 'Договор купли-продажи в соответствии со ст 454 ГК'
NBlock_7 = Node(block_7)
under_blocks_7 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_7, massive=under_blocks_7)
Node('Лист Р8', parent=under_blocks_7[0])

# UBlock_8
block_8 = 'Купля-продажа прав'
NBlock_8 = Node(block_8)
under_blocks_8 = [
    Node('Первичные требования или требования исполнения'),
    Node('Средства Правовой защиты при дифектах в исполнении договора'),
    Node('Квазидоговорные требования Ст.445 IV ГК')
]
listTOnode(parent=NBlock_8, massive=under_blocks_8)
Node('Лист Р9', parent=under_blocks_8[0])

# ____________________ End Section ____________________ #
childrenBlock_3 = [NBlock_0, NBlock_1, NBlock_2, NBlock_3, NBlock_4, NBlock_5, NBlock_6, NBlock_7, NBlock_8]
for child in childrenBlock_3:
    multipleParents(parents=parentsBlock_2, child=child)

chooseScheme = 'Выбирите схему'
chooseNode = Node(chooseScheme)
UpNBlock.parent = chooseNode