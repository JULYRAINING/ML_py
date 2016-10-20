#coding:utf-8
class classifier:
    def __init__(self, getfeatures):
        # Counts of feature/category combinations
        self.fc = {}
        # Counts of documents in each category
        self.cc = {}
        self.getfeatures = getfeatures
        
    #增加对特征/分类组合的计数值
    def incf(self, f, cat):
        self.fc.setdefault(f, {})
        self.fc[f].setdefault(cat, {})
        self.fc[f][cat] += 1
    
    #增加某一个分类的计数值:
    def incc(self, cat):
        self.cc.setdefault(cat, {})
        self.cc[cat] += 1
    
    #计算某一个特征在某一个分类中出现的次数
    def fcount(self, f, cat):
        if f in self.fc and cat in self.fc[f]:
            return self.fc[f][cat]
        else:
            return 0.0
    #属于某一个分类的文档总数
    def catcount(self, cat):
        if cat in self.cc:
            return self.cc[cat]
        return 0
    #所有的文档总数
    def totalcount(self):
        return sum(self.cc.values())
    #所有文档的种类
    def categories(self):
        return self.cc.keys()
    
    def train(self, item, cat):
        features = self.getfeatures(item)
        # 针对该分类，为每个特征增加计数值
        for f in features:
            self.incf(f, cat)

    # 增加该分类的计数值
        self.incc(cat)