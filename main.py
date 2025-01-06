characthers = {}

def main():	
	book_path ="books/frankenstein.txt"
	text = get_book_text(book_path)
	word_counts = number_of_words_in_book(text)
	report = report_soldier(book_path, word_counts, characthers)

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
	return char

def report_soldier(book_path, word_counts, characthers):
	
	print(f"--- reporting on {book_path} SIR! ---")
	print(f"{word_counts} words were found in the document!")
	new_dict= (dict(sorted(characthers.items(), key=lambda x: x[1], reverse = True)))
	for	d in new_dict:
		if d.isalpha():
			value = new_dict[d]
			print(f"The characther {d} was found {value} times")
	print(f"--- thus concluded my report SIR! BOOT! SIR! ---")

main()


