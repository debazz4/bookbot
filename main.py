def  main():
	path_dir = "books/frankenstein.txt"
	text = get_book_text(path_dir)
	num_words = get_num_words(text)
	char_dict = get_chars_dict(text)
	lis = get_con(char_dict)
	chars_sorted_list = chars_dict_to_sorted_list(char_dict)
	msg = f"{num_words} words found in the document"

	print("--- Begin report of books/frankstein.txt ---")
	print(msg)
	print()

	for item in chars_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"The '{item['char']}' character was found  {item['num']} times")

	print("--- End report ---")

def sort_on(d):
	return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
	sorted_list = []
	for ch in num_chars_dict:
		sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list
def get_chars_dict(text):
	chars = {}
	for c in text:
		lowered = c.lower()
		if lowered in chars:
			chars[lowered] += 1
		else:
			chars[lowered] = 1
	return chars

def get_con(chars):
	char_list = []
	for key, value in chars.items():
		char_list.append({key, value})
	char_list.sort(reverse=True)
	return char_list

def get_num_words(text):
	words = text.split()
	return len(words)

def get_book_text(path):
	with open(path) as f:
		return f.read()
main()
