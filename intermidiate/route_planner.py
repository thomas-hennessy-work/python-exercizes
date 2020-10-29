from abc import abstractmethod
# intentionaly over engineered into a single class

class Mountains:
    
    def __init__(self, peakList):
        self.peakList = peakList
        self.eliminationTollerence = 1
        self.pathList = []
        self.finalpathList = []
        self.currentPos = 0


    def find_path(self):
        # while all possible outcomes are being considered
        while self.eliminationTollerence < len(self.peakList):

            self.plan_route()
            self.compare_routes()
            self.inc_elim_tol()

        return self.finalpathList

    
    def inc_elim_tol(self):
        self.eliminationTollerence += 1

    
    def plan_route(self):
        count = 0

        # while peaks can still be reached using this elimination tollerence, and the current peak is not being considered
        while self.eliminationTollerence - count > 0:
            # if the next considered peak is taller than the current peak and not outside of the list given
            if ((self.currentPos + self.eliminationTollerence - count) < len(self.peakList)) and (self.peakList[self.currentPos + self.eliminationTollerence - count] > self.peakList[self.currentPos]):

                self.pathList.append(self.peakList[self.currentPos + self.eliminationTollerence - count])
                self.currentPos = self.currentPos + self.eliminationTollerence - count

                count = 0

                # recersivly calling the method untill no more peaks can be reached
                self.plan_route()

            # if it is not taller, consider the peak before it
            else:
                count += 1


    def compare_routes(self):
        if self.finalpathList == []:
            self.finalpathList = self.pathList
        elif len(self.finalpathList) < len(self.pathList):
            self.finalpathList = self.pathList

Himalayas = Mountains([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15])
print(Himalayas.find_path())