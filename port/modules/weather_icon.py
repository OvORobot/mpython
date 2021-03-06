from micropython import const

WIDTH=const(38)
HEIGHT=const(38)

# 晴,code 0/2
sunny=\
b'\x00\x00\x00\x00\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00'\
b'\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x03\xC0'\
b'\x78\x07\x00\x03\xE0\x78\x0F\x00\x03\xE0\x00\x1F\x00\x01\xF0\x00'\
b'\x3F\x00\x00\xF1\xFE\x3C\x00\x00\x63\xFF\x18\x00\x00\x0F\xFF\xC0'\
b'\x00\x00\x0F\xFF\xC0\x00\x00\x1F\x87\xE0\x00\x00\x3E\x01\xF0\x00'\
b'\x00\x3E\x00\xF0\x00\x7F\x3C\x00\xF3\xF8\x7F\x3C\x00\xF3\xF8\x7F'\
b'\x3C\x00\xF3\xF8\x7F\x3C\x00\xF3\xF8\x00\x3E\x00\xF0\x00\x00\x3E'\
b'\x01\xF0\x00\x00\x1F\x83\xE0\x00\x00\x0F\xFF\xC0\x00\x00\x0F\xFF'\
b'\xC0\x00\x00\x63\xFF\x18\x00\x00\xF1\xFE\x3C\x00\x01\xF0\x00\x3E'\
b'\x00\x03\xE0\x00\x1F\x00\x03\xE0\x78\x0F\x00\x03\xC0\x78\x07\x00'\
b'\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00'\
b'\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00\x00\x00\x00\x00'\


# 晴,code 1/3
clear= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7C\x00\x00\x00'\
b'\x07\xFE\x00\x00\x00\x1F\xFE\x00\x00\x00\x7F\xFE\x00\x00\x00\xFF'\
b'\xFE\x00\x00\x01\xFF\xBE\x00\x00\x03\xFC\x3E\x00\x00\x07\xF8\x1F'\
b'\x00\x00\x07\xF0\x1F\x00\x00\x0F\xE0\x1F\x80\x00\x0F\xC0\x0F\xC0'\
b'\x00\x1F\x80\x0F\xE0\x00\x1F\x80\x07\xF8\x00\x1F\x00\x03\xFF\x00'\
b'\x1F\x00\x01\xFF\xE0\x1F\x00\x00\xFF\xE0\x1F\x00\x00\x3F\xE0\x1F'\
b'\x00\x00\x0F\xE0\x1F\x00\x00\x01\xE0\x1F\x00\x00\x03\xE0\x1F\x00'\
b'\x00\x03\xE0\x1F\x80\x00\x03\xE0\x1F\x80\x00\x07\xE0\x0F\xC0\x00'\
b'\x0F\xC0\x0F\xE0\x00\x0F\xC0\x07\xF0\x00\x3F\x80\x07\xF8\x00\x7F'\
b'\x80\x03\xFE\x01\xFF\x00\x01\xFF\xCF\xFE\x00\x00\xFF\xFF\xFC\x00'\
b'\x00\x7F\xFF\xF8\x00\x00\x1F\xFF\xE0\x00\x00\x07\xFF\x80\x00\x00'\
b'\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\


# 多云,code 4
cloud= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x07\xFC\x00\x00\x00\x0F\xFF\x00\x00\x00\x3F\xFF'\
b'\x80\x00\x00\x3F\xBF\xC0\x00\x00\x7E\x07\xE0\x00\x00\xF8\x03\xE0'\
b'\x00\x00\xF8\x01\xF0\x00\x01\xF0\x00\xFE\x00\x07\xF0\x00\xFF\x80'\
b'\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\xFF\xE0\x3F\x00\x00\x03\xF0\x3E'\
b'\x00\x00\x01\xF0\x3C\x00\x00\x00\xF0\x3C\x00\x00\x00\xF0\x38\x00'\
b'\x00\x00\x70\x38\x00\x00\x00\x70\x3C\x00\x00\x00\xF0\x3C\x00\x00'\
b'\x00\xF0\x3E\x00\x00\x01\xF0\x1F\xC0\x00\x0F\xE0\x1F\xFF\xFF\xFF'\
b'\xE0\x07\xFF\xFF\xFF\xC0\x03\xFF\xFF\xFF\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\


