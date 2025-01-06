characthers = {}

def main():	
	book_path ="books/frankenstein.txt"
	text = get_book_text(book_path)
	word_counts = number_of_words_in_book(text)
	print(characthers)

def get_book_text(path):
	with open(path) as f:
		return f.read()

def number_of_words_in_book(text):
	words_so_far = 0
	separate = text.split()
	for word in separate:
		characther = get_number_of_each_characther(word)
		words_so_far += 1
	return words_so_far

def get_number_of_each_characther(Letter):
	lower_case_only = Letter.lower()
	for char in lower_case_only:
		if char in characthers:
			characthers[char] += 1
		else:		
			characthers[char] = 1

main()
