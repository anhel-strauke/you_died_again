default seen_ch3 = False

define v = Character("???")

label chapter_3:

  scene vn_ld_door

  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0

  a "Ah, it's over."
  show a_4 at right:
        xalign 0.25
        yalign 1.0
  a "Lunch-lunch-lunch."
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  b "Don't be so happy. Dark jumper wasn't supposed to be there."
  show a_1 at right:
        xalign 0.25
        yalign 1.0
  a "Yeah, I know."
  show a_4 at right:
        xalign 0.25
        yalign 1.0
  a "But I'm honestly impressed you recognised it."
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  b "I didn't. It's just a guess."
  a "But you made us stop before everything started happening."

  menu:
    "...":
      $ add_susp_or_jump("you_died_1_1")
    "A good habit." if word_is_known("good", "habit"):
      $ reduce_susp()
      show a_4 at right:
        xalign 0.25
        yalign 1.0
      a "Ha, right!"
      b "I just want to survive long enough to retire with a good pension."
      a "So materialistic."
      b "I have kids to feed and dress."
      b "And go back home to."
      show a_1 at right:
        xalign 0.25
        yalign 1.0
      a "Right."
    "I'm also impressed." if word_is_known("impressed", "also"):
      b "I can teach both of you later."
      a "That would be great."
      show a_1 at right:
        xalign 0.25
        yalign 1.0
      a "Don't want to die single."
      show b_4 at left:
        xalign 0.75
        yalign 1.0
      b "You'll find a person you like eventually."
    "We're back.": # язык игрока
      jump you_died_1_1

  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  a "But before lunch I really need to make a detour."
  b "I'll go to canteen right away."
  a "And you? Wanna make a detour with me or go eat?"

  menu:
    "...":
      a "Hey, are you ok?"
      $ add_susp_or_jump("you_died_1_1") # здесь должно запускаться меню кроме добавления подозрения
#      menu:
#        "...":
#          jump you_died_1_1
#        "Her.":
#          $ add_susp_or_jump("you_died_1_1")
#          b "That was really weird say to choose."
#          jump go_with_b
#        "Him."
#          $ add_susp_or_jump("you_died_1_1")
#          a "Ugh, you're really off."
#          a "So hungry, huh."
#          jump go_with_a
    "Go straight to eat."  if word_is_known("straight"):
      b "We'll get you place."
      a "Yeah, thanks."
      jump go_with_b
    "Go to the toilet." if word_is_known("toilet", "detour"):
      a "No need to call it that."
      b "But that's what it's called."
      show b_4 at left:
        xalign 0.75
        yalign 1.0
      b "Or what, suddenly wanted to call it detour?"
      a "Whatever."
      a "Let's go."
      jump go_with_a
    "Where's canteen?"  if word_is_known("canteen"):
      jump you_died_1_1
#

  label go_with_b:

  scene vn_ld_corridor
  show b_1

  b "..."
  b "Ah, right."
  b "I completely frogot about Dark Jumper. We need to report it as soon as possible."
  b "So see you in the canteen."

  menu:
    "...":
      $ add_susp_or_jump("you_died_3")
    "Where's canteen?" if word_is_known("canteen"):
      jump you_died_3
    "I can go with you." if word_is_known("can", "go"):
      show b_4
      b "No need, I'll make an actual detour."
      show b_1
      b "It won't take me long, but it would be nice to have a table for us already."

  b "..."
  b "Hey, why are you silent? And just stand there?"
  b "Didn't I tell you to go?"
  show b_2
  b "..."
  b "You don't know where canteen is, right?"
  b "That's a shame."

  jump you_died_3

  label go_with_a:

  scene vn_ld_corridor
  show a_1

  a "Ah, it's really hard to be with her for so long."
  show a_2
  a "She's so mean."
  show a_1
  a "And you aren't better."

  menu:
    "...":
      $ add_susp_or_jump("you_died_4")
    "She's fun"  if word_is_known("fun"):
      a "That's your type of person?"
      show a_4
      a "Really?"
      show a_1
      a "You break my heart."
      $ reduce_susp()
    "I'm already tired.": # язык игрока
      jump you_died_4

  a "Oh, look, there's someone else already."
  a "I'll go in and if you want to, I'll go for the second time with you."

  hide a_1

  "..."
  "..."
  "..?"
# дальше текст, тем же шрифтом, что и в изучении слов
  v "Hello there."
  show ebaka2
  v "You can hear us, right?"
  v "And you can understand us."
  v "I'm impressed you've made it this far, you know?"

  menu:
    "...":
      pass
    "Who are you?": # язык игрока
      v "The last thing you'll see if your master won't fetch you."
      jump you_died_monster_thing_2
    "Show yourself.": # язык игрока
      v "Gladly."
      jump you_died_monster_thing_2

  v "Well, you can ignore me, but I'll get to your master eventually."

  hide ebaka2
  show a_1

  a "Huh, you look pale."
  a "You really need to eat. Let's go."

  jump chapter_4

label you_died_1_1:
  scene vn_ld_door
  show a_3 at right:
        xalign 0.25
        yalign 1.0
  show b_3 at left:
        xalign 0.75
        yalign 1.0
        
  "..."
  scene deathending with fade

  if not seen_ch3:
    $ seen_ch3 = True
    jump word_learning_sc3
  else: 
    jump word_learning


label you_died_3:
  scene vn_ld_corridor
  show b_3 at left:
        xalign 0.75
        yalign 1.0
  b "..."
  scene deathending with fade
  jump word_learning
# если вдруг не умер на 1_1, то нужно, чтобы сработало word_learning_sc3
# остальное word_learning

label you_died_4:
  scene vn_ld_corridor
  show a_3 at right:
        xalign 0.25
        yalign 1.0
  a "Ugh."
  scene deathending with fade
  jump word_learning
# если вдруг не умер на 1_1, то нужно, чтобы сработало word_learning_sc3
# остальное word_learning

label you_died_monster_thing_2:
  scene vn_ld_corridor
  show ebaka2
  "I really shouldn't trust voices in my head."
  scene deathending with fade
  jump monster_2
