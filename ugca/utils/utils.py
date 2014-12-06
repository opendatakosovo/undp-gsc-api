class Utils():

    @staticmethod
    def get_number_of_answers(qid):
        '''
            Get the number of answers expected for each question.
        '''
        if qid == 1:
            return 12

        elif qid in [2, 5, 8, 10]:
            return 6

        elif qid == 3:
            return 5

        elif qid in [4, 7, 14]:
            return 2

        elif qid in [6, 9, 15]:
            return 3

        elif qid in [11, 13]:
            return 10

        elif qid == 12:
            return 4
            
        else:
            return -1

