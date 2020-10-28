from abc import abstractmethod

class Mountains:
    
    def __init__(self, peakList):
        self.peakList = peakList
        self.eliminationTollerence = 1
        self.pathList = []
        self.currentPos = 0


    def find_path(self):
        while (len(self.peakList) != self.currentPos) and (self.eliminationTollerence < len(self.peakList)):
            if self.step() == 0:
                break

            if self.currentPos != len(self.peakList):
                self.pathList.clear()
                self.inc_elim_tol()
                self.currentPos = 0
                self.find_path()

        return self.pathList


    
    def inc_elim_tol(self):
        self.eliminationTollerence += 1


    def step(self):
        count = 0
        currentPeak = self.peakList[self.currentPos]

        # checks if the next specified peak is atainable. If not, it will check for any other peaks
        # atainable between the current position and the specified peak 
        while self.eliminationTollerence - count > 0:
            
            # ensures that the selected item is not outside the list of peaks
            if (self.currentPos + self.eliminationTollerence - count) > len(self.peakList):
                consideredPeak = self.peakList[self.currentPos + self.eliminationTollerence - count]

                if consideredPeak > currentPeak:
                    self.pathList.append(consideredPeak)
                    # returns the number of steps taken to reach the next peak
                    return self.eliminationTollerence - count

            count += 1
        
        return 0

Himalayas = Mountains([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15])
print(Himalayas.find_path())