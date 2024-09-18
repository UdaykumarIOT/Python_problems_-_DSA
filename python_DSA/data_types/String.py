# class text is a mutable where string is not.

class text:
    def __init__(self,value = '') -> None:
        self.value = value
        
    def __str__(self) -> str:
        return self.value
    
    def __getitem__(self,index) -> str:
        return self.value[index]
    
    def __setitem__(self,index,value) -> None: 
        text_items = [*self.value]
        if text.ischar(value): text_items[index] = value
        else: text_items[index] = [*value]
        self.value = ''.join(text_items)
    
    def __delitem__(self,index) -> None:
        text_items = [*self.value]
        del text_items[index]
        self.value = ''.join(text_items)
    
    def __add__(self,other:object) -> object:
        return text(self.value + str(other))
    
    def __iadd__(self, other:object) -> object:
        self.value += str(other)
        return self

    def __mul__(self,other:object) -> object:
        return text(self.value * other)
    
    def __imul__(self, other:object) -> object:
        self.value *= other
        return self
    
    def __eq__(self, other: object) -> bool:
        text2 = str(other)
        if len(self.value) != len(text2): return False
        for chr1 , chr2 in zip(self.value , text2 ):
            if chr1 != chr2: return False
        return True

    def __ne__(self, other: object) -> bool:
        text2 = str(other)
        if len(self.value) != len(text2): return True
        for chr1 , chr2 in zip(self.value , text2):
            if chr1 != chr2: return True
        return False

    def __contains__(self, char) -> bool:
        for ltr in  self.value:
            if ltr == char:
                return True
        return False
    
    def __len__(self) -> int:
        cnt = 0
        for _ in self.value:
            cnt += 1
        return cnt
    
    @staticmethod
    def ischar(char) -> bool:
        if len(char) == 1: return True
        return False
    
    def title_text(self) -> str:
        dum = text()
        for idx,ltr in enumerate(self.value):
            if ltr != ' ' and (idx == 0  or self[idx - 1] == ' ') :
                dum += ltr.upper()
            else:
                dum += ltr
        return dum
    
    def upper_case(self) -> str:
        dum = text()
        for ltr in self.value:
            ascy = ord(ltr)
            if ascy >= 97 and ascy <= 122:
                dum += chr( ascy - 32)
            else:
                dum += ltr
        return dum
        
    def lower_case(self) -> str:
        dum = text()
        for ltr in self.value:
            ascy = ord(ltr)
            if ascy >= 65 and ascy <= 90:
                dum += chr( ascy + 32)
            else:
                dum += ltr
        return dum
    
    def capitalize_text(self) -> str:
        dum = text()
        for idx,ltr in enumerate(self.value):
            if ltr != ' ' and (idx == 0  or self[idx - 1] == ' ') :
                dum += ltr.upper()
                return dum + self[idx+1 :]
            else:
                dum += ltr
        return dum

    def swap_case(self) -> str:
        dum = text()
        for ltr in self.value:
            ascy = ord(ltr)
            if ascy >= 65 and ascy <= 90:
                dum += chr( ascy + 32 )
            elif ascy >= 97 and ascy <= 122:
                dum += chr( ascy - 32 )
            else:
                dum += ltr
        return dum
    
    def reverse_text(self) -> str:
        return self[::-1]
    
    def ispalindrome(self) -> bool :
        i , j = 0 , len(self.value)-1
        txt = self.value
        while i < j :
            if txt[i] != txt[j]:
                return False
            i += 1
            j -= 1
        return True
    
    @staticmethod
    def isvowel(char) -> bool :
        vowels = ['a' , 'e' , 'i' , 'o' , 'u' , 'A' , 'E' , 'I' , 'O' , 'U']
        if len(char) != 1: raise ValueError("it should be a char")
        if char in vowels: return True
        return False
    
    def count_vowels(self) -> int :
        cnt = 0 
        for char in self.value:
            if text.isvowel(char):
                cnt += 1
        return cnt
    
    def non_vowels(self) -> str:
        dum = text()
        for char in self.value:
            if not text.isvowel(char) and char != ' ':
                dum += char
        return dum
    
    def vowels(self) -> str:
        dum = text()
        for char in self.value:
            if text.isvowel(char) :
                dum += char
        return dum
    
    def count_words(self) -> int:
        word , cnt = False , 0
        for char in  self.value:
            if char != ' ' and word == False:
                word = True
                cnt += 1
            elif char == ' ' and word == True:
                word = False
        return cnt
    
    def ascii_sum(self) -> int :
        sum = 0
        for char in self.value:
            sum += ord(char)
        return sum
    
    def count_digit(self) -> int :
        cnt = 0
        for char in self.value:
            ascy = ord(char)
            if ascy >= 48 and ascy <= 57:
                cnt += 1
        return cnt
    
    def non_digit(self) -> str:
        dum = text()
        for char in self.value:
            ascy = ord(char)
            if not (ascy >= 48 and ascy <= 57):
                dum += char
        return dum
    
    def word_rvs(self) -> str:
        stack = []
        dum = text()
        for char in self.value:
            if char != ' ': stack.append(char)
            else:
                while stack : dum += stack.pop()
                dum += ' '
        while stack : dum += stack.pop()
        return dum
    
    def words_rvs(self) -> str:
        stack = []
        dum = text()
        for char in self.value[::-1] :
            if char != ' ': stack.append(char)  
            else:
                while stack: dum += stack.pop()
                dum += ' '
        while stack: dum += stack.pop()
        return dum
    
    def stack_vowel_swap(self) -> str:
        stack = []
        dum = text()
        for char in self.value:
            if text.isvowel(char): stack.append(char)
        for char in self.value:
            if text.isvowel(char): dum += stack.pop()
            else: dum += char
        return dum

    def vowel_swap(self) -> str:
        dum = text(self.value)
        i , j = 0 , len(dum)-1
        while i < j:
            while not text.isvowel(dum[i]): i += 1
            while not text.isvowel(dum[j]): j -= 1
            if i < j:
                dum[i] , dum[j] = dum[j] , dum[i]
                i += 1
                j -= 1
        return dum

    @staticmethod
    def sorted_text(txt):
        dum = text(str(txt))
        dum_len = len(dum)
        for i in range(dum_len-1):
            min = i
            for j in range(i+1 , dum_len):
                if dum[j] < dum[min] : min = j
            dum[i] , dum[min] = dum[min] , dum[i]
        return dum
    
    @staticmethod
    def isanagram(s1 , s2) -> bool :
        s1 = str(s1).strip()
        s2 = str(s2).strip()
        if len(s1) != len(s2) : return False 
        txt1 = text.sorted_text(s1)
        txt2 = text.sorted_text(s2)
        if txt1 == txt2:
            return True
        return False
    
    @staticmethod
    def isanagram_hashing(s1 , s2) -> bool:
        hash1 = [0] * 128
        hash2 = [0] * 128
        for char in  s1:
            hash1[ord(char)] += 1
        for char in s2:
            hash2[ord(char)] += 1
        for char in s2:
            if hash1[ord(char)] != hash2[ord(char)]:
                return False
        return True
    
def main():
    txt = text("dddd")
    txt2 = text("ddda")
    print(text.isanagram_hashing(txt , txt2))
    print(txt.upper_case())

if __name__ == '__main__':
    main()