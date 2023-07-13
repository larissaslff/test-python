from survey import AnonymousSurvey

question = 'What langauge did you first learn to speak? '

my_survey = AnonymousSurvey(question)
my_survey.show_question()
print('Enter q at any time to quit')
while True:
    response = input(str('Language: '))
    if response == 'q':
        break
    my_survey.store_response(response)
print('Thank you everyone who participated in the survey!')
my_survey.show_results()