﻿default seen_ch2 = False

label chapter_2:

  scene vn_ld_corridor

  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0

  a "So, how's your family?"
  b "Fine. Kids make me crazy. What about you?"
  a "I'm still single, you know. After my spouse left me last month."
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  b "Ouch, right."
  show a_4 at right:
        xalign 0.75
        yalign 1.0
  a "At least, we didn't have kids."
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  b "They aren't that bad. What about you?"

  menu:
    "Kids and spouse are ok." if word_is_known("kids", "spouse"):
      $ reduce_susp()
    "I'm single." if word_is_known("single"):
      $ reduce_susp()
  # один из этих результатов рандомом выдаёт или продолжение, или геймовер.
    "The fun thing is…": # язык игрока
      jump you_died_2
    "...":
      $ add_susp_or_jump("you_died_2")
	  show b_2 at left:
        xalign 0.75
        yalign 1.0
      a "Hey, lost in thoughts?"
      b "Don't be silent."
      menu:
        "Kids and spouse are ok." if word_is_known("kids", "spouse"):
          show b_4 at left:
            xalign 0.75
            yalign 1.0
		  b "Good to hear."
          $ reduce_susp()
          pass
        "I'm single." if word_is_known("single"):
          show a_1 at right:
            xalign 0.25
            yalign 1.0
          a "Ah, right."
          $ reduce_susp()
          pass
      # один из этих результатов рандомом выдаёт или продолжение, или геймовер.
        "The fun thing is…": # язык игрока
          jump you_died_2
        "...":
          jump you_died_2

  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  a "Anyway, I've heard it's worse on different hallways."
  b "It is, usually, but now..."
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  b "{b}Don't move.{/b}"

  menu:
    "...":
      pass
    "Huh?":
      jump you_died_monster_thing_1

# на фоне можно поиграть со светом и тенью
  a "..."
  b "..."

  menu:
    "What's going on?": # язык игрока
      jump you_died_monster_thing_1
    "...":
      pass

# мерцание исчезает
  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  b "It's gone."
  a "That wasn't the inmate from this hallway."
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  b "It wasn't. We'll have to report it after we're done here."
  b "I think, it was a dark jumper from level S."
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  b "Let's move on."
  show a_2 at right:
        xalign 0.25
        yalign 1.0
  a "I really, really hate all that paperwork."
  show b_4 at left:
        xalign 0.75
        yalign 1.0
  b "And what, would you prefer to clean cells?"
  show a_1 at right:
        xalign 0.25
        yalign 1.0
  a "Well, of corse not, but..."

  menu:
    "...":
      $ add_susp_or_jump("you_died_2")
    "But what?"  if word_is_known("what"):
      $ reduce_susp()
    "What was that?": # язык игрока
      jump you_died_2

  a "It's really impossible to just go to the toilet."
  show a_2 at right:
        xalign 0.25
        yalign 1.0
  a "Like that regulation of only being allowed to go in pairs."
  show a_1 at right:
        xalign 0.25
        yalign 1.0
  a "It's just..."
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  b "It's for your own safety. Just like {i}every{/i} regulation here."
  b "I won't dare you to go alone, because you can."

  menu:
    "He's just stupid enough for that."  if word_is_known("stupid", "enough", "just"):
      show a_2 at right:
        xalign 0.25
        yalign 1.0
      a "Hey, you're also mean!"
      show b_4 at left:
        xalign 0.75
        yalign 1.0
      b "Just stating the truth."
      a "That's not the truth, that's just straight bullying."
      b "And what are you going to do? Whine about it to Boss?"
      show a_1 at right:
        xalign 0.25
        yalign 1.0
      a "No, of course not."
      b "See."
      $ reduce_susp()
    "...":
      $ add_susp_or_jump("you_died_2")
    "Really?": # язык игрока
      jump you_died_2

  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  a "What is worse, to die instantly because you went against regulations, or to have some curse on you?"
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  b "At least death won't make you suffer much."
  a "But you can fight against some curse!"
  b "It's not that easy."
  b "It just makes you die slowly."
  b "Or even impose it on your closest ones."

  menu:
    "...":
      $ add_susp_or_jump("you_died_2")
    "Death is good."  if word_is_known("death", "good"):
      $ reduce_susp()
      b "Why do you sound like you know how it feels?"
      a "You're looking too much into it."
	  show b_1 at left:
        xalign 0.75
        yalign 1.0
      b "Just a habit."
      b "You can't imagine how many times noticing some subtle things saved my life."
    "Curse is fine." if word_is_known("curse", "fine"):
      $ reduce_susp()
      a "Really?"
      show b_1 at left:
        xalign 0.75
        yalign 1.0
	  b "And here I thought you remember that accident one month ago."
      a "What happened? I was on vacations."
      b "Some Security guy from Unit F got a curse of de-aging."
      b "So now he's like three years old physically."
      b "And the only way for him to get back is to grow-up like a normal human being."
      show a_4 at right:
        xalign 0.25
        yalign 1.0
	  a "Well, a prolonged life, no?"
      b "Yeah, and no insurance."
      show a_1 at right:
        xalign 0.25
        yalign 1.0
      a "Ouch."
      a "It depends on a curse, I guess."
      b "Mhm."
    "I don't like that conversation.": # язык игрока
      jump you_died_2

  show a_1 at right:
        xalign 0.25
        yalign 1.0
  show b_1 at left:
        xalign 0.75
        yalign 1.0
  a "Finally, a door."
  a "I think the hallway had a few more steps then the last time?"
  b "We'll check it after the lunch."
  a "Right."
  a "I really hope there won't be a big queue in canteen."
  show a_2 at right:
        xalign 0.25
        yalign 1.0
  a "And that there won't be any dead people like last time."

  jump chapter_3

label you_died_2:

  scene vn_ld_corridor
  show a_2 at right:
        xalign 0.25
        yalign 1.0
  show b_2 at left:
        xalign 0.75
        yalign 1.0

  a "..."
  scene vn_ld_door
  show a_3 at right:
        xalign 0.25
        yalign 1.0
  show b_3 at left:
        xalign 0.75
        yalign 1.0
  b "..."
  scene deathending with fade


  if not seen_ch2:
    $ seen_ch2 = True
    jump word_learning_sc2
  else: 
    jump word_learning

label you_died_monster_thing_1:

  scene vn_ld_corridor with shake
  show a_2 at right:
        xalign 0.25
        yalign 1.0
  show b_2 at left:
        xalign 0.75
        yalign 1.0
  show ebaka1
  a "Fuck."
		
  scene deathending with fade
  jump monster_1