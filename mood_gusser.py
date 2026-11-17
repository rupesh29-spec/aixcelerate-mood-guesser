train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),

    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]
practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]
happy_words = [
    "won", "medal", "lovely", "surprise",
    "great", "full", "excited"
]
sad_words = [
    "lost", "late", "upset", "failed",
    "moving", "cancelled", "lonely"
]
def count_moods(data):

    happy_count = 0
    sad_count = 0

    for sentence, mood in data:

        if mood == "Happy":
            happy_count = happy_count + 1

        elif mood == "Sad":
            sad_count = sad_count + 1

    return happy_count, sad_count

def guess_mood(sentence):

    words = sentence.lower().split()

    happy_count = 0
    sad_count = 0

    for word in words:

        word = word.strip(".,!?")

        if word in happy_words:
            happy_count = happy_count + 1

        if word in sad_words:
            sad_count = sad_count + 1

    if happy_count >= sad_count:
        return "Happy"

    else:
        return "Sad"

print("MOOD GUESSER PROJECT")
print("--------------------------")

happy, sad = count_moods(train_data)

print("Training Data:")
print("Happy Sentences:", happy)
print("Sad Sentences:", sad)

correct = 0

print("\nPractice Results:")

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Actual Mood:", actual_mood)
    print("Predicted Mood:", predicted_mood)

    if predicted_mood == actual_mood:
        correct = correct + 1

total = len(practice_data)

accuracy = (correct / total) * 100

print("\n--------------------------")
print("Correct Predictions:", correct)
print("Total Sentences:", total)
print("Accuracy:", accuracy, "%")
print("--------------------------")
