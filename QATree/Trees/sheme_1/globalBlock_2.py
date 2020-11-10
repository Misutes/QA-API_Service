from anytree import Node

from QATree.Trees.sheme_1.globalBlock_1 import parentsBlock_1
from QATree.treeGenerator import listTOnode, multipleParents
from copy import deepcopy


# ____________________ Global Block No_2 ____________________ #

MName = 'Заключение договора в соответствии со ст. 432-449 ГК'
MainNode = Node(MName)

# ____________________ Section No_1 ____________________ #
branchFor_0 = [
    Node('I. Только по акцепту, ст. 433 I ГК'),
    Node('II. Соглашение и передача, ст. 433 II ГК'),
    Node('III. Соглашение и регистрация, ст. 433 III ГК'),
    Node('IV. Прочее, ст. 433ГК')
]
listTOnode(parent=MainNode, massive=branchFor_0)

# ____________________ Section No_2 ____________________ #

parent_0_0 = branchFor_0[0]
branchFor_0_0 = [
    Node('1. Оферта и акцепт, ст. 432 ГК'),
    Node('2. Заключение договора в обязательно поряке'),
    Node('3. По судебному решению'),
    Node('4. Аукцион, ст. 447, 448, 449 ГК')
]
listTOnode(parent=parent_0_0, massive=branchFor_0_0)

parent_0_1 = branchFor_0[1]
branchFor_0_1 = [
    Node('1. Ст. 498 ГК'),
    Node('2. Другие реальные договоры ст. 520 I ГК'),
]
listTOnode(parent=parent_0_1, massive=branchFor_0_1)

parent_0_2 = branchFor_0[2]
branchFor_0_2 = [
    Node('1. Покупка жилого помещения/квартиры, Ст. 558 ГК'),
    Node('2. Приобретение предприятия, ст. 559 ГК'),
]
listTOnode(parent=parent_0_2, massive=branchFor_0_2)

# ____________________ Section No_3 ____________________ #

parent_0_0_0 = branchFor_0_0[0]
branchFor_0_0_0 = [
    Node('а. Оферта, ст. 435 ГК'),
    Node('b. Акцепт, ст. 438 ГК'),
    Node('c. Форма, ст. 434 ГК')
]
listTOnode(parent=parent_0_0_0, massive=branchFor_0_0_0)

parent_0_0_1 = branchFor_0_0[1]
branchFor_0_0_1 = [
    Node('а. Заключение договора в обязательном порядке, ст. 527, 528 ГК'),
    Node('b. Заключение договора в обязательном порядке, ст. 527, 529 ГК'),
    Node('c. Заключение договора в обязательном порядке, ст. 445 I/II ГК')
]
branchFor_0_0_1[0].parent = parent_0_0_1

parent_0_0_1_0 = branchFor_0_0_1[0]
branchFor_0_0_1_0 = [
    Node('aa. Оферта в обязательном порядке, ст. 527 I, IV; 528 I ГК'),
    Node('bb. Акцепт в обязательном порядке ст. 527 II, 528 II ГК'),
    Node('сс. Голосование ст. 528 III или суд'),
    Node('dd. Форма')
]
multipleParents(parents=branchFor_0_0_1_0, child=branchFor_0_0_1[1])

parent_0_0_1_1 = branchFor_0_0_1[1]
branchFor_0_0_1_1 = [
    Node('aa. Государственный договор с покрытием, ст. 527, 528 ГК'),
    Node('bb. Оферта ст. 529 II ГК'),
    Node('сс. Акцепт ст. 529 III ГК'),
    Node('dd. В случае ст. 443 ГК: голосование, акцепт, отказ'),
    Node('ee. В случае отказа ст. 529  ГК, суд')
]
listTOnode(parent=parent_0_0_1_1, massive=branchFor_0_0_1_1)
multipleParents(parents=branchFor_0_0_1_1, child=branchFor_0_0_1[2])

parent_0_0_1_2 = branchFor_0_0_1[2]
branchFor_0_0_1_2 = [
    Node('aa. Оферта'),
    Node('bb. Акцепт ст. 445 I, II ГК'),
    Node('cc. Форма')
]
listTOnode(parent=parent_0_0_1_2, massive=branchFor_0_0_1_2)

