# %%
import numpy as np
number = np.random.randint(1,101)    # задаем случайное число


def game_core(number):    
    '''Функция принимает загаданное число и возвращает количество попыток.
       На каждом шаге с загаданным числом сравнивается среднее чисел диапазона,
       на основании обратной связи сокращается диапазон. '''
    
    count = 0
    range_start = 0
    range_end = 101 
    ''' Диапазон увеличен на 1 в начале и в конце, чтобы функция могла 
         угадать крайние числа - 1 и 100 - путем усреднения. '''
   
    while True:
        
        guess = range_start + int((range_end-range_start)/2)
        count +=1
        
        if number > guess:
            range_start = guess
            
        elif number < guess: 
            range_end = guess
            
        else:
            break
            
    return count


def score_game(game_core):
    '''Функция запускает игру 1000 раз и возвращает среднее количество попыток.'''
    
    np.random.seed(1) # фиксируем RANDOM SEED, чтобы эксперимент был воспроизводим.
    random_array = np.random.randint(1,101, size=1000)
    
    count_ls = [game_core(number) for number in random_array]  
    score = int(np.mean(count_ls))
    
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")

# %%
score_game(game_core)