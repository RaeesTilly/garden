# imported spacy and defined its language
import spacy
nlp = spacy.load('en_core_web_sm')

# created my garden path sentences 
old_man = "i live in the USA."
complex_houses = "The comlex houses married and single soldiers and their families."
horse_raced = "The horse raced past the barn fell"
man_eats = "When Fred eats food gets thrown."
girl_cat = "I told the girl the cat scratched Bill would help her."

# added garden path sentences to a list
garden_path_sentences = [old_man, complex_houses, horse_raced, man_eats, girl_cat]

# tokenizes and uses entity recognition on each sentence
for sentences in garden_path_sentences:
    for i in nlp(sentences).ents:
        print("Entity : {} , Text {}".format(i.label_,i.text))

entity_fac = spacy.explain("GPE")
print(f"GPE:{entity_fac}")

entity_fac = spacy.explain("PERSON")
print(f"PERSON:{entity_fac}")

# the first entity i looked up was 'GPE' and its explination was countries,cities, states.
# The entity did make sense with the word associated to it becase 'GPE' is similar to 'GDP'

# the second entity i looked up was 'person' iand its explination was people, including fictional.
# the entity did make sense with the word associated to it 


