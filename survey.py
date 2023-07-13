class AnonymousSurvey():
    """
    Coleta respostas anonimas 
    """
    def __init__(self, question):
        """_summary_
        Armazena uma pergunta e se prepara para as respostas
        """
        self.question = question
        self.responses = []
    
    
    def show_question(self):
        """
        Mostra a pergunta armazenada
        """
        print(self.question)
    
    
    def store_response(self, response):
        """
        Armazena a resposta
        """
        self.responses.append(response)
    
    
    def show_results(self):
        """
        Mostra as respostas dadas
        """
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
        