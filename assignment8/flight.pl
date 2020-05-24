%flight(from, airline, to, price, duration). 

flight(toronto, aircanada, london, 500, 360).
flight(london, united, toronto, 650, 420).
flight(paris, united, toulhouse, 35, 120).
flight(london, iberia, barcelona, 220, 240).
flight(barcelona, aircanada, madrid, 100, 60).
flight(barcelona, iberia, valencia, 110, 75).
flight(valencia, iberia, malaga, 80, 120).
flight(malaga, iberia, madrid, 50, 45).
flight(madrid, aircanada, toronto, 900, 480).
flight(madrid, united, toronto, 950, 540).
flight(madrid, iberia, toronto, 800, 480).

%airport(city, airporttax, minsecuritydelay).  

airport(toronto, 50, 60).
airport(london, 75, 80).
airport(paris, 50, 60).
airport(toulhouse, 40, 30).
airport(barcelona, 40, 30).
airport(madrid, 75, 45).
airport(valencia, 40, 20).
airport(malaga, 50, 30).



flight_exist(X, Y) :- flight(X,_,Y,_,_) ; flight(Y,_,X,_,_) , 
					  write(' There is a flight from '), write(X) , write(' to '), write(Y).

two_flights(X, Z) :- flight(X,_,Y,_,_), flight(Y,_,Z,_,_),
					 write(' It is possible to go from '), write(X), write(' to '), write(Y), write(' in two flights ').

cheap_flight(A, C, B) :- flight(A, C, B, P, _) , (P < 400),
						 write(' The flight from '), write(A), write(' to '), write(B), write(' with '), write(C),
						 write(' is cheap ').

flight_preferred(A, C, B) :- cheap_flight(A, C, B) ; (C == aircanada),
							 write(' The flight from '), write(A), write(' to '), write(B), write(' with '), write(C),
							 write(' is preferred ').

flight_relation(A, aircanada, B) :- flight(A, united, B, _, _) ; flight(B, united, A, _, _),
									write(' There is a flight from '), write(A), write(' to '), write(B), write(' with '),
									write(' air canada').
