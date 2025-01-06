characthers = {}

def main():	
	book_path ="books/frankenstein.txt"
	text = get_book_text(book_path)
	word_counts = number_of_words_in_book(text)
	sorting = sorting_dictionary(characthers)
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

def sorting_dictionary(dictionary):
	list = turning_to_list(dictionary)
	list.sort(reverse=True, key=order)
	print(list)


def turning_to_list(list):
	dict_list = []
	for dictionary in characthers:
		new_dict = {}
		value = characthers[dictionary]
		new_dict[dictionary] = value
		dict_list.append(new_dict)
	return dict_list

def order(dict):
	return dict[1]

def report_soldier(book_path, word_counts, characthers):
	
	print(f"--- reporting on {book_path} SIR! ---")
	print(f"{word_counts} words were found in the document!")
	#for d in range(0, len(dict_list)):
		#print(f"SIR! {d}")

main()


