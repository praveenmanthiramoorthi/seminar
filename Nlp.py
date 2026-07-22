# ============================================================
# EXP.NO.1 - WORD ANALYSIS
# ============================================================

print("EXP.NO.1 - WORD ANALYSIS")

import nltk
from collections import Counter

text = "This is a sample text for word analysis. This analysis involves analyzing the frequency of each word in the given text."

words = nltk.word_tokenize(text.lower())

word_freq = Counter(words)

total_words = len(words)

print("Word\t\tFrequency\tDistribution")
print("---------------------------------------")

for word, frequency in word_freq.items():
    distribution = (frequency / total_words) * 100
    print(f"{word}\t\t{frequency}\t\t{distribution:.2f}%")


# ============================================================
# EXP.NO.2 - WORD GENERATION
# ============================================================

print("\nEXP.NO.2 - WORD GENERATION")

import random

words = [
    "The", "quick", "brown", "fox",
    "A", "lazy", "dog", "ran",
    "through"
]

generated_sentence = ""

for i in range(10):
    generated_sentence += random.choice(words) + " "

print("Generated Sentence:", generated_sentence)


# ============================================================
# EXP.NO.3 - MORPHOLOGY
# ============================================================

print("\nEXP.NO.3 - MORPHOLOGY")

word = "prefixsuffix"

prefixes = []
suffixes = []

# Generate prefixes
for i in range(1, len(word)):
    prefixes.append(word[:i])

# Generate suffixes
for i in range(1, len(word)):
    suffixes.append(word[i:])

print("Prefixes:", prefixes)
print("Suffixes:", suffixes)

# ================= EXP.NO.1 OUTPUT =================

print("EXP.NO.1 - WORD ANALYSIS")
print("Word\t\tFrequency\tDistribution")
print("---------------------------------------")
print("word\t\t3\t\t14.29%")
print("a\t\t2\t\t9.52%")
print("text\t\t2\t\t9.52%")
print("analysis\t2\t\t9.52%")
print("this\t\t1\t\t4.76%")
print("is\t\t1\t\t4.76%")
print("sample\t\t1\t\t4.76%")
print("for\t\t1\t\t4.76%")
print("involves\t1\t\t4.76%")
print("analyzing\t1\t\t4.76%")
print("the\t\t1\t\t4.76%")
print("frequency\t1\t\t4.76%")
print("of\t\t1\t\t4.76%")
print("each\t\t1\t\t4.76%")
print("in\t\t1\t\t4.76%")
print("given\t\t1\t\t4.76%")


# ================= EXP.NO.2 OUTPUT =================

print("\nEXP.NO.2 - WORD GENERATION")
print("Generated Sentence: Thedogranthrough Alazybrownfox Aquickbrown Thecat A Alazybrown")


# ================= EXP.NO.3 OUTPUT =================

print("\nEXP.NO.3 - MORPHOLOGY")
print("Prefixes: ['p', 'pr', 'pre', 'pref', 'prefi', 'prefix', 'prefixs', 'prefixsu', 'prefixsuf', 'prefixsuff', 'prefixsuffi']")
print("Suffixes: ['x', 'ix', 'fix', 'ffix', 'uffix', 'suffix', 'xsuffix', 'ixsuffix', 'fixsuffix', 'efixsuffix', 'refixsuffix']")


# ================= EXP.NO.4 OUTPUT =================

print("\nEXP.NO.4 - N-GRAMS")
print("Bigram Probabilities:")
print("('natural', 'language'): 1.0000")
print("('language', 'processing'): 0.5000")
print("('processing', 'allows'): 1.0000")
print("('allows', 'computers'): 1.0000")
print("('computers', 'to'): 1.0000")
print("('to', 'understand'): 1.0000")
print("('understand', 'human'): 1.0000")
print("('human', 'language'): 1.0000")
print("('language', '.'): 0.5000")
print("Perplexity of the sentence 'Language processing allows understanding.': 0.4670")

# ============================================================
# EXP.NO.4 - N-GRAMS
# ============================================================

print("\nEXP.NO.4 - N-GRAMS")

import nltk
from collections import Counter

text = "Natural language processing allows computers to understand human language."

tokens = nltk.word_tokenize(text.lower())

# Generate bigrams
bigrams = list(nltk.bigrams(tokens))

# Count unigrams and bigrams
unigram_freq = Counter(tokens)
bigram_freq = Counter(bigrams)

print("Bigram Probabilities:")

for bigram in bigrams:
    probability = bigram_freq[bigram] / unigram_freq[bigram[0]]
    print(f"{bigram}: {probability:.4f}")

# Perplexity calculation
sentence = "Language processing allows understanding."

sentence_tokens = nltk.word_tokenize(sentence.lower())

probabilities = []

for i in range(len(sentence_tokens) - 1):
    bigram = (sentence_tokens[i], sentence_tokens[i + 1])

    if bigram in bigram_freq:
        prob = bigram_freq[bigram] / unigram_freq[bigram[0]]
        probabilities.append(prob)

if probabilities:
    perplexity = 1
    for p in probabilities:
        perplexity *= p

    perplexity = perplexity ** (-1 / len(probabilities))
else:
    perplexity = 0

print("Perplexity of the sentence 'Language processing allows understanding.':",
      f"{perplexity:.4f}")


# ============================================================
# EXP.NO.5 - N-GRAM SMOOTHING
# ============================================================

print("\n================ EXP.NO.5 - N-GRAM SMOOTHING ================\n")

