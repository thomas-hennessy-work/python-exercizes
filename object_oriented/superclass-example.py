from abc import abstractmethod

class Bird:
    fly = True

    def noise(self):
        print("Birdnoise")

    babies = 0

    def reproduce(self):
        slef.babies += 1

    def children(self):
        return self.babies

    @abstractmethod
    def eat(self):
        pass

    extinct = False


class Owl(Bird):
    # polymorphism used to ovveride the reproduce method
    def reproduce(self):
        self.babies += 6

    def eat(self):
        print("Peck Peck")

    
class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        print("Nom Nom")

    # polymorphism used to ovveride the reproduce method
    def reproduce(self):
        if self.extinct == False:
            self.babies += 1
        else:
            print("No more dodos")

Hedwig = Owl()
Hedwig.reproduce()
print(Hedwig.children())

Dan = Dodo()
Dan.reproduce()
