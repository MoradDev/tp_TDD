

class FizzBuzz :

    def affiche (self, nombre) :
        reponse=""
        for i in range(nombre + 1):
            if i==0 :
                pass
            elif i%15==0 :
                reponse += "FrisBee"
            elif i%5==0 :
                reponse += "Buzz"
            elif i%3==0 :
                reponse += "Fizz"
            else :
                reponse += str(i)
        print(reponse)
        return reponse