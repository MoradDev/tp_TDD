

class FizzBuzz :

    def affiche (self, nombre) :
        reponse=""
        for i in range(nombre):
            if i%15==0 :
                reponse += "FrisBee"
            if i%5==0 :
                reponse += "Buzz"
            if i%3==0 :
                reponse += "Fizz"
            reponse += str(i)
        return reponse