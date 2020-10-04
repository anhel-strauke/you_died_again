define c = Character("Officer")
define d = Character("Some Security")
define y = Character("You")

label chapter_4:

# фон столовая, только А с нами

d "Bowl."
a "Bowl."

menu:
  "...":
    jump you_died_5
  "What, again?":
    jump you_died_5
  "Bowl.":
    # только после того, как выучим
    jump canteen

label canteen:
a "I can't see our friend over there, hm."
a "That's weird."

menu:
  "...":
    # подозрение, ура
    a "No reaction aganin?"
    a "You're somehow off, you know that?"
    a "Whatever."
    pass
  "That's what?":
    jump you_died_5
  "Report on Dark Jumper":
    # открывается только если мы с ней один раз сходили
    a "Ah, right. I forgot about that."
    pass

a "But Officer Whatshispants is here."
# показывается спрайт нужного нам на прикосновение персонажа
a "I've heard he's really buff under all that armor."
a "Big biceps or whatever."
a "But I doubt that's all muscules."
a "I guess, that's what happens after you only do paperwork."

menu:
  "...":
    # подозрение +
    a "He doesn't hear us, so you can at least support me."
    pass
  "Right.":
    # подозрение -
    a "What, no jokes on his behalf?"
    a "But there are jokes on mine."
    a "You're a good friend."
    pass
  "I hope it's almost over.":
    jump you_died_5

a "I'll go get food for us, you find a table."

# А уходит, появляется С

menu: 
  "So, what should I do?"
  "Go and just touch him.":
    c "Hey, what do you think you're doing?"
    jump you_died_5
  "Punch him.":
    c "What the actual hell?"
    c "Do you want to get fired?"
    d "Officer, he touched..."
    c "Execute him!"
    jump you_died_5
  "Go to the free table behind him.":
    # начинается шрифтом слов
    "It can't be hard, right?"
    "..."
    "Great!"
    # шрифт норм новеллы
    "So, now what?"
    pass
  "Ask to touch his biceps.":
    # единственный вариант, доступный после изучения слов "бицепс" и "тач"
    c "Are you stupid or what?"
    c "That's prohibited."
    c "And you work here for awhile, so you sure has that inmate on you."
    c "Execure him."
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
a "Oh, that inmate made it this far, huh."
a "I wonder who managed to touch him and pass this curse up."
y "I... it was me? I think."
a "Ouch."
a "Actually, that explains your behavior."
y "...you won't kill me, I hope?"
a "Nah. It's like, you've already passed the curse, so you're fine."
a "There's a regulation on this one about it."
a "The same that makes us talk all the time."
y "...because that's how you learn something is off."
a "Yeah. But also, there are, like, posters all over the facility about telling if you see him in your head."
y "I didn't see a single one."
y "Actually, all posters didn't make sense."
y "I couldn't read them."
b "You should report it them."
# теперь появляется б
y "Both of you killed me a lot, by the way."
b "It wasn't {i}us{/i}."
b "Just our copies from another dimensions."
b "Also you'll have to go to therapy now." 
b "Your cognition is from another place and there might be slight differences."
y "...huh."
a "Eat for now. It's over anyway."

"Ending one: free at last."

return 

label ending_2:
"character doesn't tell anything, and officer doesn't die, and they just talk."

"Ending two: better keep silent."

return


label you_died_5:
# А достаёт пушку
v "Really, right in front of my salad?"
"I'm dead."
jump word_learning