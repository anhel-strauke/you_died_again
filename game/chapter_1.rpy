define a = Character("Security A", kind=foreigner)
define b = Character("Security B", kind=foreigner)

default died_already = False
default died_from_susp_already = False
default died_twice_already = False
default use_skip = False

label start:
  $ red_quick_menu = False
  scene vn_ld_door

  $ SUSP = 0 # Сбрасываем подозрение в ноль

  a "Hail!"
  b "Hail!"

  menu:
    "What?": # язык игрока
      jump you_died_1
    "...":
      a "Huh, why don't you say anything?"
      a "You should say something!"
      $ add_susp_or_jump("you_died_1") # Подозрение растёт
      menu:
        "I can't understand you": # язык игрока
          jump you_died_1
        "...":
          $ add_susp_or_jump("you_died_1") # Подозрение растёт
          b "You know, it doesn't seem you understand us, huh."
          a "Just say \"Hail\" and let's just move on, please."
          a "I just want to go on with our route."
          menu:
            "What the hell...": # язык игрока
              jump you_died_1
            "...":
              jump you_died_1
            "Hail!" if word_is_known("hail"): # только если слово изучено уже
              $ reduce_susp() # Подозрение уменьшается
              jump correct_1
        "Hail!" if word_is_known("hail"): # только если слово изучено уже
          $ reduce_susp() # Подозрение уменьшается
          jump correct_1
    "Hail!" if word_is_known("hail"): # только если слово изучено уже
      jump correct_1


label correct_1:
  # Возможно можно в зависимости от уровня подозрения, добавить после первого: 
  # b "What, lost in your thoughts?"
  # вот это может тоже после второго молчания
  # b "Don't be silent, you know it's prohibited."
  # a "Everything fun is prohibited here."
  # но пока что не знаю, надо смотреть как оно будет работать и как будем успевать

  a "Ok, our funniest route for today, let's go."
  b "Not until we revise regulations."
  a "They are the same, no need to revise them every time we go in there."
  b "If you want to die – of course, not."
  b "Maybe you even want to go alone?"

  menu:
    "...":
      $ add_susp_or_jump("you_died_1")
    "That's my chance to die again.": # язык игрока
      jump you_died_1
    "Regulations are important" if word_is_known("regulations", "are", "important"):
      b "See."
      $ reduce_susp()
      
    # только после того, как все эти слова будут изучены. Минус к подозрению. продолжается как обычно

  a "Ugh, whatever."
  b "It's very important to know all the regulations before going in." # может пропустить, если персонаж это говорит в выборе меню
  b "Besides, right now they didn't catch this thing yet."
  a "Yeah-yeah, got it."
  b "Not only we should go inside only in odd numbers, but also more than two."
  b "Neither stay back or leap forward for more than one meter."
  b "But also make sure to not touch one another or me."

  menu:
    # появляется только если слова из третьего известны
    "...":
      $ add_susp_or_jump("you_died_1")
    "Fascinating.": # язык игрока
      jump you_died_1
    "Got it." if word_is_known("got", "it"):
      pass

  b "We also should always talk to each other."
  a "Talking would be less unbearable if either of you two was even remotely fun to be around."
  b "I'll smack you."

  menu:
    "...":
      $ add_susp_or_jump("you_died_1")
    "That's sort of too much.": # язык игрока
      jump you_died_1
    "You aren't fun either." if word_is_known("you", "fun", "either"):
      $ reduce_susp()
    # после него продолжается дальше диалог, подозрение падает.

  a "Hey, don't be mean!"
  b "Hey, don't be a clown!"
  a "..."
  b "..."

  menu:
    "...":
    # неожиданно, но в этот раз, ничего не падает.
      pass
    "And now we're dead." if word_is_known("now", "we", "dead"):
      a "Ha, you're right."
      b "No, we don't die because we're silent."
      b "That's different regulation altogether."
      a "Eh, because of the ability of that inmate?"
      b "Mhm."
      $ reduce_susp() # подозрение падает.
    "Silence was so good.": # язык игрока
      jump you_died_1

  b "We're already late. I want to eat on a lunch break, and not stand in the queue."
  a "Ugh, right."
  a "That stupid regulation which doesn't allow us to bring our food here."
  b "Stop whining, you're annoying."
  b "You'll get used to it, eventually."

  menu:
    "...":
      $ add_susp_or_jump("you_died_1")
      b "Hm..."
    "I wonder what's behind that door.": # язык игрока
      jump you_died_1
    "The food they make is ok." if word_is_known("food", "make"):
      a "Your definition of ok is a very low quality."
      a "I should treat you to something good to raise your standards."
      $ reduce_susp()

  b "We're coming in."

  jump chapter_2


label you_died_1:
  # Здесь ребята сменят аватары
  "I'm dead."

  if not died_already: # здесь нужно сделать так. в первый раз игра прыгает на word_learning_1 (1 раз)
    $ died_already = True
    jump word_learning_1
  elif SUSP >= SUSP_LIMIT and not died_from_susp_already and not use_skip: # если смерть от высокого подозрения word_learning_susp (1 раз)
    $ died_from_susp_already = True
    jump word_learning_susp
  elif SUSP < SUSP_LIMIT and not died_twice_already and not use_skip: # если смерть после word_learning_1 еоторая не susp word_learning_sc1 (1 раз)
    $ died_twice_already = True
    jump word_learning_sc1
  elif not use_skip and died_from_susp_already and died_twice_already:
    $ use_skip = True
    jump skip_words
  else: # все остальные после - word_learning
    jump word_learning
