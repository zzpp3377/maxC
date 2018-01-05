
class Path():
    """the Path class presents the path of streams"""

    def __init__(self,load,route):
        self.path_load=load
        self.swports=[]
        self.route=route

    def getSrc(self):
        return self.swports[0].coord

    def getDst(self):
        return self.swports[-1].coord


    
