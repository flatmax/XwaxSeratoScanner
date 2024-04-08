class Entry:
    def __init__(self, dat):
        self.data = {}
        if dat[0]=='otrk':
            for t in dat[1]:
                # if len(t) != 2:
                #     print(t)
                #     print('not of length 2, not parsing\n')
                # else:
                    self.data[t[0]] = t[1];
        # else:
        #     print('item ')
        #     print(dat)
        #     print('not ortk, not parsing\n')
        # print(self.data)

    def getFileName(self):
        if 'pfil' in self.data:
            return self.data['pfil']
        else:
            return None

    def getField(self, fn):
        if fn in self.data:
            return self.data[fn]
        else:
            return ''

    def getArtist(self):
        return self.getField('tart')

    def getSongName(self):
        return self.getField('tsng')

    def getComment(self):
        return self.getField('tcom')

    def getBPM(self):
        return self.getField('tbpm')

    def printXwaxFormat(self):
        print(self.getFileName()+'\t'+self.getArtist()+'\t'+self.getComment()+' | '+self.getSongName()+'\t'+self.getBPM())
        # dat='"'+self.getFileName()+'" "' + self.getArtist()+ '"'
        # print(dat)
        # return dat