parent_0_0_2 = branchFor_0_0[2]
branchFor_0_0_2 = [
    Node('а. Требование на заключение договора'),
    Node('b. Направление в суд по обоюдному согласию')
]
listTOnode(parent=parent_0_0_2, massive=branchFor_0_0_2)

parent_0_0_2_0 = branchFor_0_0_2[0]
branchFor_0_0_2_0 = [
    Node('aa. Суверенные договоры ст. 445 IV ГК'),
    Node('bb. Заключение договора в обязательно порядке, ст. 426 III ГК'),
    Node('cc. Договор в осоответствии со ст. 429 V ГК'),
    Node('dd. Аукцион ст. 448 V 2 ГК'),
    Node('ee. Государственные закупки ст. 528 V, 529 V ГК'),
    Node('ff. Сельскохозяйственные закупки ст. 535 II ГК'),
]
listTOnode(parent=parent_0_0_2_0, massive=branchFor_0_0_2_0)

parent_0_0_3 = branchFor_0_0[3]
branchFor_0_0_3 = [
    Node('а. Предложение участника аукциона, ст. 447 I ГК'),
    Node('b. Манифестация через итоговый протокол, ст. 448 V 1 ГК'),
    Node('c. Отсутствие причин недействительности, ст. 449 II ГК')
]
listTOnode(parent=parent_0_0_3, massive=branchFor_0_0_3)

parent_0_2_0 = branchFor_0_2[0]
branchFor_0_2_0 = [
    Node('а. Соглашение'),
    Node('b. Государственная регистрация, ст. 558 II ГК')
]
listTOnode(parent=parent_0_2_0, massive=branchFor_0_2_0)

parent_0_2_1 = branchFor_0_2[1]
branchFor_0_2_1 = [
    Node('а. Соглашение'),
    Node('b. Государственная регистрация, ст. 560 III ГК')
]
listTOnode(parent=parent_0_2_1, massive=branchFor_0_2_1)

# ____________________ Section No_4 (Local Block 0)____________________ #
parent_0_0_0_0 = branchFor_0_0_0[0]
branchFor_0_0_0_0 = [
    Node('aa. Обычный случай, ст. 435 гк'),
    Node('bb. Неопределенная группа лиц, ст. 437 ГК'),
    Node('cc. Обязанность оферты'),
]

# Local Block 0
parent_0_0_0_0_0 = branchFor_0_0_0_0[0]
branchFor_0_0_0_0_0 = [
    Node('aaa. Оферта как выражение воли, ст. 154, 153 ГК'),
    Node('bbb. Требования ст.435 I ГК: конкретная группа ли (решающий критерий в обычном случае)'),
    Node('ccс. Достаточная определенность, ст. 435 I ГК'),
    Node('ddd. Волеизъявление, порождающее правовые последствия'),
    Node('eee. Существенные условия договора, ст. 435 I 2 ГК'),
    Node('fff. Получение оферты, ст. 435 II ГК'),
    Node('ggg. Действительность оферты как законного акта'),
    Node('hhh. Результат: оферта'),
]
branchFor_0_0_0_0_0[0].parent = parent_0_0_0_0_0


parent_0_0_0_0_0_0 = branchFor_0_0_0_0_0[0]
branchFor_0_0_0_0_0_0 = [
    Node('(i) Непосредственно \n (ii) Конклюдентно')
]
listTOnode(parent=parent_0_0_0_0_0_0, massive=branchFor_0_0_0_0_0_0)
branchFor_0_0_0_0_0[1].parent = branchFor_0_0_0_0_0_0[0]
branchFor_0_0_0_0_0[2].parent = branchFor_0_0_0_0_0[1]

parent_0_0_0_0_0_2 = branchFor_0_0_0_0_0[2]
branchFor_0_0_0_0_0_2 = [
    Node('(i) Контрагенты и предмет договора'),
    Node('(ii) Цена'),
    Node('(iii) Альтернативная трактовка')
]
branchFor_0_0_0_0_0_2[0].parent = parent_0_0_0_0_0_2
branchFor_0_0_0_0_0_2[1].parent = branchFor_0_0_0_0_0_2[0]

