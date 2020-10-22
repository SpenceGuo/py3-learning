"""
Python3 XML 解析
什么是 XML？
XML 指可扩展标记语言（eXtensible Markup Language），标准通用标记语言的子集，
    是一种用于标记电子文件使其具有结构性的标记语言。 你可以通过本站学习 XML 教程

XML 被设计用来传输和存储数据。

XML 是一套定义语义标记的规则，这些标记将文档分成许多部件并对这些部件加以标识。

它也是元标记语言，即定义了用于定义其他与特定领域有关的、语义的、结构化的标记语言的句法语言。

Python 对 XML 的解析
常见的 XML 编程接口有 DOM 和 SAX，这两种接口处理 XML 文件的方式不同，当然使用场合也不同。

Python 有三种方法解析 XML，SAX，DOM，以及 ElementTree:
1.SAX (simple API for XML )
    Python 标准库包含 SAX 解析器，SAX 用事件驱动模型，通过在解析 XML 的过程中触发一个个的事件
    并调用用户定义的回调函数来处理 XML 文件。

2.DOM(Document Object Model)
    将 XML 数据在内存中解析成一个树，通过对树的操作来操作 XML。
"""