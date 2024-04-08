import struct

class SeratoData:
    def __init__(self):
        self.DECODE_FUNC_FULL = {
          None: self.decode_struct,
          'vrsn': self.decode_unicode,
          'sbav': self.noop,
        }

        self.DECODE_FUNC_FIRST = {
          'o': self.decode_struct,
          't': self.decode_unicode,
          'p': self.decode_unicode,
          'u': self.decode_unsigned,
          'b': self.noop,
        }

    def decode_struct(self, data):
        ret = []
        i = 0
        while i < len(data):
            tag = data[i:i+4].decode('ascii')
            length = struct.unpack('>I', data[i+4:i+8])[0]
            value = data[i+8:i+8+length]
            value = self.decode(value, tag=tag)
            ret.append((tag, value))
            i += 8 + length
        return ret

    def decode_unicode(self, data):
        return data.decode('utf-16-be')

    def decode_unsigned(self, data):
        return struct.unpack('>I', data)[0]

    def noop(self, data):
        return data

    def decode(self, data, tag=None):
        if tag in self.DECODE_FUNC_FULL:
            decode_func = self.DECODE_FUNC_FULL[tag]
        else:
            decode_func = self.DECODE_FUNC_FIRST[tag[0]]

        return decode_func(data)


    def loadFile(self, fname):
      with open(fname, 'rb') as f:
        return self.decode(f.read())
