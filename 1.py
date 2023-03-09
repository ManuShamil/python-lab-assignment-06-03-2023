import sys

class College:
    def __init__(self, name, facilities, academics, infrastructure):
        self.name = name
        self.facilities = facilities
        self.academics = academics
        self.infrastructure = infrastructure

    def total_score(self):
        return self.facilities + self.academics + self.infrastructure


class Authority:
    input_lines = []
    input_itr = iter( input_lines )
    colleges = []


    def __init__( self ):
        pass

    def feed_input( self) :
        self.input_lines = [ line.strip() for line in sys.stdin.readlines() ]
        self.input_itr = iter( self.input_lines )

        num_colleges = int( next( self.input_itr ) )
        print(f"Enter the number of colleges: {num_colleges}")

        for i in range(num_colleges):
            name = next( self.input_itr )
            print(f"Enter the name of the college: {name}")

            scores = [ int(x) for x in next( self.input_itr ).split() ]
            facilities = scores[0]
            academics = scores[1]
            infrastructure = scores[2]

            print(f"Enter the scores: {facilities} {academics} {infrastructure}")

            if 0 < facilities <= 25 and 0 < academics <= 50 and 0 < infrastructure <= 25:
                self.colleges.append(College(name, facilities, academics, infrastructure))
            else:
                print('Invalid input')


    # Use selection sort to sort the colleges by total score in descending order
    def sort_colleges( self, colleges_list ):
        for i in range(len(colleges_list)):
            max_score_index = i
            for j in range(i + 1, len(colleges_list)):
                if colleges_list[j].total_score() > colleges_list[max_score_index].total_score():
                    max_score_index = j

        # Swap the colleges if necessary
        if max_score_index != i:
            colleges_list[i], colleges_list[max_score_index] = colleges_list[max_score_index], colleges_list[i]

    # Print the sorted list of colleges
    def print( self ):
        for i, college in enumerate( self.colleges ):
            print(f"{i + 1}. {college.name}: {college.total_score()}")


if __name__ == '__main__':
    authority = Authority()
    authority.feed_input()
    authority.sort_colleges(authority.colleges)
    authority.print()