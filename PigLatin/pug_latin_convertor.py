# get sentence from user
original_sentence = input ("Enter your sentence: ").strip ().lower ()
# split sentence into words
words = original_sentence.split ()

# loop trough words and convert to pig latin
new_words_l = []

for w1 in words :
    if w1[0] in "aeiou" :
        new_word = w1 + "yay"
        new_words_l.append (new_word)

    else :
        vowel_pos = 0
        for w2 in w1 :
            if w2 not in "aeiou" :
                vowel_pos = vowel_pos + 1
            else :
                break
        cons = w1[:vowel_pos]
        the_rest = w1[vowel_pos :]
        p_latin_word = the_rest + cons + "ay"
        new_words_l.append (p_latin_word)

output = " ".join(new_words_l)
print(output)

# if it starts with a vowel, just add "yay"
# otherwise, move the first consonant cluster to end, and add "ay"
# stick words back together
# output the final string
