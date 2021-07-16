import random

import yaml


def test():
    right = 0
    wrong = 0
    wrongs = []

    with open('questions.yml') as stream:
        try:
            lines = yaml.safe_load(stream)
            total = len(lines)
            ids = list(range(total))
            random.shuffle(ids)

            for line_id in ids:
                line = lines[line_id]
                print('{qid}. {question}'.format(
                    qid=line.get('qid'),
                    question=line.get('question').get('text').rstrip()))
                print('---------------')
                for i, answer in enumerate(line.get('answers'), 1):
                    print(f'{i}. {answer}')

                user_answer = input('answer:')
                if user_answer and user_answer.isnumeric():
                    user_answer = int(user_answer)
                else:
                    user_answer = 0

                answer_index = line.get('metadata').get('rightAnswer') + 1

                if user_answer == answer_index:
                    right += 1
                    print('correct!')
                else:
                    print('wrong!')
                    wrong += 1
                    wrongs.append(line.get('qid'))

                while user_answer != answer_index:
                    res = input('try again:')
                    user_answer = int(res) if res.isnumeric() else -1

                print(f'score: {right} / {wrong} / {total}\n')
        except yaml.YAMLError as err:
            print(err)


if __name__ == "__main__":
    test()
