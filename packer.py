from struct import pack

class Packer:
    def __init__(self):
        self.buffer = bytearray()
    
    def write_signed_char(self, value):
        """Range: -128 to 127"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!b', int(value)))

    def write_unsigned_char(self, value):
        """Range: 0 to 255"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!B', int(value)))

    def write_boolean(self, value):
        """Range: True or False"""
        if not isinstance(value, bool):
            raise TypeError("value must be a boolean")
        
        self.buffer.extend(pack('!?', int(value)))

    def write_short(self, value):
        """Range: -32768 to 32767"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!h', int(value)))

    def write_unsigned_short(self, value):
        """Range: 0 to 65535"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!H', int(value)))

    def write_int(self, value):
        """Range: -2147483648 to 2147483647"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!i', int(value)))

    def write_unsigned_int(self, value):
        """Range: 0 to 4294967295"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!I', int(value)))

    def write_long(self, value):
        """Range: -2147483648 to 2147483647"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!l', int(value)))

    def write_unsigned_long(self, value):
        """Range: 0 to 4294967295"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!L', int(value)))

    def write_long_long(self, value):
        """Range: -9223372036854775808 to 9223372036854775807"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!q', int(value)))

    def write_unsigned_long_long(self, value):
        """Range: 0 to 18446744073709551615"""
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        
        self.buffer.extend(pack('!Q', int(value)))

    def write_float(self, value):
        """Range: 1.2E-38 to 3.4E+38"""
        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, float):
            raise TypeError("value must be a float")
            
        self.buffer.extend(pack('!f', float(value)))

    def write_double(self, value):
        """Range: 2.3E-308 to 1.7E+308"""
        if isinstance(value, int):
            value = float(value)

        if not isinstance(value, float):
            raise TypeError("value must be a float")
        
        self.buffer.extend(pack('!d', float(value)))

    def write_string(self, value):
        """Write a string to the buffer"""
        if not isinstance(value, str):
            raise TypeError("value must be a string")
        
        size = len(value)
        self.write_short(size)
        
        value = value.encode("utf-8")
        self.write(value)

    def write(self, value):
        """Write bytes to the buffer"""
        if isinstance(value, str):
            value = value.encode("utf-8")

        if not isinstance(value, bytes):
            raise TypeError("value must be a bytes")
        
        self.buffer.extend(value)

    def get_buffer(self):
        """Return the buffer as bytes"""
        return bytes(self.buffer)