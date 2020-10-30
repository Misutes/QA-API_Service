from QATree.treeGenerator import CTree

level_1_7_0 = ['предмет договора', ['предмет ст.454', 'ценные бумаги', 'имущественные права']]

level_1_0 = ['Покупка Предприятия', ['требования для 1']]
level_1_1 = ['Покупка Недвижимости', ['требования для 2']]
level_1_2 = ['Покупка энергии. ст.', ['требования для 3']]
level_1_3 = ['Покупка Сельскохоз. продукции', ['требования для 4']]
level_1_4 = ['Покупка товаров для гос. нужд', ['требования для 5']]
level_1_5 = ['Договор поставки ст.', ['требования для 6']]
level_1_6 = ['Договор розничной купли-продажи', ['требования для 7']]
level_1_7 = ['Договор купли-продажи в соответствии с общей частью', [level_1_7_0]]
schemeName = """Дело связанное с правом купли-продажи\n
Признаки: ... \n"""
level_1 = [level_1_0, level_1_1, level_1_2, level_1_3, level_1_4, level_1_5, level_1_6, level_1_7]
level_0 = [schemeName, level_1]
