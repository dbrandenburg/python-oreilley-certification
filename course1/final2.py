#!/usr/local/bin/python3
"""This program counts the length of each word in a file"""
import string
import sys
import histogram

class text_processor:
    def __init__(self,filename):
        self.filename = filename
        try:
            self.file = open(self.filename)
            self.text = str(self.file.read())
        except IOError:
            print("IOError, could not load file ",self.filename)
            quit()
        except ValueError:
            print("Could not convert data into string.")
        except:
            print("Unexpected error.")
            
    def count_chars_of_words(self,text):
        if text == '':
            return None
        text = text.split( )
        count_list = []
        for word in text:
            count_list.append(len(self.remove_punctuation(word)))
        return count_list
            
    def remove_punctuation(self,word):
        punct_removed_list = []
        for char in word:
            if char not in string.punctuation:
                punct_removed_list.append(char)
        punct_removed_word = ''.join(punct_removed_list)
        return punct_removed_word
        
    def generate_word_len_table(self,word_list=None):
        title = [("Length","Count")]
        word_list = self.count_chars_of_words(self.text)
        max_char_count = max(word_list)
        word_len_table = []
        for i in (range(1,max_char_count + 1)):
            word_len_table.append((i,word_list.count(i)))
        return word_len_table
            
    def __del__(self):
        try:
            self.file.close()
        except:
            pass

if __name__ == "__main__":

    if len(sys.argv) > 1:
        filename = str(sys.argv[1])
    else:
        filename = "declaration.txt"
        
    count = text_processor(filename)
    table = count.generate_word_len_table()
    wordcount_histogram = histogram.histogram(table,20,5,400)