# 晴间多云,code 5
day_partly_cloudy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00'\
b'\x00\x38\x00\x00\x00\x00\x38\x00\x00\x00\x00\x38\x00\x00\x00\x00'\
b'\x38\x00\x00\x03\x80\x38\x03\x00\x03\xC0\x38\x07\x80\x03\xE0\x10'\
b'\x0F\x80\x03\xF0\x00\x1F\x80\x01\xF0\x30\x1F\x00\x00\xF1\xFF\x1E'\
b'\x00\x00\x07\xFF\xC0\x00\x00\x0F\xFF\xE0\x00\x00\x0F\xC7\xE0\x00'\
b'\x00\x1F\x01\xF0\x00\x00\x1E\x00\xF0\x00\x00\x3E\x00\xF8\x00\x7E'\
b'\x3C\x00\x79\xF8\x7E\x3F\x80\x79\xF8\x7E\x7F\xC0\x79\xF8\x3C\xFF'\
b'\xE0\xF8\xF0\x00\xFF\xF0\xF0\x00\x01\xF1\xFD\xF0\x00\x07\xF0\xFF'\
b'\xF0\x00\x0F\xE0\xFF\xE0\x00\x0F\xE0\x7F\xC0\x00\x0F\x80\x0F\x9C'\
b'\x00\x0F\x00\x07\x9E\x00\x0F\x00\x07\x9F\x00\x0F\x80\x0F\x9F\x80'\
b'\x0F\xFF\xFF\x8F\x80\x07\xFF\xFF\x07\x80\x03\xFF\xFE\x00\x00\x00'\
b'\xFF\xF8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 夜晚晴间多云,code 6
night_partly_cloudy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1F\xF0\x00\x00'\
b'\x00\x7F\xF8\x00\x00\x01\xFF\xF8\x00\x00\x03\xFF\xF8\x00\x00\x07'\
b'\xFF\xF8\x00\x00\x07\xF8\xF8\x00\x00\x0F\xE0\xF8\x00\x00\x1F\xC0'\
b'\xFC\x00\x00\x1F\x80\xFC\x00\x00\x1F\x80\x7E\x00\x00\x1F\x00\x7E'\
b'\x00\x00\x1F\x00\x7F\x00\x00\x3F\xE0\x3F\xC0\x00\x3F\xF8\x1F\xF8'\
b'\x00\x7F\xFC\x0F\xF8\x00\xFF\xFE\x07\xF8\x01\xFF\xFF\x03\xF8\x01'\
b'\xFC\x7F\x03\xF0\x03\xF8\x3F\xE7\xF0\x0F\xF0\x1F\xFF\xE0\x1F\xE0'\
b'\x1F\xFF\xE0\x3F\xE0\x0F\xFF\xC0\x3F\xE0\x0F\xFF\x80\x7F\x80\x00'\
b'\xFF\x00\x7E\x00\x00\x3F\x00\x7E\x00\x00\x3F\x00\x7E\x00\x00\x3F'\
b'\x00\x7E\x00\x00\x3F\x00\x7F\x00\x00\xFE\x00\x3F\xFF\xFF\xFE\x00'\
b'\x3F\xFF\xFF\xFE\x00\x1F\xFF\xFF\xFC\x00\x0F\xFF\xFF\xF8\x00\x07'\
b'\xFF\xFF\xE0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\


# 夜晚大部多云,code 7
night_cloudy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3E\x00\x00\x00'\
b'\x01\xFF\x00\x00\x00\x03\xFF\x00\x00\x00\x07\xFF\x00\x00\x0F\xFF'\
b'\xEF\x00\x00\x1F\xFF\x8F\x00\x00\x3F\xFF\x0F\x80\x00\x7F\x3F\x87'\
b'\x80\x00\xFC\x0F\xC7\xE0\x00\xF0\x03\xC3\xF8\x01\xF0\x03\xE3\xF8'\
b'\x03\xE0\x01\xFE\xF8\x0F\xE0\x01\xFF\xF0\x1F\xE0\x01\xFF\xF0\x3F'\
b'\xE0\x01\xFF\xE0\x3E\x00\x00\x07\xE0\x7C\x00\x00\x03\xE0\x78\x00'\
b'\x00\x01\xE0\x78\x00\x00\x01\xE0\x78\x00\x00\x00\xE0\x78\x00\x00'\
b'\x01\xE0\x78\x00\x00\x01\xE0\x7C\x00\x00\x03\xE0\x3F\x00\x00\x07'\
b'\xC0\x1F\xFF\xFF\xFF\xC0\x1F\xFF\xFF\xFF\x80\x07\xFF\xFF\xFF\x00'\
b'\x01\xFF\xFF\xF8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 日间大部多云,code 8
day_cloudy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x07\x00\x00\x00\x00'\
b'\x07\x00\x00\x00\x00\x07\x00\x00\x00\x0C\x07\x01\x80\x00\x0F\x07'\
b'\x03\xC0\x00\x0F\x00\x07\xC0\x00\x0F\x00\x0F\x80\x00\x00\x1F\xC7'\
b'\x00\x00\x1F\xBF\xF2\x00\x00\x7F\xFF\xF8\x00\x00\xFF\xF8\xF8\x00'\
b'\x01\xFF\xF8\x3C\x00\x03\xE0\x78\x3C\x00\x03\xC0\x3C\x1C\xF8\x07'\
b'\x80\x3F\x1C\xF8\x1F\x80\x1F\xFC\xF8\x3F\x80\x1F\xFC\x00\x7F\x00'\
b'\x1F\xFC\x00\x78\x00\x00\xF8\x00\x78\x00\x00\x78\x00\x70\x00\x00'\
b'\x38\x00\x70\x00\x00\x3B\x80\x70\x00\x00\x3B\x80\x78\x00\x00\x7B'\
b'\xC0\x7C\x00\x00\xFB\x80\x3F\xFF\xFF\xF0\x00\x3F\xFF\xFF\xE0\x00'\
b'\x0F\xFF\xFF\xC0\x00\x01\xFF\xFE\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 '\


