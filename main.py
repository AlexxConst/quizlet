import random

capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "West": "Richmond",
    "Washington": "Olympia",
    "Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# Generate 35 quiz files.
for quiz_num in range(35):
    # Create the quiz and answer key files.
    with open(
        f"capitalsquiz{quiz_num + 1}.txt", "w", encoding="utf-8"
    ) as quiz_file, open(
        f"capitalsquiz_answers{quiz_num + 1}.txt", "w", encoding="utf-8"
    ) as answers_key_file:
        # Write out the header for the quiz.
        quiz_file.write("Name:\n\nDate:\n\nPeriod:\n\n")
        quiz_file.write((" " * 20) + f"State Capitals Quiz (Form {quiz_num + 1})")
        quiz_file.write("\n\n")

        # Shuffle the order
        states = list(capitals.keys())
        random.shuffle(states)

        # Loop through all 50 states, making a question for each.
        for question_num in range(50):
            # Get right and wrong answers.
            correct_answer = capitals[states[question_num]]
            wrong_answer = list(capitals.values())
            del wrong_answer[wrong_answer.index(correct_answer)]
            wrong_answer = random.sample(wrong_answer, 3)
            answer_options = wrong_answer + [correct_answer]
            random.shuffle(answer_options)
            # Write the question and the answer options to the quiz file.
            quiz_file.write(
                f"{question_num + 1}. What is the capital of {states[question_num]}?\n"
            )
            for i in range(4):
                quiz_file.write(f"{'ABCD'[i]}. {answer_options[i]}\n")
            # Write the answer key to a file.
            answers_key_file.write(
                f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n\n",
            )
            quiz_file.write("\n")
