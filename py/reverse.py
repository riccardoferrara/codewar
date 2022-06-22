# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

def reverse_words(text):
  return ' '.join(t[::-1] for t in text.split(' '))


print(reverse_words('The quick brown fox jumps over the lazy dog.')) #'ehT kciuq nworb xof spmuj revo eht yzal .god'