# 阴天,code 9
cloudy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x0F\xC0\x00\x00\x00\x3F\xF0\x00\x00\x00\x7F'\
b'\xF8\x00\x00\x07\x7C\xFC\x00\x00\x3F\xF8\x3C\x00\x00\x7F\xF0\x1F'\
b'\x00\x00\xFF\xF8\x1F\xC0\x01\xF0\x7C\x0F\xE0\x01\xE0\x3E\x0F\xF0'\
b'\x03\xC0\x1E\x00\xF8\x0F\xC0\x1F\xE0\x78\x1F\x80\x0F\xF0\x38\x3F'\
b'\x80\x0F\xF8\x78\x3C\x00\x00\x78\x78\x78\x00\x00\x3C\xF8\x78\x00'\
b'\x00\x3F\xF0\x70\x00\x00\x1F\xE0\x70\x00\x00\x1F\xC0\x78\x00\x00'\
b'\x3C\x00\x7C\x00\x00\x7C\x00\x3F\x00\x00\xF8\x00\x1F\xFF\xFF\xF8'\
b'\x00\x0F\xFF\xFF\xF0\x00\x07\xFF\xFF\xC0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 下雨,code 10 11  19 
shower= \
b'\x00\x00\x00\x00\x00\x00\x00\xE0\x00\x00\x00\x07\xFE\x00\x00\x00'\
b'\x1F\xFF\x00\x00\x00\x3F\xFF\xC0\x00\x00\x7F\x9F\xC0\x00\x00\x7C'\
b'\x07\xE0\x00\x00\xF8\x01\xF0\x00\x00\xF0\x01\xF0\x00\x01\xF0\x00'\
b'\xFE\x00\x07\xE0\x00\xFF\x80\x0F\xE0\x00\xFF\xE0\x1F\xE0\x00\x7F'\
b'\xE0\x3F\x00\x00\x03\xF0\x3E\x00\x00\x00\xF0\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78\x07\x80\xF0\x78\x78'\
b'\x07\x80\xF0\x78\x7C\x0F\x80\xF0\xF8\x3E\x0F\x00\xF1\xF0\x3F\x07'\
b'\x00\xE3\xF0\x1F\xC0\x38\x0F\xE0\x0F\xC0\x78\x0F\xC0\x07\xC0\x78'\
b'\x0F\x80\x01\xDC\x7B\xCE\x00\x00\x3C\x73\xC0\x00\x00\x3C\x27\xC0'\
b'\x00\x00\x3C\x07\x80\x00\x00\x3C\x03\x80\x00\x00\x01\xC0\x00\x00'\
b'\x00\x01\xE0\x00\x00\x00\x01\xE0\x00\x00\x00\x03\xE0\x00\x00\x00'\
b'\x01\xC0\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00'\


# 雷阵雨伴有冰雹,code 12
shower_hail= \
b'\x00\x00\x00\x00\x00\x00\x00\xF0\x00\x00\x00\x07\xFE\x00\x00\x00'\
b'\x1F\xFF\x00\x00\x00\x3F\xFF\xC0\x00\x00\x7F\x1F\xC0\x00\x00\xFC'\
b'\x07\xE0\x00\x00\xF8\x01\xF0\x00\x00\xF0\x01\xF0\x00\x01\xF0\x00'\
b'\xFE\x00\x07\xE0\x00\xFF\x80\x1F\xE0\x00\xFF\xE0\x1F\xE0\x00\x7F'\
b'\xE0\x3F\x00\x00\x03\xF0\x3E\x00\x00\x01\xF0\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78\x07\x9C\xF0\x78\x78'\
b'\x07\xBC\xF0\x78\x7C\x0F\xBC\xF0\xF8\x3E\x0F\x3D\xF1\xF0\x3F\x0F'\
b'\x3D\xE3\xF0\x1F\xCF\x79\xEF\xE0\x0F\xDF\x79\xEF\xC0\x07\xDE\x79'\
b'\xEF\x80\x01\xCE\xF9\xCE\x00\x00\x00\xF0\x00\x00\x00\x3C\xF3\x80'\
b'\x00\x00\x3C\xF7\x80\x00\x00\x3C\xF3\x80\x00\x00\x00\xE0\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\xC0\x00\x00\x00\x03\xC0\x00\x00\x00'\
b'\x03\xC0\x00\x00\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00'\


