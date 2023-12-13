#punctuation
punctuation = "!,@,#,$,%,^,*,<,(),_,-,+,'',:,:"
mystr = input("Enter a sentence: ")
no_punct = ""

for char in mystr:
    if char not in punctuation:
        no_punct += char  # Corrected this line to use '+=' for concatenation
       
    print("Sentence without punctuation:", no_punct)
