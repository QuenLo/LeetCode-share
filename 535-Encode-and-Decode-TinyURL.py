class Codec:
    
    alphabet = string.ascii_letters + '0123456789'
    
    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        while longUrl not in self.url2code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(5) )
            if code not in self.code2url:
                self.code2url[ code ] = longUrl
                self.url2code[ longUrl ] = code
        return "http://tinyurl.com/" + self.url2code[ longUrl ]
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL."""
        return self.code2url[shortUrl[-5:]]


# solution by counter
class Codec_counter:
    
    def __init__(self):
        self.code2url = {}
        self.url2code = {}
        self.count = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        while longUrl not in self.url2code:
            self.count += 1
            self.code2url[str(self.count)] = longUrl
            self.url2code[longUrl] = str(self.count)

        return "http://tinyurl.com/" + str(self.count)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL."""
        return self.code2url[shortUrl.split('/')[-1]]

# solution by uuid3
import uuid
class Codec_uuid3:
    
    def __init__(self):
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        code = uuid.uuid3(uuid.NAMESPACE_URL,str(longUrl))
        self.code2url[ str(code) ] = longUrl

        return "http://tinyurl.com/" + str(code)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL."""
        return self.code2url[shortUrl.split('/')[-1]]

# solution by uuid4
import uuid
class Codec_uuid4:
    
    #alphabet = string.ascii_letters + '0123456789'
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    def __init__(self):
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL."""
        code = uuid.uuid4()
        self.code2url[ str(code) ] = longUrl

        return "http://tinyurl.com/" + str(code)
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL."""
        return self.code2url[shortUrl.split('/')[-1]]
