define z = Character("Stain")
# Имя меняется с "unknown person" на "Stain" после представления

label word_learning:

z "Oh, you died. How unfortunate."
z "Hm, who am I?"
z "I don't think it's as important as you getting alive from those guys."
z "What you need to know is that you'll get back to them."
z "You want to survive, right?"
z "Everyone wants to, so."
z "You can call me Stain if you want to."
z "I'll translate words for you, but only [n] in one go."
z "We'll see each other pretty often from now on."

# запускаем экран с выбором слов. я оставила [n] слов, потому что нужно будет побалансить, плюс, возможно, переписать диалог так, чтобы больше слов повторялось.
# как вариант, можно после каждой сцены увеличивать это n для прохождения, но надо смотреть

z "That's it for this time."
z "Try to get as far as you can."

# Это для первого раза, прыгаем обратно и всё такое. просто чтобы не перегружать всеми механиками, а только изучением языка, потом объясним и подозрение, и цель персонажа и вот это вот всё.
# Хотя последние две строчки стоит использовать каждый раз после экрана выучки слов.

# стандартный экран приветствия, не считая первого и отдельно прописанных случаев
z "Hey there, welcome back."
z "Choose words you'd like to learn." # возможно упустить стоит, так как оч много раз повторение даже двух подряд такое себе, а игрок будет испытывать раздражение

# Этот конкретный кусок текста появляется только после смерти от слишком высокого подозрения
# Если самая первая смерть произошла именно от высокого подозрения, то диалог появится во время второй смерти от подозрения.
# причём появляется не постоянно
z "Ouch, that came out of nowhere, right?"
z "Well, you acted too suspicious."
z "So they killed you."
z "So let's learn some more words, so that you can survive long enough."

# Объясняет цель первой сцены – влиться в коллектив, так сказать.
z "It will end after you do something."
z "I can't tell you what exactly, this information would make no sense."
z "For now, you need to get past that door."
z "They think you're one of them, so make sure, it stays this way."

# цель второй сцены
z "Long hallways make me a bit uncomfortable, what about you?"
z "Well, doesn't really matter."
z "Because you have to go through this one."
z "You can die however many times you want, of course."
z "But you also want to leave this loop, right?"

# третья сцена
z "Ah, hey, you've made it this far! That's nice."
z "I'm really proud of you."
z "Bot it isn't all, unfortunately."
z "You need to go to the canteen."
z "One more thing left, and then you'll be free."
z "You've already made it this far, so just a little while longer."

# четвёртая сцена
z "Yes, they do have a lot of code words for each location, that isn't that nice of them."
z "But you're almost there. Find a soldier in  /description/."
z "What you need to do is touch them with nobody noticing."
z "And then you'll be free."
z "So, words."

# после например 10-15 смерти
z "Oh, you look annoyed."
z "Aren't you happy to see me again?"
z "Please, don't answer that."
