# encoding: utf-8

KNOWN_WORD_MODIFIER = 100000
REPLACEMENT_CHAR = u"\u2588" # It's a block character
REPLACEMENTS = {
    u"a": u"⁜⁖ℇ℥",
    u"b": u"ↇ∃",
    u"c": u"∆",
    u"d": u"⊗",
    u"e": u"⊕",
    u"f": u"≼",
    u"g": u"≫",
    u"h": u"≣",
    u"i": u"⋹⋕",
    u"j": u"◪",
    u"k": u"⊜",
    u"l": u"≗",
    u"m": u"☳",
    u"n": u"⎋",
    u"o": u"⊡⏅⎄⎒▦",
    u"p": u"❉",
    u"q": u"⟱",
    u"r": u"⨄",
    u"s": u"Ⱡ",
    u"t": u"Ɒ",
    u"u": u"⏂",
    u"v": u"⮹",
    u"w": u"⧕",
    u"x": u"⥉",
    u"y": u"⛤",
    u"z": u"☷",
    u"0": u"┐",
    u"1": u"└",
    u"2": u"├",
    u"3": u"╙",
    u"4": u"┋",
    u"5": u"│",
    u"6": u"┱",
    u"7": u"⑄",
    u"8": u"⑀",
    u"9": u"⑊",
    u"'": u"⑇",
}

class Token(object):
    STATE_INVISIBLE = 0
    STATE_DISTINGUISHABLE = 1
    STATE_VISIBLE = 2

    def __init__(self, toklist, position, text):
        self.text = text
        self._token_list = toklist
        self._pos = position
    
    def prev_token(self):
        return self._token_list.get_prev(self._pos)
    
    def next_token(self):
        return self._token_list.get_next(self._pos)
    
    def prev_word(self):
        return self._token_list.get_prev_word(self._pos)
    
    def next_word(self):
        return self._token_list.get_next_word(self._pos)


class WordToken(Token):
    def __init__(self, toklist, position, text):
        super(WordToken, self).__init__(toklist, position, text)
    
    @staticmethod
    def is_valid_char(c):
        return c.isalnum() or c in u"'’´`"
    
    def __repr__(self):
        return "word(%s)" % repr(self.text)
    
    def compute_state(self):
        n = self._token_list.vocabulary().get(self.text.lower(), 0)
        if n == 0:
            return Token.STATE_INVISIBLE
        elif n >= KNOWN_WORD_MODIFIER:
            return Token.STATE_VISIBLE
        return Token.STATE_DISTINGUISHABLE
    
    def visualize(self):
        n = self._token_list.vocabulary().get(self.text.lower(), 0)
        if n < KNOWN_WORD_MODIFIER:
            color = u""
            if n >= 1:
                color = u"#500050"
            # elif n >= 2:
            #     color = u"#00a100"
            # elif n >= 3:
            #     color = u"#00a100"
            h = hash(self.text)
            visible_text = ""
            for c in self.text:
                cand = REPLACEMENTS.get(c, "#")
                if len(cand) == 1:
                    visible_text += cand
                else:
                    visible_text += cand[h % len(cand)]
            if color:
                return u"{color=%s}%s{/color}" % (color, visible_text)
            else:
                return visible_text
        else:
            return self.text


class SpaceToken(Token):
    def __init__(self, toklist, position, text):
        super(SpaceToken, self).__init__(toklist, position, text)
    
    @staticmethod
    def is_valid_char(c):
        return c.isspace()
    
    def __repr__(self):
        return "space(%s)" % repr(self.text)

    def compute_state(self):
        prev_word = self.prev_word()
        next_word = self.next_word()
        prev_word_dist = True
        next_word_dist = True
        if prev_word:
            prev_word_dist = prev_word.compute_state() >= Token.STATE_DISTINGUISHABLE
        if next_word:
            next_word_dist = next_word.compute_state() >= Token.STATE_DISTINGUISHABLE
        if prev_word_dist or next_word_dist:
            return Token.STATE_VISIBLE
        else:
            return Token.STATE_INVISIBLE
    
    def visualize(self):
        if self.compute_state() == Token.STATE_VISIBLE:
            return self.text
        else:
            return REPLACEMENT_CHAR * len(self.text)


