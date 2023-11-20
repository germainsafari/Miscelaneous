def Convert(s, sbase, dbase):
    string = "0123456789ABCDEF" 
    dnbr = 0
    for char in s:
        if char.upper() in string[:sbase]: 
            dnbr = dnbr * sbase + string.index(char.upper())
        else:
            return "wrong character, do it again"

   
    res = ""
    if dnbr == 0:
        return '0'
    
    while dnbr:
        dnbr, rem = divmod(dnbr, dbase)
        res = string[rem] + res  
        
    return res

print(Convert("59", 10, 2)) 				#"111010"
print(Convert("101", 2, 10) )				#"5"
print(Convert("101001011101", 2, 16))	    #"A5D"
print(Convert("72312", 8, 8) 	)			 #"72312"
print(Convert("92312", 8, 8) )				 #Error (unrecognized digit)
print(Convert("0xA", 10, 8) 	)			 #Error (source base ambiguous)
