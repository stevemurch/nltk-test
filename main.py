import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

# When running the first time, you'll need to download these libraries
#nltk.download('stopwords')
#nltk.download('punkt')

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is blue today."

print(sent_tokenize(example_text))

stop_words = set(stopwords.words("english"))
print (stop_words)

for i in word_tokenize(example_text, "english"):
    print(i)

filtered_sentence = []

for w in word_tokenize(example_text):
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

sentences = ["Mr. Speaker, Mr. Vice President, Members of Congress, the First Lady of the United States, and my fellow Americans: Less than 1 year has passed since I first stood at this podium, in this majestic chamber, to speak on behalf of the American People — and to address their concerns, their hopes, and their dreams.  That night, our new Administration had already taken swift action.  A new tide of optimism was already sweeping across our land. Each day since, we have gone forward with a clear vision and a righteous mission — to make America great again for all Americans."]

nouns = []
for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(sentence)):
         if (pos == 'NN'): # or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
             nouns.append(word)

print(nouns)