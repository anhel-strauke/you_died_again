################################################################################
# Red and blue dialogue screens

transform trans_say_bg:
    xalign 0.5
    yalign 1.0
    alpha 0.6

style say_blue_window is default:
    xalign 0.5
    yalign 1.0
    xsize 1496
    ysize 349
    yoffset -96
    background At("gui/say_frame_base_blue.png", trans_say_bg)

style say_blue_namebox:
    xalign 0.0
    yalign 0.0
    xsize 453
    ysize 76
    yoffset 50
    xoffset -22
    background Image("gui/say_namebox_blue.png", xalign=0.0, yalign=0.0)

style say_blue_label:
    xalign 0.5
    yalign 0.5
    color "#000000"

style say_blue_dialogue:
    xalign 0.0
    xoffset 94
    yalign 0.0
    yoffset 95+50
    xsize 1386
    ysize 203
    color "#000000"

style say_red_window is say_blue_window:
    background At("gui/say_frame_base_red.png", trans_say_bg)

style say_red_namebox is say_blue_namebox:
    background Image("gui/say_namebox_red.png", xalign=0.0, yalign=0.0)

style say_red_label is say_blue_label
style say_red_dialogue is say_blue_dialogue

################################################################################
# Word learning

init python:
    def prepare_words_to_learn(examples):
        global VOCABULARY
        rv = []
        for k, v in examples.items():
            if k in VOCABULARY and VOCABULARY[k] < KNOWN_WORD_MODIFIER:
                rv.append(v)
        return rv

screen learn_words(words_to_learn):
    style_prefix "learn"
    if words_count < n and len(prepare_words_to_learn(words_to_learn)) > 0:
        side "c l":
            area (297, 123, 552, 699)
            viewport id "word_list":
                mousewheel True
                vbox:
                    spacing 59
                    style_prefix "learn_vbox"
                    for word, word_vis, who, example in prepare_words_to_learn(words_to_learn):
                        textbutton word_vis.replace("#500050", "#000000") action Call("learn_word_label", word, word_vis, who, example, from_current=True)
            vbar value YScrollValue("word_list") style "learn_vbar"
    else:
        timer 0.01 action Return() repeat False

style learn_vbox_button is button:
    xsize 382
    ysize 115
    xalign 0.5
    yalign 0.5
    left_margin 93
    left_padding 93
    top_margin 30
    top_padding 30
    background "gui/button_red.png"
    hover_background "gui/button_red_hover.png"

style learn_vbox_button_text:
    xalign 0.5
    yalign 0.5
    size 40
    color "#000000"

style learn_vbar:
    base_bar Frame("gui/scroll_bg.png", left=17, right=17, top=66, bottom=66)
    thumb Frame("gui/scroll_thumb.png", left=17, right=17, top=10, bottom=10)
    insensitive_thumb None
    xsize 36
    top_gutter 16
    bottom_gutter 16
    unscrollable "insensitive"
    bar_invert True


label learn_word_label(word, word_vis, who, example):
    call screen learn_confirm(word, word_vis, who, example)
    if _return:
        call screen learn_explain(word)
        $ VOCABULARY[word] += KNOWN_WORD_MODIFIER
        $ words_count += 1
    return

screen learn_confirm(word, word_vis, who, example):
    style_prefix "learn_confirm"
    vbox:
        style "learn_confirm_base_vbox"
        window:
            vbox:
                text word_vis style "learn_confirm_word_vis"
                text who style "learn_confirm_who"
                text visualize_text(example) style "learn_confirm_example"
                text _("Explain this word?") style "learn_confirm_question"
        hbox:
            textbutton _("Yes") action Return(True)
            textbutton _("No") action Return(False)

style learn_confirm_base_vbox:
    xalign 1.0
    yalign 0.0
    yoffset 182
    xoffset -77
    spacing 30
    top_padding 0
    xfill False

style learn_confirm_window:
    background "gui/window_red_learn.png"
    xsize 890
    ysize 435
    xalign 1.0
    yalign 0.0

style learn_confirm_window_vbox:
    top_padding 47
    xfill True
    spacing 30

style learn_confirm_text:
    color "#000000"

style learn_confirm_word_vis is learn_confirm_text:
    xoffset 130

style learn_confirm_who is learn_confirm_text:
    xoffset 130

style learn_confirm_example is learn_confirm_text:
    xoffset 260
    xmaximum 890-260-60

style learn_confirm_question is learn_confirm_text:
    xoffset 260

style learn_confirm_hbox:
    xalign 1.0
    yalign 0.0
    spacing 30

style learn_confirm_button:
    background "gui/button_red.png"
    hover_background "gui/button_red_hover.png"
    xsize 382
    ysize 115
    xalign 0.5
    yalign 0.5

style learn_confirm_button_text:
    color "#000000"
    size 60
    xalign 0.5
    yalign 0.5

screen learn_explain(word):
    style_prefix "learn_explain"
    vbox:
        style "learn_confirm_base_vbox"
        window:
            side "c":
                text _("It's „[word]“.")
        hbox:
            textbutton _("Got It") action Return(True)

style learn_explain_window is learn_confirm_window
style learn_explain_text:
    color "#000000"
    xalign 0.5
    yalign 0.5
style learn_explain_button is learn_confirm_button
style learn_explain_button_text is learn_confirm_button_text
style learn_explain_hbox is learn_confirm_hbox
style learn_explain_side:
    xfill True
    yfill True