class PunctuationToken(Token):
    CHAR_PUNCT = set(u".,?!:;\"”“„«»()@#$%^&*-—–+=≠±←→×©−•€®™¥˝§£…¿¡~≈")
    def __init__(self, toklist, position, text):
        super(PunctuationToken, self).__init__(toklist, position, text)

    @staticmethod
    def is_valid_char(c):
        return c in PunctuationToken.CHAR_PUNCT

    def __repr__(self):
        return "punct(%s)" % repr(self.text)
    
    def compute_state(self):
        prev_word = self.prev_word()
        next_word = self.next_word()
        prev_word_dist = True
        next_word_dist = True
        if prev_word:
            prev_word_dist = prev_word.compute_state() >= Token.STATE_DISTINGUISHABLE
        if next_word:
            next_word_dist = next_word.compute_state() >= Token.STATE_DISTINGUISHABLE
        if prev_word_dist or next_word_dist:
            return Token.STATE_VISIBLE
        else:
            return Token.STATE_INVISIBLE
    
    def visualize(self):
        if self.compute_state() == Token.STATE_VISIBLE:
            return self.text
        else:
            return REPLACEMENT_CHAR * len(self.text)


class SpecialWordToken(Token):
    def __init__(self, toklist, position, text):
        super(SpecialWordToken, self).__init__(toklist, position, text)


class SpecialArticleToken(SpecialWordToken):
    def __init__(self, toklist, position, text):
        super(SpecialArticleToken, self).__init__(toklist, position, text)
    
    def __repr__(self):
        return "artic(%s)" % repr(self.text)
    
    def compute_state(self):
        next_word = self.next_word()
        next_vis = False
        if next_word:
            next_vis = next_word.compute_state() >= Token.STATE_VISIBLE
        if next_vis:
            return Token.STATE_VISIBLE
        return Token.STATE_INVISIBLE
    
    def visualize(self):
        if self.compute_state() == Token.STATE_VISIBLE:
            return self.text
        else:
            return REPLACEMENT_CHAR * len(self.text)


class SpecialShortWordToken(SpecialWordToken):
    def __init__(self, toklist, position, text):
        super(SpecialShortWordToken, self).__init__(toklist, position, text)
    
    def __repr__(self):
        return "short(%s)" % repr(self.text) 
    
    def compute_state(self):
        prev_word = self.prev_word()
        next_word = self.next_word()
        prev_word_vis = True
        next_word_vis = True
        if prev_word:
            prev_word_vis = prev_word.compute_state() >= Token.STATE_VISIBLE
        if next_word:
            next_word_vis = next_word.compute_state() >= Token.STATE_VISIBLE
        if prev_word_vis and next_word_vis:
            return Token.STATE_VISIBLE
        else:
            return Token.STATE_INVISIBLE
    
    def visualize(self):
        if self.compute_state() == Token.STATE_VISIBLE:
            return self.text
        else:
            return REPLACEMENT_CHAR * len(self.text)


class TagToken(Token):
    def __init__(self, toklist, position, text):
        super(TagToken, self).__init__(toklist, position, text)
    
    def __repr__(self):
        return "tag(%s)" % repr(self.text)
    
    def compute_state(self):
        return Token.STATE_VISIBLE
    
    def visualize(self):
        return self.text