# 小雨,code 13
light_rain= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\xF0\x00\x00\x00\x07\xFE\x00\x00\x00\x1F'\
b'\xFF\x00\x00\x00\x3F\xFF\xC0\x00\x00\x7F\x1F\xC0\x00\x00\x7C\x07'\
b'\xE0\x00\x00\xF8\x01\xF0\x00\x00\xF0\x01\xF0\x00\x01\xF0\x00\xFE'\
b'\x00\x07\xE0\x00\xFF\x80\x1F\xE0\x00\xFF\xE0\x1F\xE0\x1C\x7F\xE0'\
b'\x3F\x00\x1C\x03\xF0\x3C\x00\x1E\x01\xF0\x7C\x06\x1E\x00\xF8\x78'\
b'\x0F\x1C\x00\x78\x78\x0F\x00\x00\x78\x78\x1F\x80\x00\x78\x78\x1F'\
b'\x88\x00\x78\x7C\x1F\x9C\x00\xF8\x3E\x0F\x3E\x01\xF0\x3F\x00\x7F'\
b'\x03\xF0\x1F\xC0\x7F\x0F\xE0\x0F\xC0\xFF\x8F\xC0\x07\xC0\xFF\x8F'\
b'\x80\x01\xC0\xFF\x8E\x00\x00\x00\xFF\x80\x00\x00\x00\xFF\x00\x00'\
b'\x00\x00\x7F\x00\x00\x00\x00\x1C\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 中雨 ,code 14
moderate_rain= \
b'\x00\x00\x00\x00\x00\x00\x01\xF8\x00\x00\x00\x0F\xFE\x00\x00\x00'\
b'\x1F\xFF\x80\x00\x00\x3F\xFF\xC0\x00\x00\x7F\x0F\xE0\x00\x00\xFC'\
b'\x03\xE0\x00\x00\xF8\x01\xF0\x00\x00\xF0\x01\xF0\x00\x03\xF0\x00'\
b'\xFF\x00\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\xFF\xE0\x3F\xE0\x00\x7F'\
b'\xF0\x3F\x00\x00\x03\xF0\x7C\x00\x00\x00\xF8\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x03\x00\x00\x78\x78\x07\x80\xF0\x78\x78'\
b'\x07\x80\xF0\x78\x7C\x0F\x80\xF0\xF8\x3E\x0F\x00\xF1\xF0\x3F\x87'\
b'\x00\xE7\xF0\x1F\xCE\x79\xCF\xE0\x0F\xDE\x79\xCF\xC0\x07\xCE\x79'\
b'\xCF\x80\x00\xC4\x78\x8C\x00\x00\x1C\x73\x80\x00\x00\x3C\xE3\x80'\
b'\x00\x00\x3C\xE7\x80\x00\x00\x3C\xE3\x80\x00\x00\x18\xE3\x00\x00'\
b'\x00\x01\xC0\x00\x00\x00\x01\xC0\x00\x00\x00\x03\xC0\x00\x00\x00'\
b'\x03\xC0\x00\x00\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00'\

