class Array:
    def __init__(self, ar = []):
        self.array = ar



    def BubbleSort(self):
        # loop to access each array element
        for i in range(len(self.array)):

            # loop to compare array elements
            for j in range(0, len(self.array) - i - 1):

                # compare two elements
                if self.array[j] > self.array[j + 1]:
                    # swapping elements
                    temp = self.array[j]
                    self.array[j] = self.array[j + 1]
                    self.array[j + 1] = temp
        return self.array




