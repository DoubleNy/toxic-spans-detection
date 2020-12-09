from src.server.core.interfaces import Handler

# class Handler:
#     def execute(self, args) -> None:
#         """
#         Main method for executing handlers
#         :param args: dict
#         """
#         pass

class PollingLayer(Handler):
    """
    A polling layer defines a strategy for reducing the processed input of a `:class:`ConvolutionalLayer`.
    Implementations for this can be using kNN, weighted subsampling, etc.
    """
    def __init__(self):
        pass

    def execute(self, args) -> None:
        pass

    def apply(self, input, filter_x, filter_y):
        """
        Applies the polling implementation over the given convolutional layer
        :param cnn:
        :param kwargs:
        :return:
        """
        # print(filter_x)
        # print(len(input) // filter_x)
        sliced_x = len(input) // filter_x
        sliced_y = len(input[0]) // filter_y
        new_matrix = []
        for piece_x in range(sliced_x):
            print("\n[X] - We're at piece " + str(piece_x))
            new_line = []
            for piece_y in range(sliced_y):
                print("[Y] - We're at piece " + str(piece_y))
                max_cell = 0
                for row in range(filter_x):
                    for col in range(filter_y):
                        current_x = row + (piece_x * filter_x)
                        current_y = col + (piece_y * filter_y)
                        print("*Cell-[%s][%s]"%(current_x, current_y))
                        focus_cell = input[current_x][current_y]
                        if max_cell < focus_cell:
                            max_cell = focus_cell
                new_line.append(max_cell)
            new_matrix.append(new_line)

        print("\n!!! Input -> Maxpolling -> New matrix: ")
        for line in new_matrix:
            print(line)

# if __name__ == '__main__':
#     print("Testing max po0ling")
#     input = [
#         [1, 0, 2, 3],
#         [4, 6, 6, 8],
#         [3, 1, 1, 0],
#         [1, 2, 2, 4]
#         # [2, 3, 4, 5]
#     ]
#     x, y = (2, 1)
#     o = PollingLayer()
#     o.apply(input, x, y)