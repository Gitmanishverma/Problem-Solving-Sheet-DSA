# question-Given a string S, the task is to print all the duplicate characters with their occurrences in the given string.

# Example:

# Input: S = “geeksforgeeks”
# Output:
# e, count = 4
# g, count = 2
# k, count = 2
# s, count = 2

#question link-https://www.google.com/url?q=https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/&sa=D&source=editors&ust=1725950434689487&usg=AOvVaw3kA9q0B-u12Nl65_Pvm00B

a=input("Enter the string")
lis=list(a)
lis.sort()
print(lis)

i=0
while(i< len(lis)):
    count=1
    
    while(i<len(lis)-1 and lis[i]==lis[i+1]):
        count+=1
        i+=1
    if count>1:
        print(lis[i],':',"have",count,"duplicates")
    i+=1
    