class TokenList(object):
    _BASE_TOKEN_TYPES = [
        PunctuationToken,
        SpaceToken,
        WordToken,
    ]

    _SPECIAL_WORDS = {
        u"a": SpecialArticleToken,
        u"the": SpecialArticleToken,
        u"to": SpecialShortWordToken,
        u"in": SpecialShortWordToken,
        u"of": SpecialShortWordToken,
        u"at": SpecialShortWordToken,
        u"on": SpecialShortWordToken,
        u"is": SpecialShortWordToken,
        u"be": SpecialShortWordToken,
        u"not": SpecialShortWordToken,
        u"do": SpecialShortWordToken,
        u"will": SpecialShortWordToken,
        u"it's": SpecialShortWordToken,
    }

    class StrWithGet:
        def __init__(self, s):
            self._s = s
        
        def get(self, i):
            if i < 0 or i >= len(self._s):
                return ""
            return self._s[i]
        
        def __len__(self):
            return len(self._s)

    def __init__(self, text, who, vocabulary, examples):
        self._vocab = vocabulary
        self._examples = examples
        self._who = who
        self._tokens = []
        self._text = text
        self._parse(text)

    def vocabulary(self):
        return self._vocab
    
    def get_next(self, i):
        j = i + 1
        while j < len(self._tokens) and type(self._tokens[j]) is TagToken:
            j += 1
        if j < len(self._tokens):
            return self._tokens[j]
        return None

    def get_prev(self, i):
        j = i - 1
        while j >= 0 and type(self._tokens[j]) is TagToken:
            j -= 1
        if j >= 0:
            return self._tokens[j]
        return None
    
    def get_next_word(self, i):
        j = i + 1
        while j < len(self._tokens) and type(self._tokens[j]) is not WordToken:
            j += 1
        if j < len(self._tokens):
            return self._tokens[j]
        return None
    
    def get_prev_word(self, i):
        j = i - 1
        while j >= 0 and type(self._tokens[j]) is not WordToken:
            j -= 1
        if j >= 0:
            return self._tokens[j]
        return None

    def _save_token(self, token_class, text):
        if token_class is None or not text:
            return
        pos = len(self._tokens)
        token = token_class(self, pos, text)
        self._tokens.append(token)

    def _token_class_for_char(self, c):
        for token_class in self._BASE_TOKEN_TYPES:
            if token_class.is_valid_char(c):
                return token_class
        return PunctuationToken

    def _parse(self, text):
        current_token_class = None
        current_token_text = u""
        i = 0
        txt = self.StrWithGet(text)
        while i < len(txt):
            c = txt.get(i)
            if c == u"{" and txt.get(i + 1) != u"{":
                close_brace_pos = text.find(u"}", i + 1)
                if close_brace_pos != -1:
                    self._save_token(current_token_class, current_token_text)
                    tag = text[i:close_brace_pos + 1]
                    self._save_token(TagToken, tag)
                    current_token_text = u""
                    current_token_class = None
                    i = close_brace_pos + 1
                    continue
            token_class_for_char = self._token_class_for_char(c)
            if current_token_class is not token_class_for_char:
                #print("Switching class to %s" % token_class_for_char.__name__)
                self._save_token(current_token_class, current_token_text)
                current_token_class = token_class_for_char
                current_token_text = c
            else:
                current_token_text += c
            i += 1
        self._save_token(current_token_class, current_token_text)
        self._update_token_types()

    def _update_token_types(self):
        for i in xrange(len(self._tokens)):
            token = self._tokens[i]
            if type(token) is WordToken:
                text = token.text.lower()
                if text in self._SPECIAL_WORDS:
                    new_token_class = self._SPECIAL_WORDS[text]
                    new_token = new_token_class(self, i, token.text)
                    self._tokens[i] = new_token
    
    def collect_words(self):
        words = [t.text for t in self._tokens if type(t) is WordToken]
        return set(words)
    
    def update_vocabulary(self):
        words = self.collect_words()
        visible_text = self._text
        for w in words:
            word = w.lower()
            if word in self._vocab:
                self._vocab[word] += 1
                word_token = None
                for tok in self._tokens:
                    if type(tok) is WordToken and tok.text.lower() == word:
                        word_token = tok
                        break
                if word_token:
                    self._examples[word] = (word, word_token.visualize(), self._who, visible_text)
            else:
                self._vocab[word] = 1

    def visualize(self):
        return u"".join([t.visualize() for t in self._tokens])
