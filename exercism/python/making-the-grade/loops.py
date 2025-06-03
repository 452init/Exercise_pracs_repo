"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    new_list = [round (num) for num in student_scores]
    return new_list


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    failed_students = 0
    
    for num in student_scores:
        if num <= 40:
            failed_students = failed_students + 1
    return failed_students


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    above_threshold_score = []

    for num in student_scores:
        if num >= threshold:
            above_threshold_score.append(num)
    return above_threshold_score


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    final_result_data = []

    final_result_data.append(41)
    num_range = highest - 41 + 1
    range_potion = num_range / 4

    if highest >= 41 and highest <= 100:
        for num in range(1, 4):
            next_threshold = 41 + num * round(range_potion)
            final_result_data.append(next_threshold)
    return final_result_data


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    student_list = []

    for index, score in enumerate(student_scores):
        score = student_scores[index]
        student = student_names[index]
        student_list.append(f"{index + 1}. {student}: {score}")
    return student_list


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    empty_list = []

    for student in student_info:
        if student[1] == 100:
            return student
            break
    else:
        return empty_list
