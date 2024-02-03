def high_scores():
    scores_input = input("Please introduce the score of your students: ").split()
    student_scores = []
    for n in range(0, len(scores_input)):
        student_scores.append(int(scores_input[n]))

    highest_score = 0

    for score in student_scores:
        if score > highest_score:
            highest_score = score
    print(highest_score)


high_scores()
