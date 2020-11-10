from anytree import Node

from QATree.treeGenerator import listTOnode, multipleParents, CTree

# ____________________ Global Block No_1 ____________________ #

UpBlockName = '''
    <div>Дело связанное с правом купли продажи. </div>
    <div>Признаки: </div>
    <div>-Одна из сторон обязалась передать право собственности на объект; </div>
    <div>-Одна из сторон платит;</div>
    <div>-Форма оформления договора (Арбитражный суд); </div>
    <div>-Сделка в соответствии со ст. 454 ГК;</div>
    <div>-Ограничение от других типов контрактов, напри. аренда и т.п.</div>
'''
UpNBlock = Node(UpBlockName)

# ____________________ Section No_1 ____________________ #
under_block_0 = [
    Node('Покупка предприятия, ст. 559 ff. ГК'),
    Node('Покупка недвижимости, ст. 549 ff. ГК'),
    Node('Покупка энергии, ст. 539 ff. ГК'),
    Node('Сельскохозяйственная продукция, ст. 535 ff. ГК'),
    Node('Товар для государственных нужд, ст. 526 ff. ГК'),
    Node('Договор поставки, ст. 506 ff. ГК'),
    Node('Договор розничной купли-продажи, ст. 492 ff. ГК'),
    Node('Договор купли-продажи, ст. 454 ff. ГК')
]
listTOnode(parent=UpNBlock, massive=under_block_0)

# ____________________ Section No_2 ____________________ #
parent_0_0 = under_block_0[0]
under_block_0_0 = [
    Node('Предметом договора является предприятие (см. часть 2, С. II)'),
    Node('Контрагенты: любые')
]
listTOnode(parent=parent_0_0, massive=under_block_0_0)


parent_0_1 = under_block_0[1]
under_block_0_1 = [
    Node('Предмет договора: недвижимость в соответствии со ст. 130 ГК'),
    Node('Контрагенты: любые')
]
listTOnode(parent=parent_0_1, massive=under_block_0_1)

parent_0_2 = under_block_0[2]
under_block_0_2 = [
    Node('Предмет договора: электричество, газ, централизованное отопление в соответствии со ст. 539, 548 II ГК'),
    Node('Потребительская сеть')
]
listTOnode(parent=parent_0_2, massive=under_block_0_2)

parent_0_3 = under_block_0[3]
under_block_0_3 = [
    Node('Предмет договора: сельскохозяйственная продукция'),
    Node('Определенные договаривающиеся стороны')
]
listTOnode(parent=parent_0_3, massive=under_block_0_3)

parent_0_4 = under_block_0[4]
under_block_0_4 = [
    Node('Предмет договора: товары для государственных нужд'),
    Node('Договаривающиеся стороны')
]
listTOnode(parent=parent_0_4, massive=under_block_0_4)

parent_0_5 = under_block_0[5]
under_block_0_5 = [
    Node('Предмет договора: комерческое назначение'),
    Node('Договаривающиеся стороны'),
    Node('Срок поставки(спорно)')
]
listTOnode(parent=parent_0_5, massive=under_block_0_5)

parent_0_6 = under_block_0[6]
under_block_0_6 = [
    Node('Предмет договора: некомерческое назначение'),
    Node('Договаривающиеся стороны')
]
listTOnode(parent=parent_0_6, massive=under_block_0_6)

parent_0_7 = under_block_0[7]
under_block_0_7 = [
    Node('Предмет договора'),
    Node('Договаривающиеся стороны')
]
listTOnode(parent=parent_0_7, massive=under_block_0_7)


# ____________________ Section No_3 ____________________ #
under_block_0_3_1 = [
    Node('а. Продавец: Производитель'),
    Node('b. Покупатель: Дилер(не потребитель)')
]
listTOnode(parent=under_block_0_3[1], massive=under_block_0_3_1)

under_block_0_4_1 = [
    Node('а. Государственный заказчик'),
    Node('b. Поставщик (как правило дилер)')
]
listTOnode(parent=under_block_0_4[1], massive=under_block_0_4_1)

under_block_0_5_1 = [
    Node('а. Поставщик: предприниматель в соотетствии со ст.2 II ГК'),
    Node('b. Покупатель: спорно, как правило так же предприниматель')
]
listTOnode(parent=under_block_0_5[1], massive=under_block_0_5_1)

under_block_0_6_1 = [
    Node('а. Продавец: Комерсант'),
    Node('b. Покупатель: потребители и дилеры')
]
listTOnode(parent=under_block_0_6[1], massive=under_block_0_6_1)

under_block_0_7_0 = [
    Node('а. Предметы, ст. 454 ГК'),
    Node('b. Ценные бумаги, ст. 454 II ГК'),
    Node('с. Имущественные права, ст. 454 IV ГК')
]
listTOnode(parent=under_block_0_7[0], massive=under_block_0_7_0)

under_block_0_7_1 = [
    Node('а. Продавец: граждане, дилеры'),
    Node('b. Покупатель: граждане, дилеры')
]
listTOnode(parent=under_block_0_7[1], massive=under_block_0_7_1)


parentsBlock_1 = [
    under_block_0_0[0],
    under_block_0_0[1],
    under_block_0_1[0],
    under_block_0_1[1],
    under_block_0_2[0],
    under_block_0_2[1],
    under_block_0_3[0],
    under_block_0_3_1[0],
    under_block_0_3_1[1],
    under_block_0_4[0],
    under_block_0_4_1[0],
    under_block_0_4_1[1],
    under_block_0_5[0],
    under_block_0_5_1[0],
    under_block_0_5_1[1],
    under_block_0_5[2],
    under_block_0_6[0],
    under_block_0_6_1[0],
    under_block_0_6_1[1],
    under_block_0_7_0[0],
    under_block_0_7_0[1],
    under_block_0_7_0[2],
    under_block_0_7_1[0],
    under_block_0_7_1[1]
]