parent_0_0_0_0_0_2_1 = branchFor_0_0_0_0_0_2[1]
branchFor_0_0_0_0_0_2_1 = [
    Node('(a.) Цена = достаточно определенный термин? \n (b.)  Цена подпадает под определение "достаточно определенно"')
]
branchFor_0_0_0_0_0_2_1[0].parent = parent_0_0_0_0_0_2_1
branchFor_0_0_0_0_0_2[2].parent = branchFor_0_0_0_0_0_2_1[0]
branchFor_0_0_0_0_0[3].parent = branchFor_0_0_0_0_0_2[2]
branchFor_0_0_0_0_0[4].parent = branchFor_0_0_0_0_0[3]

parent_0_0_0_0_0_4 = branchFor_0_0_0_0_0[4]
branchFor_0_0_0_0_0_4 = [
    Node('(i) Условия касающиеся предмета договора'),
    Node('(ii) Условя, обязательные по закону или другими нормативными актами'),
    Node('(iii) Существнные условия в соответствии с заявлениями контрагентов')
]
branchFor_0_0_0_0_0_4[0].parent = parent_0_0_0_0_0_4
branchFor_0_0_0_0_0_4[1].parent = branchFor_0_0_0_0_0_4[0]

parent_0_0_0_0_0_4_1 = branchFor_0_0_0_0_0_4[1]
branchFor_0_0_0_0_0_4_1 = [
    Node('(a.) Существенные условия, ст. 432 I 2 альт. 1 ГК'),
    Node('(b.)  Характеристики договора, ст. 432 I 2 альт. 2 ГК')
]
listTOnode(parent=parent_0_0_0_0_0_4_1, massive=branchFor_0_0_0_0_0_4_1)

parent_0_0_0_0_0_4_1_0 = branchFor_0_0_0_0_0_4_1[0]
branchFor_0_0_0_0_0_4_1_0 = [
    Node('(аа.) Объект права в соответствии со ст. 435 ГК'),
    Node('(bb.) Количество товара, ст. 465 ГК'),
]
listTOnode(parent=parent_0_0_0_0_0_4_1_0, massive=branchFor_0_0_0_0_0_4_1_0)

parent_0_0_0_0_0_4_1_0_0 = branchFor_0_0_0_0_0_4_1_0[0]
branchFor_0_0_0_0_0_4_1_0_0 = [
    Node('(ааа.) Принцип ст. 129 I ГК \n (bbb.) Ст. 129 II ГК \n (ccc.) Ст. 129 III ГК')
]
branchFor_0_0_0_0_0_4_1_0_0[0].parent = parent_0_0_0_0_0_4_1_0_0

parent_0_0_0_0_0_4_1_0_1 = branchFor_0_0_0_0_0_4_1_0[1]
branchFor_0_0_0_0_0_4_1_0_1 = [
    Node('(ааа.) Определенное количество товаров \n (bbb.) Определяемое количество товаров')
]
branchFor_0_0_0_0_0_4_1_0_1[0].parent = parent_0_0_0_0_0_4_1_0_1

parent_0_0_0_0_0_4_1_1 = branchFor_0_0_0_0_0_4_1[1]
branchFor_0_0_0_0_0_4_1_1 = [
    Node('(аа.) Государственные закупки, ст. 527 ГК \n '
         '(bb.) Покупка энергии, ст. 539 ГК \n '
         '(cc.) Покупка недвижимости, ст. 549, 554, 558 ГК \n '
         '(dd.) Покупка предприятия, ст. 559 ГК \n '
         '(ee.) Покупка в расрочку, ст. 489 ГК \n '
         '(ff.) Ст. 491 ГК')
]
branchFor_0_0_0_0_0_4_1_1[0].parent = parent_0_0_0_0_0_4_1_1
multipleParents(parents=[branchFor_0_0_0_0_0_4_1_0_0[0], branchFor_0_0_0_0_0_4_1_0_1[0], branchFor_0_0_0_0_0_4_1_1[0]],
                child=branchFor_0_0_0_0_0_4[2])


parent_0_0_0_0_0_4_2 = branchFor_0_0_0_0_0_4[2]
branchFor_0_0_0_0_0_4_2 = [
    Node('(a.) Принцип'),
    Node('(b.) Общие положения и условия')
]
listTOnode(parent=parent_0_0_0_0_0_4_2, massive=branchFor_0_0_0_0_0_4_2)