# 大雨,code 15
heavy_rain= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xFE\x00\x00\x00'\
b'\x1F\xFF\x00\x00\x00\x3F\xFF\x80\x00\x00\x7F\xBF\xC0\x00\x00\x7C'\
b'\x07\xE0\x00\x00\xF8\x03\xE0\x00\x00\xF0\x01\xF0\x00\x01\xF0\x00'\
b'\xFE\x00\x07\xE0\x00\xFF\x80\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\x7F'\
b'\xE0\x3F\x00\x00\x03\xF0\x3E\x00\x00\x01\xF0\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78\x07\x1C\xF0\x78\x78'\
b'\x07\xBC\xF0\x78\x7C\x0F\xBC\xF0\xF8\x7E\x0F\x3D\xF1\xF0\x3F\x0F'\
b'\x3D\xE3\xF0\x1F\xCF\x7D\xEF\xE0\x1F\xDF\x79\xEF\xE0\x07\xDE\x7B'\
b'\xEF\x80\x01\xDE\xFB\xCE\x00\x00\x3E\xF3\xC0\x00\x00\x3C\xF7\xC0'\
b'\x00\x00\x3C\xF7\x80\x00\x00\x3D\xF3\x80\x00\x00\x01\xE0\x00\x00'\
b'\x00\x01\xE0\x00\x00\x00\x03\xE0\x00\x00\x00\x03\xC0\x00\x00\x00'\
b'\x01\xC0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 暴雨,code 16~18
storm= \
b'\x00\x00\x00\x00\x00\x00\x01\xF8\x00\x00\x00\x0F\xFE\x00\x00\x00'\
b'\x1F\xFF\x80\x00\x00\x3F\xFF\xC0\x00\x00\x7F\x0F\xE0\x00\x00\xFC'\
b'\x03\xE0\x00\x00\xF8\x01\xF0\x00\x00\xF0\x01\xF0\x00\x03\xF0\x00'\
b'\xFF\x00\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\xFF\xE0\x3F\xE0\x00\x7F'\
b'\xF0\x3F\x00\x00\x03\xF0\x7C\x00\x00\x00\xF8\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x08\x20\x78\x78\x3F\x1C\xF0\x78\x78'\
b'\x7F\x3C\xF0\x78\x7C\x7F\x3C\xF0\xF8\x3E\xFE\x3D\xF1\xF0\x3F\xFC'\
b'\x3D\xE7\xF0\x1F\xFC\x79\xEF\xE0\x0F\xF8\x79\xEF\xC0\x07\xF8\x7B'\
b'\xEF\x80\x01\xFF\xFB\xCC\x00\x03\xFF\xF3\xC0\x00\x03\xFE\xF3\xC0'\
b'\x00\x00\x3C\xF3\xC0\x00\x00\x7D\xF3\x80\x00\x00\x79\xE0\x00\x00'\
b'\x00\x71\xE0\x00\x00\x00\x71\xE0\x00\x00\x00\xE1\xE0\x00\x00\x00'\
b'\xC1\xC0\x00\x00\x00\xC0\x00\x00\x00\x00\x00\x00\x00\x00'\

# 雨夹雪 ,code 20
sleet= \
b'\x00\x00\x00\x00\x00\x00\x01\xF8\x00\x00\x00\x0F\xFE\x00\x00\x00'\
b'\x1F\xFF\x80\x00\x00\x3F\xFF\xC0\x00\x00\x7F\x0F\xE0\x00\x00\xFC'\
b'\x03\xE0\x00\x00\xF8\x01\xF0\x00\x00\xF0\x01\xF0\x00\x03\xF0\x00'\
b'\xFF\x00\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\xFF\xE0\x3F\xE0\x00\x7F'\
b'\xF0\x3F\x00\x00\x03\xF0\x7C\x00\x00\x00\xF8\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78'\
b'\x00\x00\x00\x78\x7C\x00\x00\x00\xF8\x3E\x00\x00\x01\xF0\x3F\x80'\
b'\x00\x07\xF0\x1F\xCE\x79\xCF\xE0\x0F\xDE\x79\xCF\xC0\x07\xCE\x79'\
b'\xCF\x80\x00\x4C\x79\x8C\x00\x00\x1C\x73\x80\x00\x00\x3C\xE7\x80'\
b'\x00\x00\x3C\xE7\x80\x00\x00\x3C\xE7\x80\x00\x00\x18\xE3\x00\x00'\
b'\x00\x01\xC0\x00\x00\x00\x03\xC0\x00\x00\x00\x03\xC0\x00\x00\x00'\
b'\x03\xC0\x00\x00\x00\x01\x80\x00\x00\x00\x00\x00\x00\x00'\

