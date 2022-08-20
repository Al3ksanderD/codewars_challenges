
def reverse(x):
    return x[::-1]


def spin_words(sentence):
    word_list = sentence.split()
    reversed_sentence = ""
    print(word_list)
    for index in range(len(word_list)):
        if len(word_list[index]) >= 5:
            word_list[index] = reverse(word_list[index])
    reversed_sentence = " ".join(word_list)
    return reversed_sentence


print(spin_words("My Small sentence"))