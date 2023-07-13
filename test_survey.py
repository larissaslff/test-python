import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """
    Teste AnonymousSurvey
    """
    def setUp(self):
        question = 'What langauge did you first learn to speak? '
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Portuguese', 'Spanish']
        
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_tree_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.responses)
        
        
unittest.main()