# 小中雪,code 21 22 23
snow= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xFC\x00\x00\x00'\
b'\x1F\xFF\x00\x00\x00\x3F\xFF\x80\x00\x00\x7F\x9F\xC0\x00\x00\x7C'\
b'\x07\xE0\x00\x00\xF8\x03\xE0\x00\x00\xF0\x01\xF0\x00\x01\xF0\x00'\
b'\xFC\x00\x07\xE0\x00\xFF\x80\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\x7F'\
b'\xE0\x3F\x00\x00\x03\xF0\x3E\x00\x00\x01\xF0\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78'\
b'\x00\x00\x00\x78\x7C\x00\x30\x00\xF8\x7C\x00\x78\x00\xF8\x3F\x00'\
b'\x78\x03\xF0\x3F\xCE\x79\xCF\xE0\x1F\xCF\x01\xCF\xE0\x0F\xCF\x01'\
b'\xCF\x80\x03\xCE\x31\xCF\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00'\
b'\x00\x00\x06\x79\xC0\x00\x00\x0E\x01\xC0\x00\x00\x0F\x01\xC0\x00'\
b'\x00\x0E\x01\xC0\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00'\
b'\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 大雪 ,code 24
heavy_snow= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xFC\x00\x00\x00'\
b'\x1F\xFF\x00\x00\x00\x3F\xFF\x80\x00\x00\x7F\x9F\xC0\x00\x00\x7C'\
b'\x07\xE0\x00\x00\xF8\x03\xE0\x00\x00\xF0\x01\xF0\x00\x01\xF0\x00'\
b'\xFC\x00\x07\xE0\x00\xFF\x80\x0F\xE0\x00\xFF\xC0\x1F\xE0\x00\x7F'\
b'\xE0\x3F\x00\x00\x03\xF0\x3E\x00\x00\x01\xF0\x7C\x00\x00\x00\xF8'\
b'\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78\x00\x00\x00\x78\x78'\
b'\x00\x00\x00\x78\x7C\x00\x30\x00\xF8\x7C\x00\x78\x00\xF8\x3F\x00'\
b'\x78\x03\xF0\x3F\xCE\x79\xCF\xE0\x1F\xCF\x01\xCF\xE0\x0F\xCF\x01'\
b'\xCF\x80\x03\xCE\x61\xCF\x00\x00\x00\x70\x00\x00\x00\x00\xF0\x00'\
b'\x00\x00\x18\x73\x00\x00\x00\x3C\x07\x80\x00\x00\x3C\x07\x80\x00'\
b'\x00\x1C\x07\x80\x00\x00\x01\xE0\x00\x00\x00\x01\xE0\x00\x00\x00'\
b'\x01\xE0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 沙尘暴,code 25~29
dust_storm= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x7F\xF3\xFF\xFE\x78\x7F\xFF\xFF\xFF\xF8\x7F\xFB\xFF'\
b'\xFE\xF8\x7F\xF3\xFF\xFE\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x01\xE7\xFF\x9F\xE0\x01\xEF\xFF\xBF\xE0\x03\xEF\xFF\xBF\xE0'\
b'\x01\xEF\xFF\xBF\xE0\x01\xE7\xFF\x9F\xE0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x3F\xFF\xCF\x3F\xF0\x7F\xFF\xEF\x7F\xF8\x7F\xFF'\
b'\xFF\xFF\xF8\x7F\xFF\xEF\x7F\xF0\x3F\xFF\xC6\x3F\xF0\x00\x00\x00'\
b'\x00\x00\x04\x1F\xF8\x7C\x00\x0F\x7F\xFD\xFF\x00\x1F\x7F\xFD\xFF'\
b'\x00\x1F\x7F\xFD\xFF\x00\x0F\x7F\xFD\xFF\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

#雾,code 30
foggy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\xFC\x00\x00\x00\x03\xFF\x00\x00\x00\x0F\xFF\x80\x00\x00\x1F\xFF'\
b'\xC0\x00\x00\x1F\x07\xE0\x00\x00\x3E\x01\xE0\x00\x00\x3C\x01\xE0'\
b'\x00\x00\xFC\x00\xFE\x00\x01\xF8\x00\xFF\x80\x03\xF8\x00\xFF\xC0'\
b'\x07\xC0\x00\x07\xC0\x07\x80\x00\x03\xC0\x07\x00\x00\x01\xC0\x00'\
b'\x00\x00\x00\x00\x07\xFF\xFF\xFF\xC0\x07\xFF\xFF\xFF\xC0\x07\xFF'\
b'\xFF\xFF\xC0\x00\x00\x00\x00\x00\x7F\xFF\xFF\xFC\x00\x7F\xFF\xFF'\
b'\xFE\x00\x7F\xFF\xFF\xFE\x00\x3F\xFF\xFF\xFC\x00\x00\x00\x00\x00'\
b'\x00\x01\xFF\xFF\xFF\xF8\x01\xFF\xFF\xFF\xF8\x00\xFF\xFF\xFF\xF8'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

