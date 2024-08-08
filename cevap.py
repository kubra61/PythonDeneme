sayi = int(input("Pozitig bir sayi giriniz:"))

if sayi >= 0 :
    def format_number(sayi):
        count = 0
        while(sayi >= 1000):
            count += 1
            sayi // 1000
        str_sayi = str(sayi)
        virgullu_str_sayi = ""
        
        for i in str_sayi:
            virgullu_str_sayi += i
            if (virgullu_str_sayi.count() == 3 or virgullu_str_sayi.count() == 6):
                virgullu_str_sayi += ","

        return virgullu_str_sayi
    
format_number(1000000)
    
