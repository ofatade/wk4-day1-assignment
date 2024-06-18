def mood_response(mood):
    if mood == 'sad':
        return "Am sorry, I hope you feel better soon"
    elif mood == 'happy':
        return "Good, let's go have some fun"
    elif mood == 'tired':
        return "Ok, go take a nap"
    elif mood == 'active':
        return "Nice! Let's go play some ball"
    else:
        return "Please enter one of the given options"