#霾,code 31
haze= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x01\x80\x00\x00\x00\x03\x80\x00\x00\x00'\
b'\x03\x80\x00\x00\x00\x03\x80\x00\x00\x03\x83\x83\xC0\x00\x03\xC1'\
b'\x87\xC0\x00\x03\xC0\x07\x80\x00\x00\x0F\xE7\x00\x00\x07\xFF\xF8'\
b'\x00\x00\x1F\xFF\xF8\x00\x00\x3F\xFC\x3C\x00\x00\x7C\x3E\x1C\x00'\
b'\x00\x78\x1E\x1C\xF8\x00\xF0\x0F\x9C\xF8\x03\xF0\x0F\xFC\xF8\x07'\
b'\xE0\x07\xFC\x00\x07\xC0\x01\xFC\x00\x0F\x00\x00\x78\x00\x0E\x00'\
b'\x00\x38\x00\x07\xFF\xFF\xFB\x00\x0F\xFF\xFF\xFB\x80\x0F\xFF\xFF'\
b'\xFB\xC0\x00\x00\x00\x01\x80\x7F\xFF\xFF\xC0\x00\x7F\xFF\xFF\xC0'\
b'\x00\x7F\xFF\xFF\xC0\x00\x00\x00\x00\x00\x00\x03\xFF\xFF\xFE\x00'\
b'\x03\xFF\xFF\xFF\x00\x01\xFF\xFF\xFE\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 风,code 32
windy= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\xFF\xFF\xF0'\
b'\x00\x07\xFF\xFF\xF8\x00\x07\xFF\xFF\xF8\x00\x07\xFF\xFF\xF8\x00'\
b'\x00\x00\x00\x00\x00\x3F\xFF\xFF\x3F\xF0\x7F\xFF\xFF\xBF\xF8\x7F'\
b'\xFF\xFF\xBF\xF8\x7F\xFF\xFF\xBF\xF0\x00\x00\x00\x00\x00\x00\xFF'\
b'\xFF\xFF\x00\x00\xFF\xFF\xFF\x00\x00\xFF\xFF\xFF\x00\x00\x7F\xFF'\
b'\xFE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 大风,code 33
strong_wind= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x03\xE0\x00\x00\x00\x07\xF0\x00\x00\x00\x07\xF8\x00\x00\x00\x07'\
b'\xF8\x00\x00\x00\x02\x78\x00\x00\x00\x00\xF8\x7F\xFF\xFF\xFF\xF8'\
b'\x7F\xFF\xFF\xFF\xF0\x7F\xFF\xFF\xFF\xE0\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x7F\xFF\xFF\xE0\x00\x7F\xFF\xFF\xF0\x00\x7F\xFF'\
b'\xFF\xF8\x00\x00\x00\x00\x78\x00\x00\x00\x02\x78\x00\x00\x00\x07'\
b'\xF8\x00\x00\x00\x07\xF8\x00\x00\x00\x07\xF0\x00\x00\x00\x03\xE0'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 飓风,code 34~36
hurricane= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x1E\x00\x00\x00\x00\x7E\x00\x00\x00\x00\xFE\x00\x00\x00\x01'\
b'\xFC\x00\x00\x00\x03\xF0\x00\x00\x00\x03\xE0\x00\x00\x00\x07\xC0'\
b'\x00\x00\x00\x0F\xB0\x00\x00\x00\x0F\xFE\x00\x00\x00\x0F\xFF\x80'\
b'\x00\x00\x1F\xFF\xC0\x00\x00\x1F\xFF\xC0\x00\x00\x1F\x87\xE0\x00'\
b'\x00\x1F\x03\xE0\x00\x00\x1E\x01\xE0\x00\x00\x3E\x01\xF0\x00\x00'\
b'\x3E\x01\xF0\x00\x00\x1E\x01\xE0\x00\x00\x1F\x03\xE0\x00\x00\x1F'\
b'\x87\xE0\x00\x00\x0F\xFF\xE0\x00\x00\x0F\xFF\xE0\x00\x00\x07\xFF'\
b'\xC0\x00\x00\x01\xFF\xC0\x00\x00\x00\x07\xC0\x00\x00\x00\x0F\x80'\
b'\x00\x00\x00\x1F\x00\x00\x00\x00\x3F\x00\x00\x00\x00\x7E\x00\x00'\
b'\x00\x01\xFC\x00\x00\x00\x01\xF8\x00\x00\x00\x01\xE0\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 冷,code 37
cold= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x78\x00\x00\x00'\
b'\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00\x80'\
b'\x30\x04\x00\x01\xC0\x78\x0F\x00\x03\xC0\x78\x0F\x00\x01\xD0\x78'\
b'\x2E\x00\x00\x3C\x78\xF0\x00\x00\x7E\x79\xF8\x00\x00\x3F\x7B\xF0'\
b'\x00\x00\x3F\xFF\xF0\x00\x00\x1F\xFF\xE0\x00\x00\x0F\xFF\xC0\x00'\
b'\x00\x07\xFF\x80\x00\x3D\xFF\xFF\xFE\xF0\x3F\xFF\xFF\xFF\xF0\x3F'\
b'\xFF\xFF\xFF\xF0\x3D\xFF\xFF\xFE\xF0\x00\x07\xFF\x80\x00\x00\x0F'\
b'\xFF\xC0\x00\x00\x1F\xFF\xE0\x00\x00\x3F\xFB\xF0\x00\x00\x3F\x79'\
b'\xF0\x00\x00\x7E\x78\xF8\x00\x00\x3C\x78\x70\x00\x01\xD0\x78\x2E'\
b'\x00\x03\xC0\x78\x0F\x00\x01\xC0\x78\x0F\x00\x00\x80\x30\x04\x00'\
b'\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00\x00\x78\x00\x00\x00'\
b'\x00\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 热,code 38
hot= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x00\x00\x00'\
b'\x01\xC0\x00\x00\x00\x03\xC0\x00\x00\x00\x07\xC0\x00\x00\x00\x0F'\
b'\xC0\x00\x00\x00\x1F\xC3\x00\x00\x00\x1F\xC3\x80\x00\x00\x3F\xE1'\
b'\xC0\x00\x00\x3F\xF1\xE0\x00\x00\x3F\xFB\xE0\x00\x00\x7F\xFF\xF0'\
b'\x00\x00\x7F\xFF\xF0\x00\x00\x7F\xFF\xF8\x00\x00\x7F\xFF\xF8\x00'\
b'\x00\x7F\xFF\xF8\x00\x01\x3F\xFF\xF8\x00\x03\xBF\xFF\xF8\x00\x03'\
b'\xFF\xFF\xFB\x00\x03\xFF\xFF\xFB\x00\x03\xFF\xFF\xFF\x00\x03\xFF'\
b'\xFF\xFF\x00\x03\xFF\xFF\xFF\x00\x03\xFF\xFF\xFF\x00\x03\xFF\xFF'\
b'\xFF\x00\x03\xFF\xFF\xFF\x00\x01\xFF\xFF\xFE\x00\x00\xFF\xFF\xFE'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xFF\xFF\xFF\x80'\
b'\x0F\xFF\xFF\xFF\xC0\x0F\xFF\xFF\xFF\xC0\x0F\xFF\xFF\xFF\xC0\x07'\
b'\xFF\xFF\xFF\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# NA,code 99
na= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1F\x3E\x0F\x3E'\
b'\x00\x1F\x3E\x0F\x7E\x00\x1F\xBE\x1F\x7F\x00\x1F\xFE\x1E\xFF\x00'\
b'\x1F\xFE\x1E\xFF\x00\x1F\xFE\x3C\xFF\x80\x1F\xFE\x3D\xFF\x80\x1F'\
b'\xFE\x3D\xFF\x80\x1F\xFE\x79\xFF\xC0\x1E\xFE\x7B\xFF\xC0\x1E\xFE'\
b'\xFB\xFF\xE0\x1E\x7E\xF3\xFF\xE0\x1E\x3E\xF7\xE3\xE0\x1E\x3F\xE7'\
b'\xC3\xE0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

