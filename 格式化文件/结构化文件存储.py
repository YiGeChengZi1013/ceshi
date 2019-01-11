# encoding=utf-8

"""
结构化文件存储
    xml, json
    为了解决不同设备之间的信息交换

    xml 可扩展标记语言
        标记语言,语言中使用尖括号括起来的文本字符标记
        可扩展,用户可以自己定义需要的标记
        例如:
        <there>
            ..........
        </there>
        是w3c组织制定的一个标准
        xml描述的是数据本身,数据的结构和语义
        html则侧重于如何显示web页面中的数据
    xml文档的构成
        处理指令(可以认为一个文件内只有一个处理指令)
            最多只有一行
            且必须在第一行
            内容是与xml本身处理器相关的一些声明或者指令
            以xml关键字开头
            在xml文件中只能出现一次并且必须在头部
                一般用于声明xml的版本和采用的编码
                version属性是必须有的
                encoding属性用来指出xml解释器使用的编码
        根元素(一个文件内只有一个根元素)
            在整个xml文件中,可以把他看作一个树形结构,
            根元素有且只能有一个
        子元素

        属性
        内容
            表明标签所存储的信息
        注释
            说明作用的信息
            注释不能嵌套在标签中
            只有在注释的开始和结尾使用双短横线,内容中间不能有双横线和三横线
            三短短横线只能出现在注释的开头而不能用在结尾
                <!---      -->(前面3个,后面只能出项两个)
                <!--       -->
        保留字符前的处理
            xml中使用的符号可能跟实际符号相冲突,典型的就是左右尖括号
            使用实体应用(entityreference)来表示保留字符(可以理解为转义字符)
            把含有保留字符的前部分放在CDATA块内部,CDATA块把内部信息视为不需要转义
            常用的需要转义的保留字符和对应实体应用
                字符名称     字符   	实体引用
                和	        &	    &amp;
                大于号	    > 	    &gt;
                小于号	    < 	    &lt;
                单引号	    ‘	    &apos;
                双引号	    “	    &quot;

    xml标签的命名规则
        Pascal命名法
        用单词表示,第一个单词大写
        大小写严格区分
        配对的标签必须一致

    命名空间
        为了防止命名冲突
        为了避免冲突,需要给可能冲突元素添加命名空间
        xmlns : xml name space 的缩写

            <school xmlns:student="http://my_student" xmlns:room="http://my_name">
                <student:nanme> </student:name>

    xml访问
        读取
            xml读取分两个主要技术,SAX,DOM
            SAX (simple API for xml):
                基于事件驱动的API
                利用SAX解析文档设计到解析器和事件处理两部分
                特点:
                    块,流式读取
            DOM
                是W3C规定 的xml编程接口
                一个xml文件在缓存中以树状结构保存,读取.
                用途:
                    定位浏览xml任何节点信息
                    添加删除相应的内容
                    minidom
                        minidom.parse(filename):加载读取的xml文件, filename也可以是xml代码
                        doc.documentElement:获取xml文档对象，一个xml文件只有一个对于的文档对象
                        node.getAttribute(attr_name):获取xml节点的属性值
                        node.getElementByTagName(tage_name)：得到一个节点对象集合
                        node.childNodes:得到所有孩子节点
                        node.childNodes[index].nodeValue:获取单个节点值
                        node.firstNode:得到第一个节点，等价于node.childNodes[0]
                        node.attributes[tage_name]



    json:




"""