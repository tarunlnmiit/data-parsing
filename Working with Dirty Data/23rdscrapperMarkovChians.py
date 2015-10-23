from urllib.request import urlopen
from urllib.error import HTTPError
from random import randint

def wordListSum(wordList):
	sum = 0
	for word, value in wordList.items():
		sum += value
	return sum

def retrieveRandomWord(wordList):
	randIndex = randint(1, wordListSum(wordList))
	for word, value in wordList.items():
		randIndex -= value
		if randIndex <= 0:
			return word

def buildWordDict(text):
	# Remove newline and quotes
	text = text.replace('\n', ' ')
	text = text.replace('"', '')
	# Make sure punctuation marks are treated as their own 'words,' so that they will be included in the Markov Chain
	punctuation = [',','.',';',':']
	for symbol in punctuation:
		text = text.replace(symbol, ' '+symbol+' ')

	words = text.split(' ')
	# Filter out empty words
	words = [word for word in words if word != '']

	wordDict = dict()
	for i in range(1, len(words)):
		if words[i-1] not in wordDict:
			# Create a new dictionary for this word
			wordDict[words[i-1]] = dict()
		if words[i] not in wordDict[words[i-1]]:
			wordDict[words[i-1]][words[i]] = 0
		wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
	return wordDict

def getData(url):
	try:
		text = str(urlopen(url).read(), 'utf-8')
	except HTTPError as e:
		return None
	wordDict = buildWordDict(text)
	return wordDict

url = input('Enter url(Press Enter to redirect to default URL): ')

if url == '':
	url = 'http://pythonscraping.com/files/inaugurationSpeech.txt'
wordDict = getData(url)

# Generate a Markov chain of length 100
length = 100
chain = ''
currentWord = 'I'
for i in range(length):
	chain += currentWord + ' '
	currentWord = retrieveRandomWord(wordDict[currentWord])

print (chain)