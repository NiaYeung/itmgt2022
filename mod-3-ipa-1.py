#!/usr/bin/env python
# coding: utf-8

# In[2]:


def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.
    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "
    
    
    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 
    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    ret = ""
    if letter == ' ':
        return " "
    else:
        if (letter.isupper()):
            ret = chr((ord(letter) + shift - 65 )%26 + 65);
        else:
            ret = chr((ord(letter) + shift - 97)%26 + 97);
        
    return ret;


# In[3]:


shift_letter("H",3)


# In[4]:


shift_letter("X",5)


# In[5]:


shift_letter("J",26)


# In[7]:


shift_letter(" ",26)


# In[17]:


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    
    cipher = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in message:
        if i == ' ':
            cipher += " "
        else:
            if alphabet.index(i) + shift < 26:
                cipher += alphabet[alphabet.index(i) + shift]
            else:
                cipher += alphabet[alphabet.index(i) + shift]%26
            
    return cipher


# In[20]:


caesar_cipher(" ",7)


# In[21]:


caesar_cipher("POLI",7)


# In[22]:


caesar_cipher("PING",4)


# In[8]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.
    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "
    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.
    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    ret = ""
    
    if letter == ' ':
        return " "
    else: 
        if (letter.isupper()):
            ret = chr((ord(letter) + ord(letter_shift))%26 + 65);
        else:
            ret = chr((ord(letter) + ord(letter_shift))%26 + 97);
        
    return ret;


# In[9]:


shift_by_letter("A", "C")


# In[10]:


shift_by_letter("B", "K")


# In[11]:


shift_by_letter("A", "A")


# In[12]:


shift_by_letter(" ", "A")


# In[60]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.
    Example:
    vigenere_cipher("A C", "KEY") -> "K A"
    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.
    Returns
    -------
    str
        the message, shifted appropriately.
    '''
def vigenere_cipher(message, key): 

    ret = ''
    newkey = [ord(i) for i in key]
    newmessage = [ord(i) for i in message]
    
    for i in range(len(newmessage)):
        if message[i].isalpha():
            ret += chr(((newmessage[i] + newkey[i %len(key)])%26) + 65)
        else:
            ret += message[i]
                   
    return ret
                   
                   
                   
                   


# In[61]:


vigenere_cipher("LONGTEXT","KEY")


# In[62]:


vigenere_cipher("HAPPINESS","PLAY")


# In[31]:


vigenere_cipher("A C","KEY")


# In[100]:


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.
    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.
    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale
    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".
    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the encoded message
    '''
    
    
'''
this is wrong, but im still disecting why, so please ignore this 

def scytale_cipher(message, shift):
    n = len(message)
    columns = n // shift
    ciphertext = ['_'] * n
    for i in range(n):
        row = i//columns
        col = i % columns
        ciphertext[col * shift + row] = message[i]
        
    return "".join(ciphertext)
'''


def scytale_cipher(message, shift):

    if len(message) %shift == 0:
        n = len(message)
        ret = [''] * n
        for i in range(n):
            ret[(i %(n // shift)) * shift + (i // (n // shift))] = message[i]
        return "".join(ret)
    else:
        n = len(message)
        underscore = '_'
        mix = message + ''.join([char * (shift - (n % shift)) for char in underscore])
        ret = len(mix) * ['-']
        for i in range(len(mix)):
            ret[(i %(len(mix) // shift)) * shift + (i //(len(mix) // shift))] = mix[i]
        return "".join(ret)
    


# In[101]:


scytale_cipher(" ", 3)


# In[94]:


scytale_cipher("INFORMATION_AGE", 3)


# In[95]:


scytale_cipher("INFORMATION_AGE", 6)


# In[96]:


scytale_cipher("MEETING", 5)


# In[97]:


scytale_cipher("PLEASE_I_WANT_AN_A", 5)


# In[53]:


scytale_cipher("PEACE_AND_LOVE", 7)


# In[25]:


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.
    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.
    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"
    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
    Returns
    -------
    str
        the decoded message
'''

def scytale_cipher(message, shift):
    n = len(message)
    columns = n // shift
    ciphertext = ['_'] * n
    for i in range(n):
        row = i//columns
        col = i % columns
        ciphertext[col * shift + row] = message[i]
        
    return "".join(ciphertext)
    
def scytale_decipher(ciphertext, shift):
    return scytale_cipher(ciphertext,len(ciphertext)//shift)


# In[18]:


scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8)


# In[19]:


scytale_decipher("IMNNA_FTAOIGROE", 3)


# In[26]:


scytale_decipher("MEIG_ETN__", 5)


# In[36]:


scytale_decipher("PS_T_LEW_AE_AA_AINN_", 5)


# In[31]:


scytale_decipher("PAEADLVEC_N_OE", 7)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




