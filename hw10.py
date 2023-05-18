import os
import pickle
def input_scores():
    print('[점수 입력]')
    scores = []
    i = 1
    while True:
        a = int(input(f'#{i}? '))
        if a < 0:
            break
        scores.append(a)
        i += 1
    return scores

def get_average(lst):
    all_scores = 0
    for i in range(len(lst)):
        all_scores += scores[i]
    return all_scores/len(lst)

def show_scores(lst, avg):
    print('\n[점수 출력]')
    print('개인점수: ', end = '')
    for i in range(len(lst)):
        print(f'{lst[i]} ', end = '')
    print()
    print(f'평균: {avg}')

filepath = 'data/score.bin'
if os.path.exists(filepath):
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
        average = pickle.load(file)
    print('[파일 읽기]')
    show_scores(scores, average)
else:  
    scores = input_scores()
    average = get_average(scores)
    show_scores(scores, average)
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)
        pickle.dump(average, file)
