from struct import unpack

class Unpacker:
    def __init__(self, buffer=b''):
        self.buffer = buffer
        self.offset = 0

    def read_signed_char(self):
        """Range: -128 to 127"""
        value = unpack('!b', self.buffer[self.offset:self.offset+1])[0]
        self.offset += 1
        return value
    
    def read_unsigned_char(self):
        """Range: 0 to 255"""
        value = unpack('!B', self.buffer[self.offset:self.offset+1])[0]
        self.offset += 1
        return value
    
    def read_boolean(self):
        """Range: True or False"""
        value = unpack('!?', self.buffer[self.offset:self.offset+1])[0]
        self.offset += 1
        return value
    
    def read_short(self):
        """Range: -32768 to 32767"""
        value = unpack('!h', self.buffer[self.offset:self.offset+2])[0]
        self.offset += 2
        return value
    
    def read_unsigned_short(self):
        """Range: 0 to 65535"""
        value = unpack('!H', self.buffer[self.offset:self.offset+2])[0]
        self.offset += 2
        return value
    
    def read_int(self):
        """Range: -2147483648 to 2147483647"""
        value = unpack('!i', self.buffer[self.offset:self.offset+4])[0]
        self.offset += 4
        return value
    
    def read_unsigned_int(self):
        """Range: 0 to 4294967295"""
        value = unpack('!I', self.buffer[self.offset:self.offset+4])[0]
        self.offset += 4
        return value
    
    def read_long(self):
        """Range: -2147483648 to 2147483647"""
        value = unpack('!l', self.buffer[self.offset:self.offset+4])[0]
        self.offset += 4
        return value
    
    def read_unsigned_long(self):
        """Range: 0 to 4294967295"""
        value = unpack('!L', self.buffer[self.offset:self.offset+4])[0]
        self.offset += 4
        return value
    
    def read_long_long(self):
        """Range: -9223372036854775808 to 9223372036854775807"""
        value = unpack('!q', self.buffer[self.offset:self.offset+8])[0]
        self.offset += 8
        return value
    
    def read_unsigned_long_long(self):
        """Range: 0 to 18446744073709551615"""
        value = unpack('!Q', self.buffer[self.offset:self.offset+8])[0]
        self.offset += 8
        return value
    
    def read_float(self):
        """Range: 1.2e-38 to 3.4e+38"""
        value = unpack('!f', self.buffer[self.offset:self.offset+4])[0]
        self.offset += 4
        return value
    
    def read_double(self):
        """Range: 2.3e-308 to 1.7e+308"""
        value = unpack('!d', self.buffer[self.offset:self.offset+8])[0]
        self.offset += 8
        return value
    
    def read_string(self):
        """Range: 0 to 65535"""
        length = self.read_unsigned_short()
        value = self.buffer[self.offset:self.offset+length].decode('utf-8')
        self.offset += length
        return value
    
    def get_buffer(self):
        """Returns the remaining buffer"""
        return self.buffer[self.offset:]
    
    def get_buffer_all(self):
        """Returns the whole buffer"""
        return self.buffer
    
    def get_offset(self):
        """Returns the current offset"""
        return self.offset