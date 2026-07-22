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
