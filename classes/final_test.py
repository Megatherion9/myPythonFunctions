file_contents = "The mental features discoursed of as the analytical, are, in themselves, but little susceptible of analysis. We appreciate them only in their effects. We know of them, among other things, that they are always to their possessor, when inordinately possessed, a source of the liveliest enjoyment. As the strong man exults in his physical ability, delighting in such exercises as call his muscles into action, so glories the analyst in that moral activity which disentangles."

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", " ", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    myList = []
    myDictionary = {}
    separatedWords = file_contents.split(" ")
    value = 0
    
    # Fill myList with all words without punctuations signs
    for word in separatedWords:
        if not word[-1].isalpha():
            myList.append(word[:-1])
        else:
            myList.append(word)

    # Fill myDictionary with all the words that don't belong to uninteresting_words list
    for leanWord in myList:
        if leanWord.lower() not in uninteresting_words:
            myDictionary[leanWord.lower()] = value
            value += 1

    return myDictionary

print(calculate_frequencies(file_contents))
            
    # Instantiate the Class
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(myDictionary)
    cloud.to_file("myfile.jpg")
    return cloud.to_array()


    # Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()