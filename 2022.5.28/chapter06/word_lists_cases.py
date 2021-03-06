from collections import OrderedDict

word_lists = OrderedDict()

word_lists['if'] = '通过一条或多条语句的执行结果（True或者False）来决定执行的代码块'
word_lists['for'] = 'for循环可以遍历任何序列的项目'
word_lists['sort'] = '以字母顺序对列表进行排序'
word_lists['list'] = '有序且可更改的集合'
word_lists['dict'] = '一个无序、可变和有索引的集合。在 Python 中，字典用花括号编写，拥有键和值'
word_lists['set'] = '创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等'
word_lists['in'] = '用于检查序列（列表、范围、字符串等）中是否存在值，还用于在 for 循环中迭代序列'
word_lists['tuple'] = '元组是有序且不可更改的集合，用圆括号编写'
word_lists['and'] = '用于组合条件语句，如果两条语句都返回 True，则返回值将为 True，否则返回 False'
word_lists['del'] = '用于删除对象。在 Python，一切都是对象，因此 del 关键字可用于删除变量、列表或列表片段等'

for word, meaning in word_lists.items():
    print(word + "\n\t" + meaning)
