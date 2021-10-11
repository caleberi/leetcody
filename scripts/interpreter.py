#Token type
#
#EOF (end-of-file) token is used to indicate that 
#there is no more input left for lexical analysis

INTEGER,PLUS,EOF = "INTEGER" , "PLUS" , "EOF"

class Token(object):
    """
    Create a Token of a particular type an value\n
    param: <str> type represent a token type \n
    param: <any> value attached to the token\n
    returns: None
    """
    def __init__(self,type,value):
        super().__init__()
        #token type : INTEGER,PLUS,EOF
        self.type =  type
        self.value = value

    def __str__(self):
        """
        Creates a string representation of a Token\n
        ................\n
        example
        - Token("INTEGER",5)
        """
        return "Token ({type},{value})".format(type=self.type,value=repr(self.value))

    def __repr__(self):
        return self.__str__()



class Interpreter(object):
    def __init__(self,text):
        super().__init__()
        self.code = text
        self.cursor_pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing code')

    def get_next_token(self):
        """
        Lexical analyzer (also known as scanner or tokenizer)\n
        This method is responsible for breaking a sentence\n
        apart into tokens. One token at a time.
        """

        code = self.code

        # checking for end of file
        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.cursor_pos > len(code)-1:
            return Token(EOF,None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = code[self.cursor_pos]

        if current_char.isdigit():
            token = Token(INTEGER,int(current_char))
            self.cursor_pos+=1
            return token

        if current_char=="+":
            token = Token(PLUS,current_char)
            self.cursor_pos+=1
            return token

        # if we get here then something is wrong with the parsed token
        self.error()


    def eat(self,token_type):
        """
        compare the current token type with the passed token\n
        type and if they match then "eat" the current token\n
        and assign the next token to the self.current_token,\n
        otherwise raise an exception.
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
            return
        self.error

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""

        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()
        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)
        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(PLUS)
        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token
        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = left.value + right.value
        return result

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()