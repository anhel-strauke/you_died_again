﻿define z = Character("Stain")
# Имя меняется с "???" на "Stain" после представления
$ n = 5

label word_learning_1:

z "Oh, you died. How unfortunate."
z "Hm, who am I?"
z "I don't think it's as important as you getting alive from those guys."
z "What you need to know is that you'll get back to them."
z "You want to survive, right?"
z "Everyone wants to, so."
z "You can call me Stain if you want to."
z "I'll translate words for you, but only [n] in one go."
z "We'll see each other pretty often from now on."
jump bye_bye
# запускаем экран с выбором слов. я оставила [n] слов, потому что нужно будет побалансить, плюс, возможно, переписать диалог так, чтобы больше слов повторялось.
# как вариант, можно после каждой сцены увеличивать это n для прохождения, но надо смотреть

label word_learning:
# стандартный экран приветствия, не считая первого и отдельно прописанных случаев
z "Hey there, welcome back."
z "Choose words you'd like to learn." # возможно упустить стоит, так как оч много раз повторение даже двух подряд такое себе, а игрок будет испытывать раздражение
jump bye_bye

label bye_bye:
"Here we learn words"
z "That's it for this time."
z "Try to get as far as you can."
jump start

label word_learning_susp:
# Этот конкретный кусок текста появляется только после смерти от слишком высокого подозрения
# Если самая первая смерть произошла именно от высокого подозрения, то диалог появится во время второй смерти от подозрения.
# причём появляется не постоянно
z "Ouch, that came out of nowhere, right?"
z "Well, you acted too suspicious."
z "So they killed you."
z "So let's learn some more words, so that you can survive long enough."
jump bye_bye

label word_learning_sc1:
# Объясняет цель первой сцены – влиться в коллектив, так сказать.
z "It will end after you do something."
z "I can't tell you what exactly, this information would make no sense."
z "For now, you need to get past that door."
z "They think you're one of them, so make sure, it stays this way."
jump bye_bye

label word_learning_sc2:
# цель второй сцены
z "Long hallways make me a bit uncomfortable, what about you?"
z "Well, doesn't really matter."
z "Because you have to go through this one."
z "You can die however many times you want, of course."
z "But you also want to leave this loop, right?"
jump bye_bye

label word_learning_sc3:
# третья сцена
z "Ah, hey, you've made it this far! That's nice."
z "I'm really proud of you."
z "Bot it isn't all, unfortunately."
z "You need to go to the canteen."
z "One more thing left, and then you'll be free."
z "You've already made it this far, so just a little while longer."
jump bye_bye

label word_learning_sc4:
# четвёртая сцена
z "Yes, they do have a lot of code words for each location, that isn't that nice of them."
z "But you're almost there. Find a soldier in  /description/."
z "What you need to do is touch them with nobody noticing."
z "And then you'll be free."
z "So, words."
# слово Bowl автоматически должно выдаваться первым и может даже как-то прям отмечаться
jump bye_bye

label tired_of_dying:
# после например 10-15 смерти
z "Oh, you look annoyed."
z "Aren't you happy to see me again?"
z "Please, don't answer that."
jump bye_bye


label monster_1:
z "What a nasty thing."
z "I'm happy we're safe here."
z "But maybe you shouldn't move?"
z "Or say something."
jump bye_bye


label monster_2:
z "Didn't you learn not to talk in that language?"
z "It doesn't matter what that thing was."
z "Ignore it."
z "..."
z "Listen, it's not your concern anyway."
z "Let's just move on with learning."
jump bye_bye