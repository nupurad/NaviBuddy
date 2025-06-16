import speech_recognition as sr
from grid_config import locations
from pathfinder import astar

# Optional: fuzzy matching fallback
from difflib import get_close_matches

def get_speech_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak your command: (e.g., 'I'm at TSA, guide me to Gate 45')")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
        return text.lower()
    except:
        return None

def extract_locations(text):
    start, end = None, None
    matches = [key for key in locations if key in text]
    if len(matches) >= 2:
        start, end = matches[0], matches[1]
    elif len(matches) == 1:
        # Try fuzzy match
        remaining = text.replace(matches[0], '')
        alt = get_close_matches(remaining, locations.keys(), n=1)
        if alt:
            start, end = matches[0], alt[0]
    return start, end

def path_to_steps(path):
    steps = []
    for i in range(1, len(path)):
        r1, c1 = path[i - 1]
        r2, c2 = path[i]
        if r2 > r1:
            steps.append("move up")     
        elif r2 < r1:
            steps.append("move down")   
        elif c2 > c1:
            steps.append("move right")
        elif c2 < c1:
            steps.append("move left")
    return steps

def resolve_location(loc):
    if isinstance(loc, list):
        return tuple(loc[0])
    elif isinstance(loc, tuple):
        return loc
    elif isinstance(loc, (int, float)):
        raise TypeError(f"Location {loc} is a number, not a coordinate — check your 'locations' dictionary.")
    else:
        raise ValueError(f"Unknown format for location: {loc}")

def guide_user():
    # You can replace this with get_speech_input() to use voice
    command = "i am at gate 47, guide me to the nearest restroom"

    if not command:
        print("❌ Could not understand speech.")
        return

    start_label, end_label = extract_locations(command)
    if not start_label or not end_label:
        print("❌ Could not detect valid start or destination.")
        return

    start = resolve_location(locations[start_label])
    goal = resolve_location(locations[end_label])

    path = astar(start, goal)

    if not path:
        print(f"⚠️ No valid path from {start_label} to {end_label}.")
        return

    steps = path_to_steps(path)
    print(f"🗺️ Path from {start_label.title()} to {end_label.title()}:")
    print(f"From {start_label.title()}, " + ", then ".join(steps) + f", and you will reach {end_label.title()}.")