parent_0_0_0_0_0_4_2_1 = branchFor_0_0_0_0_0_4_2[1]
branchFor_0_0_0_0_0_4_2_1 = [
    Node('(aa.) Примерные условия, ст. 427 ГК'),
    Node('(bb.) Контроль, ст. 428 ГК, AGB')
]
listTOnode(parent=parent_0_0_0_0_0_4_2_1, massive=branchFor_0_0_0_0_0_4_2_1)

parent_0_0_0_0_0_4_2_1_0 = branchFor_0_0_0_0_0_4_2_1[0]
branchFor_0_0_0_0_0_4_2_1_0 = [
    Node('(aaa.) Оглашение, ст. 427 I ГК'),
    Node('(bbb.) Cт. 427 I ГК --> ст. 421 V ГК')
]
listTOnode(parent=parent_0_0_0_0_0_4_2_1_0, massive=branchFor_0_0_0_0_0_4_2_1_0)
multipleParents(parents=[branchFor_0_0_0_0_0_4_2[0], branchFor_0_0_0_0_0_4_2_1_0[0], branchFor_0_0_0_0_0_4_2_1_0[1], branchFor_0_0_0_0_0_4_2_1[1]],
                child=branchFor_0_0_0_0_0[5])

parent_0_0_0_0_0_5 = branchFor_0_0_0_0_0[5]
branchFor_0_0_0_0_0_5 = [
    Node('(i) Получение ст. 435 I ГК'),
    Node('(ii) Отзыв ст. 436 ГК')
]
listTOnode(parent=parent_0_0_0_0_0_5, massive=branchFor_0_0_0_0_0_5)
multipleParents(parents=[branchFor_0_0_0_0_0_5[0], branchFor_0_0_0_0_0_5[1]],
                child=branchFor_0_0_0_0_0[6])
branchFor_0_0_0_0_0[7].parent = branchFor_0_0_0_0_0[6]
branchFor_0_0_0_0[1].parent = branchFor_0_0_0_0_0[7]

# Local Block 1

parent_0_0_0_0_1 = branchFor_0_0_0_0[1]
branchFor_0_0_0_0_1 = [
    Node('aaa. Основные требования к выражению воли'),
    Node('bbb. Неопределенная группа лиц, ст. 437 ГК'),
    Node('ccc. Выражение воли неопределенной группы лиц с правовым последствием'),
    Node('ddd. Исполнительное определение, существенные договорные условия, действительность юридической сделки'),
    Node('eee. "Получение" с отдачей: отсутствие непосредственного исключения обязательств'),
    Node('Результат: оферта(+)')
]
branchFor_0_0_0_0_1[0].parent = parent_0_0_0_0_1

parent_0_0_0_0_1_0 = branchFor_0_0_0_0_1[0]
branchFor_0_0_0_0_1_0 = [
    Node('Последствие: нет обязательств из предложения')
]
branchFor_0_0_0_0_1_0[0].parent = parent_0_0_0_0_1_0
branchFor_0_0_0_0_1[1].parent = branchFor_0_0_0_0_1_0[0]

parent_0_0_0_0_1_1 = branchFor_0_0_0_0_1[1]
branchFor_0_0_0_0_1_1 = [
    Node('(ii) offerte ad incertas personas, ст. 437 II ГК'),
    Node('(iii) Модификация в законе купле-продаже'),
    Node('(i) invitatio ad offerendum, ст. 437 I ГК'),
]
listTOnode(parent=parent_0_0_0_0_1_1, massive=branchFor_0_0_0_0_1_1)

parent_0_0_0_0_1_1_0 = branchFor_0_0_0_0_1_1[0]
branchFor_0_0_0_0_1_1_0 = [
    Node('Обязывающий эффект для всех комерческих организаций')
]
branchFor_0_0_0_0_1_1_0[0].parent = parent_0_0_0_0_1_1_0
tempCopy_0 = deepcopy(branchFor_0_0_0_0_1_0[0])
tempCopy_0.parent = branchFor_0_0_0_0_1_1_0[0]

