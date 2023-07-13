import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """
    Teste AnonymousSurvey
    """
    def test_store_single_response(self):
        question = 'What langauge did you first learn to speak? '
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
    
    def test_store_tree_responses(self):
        question = 'What langauge did you first learn to speak? '
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Portuguese', 'Spanish']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, responses)
        
        
unittest.main()
