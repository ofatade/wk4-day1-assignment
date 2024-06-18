import mood_today

mood = input("How are you feeling today, are you: sad, happy, tired, or active? ")

print(mood_today.mood_response(mood.lower()))