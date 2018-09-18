import re
words = '我，来。上海？吃？上海菜'
wordlist = re.split('，|。|？',words)
print(wordlist)