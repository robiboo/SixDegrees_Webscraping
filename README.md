# SixDegrees_Webscraping

  The program's goal is to find a path using webscraping.
  Starting from a random wiki page until it finds the wiki page of Star Wars with no more than six hops
  
    https://en.wikipedia.org/wiki/Star_Wars
    
  The program will use Breadth First Search for finding the shortest path.
  
  If the program is able to find the wiki page of Star Wars, it will print the paths.
  
    Example Output:
    
        Baseball (https://en.wikipedia.org/wiki/Baseball)
          Trading card (https://en.wikipedia.org/wiki/Trading_card)
            Star Wars (https://en.wikipedia.org/wiki/Star_Wars)
           
  If the program fails to find a path, it will prompt the user that No path found
