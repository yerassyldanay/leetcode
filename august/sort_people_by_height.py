from typing import List, Any
import sys


class Solution:
    def __init__(self):
        self.temp = [float("inf"), float("inf")]

    def reconstructQueue(self, people: List[List[Any]]) -> List[List[int]]:

        print(">>> ", people)

        result = []
        num_of_elements = 0
        for i, person in enumerate(people):
            if person[1] == 0:
                result.append(person)
                people[i] = self.temp.copy()
            else:
                num_of_elements = num_of_elements + 1
        
        #
        # it was [[7, 0], [5, 0]]
        #      it will become [[5, 0], [7, 0]]
        result = sorted(result, key=lambda x: x[0])

        #
        # do until no person left in an initial order / list
        while num_of_elements:
            person = self.temp.copy()
            i = 0
            for ix, per in enumerate(people):
                if (per[1] == person[1] and per[0] < person[0]) or per[1] < person[1]:
                    person = per
                    i = ix

            print(num_of_elements, people, result)
            if not person:
                continue

            if len(result) < person[1]:
                continue

            # if person[1] == 4:
            #     return result

            count_higher_people = 0
            height = person[0] # 7
            frontier = person[1] # 1

            inserted = False
            for j, res in enumerate(result):
                if res[0] >= height:
                    #
                    # go through result list and count the number of person with height higher than
                    #       the given one
                    count_higher_people = count_higher_people + 1

                if count_higher_people == person[1]:
                    #
                    # consider whether an element has heights lower than its
                    #       we must put after them as this does not affect person (we are considering)
                    #       but will affect the next one
                    ti = j + 1
                    while len(result) < ti and result[ti][0] < height:
                        ti = ti + 1

                    result.insert(ti, person)

                    #
                    # remove person from the unordered / provided list
                    #      decrement number of valid elements in that list
                    people[i] = self.temp.copy()
                    num_of_elements -= 1

                    inserted = True

                else:
                    continue

            if not inserted:
                num_of_elements -= 1
                people[i] = self.temp.copy()
                result.append(person)

        print(people)
        return result

s = Solution()
a = s.reconstructQueue( [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]] )

print(a)

assert a == [[3,0],[6,0],[7,0],[5,2],[3,4],[5,3],[6,2],[2,7],[9,0],[1,9]]

