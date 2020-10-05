default seen_ch4 = False
default touch_him = False
default punch_him = False
default touch_biceps = False

define c = Character("Officer", kind=foreigner)
define d = Character("Some Security", kind=foreigner)
define m = Character("Security A")
define l = Character("Security B")
define y = Character("You")

label chapter_4:

# фон столовая, только А с нами

d "Bowl."
a "Bowl."

menu:
  "...":
    jump you_died_5
  "What, again?": # язык игрока
    jump you_died_5
  "Bowl." if word_is_known("bowl"):
    # только после того, как выучим
    jump canteen

label canteen:
a "I can't see our friend over there, hm."
a "That's weird."

menu:
  "...":
    $ add_susp_or_jump("you_died_5")
    a "No reaction aganin?"
    a "You're somehow off, you know that?"
    a "Whatever."
  "That's what?": # язык игрока
    jump you_died_5
  "Report on the Dark Jumper" if word_is_known("report", "dark", "jumper"):
    # открывается только если мы с ней один раз сходили
    a "Ah, right. I forgot about that."
    $ reduce_susp()

a "But Officer Whatshispants is here."
# показывается спрайт нужного нам на прикосновение персонажа
a "I've heard he's really buff under all that armor."
a "Big biceps or whatever."
a "But I doubt that's all muscules."
a "I guess, that's what happens after you only do paperwork."

menu:
  "...":
    $ add_susp_or_jump("you_died_5")
  "Right." if word_is_known("right"):
    $ reduce_susp()
    a "What, no jokes on his behalf?"
    a "But there are jokes on mine."
    a "You're a good friend."
  "I hope it's almost over.": # язык игрока
    jump you_died_5

a "I'll go get food for us, you find a table."

# А уходит, появляется С

menu: 
  "So, what should I do?"
  "Go and just touch him.": # язык игрока
    c "Hey, what do you think you're doing?"
    $ touch_him = True
    jump you_died_5
  "Punch him.": # язык игрока
    c "What the actual hell?"
    c "Do you want to get fired?"
    d "Officer, he touched..."
    c "Execute him!"
    $ punch_him = True
    jump you_died_5
  "Go to the free table behind him.": # язык игрока
    # начинается шрифтом слов
    "It can't be hard, right?"
    "..."
    "Great!"
    # шрифт норм новеллы
    "So, now what?"
    pass
  "Ask to touch his biceps." if word_is_known("touch", "biceps"): # язык игрока
    c "Are you stupid or what?"
    c "That's prohibited."
    c "And you work here for awhile, so you sure has that inmate on you."
    c "Execure him."
    $ touch_biceps = True
    jump you_died_5

a "Ah, you've got a nice table here."
a "So, about that new series they broadcast on in-facility TV, did you watch it?"
y "Huh?"
a "What huh?"
a "Hey, you've been weird for at least half of the shift, are you ok?"
"I can understand everything he says just fine."
"Am I free, just like that person said?"
"But free of what?"
"My mind is a bit blurry..."

menu:
  "Tell him.":
    jump ending_1
  "Stay silent.":
    jump ending_2

label ending_1:

y "I think someone was just in my head, and..."
c "What's going on?" # на "иностранном" языке
d "Kill him!"
m "Oh, that inmate made it this far, huh."
m "I wonder who managed to touch him and pass this curse up."
y "I... it was me? I think."
m "Ouch."
m "Actually, that explains your behavior."
y "...you won't kill me, I hope?"
m "Nah. It's like, you've already passed the curse, so you're fine."
m "There's a regulation on this one about it."
m "The same that makes us talk all the time."
y "...because that's how you learn something is off."
m "Yeah. But also, there are, like, posters all over the facility about telling if you see him in your head."
y "I didn't see a single one."
y "Actually, all posters didn't make sense."
y "I couldn't read them."
l "You should report it them."
# теперь появляется б
y "Both of you killed me a lot, by the way."
l "It wasn't {i}us{/i}."
l "Just our copies from another dimensions."
l "Also you'll have to go to therapy now." 
l "Your cognition is from another place and there might be slight differences."
y "...huh."
m "Eat for now. It's over anyway."

"Ending one: free at last."

return 

label ending_2:
"Is it over now?"
"If I tell someone, they'll shoot me."
"So I better keep silent."
"And the Officer seems fine."
"I don't want to check if I'll be revived."
"I've died enough times for today."
"And for my life."

"Ending two: better keep silent."

return


label you_died_5:
# А достаёт пушку
v "Really, right in front of my salad?"
"I'm dead."

if not seen_ch4:
  $ seen_ch4 = True
  jump word_learning_sc4
elif touch_him:
  jump touchy_words
elif punch_him:
  jump punchy_words
elif touch_biceps:
  jump biceps_words
else: 
  jump word_learning
  
  
jump word_learning
# в первый раз прыгает на word_learning_sc4
# потом обычное word_learning