parent_0_0_0_0_1_1_1 = branchFor_0_0_0_0_1_1[1]
branchFor_0_0_0_0_1_1_1 = [
    Node('(a.) Розничная купля-продажа (ст. 492 ГК); характеристика как у государственных закупок (ст.426 ГК)')
]
branchFor_0_0_0_0_1_1_1[0].parent = parent_0_0_0_0_1_1_1

parent_0_0_0_0_1_1_1_0 = branchFor_0_0_0_0_1_1_1[0]
branchFor_0_0_0_0_1_1_1_0 = [
    Node('Последствие: ст. 426 ГК публичное предложение --> в соответствии с ст. 437 II ГК действует '
         'как оферта по отношению к тому, кто на нее отозвался')
]
branchFor_0_0_0_0_1_1_1_0[0].parent = parent_0_0_0_0_1_1_1_0
tempCopy_1 = deepcopy(branchFor_0_0_0_0_1_0[0])
tempCopy_1.parent = branchFor_0_0_0_0_1_1_1_0[0]

parent_0_0_0_0_1_1_2 = branchFor_0_0_0_0_1_1[2]
branchFor_0_0_0_0_1_1_2 = [
    Node('(b.) Покупка по образцу, ст. 497 ГК')
]
branchFor_0_0_0_0_1_1_2[0].parent = parent_0_0_0_0_1_1_2

parent_0_0_0_0_1_1_2_0 = branchFor_0_0_0_0_1_1_2[0]
branchFor_0_0_0_0_1_1_2_0 = [
    Node('Оценка как оканчательная норма --> в этом случае проблемы ст. 492 ГК'),
    Node('Оценка как стандарт содержания --> в этм случае договор считается уже заглюченным'),
]
listTOnode(parent=parent_0_0_0_0_1_1_2_0, massive=branchFor_0_0_0_0_1_1_2_0)
multipleParents(parents=branchFor_0_0_0_0_1_1_2_0 + [tempCopy_0, tempCopy_1], child=branchFor_0_0_0_0_1[2])


parent_0_0_0_0_1_2 = branchFor_0_0_0_0_1[2]
branchFor_0_0_0_0_1_2 = [
    Node('(i) Принцип \n (ii) В розничной купле-продаже')
]
branchFor_0_0_0_0_1_2[0].parent = parent_0_0_0_0_1_2
branchFor_0_0_0_0_1[3].parent = branchFor_0_0_0_0_1_2[0]

parent_0_0_0_0_1_3 = branchFor_0_0_0_0_1[3]
listTOnode(parent=parent_0_0_0_0_1_3, massive=[branchFor_0_0_0_0_1[4]])
branchFor_0_0_0_0_1[5].parent = branchFor_0_0_0_0_1[4]

branchFor_0_0_0_0[2].parent = branchFor_0_0_0_0_1[5]
branchFor_0_0_0[1].parent = branchFor_0_0_0_0[2]

# Local block 2
parent_0_0_0_1 = branchFor_0_0_0[1]
branchFor_0_0_0_1 = [
    Node('аа. Обычный случай, ст.435 ГК'),
    Node('bb. Акцепт через молчание, ст.498 II ГК'),
    Node('cc. Конклюдентно, ст.438 III ГК'),
    Node('dd. Акцепт в обязательно порядке, ст.435 ГК')
]
branchFor_0_0_0_1[0].parent = parent_0_0_0_1

parent_0_0_0_1_0 = branchFor_0_0_0_1[0]
branchFor_0_0_0_1_0 = [
    Node('aaa. Акцепт как выражение воли'),
    Node('bbb. Требования ст. 438 I ГК'),
    Node('ccc. Получение акцепта в срок'),
    Node('ddd. Отсутствие отзыва в соответствии со ст 439 ГК'),
    Node('eee. Действительность акцепта как законного акта'),
    Node('fff. Результат')
]
branchFor_0_0_0_1_0[0].parent = parent_0_0_0_1_0
branchFor_0_0_0_1_0[1].parent = branchFor_0_0_0_1_0[0]

parent_0_0_0_1_0_1 = branchFor_0_0_0_1_0[1]
branchFor_0_0_0_1_0_1 = [
    Node('(i) Ссылка на оферту'),
    Node('(iii) Безоговорочно'),
    Node('(ii) Всецело')
]
listTOnode(parent=parent_0_0_0_1_0_1, massive=branchFor_0_0_0_1_0_1)


