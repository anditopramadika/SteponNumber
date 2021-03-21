# 0 =  [0,0]    habis di Mod 2
# 1 =  [1,1]    --
# 2 =  [2,0]    habis di Mod 2
# 3 =  [3,1]    --
# 4 =  [2,2]    habis di Mod 2
# 5 =  [3,3]    --
# 6 =  [4,2]    habis di Mod 2
# 7 =  [5,3]    --
# 8 =  [4,4]    habis di Mod 2
# 9 =  [5,5]    --
# 10 = [6,4]    habis di Mod 2
# 11 = [7,5]    --
# 12 = [6,6]    habis di Mod 2
# Def Function 
def steponNumber(numbers):               
    x = numbers[0]                               # x = list paling depan (0)
    y = numbers[1]                               # y = list selanjutnya (1)
    list_akhir = []                              # list kosong untuk append di akhir
    if x < 0 and y < 0 :                            # Jika x dan y lebih kecil dari 0, maka dia No Number
        print('No Number')

    else :
        if x == 0 and y == 0 :                          # Jika x dan y sama dengan 0, maka dia akan 0 juga di grafik
            i = 0
            return i
        elif x % 2 == 0 and y % 2 == 0 :                # Jika x dan y habis di mod 2, maka value keluar
            i = x+y
            return i
        elif x == 1 and y == 1 :                        # jika x dan y 1, hasilnya x+y-1
            i = x+y-1
            return i
        elif x == 3 and y == 1 :                        # Jika x = 3 dan y = 1, hasilnya x+y-1
            i = x+y-1
            return i
        elif x == 3 and y == 3 :                        # Jika x = 3 dan y = 3, hasilnya x+y-1
            i = x+y-1
            return i
        elif x == 5 and y == 3 :                        # Jika x = 5 dan y = 3, hasilnya x+y-1
            i = x+y-1
            return i
        elif x == 5 and y == 5 :                        # Jika x = 5 dan y = 5, hasilnya x+y-1
            i = x+y-1
            return i
        elif x == 7 and y == 5 :                        # Jika x = 7 dan y = 5, hasilnya x+y-1
            i = x+y-1
            return i
        else :
            return('No Number')                         # Jika selain diatas, maka 'No Number'

numbers = [[4,2],[6,6],[3,4]]                           # List numbers yang diinginkan


print(steponNumber(numbers[0]))                         # Print per List dari awal sampai akhir
print(steponNumber(numbers[1]))
print(steponNumber(numbers[2]))