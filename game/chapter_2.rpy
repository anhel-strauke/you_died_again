label chapter_2:

scene bg corridor # вторая сцена

a "So, how's your family?"
b "Fine. Kids make me crazy. What about you?"
a "I'm still single, you know. After my spouse left me last month."
b "Ouch, right."
a "At least, we didn't have kids."
b "They aren't that bad. What about you?"

menu:
  "Kids and spouse are ok.":
    pass
  "I'm single.":
    pass
  # один из этих результатов рандомом выдаёт или продолжение, или геймовер.
  "The fun thing is…": # язык игрока
    jump you_died_2
  "...":
    $ susp += 1
    if susp == 3:
      jump you_died_2
    else:
      a "Hey, lost in thoughts?"
      b "Don't be silent."
      pass
    menu:
      "Kids and spouse are ok.":
        b "Good to hear."
        pass
      "I'm single.":
        a "Ah, right."
        pass
      # один из этих результатов рандомом выдаёт или продолжение, или геймовер.
      "The fun thing is…": # язык игрока
        jump you_died_2
      "...":
        jump you_died_2

a "Anyway, I've heard it's worse on different hallways."
b "It is, usually, but now..."
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
b "It's gone."
a "That wasn't the inmate from this hallway."
b "It wasn't. We'll have to report it after we're done here."
b "I think, it was a dark jumper from level S."
b "Let's move on."
a "I really, really hate all that paperwork."
b "And what, would you prefer to clean cells?"
a "Well, of corse not, but..."

menu:
  "...":
    $ susp += 1
    if susp == 3:
      jump you_died_2
    else:
      pass
  "But what?":
    pass
  "What was that?": # язык игрока
    jump you_died_2

a "It's really impossible to just go to the toilet."
a "Like that regulation of only being allowed to go in pairs."
a "It's just..."
b "It's for your own safety. Just like {i}every{/i} regulation here."
b "I won't dare you to go alone, because you can."

menu:
  "He's just stupid enough for that.":
    a "Hey, you're also mean!"
    b "Just stating the truth."
    a "That's not the truth, that's just straight bullying."
    b "And what are you going to do? Whine about it to Boss?"
    a "No, of course not."
    b "See."
  "...":
    $ susp += 1
    if susp == 3:
      jump you_died_2
    else:
      pass
  "Really?": # язык игрока
    jump you_died_2

a "What is worse, to die instantly because you went against regulations, or to have some curse on you?"
b "At least death won't make you suffer much."
a "But you can fight against some curse!"
b "It's not that easy."
b "It just makes you die slowly."
b "Or even impose it on your closest ones."

menu:
  "...":
    $ susp += 1
    if susp == 3:
      jump you_died_2
    else:
      pass
  "Death is good.":
    b "Why do you sound like you know how it feels?"
    a "You're looking too much into it."
    b "Just a habit."
    b "You can't imagine how many times noticing some subtle things saved my life."
    pass
  "Curse is fine.":
    a "Really?"
    b "And here I thought you remember that accident one month ago."
    a "What happened? I was on vacations."
    b "Some Security guy from Unit F got a curse of de-aging."
    b "So now he's like three years old physically."
    b "And the only way for him to get back is to grow-up like a normal human being."
    a "Well, a prolonged life, no?"
    b "Yeah, and no insurance."
    a "Ouch."
    a "It depends on a curse, I guess."
    b "Mhm."
    pass
  "I don't like that conversation.": # язык игрока
    jump you_died_2

a "Finally, a door."
a "I think the hallway had a few more steps then the last time?"
b "We'll check it after the lunch."
a "Right."

jump chapter_3

label you_died_2:
a "..."
b "..."
# меняется на картинку камеры фон, персонажи стреляют
"I'm dead."
jump word_learning
# после первой смерти word_learning_sc2
# затем снова на обучное word_learning

label you_died_monster_thing_1:
a "Fuck."
# изображение ебаки, и по бокам товарищи а и б
"We're dead."
jump monster_1