# 温度计
thermometer= \
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\
b'\x00\xFC\x00\x00\x00\x01\xFE\x00\x00\x00\x01\xFF\x00\x00\x00\x03'\
b'\xCF\x00\x00\x00\x03\xCF\x00\x00\x00\x03\xCF\x00\x00\x00\x03\xCF'\
b'\x00\x00\x00\x03\xCF\x00\x00\x00\x03\xCF\x00\x00\x00\x03\xFF\x00'\
b'\x00\x00\x03\xFF\x00\x00\x00\x03\xFF\x00\x00\x00\x03\xFF\x00\x00'\
b'\x00\x03\xFF\x00\x00\x00\x03\xFF\x00\x00\x00\x03\xFF\x00\x00\x00'\
b'\x03\xFF\x00\x00\x00\x03\xFF\x00\x00\x00\x03\xFF\x00\x00\x00\x07'\
b'\xFF\x80\x00\x00\x0F\xFF\xC0\x00\x00\x0F\xFF\xC0\x00\x00\x1F\xFD'\
b'\xE0\x00\x00\x1F\xFF\xE0\x00\x00\x1F\xFF\xE0\x00\x00\x1F\xFF\xE0'\
b'\x00\x00\x1F\xFF\xE0\x00\x00\x0F\xFF\xC0\x00\x00\x0F\xB7\xC0\x00'\
b'\x00\x07\xFF\x80\x00\x00\x07\xFF\x80\x00\x00\x01\xFE\x00\x00\x00'\
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'\

code = {'0': sunny, '1': clear, '2': sunny, '3': clear, '4': cloud, '5': day_partly_cloudy, '6': night_partly_cloudy, '7': night_cloudy,
       '8': day_cloudy, '9': cloudy, '10': shower, '11': shower, '19': shower, '12': shower_hail, '13': light_rain, '14': moderate_rain,
       '15': heavy_rain, '16': storm, '17': storm, '18': storm, '20': sleet, '21': snow, '22': snow, '23': snow, '24': heavy_snow, '25': dust_storm,
       '26': dust_storm, '27': dust_storm, '28': dust_storm, '29': dust_storm, '30': foggy, '31': haze, '32': windy, '33': strong_wind,
       '34': hurricane, '35': hurricane, '36': hurricane, '37': cold, '38': hot, '99': na
       }



