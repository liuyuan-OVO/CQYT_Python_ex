while True:
    data = [['xiaoming{}'.format(i),
             'xianming{}@china.com'.format(i),
             'pwd{}'.format(i)] for i in range(1,202)
            ]
    page = int(input('请输入页码：'))
    for j in range((page - 1) * 10, page * 10):
        print(data[j])