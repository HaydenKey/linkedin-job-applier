import json


def load_answers(json_file):
    with open(json_file, 'r') as file:
        return json.load(file)


def save_unanswered_questions(unanswered_questions, json_file):
    with open(json_file, 'w') as file:
        json.dump(unanswered_questions, file, indent=4)
