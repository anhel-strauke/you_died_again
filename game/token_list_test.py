# encoding: utf-8

from token_list import TokenList, KNOWN_WORD_MODIFIER

vocab = {}
tl = None

print("TokenList Test Program")
print
print("/vocab      Print current vocabulary")
print("/list       Print last token list")
print("Just ENTER  Quit")
print

while True:
    s = raw_input("TEXT>")
    if s:
        if s == "/vocab":
            print("Current vocabulary:")
            for k, v in vocab.items():
                print("%-30s %d" % (k, v))
            print
        elif s == "/list":
            print("Last token list:")
            if tl:
                for t in tl._tokens:
                    print "   ", repr(t)
            print
        else:
            tl = TokenList(s, vocab)
            print(tl.visualize())
            words = tl.collect_words()
            for word in words:
                w = word.lower()
                if w in vocab:
                    vocab[w] += 1
                    if vocab[w] == 3:
                        vocab[w] += KNOWN_WORD_MODIFIER
                else:
                    vocab[w] = 1
            print
    else:
        print("Bye!")
        break