# Checkers game report

## Introduction

The goal of this course work was to create a project for the creation and documentation of a system, based on the analysis of functional requirements and the principles of object-oriented programming using the Python programming language. Goal for me was to create checkers game using Python language.

To run my program, you have to be installed python first. Then you have to navigate to the directory containing checkers game script. And then just open it using terminal or command prompt.

Program is very easy to use. You just have to run it, and then use your mouse(left click) to move checker pieces that you see on the board.

## Analysis
### Usage of 4 OOP Pillars and design patterns
1. **Encapsulation**
Encapsulation ensures that the internal state of an object is hidden from the outside world and accessed only through well-defined interfaces. In your code, encapsulation is achieved through class definitions, where attributes and methods are encapsulated within each class.

In my code encapsulation is exemplified by the Piece and CheckerPiece classes, where attributes such as color, row, and col are encapsulated within each class. Access to these attributes is controlled through class methods, ensuring proper encapsulation.

    class Piece:
    
      def __init__(self, color):
        self.color = color  # Encapsulation of color attribute within the Piece class
      def can_move(self):
        pass  # Encapsulation of can_move method
        
    class CheckerPiece(Piece):
    
      def __init__(self, color, row, col):
        super().__init__(color)
        self.row = row
        self.col = col  
2. **Inheritance**
   Inheritance is a mechanism by which one class (subclass) inherits attributes and methods from another class (superclass). It allows for code reuse and establishes a hierarchical relationship between classes, where subclasses can extend or override the behavior of their superclass.
   
  In my code inheritance is being used in the CheckerPiece class, which inherits from the Piece class. By inheriting from Piece, CheckerPiece inherits the color attribute and can leverage the can_move method defined in Piece. This promotes code reuse and maintains a logical relationship between different types of game pieces. 


       class CheckerPiece(Piece):
   
         def __init__(self, color, row, col):
   
       super().__init__(color)
         self.row = row
         self.col = col
3. **Polymorphism**
   Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables methods to do different things based on the object that they are acting upon, thereby facilitating flexibility and extensibility in code.
   
I use polymorphism in, the can_move method in the Piece and CheckerPiece classes. While both classes have a can_move method, the specific behavior of each method differs based on the type of piece (Piece or CheckerPiece). This allows for different types of game pieces to have their own movement rules while adhering to a common interface.

        class Piece:
   
        def can_move(self):
          pass

        class CheckerPiece(Piece):
   
        def can_move(self):
          return True 
4. **Abstraction**
   Abstraction is the concept of hiding complex implementation details and showing only the essential features of an object. It allows users to interact with objects without needing to understand their internal workings, thus simplifying the usage and maintenance of code.
   
   In my game code abstraction is being used by the CheckerBoard class, where the internal representation of the game board is hidden from the outside world. Users interact with the CheckerBoard object through methods such as draw, move_piece, and setup_board, without needing to know how these methods are implemented internally. This promotes code maintainability and ease of use.
   
         class CheckerBoard:
   
         def __init__(self):
           self.board = [[' ' for _ in range(8)] for _ in range(8)]  
           self.player = 'W'  
           self.setup_board()
   **Design Patterns**
   
   I used two design patterns while doing my game. They are Factory Method Pattern and Observer Pattern.

   **Observer Pattern**
   
   The Observer Pattern establishes a one-to-many dependency between objects, where one object (subject) maintains a list of its dependents (observers) and notifies them of any state changes.
   
   In my game the Observer Pattern is used to notify observers (such as the scoreboard) of game events (such as score updates). This pattern is suitable because it decouples the subject (game) from its observers (scoreboard), allowing for easy addition or removal of observers without modifying the subject.

       class GameObserver:

          def __init__(self):
          self.observers = []

          def add_observer(self, observer):
        self.observers.append(observer)

        def notify_observers(self, event):
        for observer in self.observers:
            observer.update(event)

        class ScoreBoard(GameObserver):

        def __init__(self):
        super().__init__()
        self.score = 0

        def update(self, event):
        pass
**Factory Method Pattern**

The Factory Method Pattern encapsulates the creation of objects, allowing subclasses to provide different implementations of objects without exposing the instantiation logic directly to the client code.

In my work, the PieceFactory class serves as a factory for creating different types of game pieces. This pattern is suitable because it allows for the creation of various types of pieces like checker pieces without tightly coupling the client code to specific piece implementations. How it works: The PieceFactory class contains a method create_piece that takes a piece type and color as parameters. Based on the specified piece type, it instantiates and returns the corresponding piece object.

    class PieceFactory:
    
    def create_piece(self, piece_type, color):
        if piece_type == "checker":
            return CheckerPiece(color)
## Results 

1. Implementing two design patterns, the Factory Method Pattern and the Observer Pattern, added significant flexibility and modularity to the codebase. But also it added quite big challenge for me because it was a bit hard for me personally implementing them into my code. 

2. Also speaking about challenges implementation of the real game into my project was a bit complicated for me too, in this stage was tons of wrong code lines.

3. Despite facing difficulties, using design patterns made the code easier to understand and work with. It helped me organize everything neatly, making it simpler to add new features or make changes as needed while we continued developing the project.

## Summary 

The coursework successfully implemented a game of checkers, overcoming challenges such as incorporating two design patterns and implementing the intricate rules of the real game. The resulting program provides a functional and organized implementation of checkers, offering players an engaging gaming experience. It was a great experience for me to test my abilities, and also to find something new like github and other platforms that I had to find during creation of the game. Speaking about my program's future prospects it includes potential enhancements such as implementing additional game features, improving the user interface, and optimizing game mechanics for better performance.




   

