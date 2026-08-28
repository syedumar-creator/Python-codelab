import random
import string
pass_len=8
char=string.ascii_letters+string.digits+string.punctuation
password="".join([random.choice(char)for i in range(pass_len)])
print("Your Random Password is:",password)