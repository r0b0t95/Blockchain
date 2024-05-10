from colorama import Fore


class Color:
     def __init__( self ):
          self.__green = Fore.GREEN
          self.__red = Fore.RED
          self.__magenta = Fore.MAGENTA
          self.__yellow = Fore.YELLOW
          self.__cyan = Fore.CYAN
          self.__white = Fore.WHITE
          self.__reset = Fore.RESET
          
     def green( self ):
          return self.__green
     
     def red( self ):
          return self.__red
     
     def magenta( self ):
          return self.__magenta
     
     def yellow( self ):
          return self.__yellow
     
     def cyan( self ):
          return self.__cyan
     
     def white( self ):
          return self.__white
     
     def reset( self ):
          return self.__reset