import re

p = re.compile('[a-z]+')


## match 는 정확히 match ###
m = p.match('3 python')
print(m)


m = p.match('python')
print(m)

## search는 일부만 찾기 ###

m = p.search('3 python')
print(m)

## findall 일치하는 것을 list로 담아서 return#

m = p.findall('life is too short')
print(m)

## finditer 일치하는 것을 match 객체로 return##

m = p.finditer('life is too short')
print(m)

for i in m:
    print(i)


## match 객체 심화 ###

m = p.match('python')
print(m)

print(m.group())
print(m.start())
print(m.end())
print(m.span())


###########################################################################
#### compile option ####


## DOTALL,  S

import re
p = re.compile('a.b')
m = p.match('a\nb')
print(m)

p = re.compile('a.b', re.DOTALL) ## '.'은 원래 줄바꿈은 포함이 안되는데, 줄바꿈까지 포함
m = p.match('a\nb')
print(m)


## INGORECASE, I
p = re.compile('[a-z]')

print(p.match('python'))
print(p.match('Python'))
print(p.match('PYHTON'))

p = re.compile('[a-z]', re.I)  ## 대소문자 무시하고 match

print(p.match('python'))
print(p.match('Python'))
print(p.match('PYHTON'))


## MULTILINE, M
p = re.compile("^python\s\w+") ## ^:맨처음, \s:공백, \w:단어, 즉 맨처음에 python이라는 단어나 나오고 공백 뒤에 다른 단어 하나

data = """python one
life is too short
python two
you need python
python three """

print(p.findall(data))
print('\n')

p = re.compile("^python\s\w+", re.M)  ## 라인별로 인식

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

## VERBOSE,     ## 긴 정규 표현식을 나눠서 쓸수 있게 만들어주는 옵션, 공백을 무시하도록 만들어줌)

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

charref = re.compile(r"""
&[#]                      # Start of a numeric entity reference
(
    0[0-7]+               # Octal form
    |[0-9]+               # Decimal form
    |x[0-9a-fA-F]+
)
;                         # Trailing semiconlon
""", re.VERBOSE)

## 백 슬래시 문제

# '\section' print
p = re.compile('\\section')
print(p)

# '\\section' print
p = re.compile('\\\\section')
print(p)
p = re.compile(r'\\section')  ### '\\\\section으로 알아서 바꿔줌'
print(p)


######################################################################
##### 메타문자 ######

## | ##
p = re.compile('Crow|Servo') # | : or와 동일
m = p.match('CrowHello')
print(m)

m = p.match('ServoMotor')
print(m)

## ^ ##

# cf> 정규표현식을 compile하고 쓰지 않아도 ',앞에는 compile', ', 뒤에는 찾을 문자열로 인식'함
print(re.search('^Life', 'Life is too short'))  ### ^ : 맨처음을 의미
print(re.search('^Life', 'My Life'))

## $ ##

print(re.search('short$', 'Life is too short')) ### $ : 끝을 의미
print(re.search('short$', 'short leg'))

## \b ##

p = re.compile(r'\bclass\b')   ### \b : 공백을 의미

print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))


######################################################################
#####  ######

## 그루핑 () ##
# (ABC)+


p = re.compile('ABC+')
m = p.search('ABCABCABC OK?')

print(m)

print(m.group())


p = re.compile('(ABC)+')         ### () : 그루핑
m = p.search('ABCABCABC OK?')

print(m)

print(m.group())
#ABCABCABC

p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search('park 010-1234-1234')

print(m.group(1))    ### 그룹핑 단위로 인덱싱 ### cf> 인덱싱에 () 사용, 1부터 시작


p = re.compile(r'(\b\w+)\s+\1')   ### 그루핑 된 것을 한번 더 부름
#print(p.search('Paris in the spring').group())
print(p.search('Paris in the the spring').group())


## 그루핑된 문자열에 이름 붙이기 ?P<name>

p = re.compile(r'(?P<name>\w+)\s((\d+)[-]\d+[-]\d+)')  ## ?P< > : 그루핑된 문자열에 이름 붙이기
m = p.search('park 010-1234-1234')

print(m.group('name'))

print('\n')
p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')         ## ?P< > : taging한 이름으로도 사용 가능
print(p.search('Paris in the the spring.').group())

p = re.compile(r'(?P<word>\b\w+)\s+\1')
print(p.search('Paris in the the spring.').group())


#####################################################################
##### 전방 탐색 ###########


## 긍정형 (?=)

p = re.compile('.+:')                  ## .+ : 문자열이 반복
m = p.search('http://google.com')
print(m.group())

p = re.compile('.+(?=:)')              ## (?= )검색 조건은 포함하되 결과 안에는 포함시키지 않음
m = p.search('http://google.com')
print(m.group())


## 부정형 (?!)

p = re.compile('.*[.](?!bat$).*$', re.M)  ## (?! ) 검색 조건에서 제외
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)

p = re.compile('.*[.](?!bat$|exe$).*$', re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)


## 문자열 바꾸기 sub

p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes')) # p의 문자열을 'color'로 변경


## Gready vs Non-Greedy

s = '<html><head><title>Title</title>'

print(re.match('<.*>', s).group())  ## Greedy      : 가장 큰 pattern으로 match
print(re.match('<.*?>', s).group()) ## Non-Greedy  : 가장 작은 pattern으로 match
