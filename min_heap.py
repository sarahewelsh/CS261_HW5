# Course: CS261 - Data Structures
# Student Name:  Sarah Welsh
# Assignment: 5
# Description: Min heap methods


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Add new node at end of heap array and move to appropriate location in heap array.
        """
        self.heap.append(node)

        new_index = self.heap.length() - 1
        if new_index == 0:
            parent_index = 0
        else:
            parent_index = (new_index - 1) // 2

        # while the parent node is larger than the child node, swap the nodes
        while self.heap.get_at_index(parent_index) > self.heap.get_at_index(new_index):
            self.heap.swap(parent_index, new_index)
            new_index = parent_index
            if new_index == 0:
                parent_index = 0
            else:
                parent_index = (new_index - 1) // 2

    def get_min(self) -> object:
        """
        Return value of node with minimum value
        """
        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Remove the node with the minimum value and rearrange nodes as necessary.
        """
        if self.heap.length() == 0:
            raise MinHeapException

        # save min val and last node
        min_val = self.heap.get_at_index(0)
        last = self.heap.get_at_index(self.heap.length() - 1)

        # move last node to front
        self.heap.set_at_index(0, last)
        self.heap.pop()

        # if top of heap has at least 2 children, set indexes for current node and children nodes
        if self.heap.length() > 2:
            curr_index = 0
            left_child_index = (curr_index * 2) + 1
            right_child_index = (curr_index * 2) + 2

            # if the current nodes is still bigger than at least one of the children, keep going
            while self.heap.get_at_index(curr_index) > self.heap.get_at_index(left_child_index) or self.heap.get_at_index(curr_index) > self.heap.get_at_index(right_child_index):

                # if left child index updated on last round, but right child index didn't, break out of the loop
                if right_child_index < left_child_index:
                    break

                # if right child doesn't exist, swap with left child, updated indexes if possible
                if right_child_index >= self.heap.length():
                    self.heap.swap(curr_index, left_child_index)
                    curr_index = left_child_index
                    if (curr_index * 2) + 1 < self.heap.length() - 1:
                        left_child_index = (curr_index * 2) + 1
                    else:
                        break
                    if (curr_index * 2) + 2 < self.heap.length() - 1:
                        right_child_index = (curr_index * 2) + 2
                    else:
                        continue

                # if left child is smaller, swap with left child and update indexes if possible
                elif self.heap.get_at_index(left_child_index) <= self.heap.get_at_index(right_child_index):
                    self.heap.swap(curr_index, left_child_index)
                    curr_index = left_child_index
                    if (curr_index * 2) + 1 < self.heap.length() - 1:
                        left_child_index = (curr_index * 2) + 1
                    else:
                        break
                    if (curr_index * 2) + 2 < self.heap.length() - 1:
                        right_child_index = (curr_index * 2) + 2
                    else:
                        continue

                # otherwise, swap with right child and update indexes if possible
                else:
                    self.heap.swap(curr_index, right_child_index)
                    curr_index = right_child_index
                    if (curr_index * 2) + 1 < self.heap.length() - 1:
                        left_child_index = (curr_index * 2) + 1
                    else:
                        break
                    if (curr_index * 2) + 2 < self.heap.length() - 1:
                        right_child_index = (curr_index * 2) + 2
                    else:
                        continue

            # If the new right child would be the last value in the array, check which child is smaller and swap if
            # necessary.
            if (curr_index * 2) + 2 == self.heap.length() - 1:
                if self.heap.get_at_index((curr_index * 2) + 1) <= self.heap.get_at_index((curr_index * 2) + 2):
                    if self.heap.get_at_index(curr_index) > self.heap.get_at_index((curr_index * 2) + 1):
                        self.heap.swap(curr_index, (curr_index * 2) + 1)
                elif self.heap.get_at_index(curr_index) > self.heap.get_at_index((curr_index * 2) + 2):
                    self.heap.swap(curr_index, (curr_index * 2) + 2)

            # If the new left child would be the last value in the array, swap if necessary.
            elif (curr_index * 2) + 1 == self.heap.length() -1:
                if self.heap.get_at_index(curr_index) > self.heap.get_at_index((curr_index * 2) + 1):
                    self.heap.swap(curr_index, (curr_index * 2) + 1)

        # if only 2 items in heap now, swap if necessary
        elif self.heap.length() == 2:
            if self.heap.get_at_index(0) > self.heap.get_at_index(1):
                self.heap.swap(0, 1)

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        i = self.heap.length()
        while i > 0:
            self.heap.pop()
            i -= 1

        for j in range(0, da.length()):
            self.heap.append(None)
            self.heap.set_at_index(j, da.get_at_index(j))

        curr_index = (da.length()//2) - 1
        left_child_index = ((curr_index * 2) + 1)
        right_child_index = ((curr_index * 2) + 2)
        while curr_index >= 0:
            if self.heap.get_at_index(curr_index) > self.heap.get_at_index(left_child_index) or self.heap.get_at_index(curr_index) > self.heap.get_at_index(right_child_index):
                if self.heap.get_at_index(left_child_index) <= self.heap.get_at_index(right_child_index):
                    if self.heap.get_at_index(curr_index) > self.heap.get_at_index(left_child_index):
                        self.heap.swap(curr_index, left_child_index)
                        curr_index = curr_index - 1
                        left_child_index = ((curr_index * 2) + 1)
                        right_child_index = ((curr_index * 2) + 2)
                elif self.heap.get_at_index(left_child_index) > self.heap.get_at_index(right_child_index):
                    if self.heap.get_at_index(curr_index) > self.heap.get_at_index(right_child_index):
                        self.heap.swap(curr_index, right_child_index)
                        curr_index = curr_index - 1
                        left_child_index = ((curr_index * 2) + 1)
                        right_child_index = ((curr_index * 2) + 2)
            else:
                curr_index = curr_index - 1
                left_child_index = ((curr_index * 2) + 1)
                right_child_index = ((curr_index * 2) + 2)


# BASIC TESTING
if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)
    #
    #
    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())
    #
    #
    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    # print("\nPDF - remove_min example 2")
    # print("--------------------------")
    # h = MinHeap([869, 871, 909, 888, 899, 913, 911, 893, 903, 968, 965, 916, 926, 912, 932, 923, 994, 937, 955, 970, 990, 997, 975, 992, 972, 979, 997, 938, 918, 959, 974, 927, 982])
    # print(h.remove_min())
    # print(h)
    #
    # print("\nPDF - remove_min example 3")
    # print("--------------------------")
    # h = MinHeap([216, 226, 222, 228, 231, 249, 278, 230, 237, 284, 251, 256, 254, 302, 354, 238, 250, 284, 258, 402, 321, 287, 277, 287, 426, 263, 456, 339, 512, 380, 356, 264, 345, 389, 289, 307, 337, 262, 329, 522, 573, 416, 525, 480, 364, 298, 345, 496, 304, 656, 436, 277, 275, 568, 556, 607, 390, 513, 664, 576, 397, 457, 368, 277, 330, 451, 359, 506, 400, 482, 440, 444, 445, 488, 770, 309, 930, 411, 383, 857, 537, 758, 634, 674, 472, 601, 703, 597, 766, 960, 509, 362, 376, 517, 384, 823, 548, 327, 403, 772, 779, 646, 891, 320, 376, 590, 487, 625, 638, 910, 635, 875, 915, 441, 772, 721, 590, 827, 713, 690, 752, 670, 512, 530, 627, 727, 661, 338, 416, 384, 359, 498, 691, 553, 595, 612, 589, 661, 963, 535, 701, 579, 614, 848, 444, 996, 798, 743, 838, 883, 894, 410, 440, 946, 997, 580, 894, 699, 867, 886, 918, 604, 542, 922, 814, 636, 912, 737, 973, 772, 628, 733, 927, 921, 748, 610, 764, 915, 996, 961, 967, 749, 560, 671, 663, 656, 995, 941, 704, 724, 866, 962, 893, 845, 978, 846, 936, 602, 900, 848, 884, 956, 879, 720, 997, 965, 935, 617, 993, 971, 986, 849, 933, 749, 740, 934])
    # print(h.remove_min())
    # print([[222, 226, 249, 228, 231, 254, 278, 230, 237, 284, 251, 256, 263, 302, 354, 238, 250, 284, 258, 402, 321, 287, 277, 287, 426, 275, 456, 339, 512, 380, 356, 264, 345, 389, 289, 307, 337, 262, 329, 522, 573, 416, 525, 480, 364, 298, 345, 496, 304, 656, 436, 277, 487, 568, 556, 607, 390, 513, 664, 576, 397, 457, 368, 277, 330, 451, 359, 506, 400, 482, 440, 444, 445, 488, 770, 309, 930, 411, 383, 857, 537, 758, 634, 674, 472, 601, 703, 597, 766, 960, 509, 362, 376, 517, 384, 823, 548, 327, 403, 772, 779, 646, 891, 320, 376, 590, 740, 625, 638, 910, 635, 875, 915, 441, 772, 721, 590, 827, 713, 690, 752, 670, 512, 530, 627, 727, 661, 338, 416, 384, 359, 498, 691, 553, 595, 612, 589, 661, 963, 535, 701, 579, 614, 848, 444, 996, 798, 743, 838, 883, 894, 410, 440, 946, 997, 580, 894, 699, 867, 886, 918, 604, 542, 922, 814, 636, 912, 737, 973, 772, 628, 733, 927, 921, 748, 610, 764, 915, 996, 961, 967, 749, 560, 671, 663, 656, 995, 941, 704, 724, 866, 962, 893, 845, 978, 846, 936, 602, 900, 848, 884, 956, 879, 720, 997, 965, 935, 617, 993, 971, 986, 849, 933, 749, 934]])
    # print(h)
    #
    # print("\nPDF - remove_min example 3")
    # print("--------------------------")
    # h = MinHeap([412, 412, 412, 414, 420, 453, 412, 423, 420, 434, 437, 462, 454, 449, 424, 426, 452, 447, 420, 484, 436, 458, 439, 491, 464, 520, 507, 485, 469, 463, 435, 449, 451, 477, 466, 499, 456, 459, 428, 567, 558, 484, 579, 490, 474, 443, 456, 510, 509, 536, 523, 609, 596, 582, 535, 497, 574, 628, 631, 540, 480, 448, 461, 488, 607, 503, 572, 692, 528, 478, 534, 514, 659, 686, 513, 649, 471, 532, 542, 613, 580, 612, 584, 616, 596, 612, 629, 603, 527, 492, 498, 757, 665, 464, 816, 511, 540, 518, 605, 732, 748, 669, 574, 639, 780, 623, 626, 650, 674, 665, 599, 616, 588, 705, 629, 733, 648, 666, 708, 553, 673, 512, 485, 451, 599, 732, 667, 578, 558, 663, 612, 554, 525, 644, 831, 713, 862, 560, 567, 637, 603, 591, 735, 598, 523, 681, 675, 739, 751, 736, 561, 868, 755, 725, 681, 807, 657, 662, 734, 705, 848, 786, 634, 873, 840, 826, 773, 680, 657, 731, 612, 722, 701, 718, 925, 746, 644, 907, 551, 614, 595, 921, 745, 938, 868, 896, 698, 725, 492, 890, 955, 609, 964, 698, 994, 840, 776, 738, 798, 846, 754, 928, 765, 863, 994, 959, 665, 975, 718, 968, 836, 686, 630, 882, 627, 757, 825, 739, 925, 936, 983, 880, 979, 906, 915, 610, 704, 964, 867, 633, 664, 865, 912, 799, 778, 936, 818, 739, 973, 703, 850, 707, 751, 791, 986, 885, 515, 911, 694, 934, 877, 898, 970, 940, 751, 773, 824, 862, 813, 713, 681, 744, 767, 697, 554, 528, 761, 693, 853, 932, 846, 835, 836, 876, 924, 944, 763, 819, 839, 893, 670, 719, 706, 971, 603, 818, 866, 966, 970, 965, 904, 958, 929, 720, 854, 740, 909, 812, 899, 908, 738, 583, 797, 869, 916, 825, 962, 823, 792, 843, 844, 932, 907, 773, 744, 882])
    # print(h.remove_min())
    # print(h)
    #
    # print("\nPDF - remove_min example 3")
    # print("--------------------------")
    # h = MinHeap([976, 976, 982, 998, 989, 998])
    # print(h.remove_min())
    # print(h)
    #
    # print("\nPDF - remove_min example 3")
    # print("--------------------------")
    # h = MinHeap([988, 996, 994])
    # print(h.remove_min())
    # print(h)


    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)

    # print("\nPDF - build_heap example 1")
    # print("--------------------------")
    # da = DynamicArray([123, 5423, 32, 50, 4382, 43, -2, 4345, 3, 453])
    # h = MinHeap(['zebra', 'apple'])
    # print(h)
    # h.build_heap(da)
    # print(h)
    # da.set_at_index(0, 500)
    # print(da)
    # print(h)

    # print("\nPDF - build_heap example 2")
    # print("--------------------------")
    # da = DynamicArray([840, 727, 85, -977, -65, 840, 575, 567, 297, 526, 988, -502, 67, -469, -130, -312, 927, 199, 960, -861, -66, 605, -530, -310, -163, -257, -317, 562, 318, -770, -873, 763, 729, -552, 303, -37, -996, 147, 520, 489, -264, -703, 117, 90, -433, -798, -216, -918, -100, 497, 751, 122, 746, -976, 658, -521, -476, 565, -684, -643, 915, 662, -870, 969, -999, 910, 733, 828, 22, 872, -804, -886, 840, -458, -495, -244, 606, 559, 84, 199, 806, 120, -611, 717, -294, -542, -796, -39, 894, 540, -574, -351, -446, 22, 50, -643, -965, -366, 444, -117, 466, 560, -309, 719, -227, 583, -996, 642, -804, 620, -871, 59, 919, -278, 171, -874, 609, 722, -126, -705, -992, 410, -428, 523, 429, -568, 815, -709, -678, 185, 73, -622, 851, -373, -770, -671, 33, -197, -702, 535, 910, 412, 477, -606, 895, -365, -167, -288, -467, 765, -886, -28, 89, 584, 97, 971, 446, 493, 728, -768, 568, -893, 105, -89, -72, 21, 555, 855, 947, 670, -551, -962, 781, 131, 688, 525, -619, 934, 547, 684, 706, -200, 325, -556, -111, 712, 74, 357, -255, -169, -664, -987, -382, -413, 432, 498, 306, -812, 365, -420, -707, 293, -367, -226, -932, -449, 307, -989, -157, -508, -337, 6, 193, -583, -989, 565, 749, 61, -799, 496, -301, 548, 289, -792, 240, -845, -51, -814, -765, -202, -385, 237, -131, 111, 443, 886, 668, 232, 333, 458, -178, 88, -962, -620, 866, 447, 314, 617, -614, 647, 702, -800, -945, 187, 738, 495, 707, -984, 10, 657, -645, 827, -984, 545, 439, -753, 406, -479, 75, -479, -13, -121, 414, -236, 168, -246, 27, 614, -789, -790, -145, 229, 726, -330, 349, 837, 395, -76, 74, 877, 584, 293, 449, 383, 432, 421, -948, -440, -352, -979, -969, -46, -825, -684, 854, -237, 989, -811, 655, 893, 356, -729, 77, -426, 713, -419, -673, -230, 689, 349, 323, -457, 68, -649, -578, 997, -64, 910, 42, -311, 317, -105, -545, -849, -55, 998, 46, -50, -497, 955, -299, 637, -641, -942, 500, -968, -45, -20, -69, 836, 108, -253, -66, 383, -287, 202, -843, -920, 208, 204, 617, 806, 579, 325, -741, 343, -87, 747, 165, 22, -574, 523, -457, -695, 825, -259, 431])
    # h = MinHeap(['zebra', 'apple'])
    # h.build_heap(da)
    # print(h)

    print("\nPDF - build_heap example 2")
    print("--------------------------")
    da = DynamicArray([840, 727, 85, -977, -65, 840, 575, 567, 297, 526, 988, -502, 67, -469, -130, -312, 927, 199, 960, -861, -66, 605, -530, -310, -163, -257, -317, 562, 318, -770, -873, 763, 729, -552, 303, -37, -996, 147, 520, 489, -264, -703, 117, 90, -433, -798, -216, -918, -100, 497, 751, 122, 746, -976, 658, -521, -476, 565, -684, -643, 915, 662, -870, 969, -999, 910, 733, 828, 22, 872, -804, -886, 840, -458, -495, -244, 606, 559, 84, 199, 806, 120, -611, 717, -294, -542, -796, -39, 894, 540, -574, -351, -446, 22, 50, -643, -965, -366, 444, -117, 466, 560, -309, 719, -227, 583, -996, 642, -804, 620, -871, 59, 919, -278, 171, -874, 609, 722, -126, -705, -992, 410, -428, 523, 429, -568, 815, -709, -678, 185, 73, -622, 851, -373, -770, -671, 33, -197, -702, 535, 910, 412, 477, -606, 895, -365, -167, -288, -467, 765, -886, -28, 89, 584, 97, 971, 446, 493, 728, -768, 568, -893, 105, -89, -72, 21, 555, 855, 947, 670, -551, -962, 781, 131, 688, 525, -619, 934, 547, 684, 706, -200, 325, -556, -111, 712, 74, 357, -255, -169, -664, -987, -382, -413, 432, 498, 306, -812, 365, -420, -707, 293, -367, -226, -932, -449, 307, -989, -157, -508, -337, 6, 193, -583, -989, 565, 749, 61, -799, 496, -301, 548, 289, -792, 240, -845, -51, -814, -765, -202, -385, 237, -131, 111, 443, 886, 668, 232, 333, 458, -178, 88, -962, -620, 866, 447, 314, 617, -614, 647, 702, -800, -945, 187, 738, 495, 707, -984, 10, 657, -645, 827, -984, 545, 439, -753, 406, -479, 75, -479, -13, -121, 414, -236, 168, -246, 27, 614, -789, -790, -145, 229, 726, -330, 349, 837, 395, -76, 74, 877, 584, 293, 449, 383, 432, 421, -948, -440, -352, -979, -969, -46, -825, -684, 854, -237, 989, -811, 655, 893, 356, -729, 77, -426, 713, -419, -673, -230, 689, 349, 323, -457, 68, -649, -578, 997, -64, 910, 42, -311, 317, -105, -545, -849, -55, 998, 46, -50, -497, 955, -299, 637, -641, -942, 500, -968, -45, -20, -69, 836, 108, -253, -66, 383, -287, 202, -843, -920, 208, 204, 617, 806, 579, 325, -741, 343, -87, 747, 165, 22, -574, 523, -457, -695, 825, -259, 431])
    h = MinHeap(['zebra', 'apple'])
    h.build_heap(da)
    print("expected")
    print([-999, -996, -996, -984, -968, -989, -992, -984, -979, -962, -920, -987, -989, -874, -962, -977, -804, -969, -811, -893, -942, -843, -798, -965, -932, -583, -976, -845, -684, -770, -945, -709, -770, -789, -790, -886, -948, -684, -729, -861, -849, -703, -796, -619, -741, -695, -664, -918, -812, -707, -449, -508, -257, -804, -871, -792, -814, -131, -469, -705, -620, -614, -873, -678, -645, -753, -479, -671, -702, -145, -330, -606, -365, -467, -886, -244, 97, -426, -673, -768, -649, -311, -611, -497, -641, -542, -69, -287, 90, 204, -574, -574, -530, -259, -216, -643, -413, -366, -100, -420, -367, -226, -309, -157, -337, 6, 85, 565, -799, -301, 289, 59, -521, -765, -385, 237, 111, 668, -126, -178, -643, 410, -428, 523, 429, -870, 187, -312, 10, 185, 73, -622, 406, -373, -479, -121, -236, -246, -552, 535, 229, 303, 395, -76, 584, 293, -167, -458, -440, -495, -825, -28, -237, 584, 147, 77, 446, -419, -230, 199, -457, -578, -64, -89, -72, -545, -264, 46, -50, -299, -551, -66, -45, -65, 108, -253, -39, 202, 208, 540, 579, -433, -87, -556, -351, -457, -446, 22, -255, -169, 50, -502, -382, -310, 432, 498, 306, 444, 365, 497, -117, 293, 466, 751, 560, -163, 307, 719, 122, -227, 67, 583, 193, 840, 746, 642, 749, 61, -317, 496, 620, 548, 658, 562, 240, 919, -51, -278, -476, -202, 171, 318, 565, 609, 443, 886, 722, 232, 333, 458, 575, 88, -130, 915, 866, 447, 314, 617, 662, 647, 702, -800, -568, 815, 738, 495, 707, 969, 840, 657, 567, 827, 763, 545, 439, 851, 910, 729, 75, 733, -13, 828, 414, 33, 168, -197, 27, 614, 22, 927, 872, 910, 726, 412, 349, 837, 477, -37, 74, 877, 895, 840, 449, 383, 432, 421, -288, 727, -352, 765, 199, -46, 297, 960, 854, 89, 989, 606, 655, 893, 356, 971, 559, 520, 713, 84, 493, 728, 689, 349, 323, 568, 68, 806, 489, 997, 105, 910, 42, 120, 317, -105, 21, 555, -55, 998, 855, 717, 947, 955, 670, 637, -294, 117, 500, 781, 526, -20, 131, 836, 688, 525, -66, 383, 988, 605, 934, 547, 894, 684, 617, 806, 706, 325, -200, 343, 325, 747, 165, 22, -111, 523, 712, 74, 825, 357, 431])
    print("acutal")
    print(h)