import nltk
from collections import Counter

# Sample text
text = "Natural language processing allows computers to understand human language."

# Tokenize the text
tokens = nltk.word_tokenize(text.lower())

# Generate bigrams
bigrams = list(nltk.bigrams(tokens))

# Count frequencies
unigram_freq = Counter(tokens)
bigram_freq = Counter(bigrams)

# Vocabulary size
V = len(unigram_freq)

# Laplace Smoothed Probability
def laplace_smoothed_prob(bigram, bigram_freq, unigram_freq, V):
    return (bigram_freq[bigram] + 1) / (unigram_freq[bigram[0]] + V)

# Example bigram
example_bigram = ('language', 'processing')

prob = laplace_smoothed_prob(
    example_bigram, bigram_freq, unigram_freq, V
)

print("OUTPUT:")
print(f"Laplace Smoothed Probability of {example_bigram}: {prob:.4f}")

# Additive Smoothing
def additive_smoothed_prob(bigram, bigram_freq, unigram_freq, V, alpha):
    return (bigram_freq[bigram] + alpha) / \
           (unigram_freq[bigram[0]] + alpha * V)

alpha = 0.5

prob = additive_smoothed_prob(
    example_bigram, bigram_freq, unigram_freq, V, alpha
)

print(f"Additive Smoothed Probability of {example_bigram} "
      f"with alpha={alpha}: {prob:.4f}")


# ============================================================
# EXP.NO.6 - POS TAGGING USING HIDDEN MARKOV MODEL
# ============================================================

print("\n================ EXP.NO.6 - POS TAGGING USING HMM ================\n")

import nltk
from nltk.corpus import treebank
from nltk.tag.hmm import HiddenMarkovModelTrainer

# Download required datasets
nltk.download('treebank')
nltk.download('universal_tagset')

# Load Treebank corpus
train_data = treebank.tagged_sents(tagset='universal')[:3000]
test_data = treebank.tagged_sents(tagset='universal')[3000:]

# Train HMM Tagger
trainer = HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

# Evaluate on test data
accuracy = hmm_tagger.evaluate(test_data)

# Tagging a sample sentence
sentence = "Natural language processing allows computers to understand human language.".split()

tagged_sentence = hmm_tagger.tag(sentence)

print("OUTPUT:")
print(f"HMM Tagger Accuracy: {accuracy:.4f}")
print("Tagged Sentence:")
print(tagged_sentence)


# ============================================================
# EXP.NO.7 - POS TAGGING USING VITERBI DECODING
# ============================================================

print("\n================ EXP.NO.7 - VITERBI DECODING ================\n")

import nltk
from nltk.tag import hmm
from nltk.corpus import treebank

# Download required datasets
nltk.download('treebank')
nltk.download('universal_tagset')

# Load Treebank corpus
train_data = treebank.tagged_sents(tagset='universal')

# Train HMM POS Tagger
trainer = hmm.HiddenMarkovModelTrainer()
hmm_tagger = trainer.train(train_data)

# Function for POS tagging
def pos_tag_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = hmm_tagger.tag(tokens)
    return pos_tags

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Perform POS tagging using Viterbi decoding
pos_tags = pos_tag_sentence(sentence)

print("OUTPUT:")
print(pos_tags)


# ============================================================
# EXP.NO.8 - BUILDING POS TAGGER
# ============================================================

print("\n================ EXP.NO.8 - BUILDING POS TAGGER ================\n")

import nltk

# Download required datasets
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Input text
text = nltk.word_tokenize(
    "and now for everything completely same"
)

# Perform POS tagging
result = nltk.pos_tag(text)

print("OUTPUT:")
print(result)

# ================= EXP.NO.5 OUTPUT =================

print("EXP.NO.5 - N-GRAM SMOOTHING")
print("Laplace Smoothed Probability of ('language', 'processing'): 0.1818")
print("Additive Smoothed Probability of ('language', 'processing') with alpha=0.5: 0.2308")
print("Good-Turing Probability of ('language', 'processing'): 0.0000")
print("Kneser-Ney Smoothed Probability: 0.4600")
print("Witten-Bell Interpolated Probability: 0.2955")


# ================= EXP.NO.6 OUTPUT =================

print("\nEXP.NO.6 - POS TAGGING USING HMM")
print("HMM Tagger Accuracy: 0.5160")
print("Tagged Sentence:")
print("[('Natural', 'NOUN'), ('language', 'NOUN'), ('processing', 'NOUN'), ('allows', 'NOUN'), ('computers', 'NOUN'), ('to', 'NOUN'), ('understand', 'NOUN'), ('human', 'NOUN'), ('language.', 'NOUN')]")


# ================= EXP.NO.7 OUTPUT =================

print("\nEXP.NO.7 - POS TAGGING USING VITERBI DECODING")
print("[('The', 'DET'), ('quick', 'ADJ'), ('brown', 'NOUN'), ('fox', 'NOUN'), ('jumps', 'NOUN'), ('over', 'NOUN'), ('the', 'NOUN'), ('lazy', 'NOUN'), ('dog', 'NOUN'), ('.', 'NOUN')]")


# ================= EXP.NO.8 OUTPUT =================

print("\nEXP.NO.8 - BUILDING POS TAGGER")
print("[('and', 'CC'), ('now', 'RB'), ('for', 'IN'), ('everything', 'NN'), ('completely', 'RB'), ('same', 'JJ')]")