parent_0_0_0_1_0_1_1 = branchFor_0_0_0_1_0_1[1]
branchFor_0_0_0_1_0_1_1 = [
    Node('(а.) Ограничение к ст. 43 ГК')
]
branchFor_0_0_0_1_0_1_1[0].parent = parent_0_0_0_1_0_1_1
multipleParents(parents=[branchFor_0_0_0_1_0_1[0], branchFor_0_0_0_1_0_1_1[0], branchFor_0_0_0_1_0_1[2]],
                child=branchFor_0_0_0_1_0[2])

parent_0_0_0_1_0_2 = branchFor_0_0_0_1_0[2]
branchFor_0_0_0_1_0_2 = [
    Node('(i) 1. ситуация: срок акцепта определен, ст. 440 ГК'),
    Node('(ii) 2. ситуация: срок акцепта не определен, ст. 441 ГК'),
    Node('(iii) 3. ситуация: акцепт с опазданием, ст. 442 ГК')
]
listTOnode(parent=parent_0_0_0_1_0_2, massive=branchFor_0_0_0_1_0_2)

parent_0_0_0_1_0_2_1 = branchFor_0_0_0_1_0_2[1]
branchFor_0_0_0_1_0_2_1 = [
    Node('(a.) При устной оферте'),
    Node('(b.) При письменной оферте')
]
listTOnode(parent=parent_0_0_0_1_0_2_1, massive=branchFor_0_0_0_1_0_2_1)
multipleParents(parents=[branchFor_0_0_0_1_0_2[0], branchFor_0_0_0_1_0_2_1[0], branchFor_0_0_0_1_0_2_1[1], branchFor_0_0_0_1_0_2[2]],
                child=branchFor_0_0_0_1_0[4])
branchFor_0_0_0_1_0[5].parent = branchFor_0_0_0_1_0[4]

parent_0_0_0_1_0_5 = branchFor_0_0_0_1_0[5]
branchFor_0_0_0_1_0_5 = [
    Node('(i) При наличии описанных условий'),
    Node('(ii) При измененных условиях, ст. 443 ГК')
]
listTOnode(parent=parent_0_0_0_1_0_5, massive=branchFor_0_0_0_1_0_5)

parent_0_0_0_1_0_5_0 = branchFor_0_0_0_1_0_5[0]
branchFor_0_0_0_1_0_5_0 = [
    Node('(a.) Заключенный договор купли-продажи')
]
branchFor_0_0_0_1_0_5_0[0].parent = parent_0_0_0_1_0_5_0

parent_0_0_0_1_0_5_1 = branchFor_0_0_0_1_0_5[1]
branchFor_0_0_0_1_0_5_1 = [
    Node('(b.) Договор не заключен, ст. 443 ГК')
]
branchFor_0_0_0_1_0_5_1[0].parent = parent_0_0_0_1_0_5_1
multipleParents(parents=[branchFor_0_0_0_1_0_5_0[0], branchFor_0_0_0_1_0_5_0[0]],
                child=branchFor_0_0_0_1[1])

parent_0_0_0_1_1 = branchFor_0_0_0_1[1]
branchFor_0_0_0_1_1 = [
    Node('aaa. По закону: здесь право по купле-продаже'),
    Node('bbb. Молчание как торговый обычай'),
    Node('ccc. Молчание в связи с прежними деловыми отношениями')
]
listTOnode(parent=parent_0_0_0_1_1, massive=branchFor_0_0_0_1_1)

parent_0_0_0_1_1_0 = branchFor_0_0_0_1_1[0]
branchFor_0_0_0_1_1_0 = [
    Node('(i) Договор энергоснабжения, ст. 540 II ГК')
]
branchFor_0_0_0_1_1_0[0].parent = parent_0_0_0_1_1_0

