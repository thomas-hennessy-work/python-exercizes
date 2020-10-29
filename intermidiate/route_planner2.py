from abc import abstractmethod
# again, intentionaly over engineered into a single class

class Mountains:

    def __init__(self, peakList):
        self.peakList = peakList
        self.pathList = []
        self.currentPos = 0

    def find_path(self):
        self.find_next(True)

        while self.currentPos < len(self.peakList):
            self.find_next(False)

        return self.pathList


    def find_next(self, first):
        # used to track the best number in this cycle
        best_elim_pos = -1
        best_elim_value = len(self.peakList)+1

        # used to track the curently considered numebr
        current_elim_amount = 0
        current_elim_position = 0 
        # enusres the first value of the list is considered
        if first == True:
            count = 0
        else:
            count = 1

        # going through each number available, so long as they dont become pointless to evaluate
        while((count < best_elim_value) and (len(self.peakList)) > best_elim_pos):
            # gets the next value for consideration
            current_elim_position = count + self.currentPos
            # gets the number in the selected position
            current_elim_amount = self.peakList[current_elim_position]

            # any values between this value and the previously selected value are counted as a point 
            current_elim_value = count
            # used to go through each value after the considered value
            considered_count = 1

            # goes through values after the given value
            while(current_elim_position + considered_count) < len(self.peakList):

                # if one of the vlaues after is smaller, add a point
                if self.peakList[current_elim_position + considered_count] > current_elim_value:
                    current_elim_value += 1

                # select next value
                considered_count += 1
            
            count += 1

            if current_elim_value < best_elim_value:
                best_elim_value = current_elim_value
                best_elim_pos = current_elim_position

        self.pathList.append(best_elim_value)
        current_elim_position = best_elim_pos




Himalayas = Mountains([0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15])
print(Himalayas.find_path())