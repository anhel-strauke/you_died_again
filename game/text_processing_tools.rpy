# Text processing and player's vocabulary

init -1:
    default VOCABULARY = {}

init -1 python:
    from token_list import TokenList, KNOWN_WORD_MODIFIER

    class Tokenizer(TokenList):
        def __init__(self, text):
            global VOCABULARY
            super(Tokenizer, self).__init__(text, VOCABULARY)

    class ForeignCharacter(ADVCharacter):
        def __call__(self, what, interact=True, _call_done=True, multiple=None, **kwargs):
            tok = Tokenizer(what)
            real_what = tok.visualize()
            tok.update_vocabulary()
            super(ForeignCharacter, self).__call__(real_what, interact, _call_done, multiple, **kwargs)
    
    def word_is_known(word):
        global VOCABULARY
        if word.lower() in VOCABULARY:
            return VOCABULARY[word.lower()] >= KNOWN_WORD_MODIFIER
        return False

init -1:
    define foreigner = ForeignCharacter(
                            None,
                            who_prefix='',
                            who_suffix='',
                            what_prefix='',
                            what_suffix='',

                            show_function=renpy.show_display_say,
                            predict_function=renpy.predict_show_display_say,

                            condition=None,
                            dynamic=False,
                            image=None,

                            interact=True,
                            slow=True,
                            slow_abortable=True,
                            afm=True,
                            ctc=None,
                            ctc_pause=None,
                            ctc_timedpause=None,
                            ctc_position="nestled",
                            all_at_once=False,
                            with_none=None,
                            callback=None,
                            type='say',
                            advance=True,

                            who_style='say_label',
                            what_style='say_dialogue',
                            window_style='say_window',
                            screen='say',
                            mode='say',
                            voice_tag=None,

                            kind=False)