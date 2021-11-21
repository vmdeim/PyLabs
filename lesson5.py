# Задание 1 : Выбрать самого высокого используя лист
discript = [
    ["Бильбо Бэггинс", 190, 143, 51, 0],
    ["Фродо Бэггинс", 89, 153, 55, 0],
    ["Перегрин Тук", 78, 123, 49, 0],
    ["Сэмуайз Гэмджи", 75, 133, 53, 0],
    ["Смеагол", 500, 113, 25, 0]
]

def max_hight(a_list):
    rez=sorted(a_list, key=lambda x:x[2]) [-1]
    return rez

print (max_hight(discript))

# Задание 2 : Выбрать самого высокого используя словарь
discript2 = {
    "Бильбо Бэггинс":   { "Возраст" : 190, "Рост" : 143, "Вес" : 51,"Убито орков" : 0},
    "Фродо Бэггинс":  { "Возраст" : 89,"Рост" : 153, "Вес" : 55, "Убито орков" : 0},
    "Перегрин Тук":     { "Возраст" : 78, "Рост" : 123, "Вес" : 49,"Убито орков" : 0},
    "Сэмуайз Гэмджи":   { "Возраст" : 75,  "Рост" : 133, "Вес" : 53, "Убито орков" : 0},
    "Смеагол":       { "Возраст" : 500,  "Рост" : 113,"Вес" : 25, "Убито орков" : 0},
}

def max_hight_dict(a_dict):
    sorted_dict = {k: v for k, v in sorted(a_dict.items(), key=lambda x:x[1]["Рост"])}
    last = list(sorted_dict.keys())[-1]
    return last, a_dict[last]

print (max_hight_dict(discript2))

# Задание 3 Нечеткое сравнение

def compare(S1, S2):
    # триграммы
    ngrams = [
        S1[i:i+3] for i in range(len(S1)-2)
    ]
    count=0
    for ngram in ngrams:
        count += S2.count(ngram)
    count3 = count/max(len(S1),len(S2))
    # двуграммы
    ngrams = [
        S1[i:i+2] for i in range(len(S1)-1)
    ]
    count=0
    for ngram in ngrams:
        count += S2.count(ngram)
    count2 = count / max(len(S1), len(S2))
    # одинаковые буквы
    ngrams = [
        S1[i:i + 1] for i in range(len(S1))
    ]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    count1 = count / max(len(S1), len(S2))

    return round(count1, 1),  round(count2, 1), round(count3, 1)

one, two, tri = compare("столик", "стул")

print("Одинаковые буквы - %.2f" % one)
print("Двуграммы - %.2f" % two)
print("Триграммы - %.2f" % tri)

