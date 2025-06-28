

def get_recommendation(mood):
    
    mood_dict = {
        "happy": ("yellow", "yellow t-shirt"),
        "sad": ("pink", "pink sweater"),
        "angry": ("green", "green hoodie"),
        "stressed": ("blue", "blue shirt"),
        "relaxed": ("green", "green kurta"),
        "energetic": ("red", "red jacket"),
        "professional": ("black", "black blazer"),
        "caring": ("pink", "pink scarf")
    }
    
    mood = mood.lower().strip()
    
    if mood in mood_dict:
        color, outfit = mood_dict[mood]
        return f"Based on your mood ('{mood}'), we recommend wearing {outfit} to match the mood with {color} color."
    else:
        return "Sorry, we don't have a recommendation for that mood. Please try again with moods like happy, sad, stressed, etc."

def main():
    print("🎨 Welcome to the Color Psychology Outfit Recommender!")
    mood = input("How are you feeling today? (e.g., happy, sad, stressed, energetic): ")
    recommendation = get_recommendation(mood)
    print(recommendation)

if __name__ == "__main__":
    main()
