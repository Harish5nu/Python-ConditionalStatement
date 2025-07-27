# Fun Mood Checker for Beginners

print("Welcome to the Mood Checker!")
mood = input("How are you feeling today? (happy/sad/angry/lazy) 🤔: ").lower()

if mood == "happy":
    print("😊 That's awesome! Spread those good vibes!")
elif mood == "sad":
    print("😢 It's okay to feel sad. Better days are coming.")
elif mood == "angry":
    print("😠 Take a deep breath... and maybe punch a pillow 😄")
elif mood == "lazy":
    print("😴 Lazy days are necessary. Recharge yourself!")
else:
    print("🤷 Hmm, I can't read that mood... but I hope it's a good one!")

print("Thanks for sharing your mood! 💖")