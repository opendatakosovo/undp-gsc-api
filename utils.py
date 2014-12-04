class Utils():

    @staticmethod
    def get_number_of_answers(qid):
        '''
            Get the number of answers expected for each question.
        '''
        if qid == 1:
            return 12

        elif qid in [2, 5, 7]:
            return 6

        elif qid == 10:
            return 7

        elif qid == 11:
            return 11

        elif qid == 12:
            return 4

        elif qid == 13:
            return 10
            
        else:
            return -1