parent_0_0_0_1_1_1 = branchFor_0_0_0_1_1[1]
branchFor_0_0_0_1_1_1 = [
    Node('(i) Молчание как русский торговый обычай'),
    Node('(ii) Интернациональные торговые обычаи')
]
listTOnode(parent=parent_0_0_0_1_1_1, massive=branchFor_0_0_0_1_1_1)
multipleParents(parents=[branchFor_0_0_0_1_1_0[0], branchFor_0_0_0_1_1_1[0], branchFor_0_0_0_1_1_1[1], branchFor_0_0_0_1_1[2]],
                child=branchFor_0_0_0_1[2])

parent_0_0_0_1_2 = branchFor_0_0_0_1[2]
branchFor_0_0_0_1_2 = [
    Node('aaa. Если иное не предусмотренно законом или иными правовыми нормами (здесь закон купле-продажи)'),
    Node('bbb. Отсутствие отказа акцепта в оферте')
]
listTOnode(parent=parent_0_0_0_1_2, massive=branchFor_0_0_0_1_2)

parent_0_0_0_1_2_0 = branchFor_0_0_0_1_2[0]
branchFor_0_0_0_1_2_0 = [
    Node('(i) Розничная купля-продажа, ст. 493 ГК'),
    Node('(ii) Конклюдентный акцепт в договорах энергоснабжения, ст. 540 I ГК (реальный договор)'),
    Node('(iii) Акцепт в соответствии со ст. 498 ГК')
]
listTOnode(parent=parent_0_0_0_1_2_0, massive=branchFor_0_0_0_1_2_0)

parent_0_0_0_1_2_0_0 = branchFor_0_0_0_1_2_0[0]
branchFor_0_0_0_1_2_0_0 = [
    Node('(a.) Проблема: ст. 498 ГК противоречит ст. 494 ГК'),
    Node('(b.) Решение')
]
listTOnode(parent=parent_0_0_0_1_2_0_0, massive=branchFor_0_0_0_1_2_0_0)
multipleParents(parents=[branchFor_0_0_0_1_2_0_0[0], branchFor_0_0_0_1_2_0_0[1], branchFor_0_0_0_1_2_0[1], branchFor_0_0_0_1_2_0[2], branchFor_0_0_0_1_2[1]],
                child=branchFor_0_0_0_1[3])

parent_0_0_0_1_3 = branchFor_0_0_0_1[3]
branchFor_0_0_0_1_3 = [
    Node('aaa. Акцепт в обязательно проядке, ст. 445 I ГК'),
    Node('bbb. Акцепт в обязательном порядке, ст. 445 II ГК'),
    Node('ссс. Заключение договора в обязательном порядке, ст. 557 II ГК')
]
multipleParents(parents=branchFor_0_0_0_1_3,
                child=branchFor_0_0_0[2])

# Local block 3
parent_0_0_0_2 = branchFor_0_0_0[2]
branchFor_0_0_0_2 = [
    Node('aa. В соответсвтии с формой первого акта ст. 434 I ГК'),
    Node('bb. Специальные положение закона о купле-продаже, которые применяются в целом к договору ')
]
listTOnode(parent=parent_0_0_0_2, massive=branchFor_0_0_0_2)

parent_0_0_0_2_1 = branchFor_0_0_0_2[1]
branchFor_0_0_0_2_1 = [
    Node('aaa. Покупка предприятия, ст. 560 III ГК'),
    Node('bbb. Покупка недвижимости, ст. 550 ГК + Покпка жилья ст. 558 ГК'),
    Node('ccc. Розничная купля-продажа ст. 498 ГК')
]
listTOnode(parent=parent_0_0_0_2_1, massive=branchFor_0_0_0_2_1)

# ____________________ End Section ____________________ #
multipleParents(child=MainNode, parents=parentsBlock_1)
parentsBlock_2 = [
    branchFor_0_0_0_2_1[0],
    branchFor_0_0_0_2_1[1],
    branchFor_0_0_0_2_1[2],
    branchFor_0_0_1_2[0],
    branchFor_0_0_1_2[1],
    branchFor_0_0_1_2[2],
    branchFor_0_0_2[1],
    branchFor_0_0_3[0],
    branchFor_0_0_3[1],
    branchFor_0_0_3[2],
    branchFor_0_1[0],
    branchFor_0_1[1],
    branchFor_0_2_0[0],
    branchFor_0_2_0[1],
    branchFor_0_2_1[0],
    branchFor_0_2_1[1],
    branchFor_0[3]
]