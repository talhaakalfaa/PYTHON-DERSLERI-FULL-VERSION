class Class:
    def __init__(self,id,name,teacherid):
        self.id = id
        self.name = name
        self.teacherid = teacherid

    @staticmethod
    def CreateClass(obj):
        list = []

        for i in obj:
            list.append(Class(i[0],i[1],i[2]))

        return list