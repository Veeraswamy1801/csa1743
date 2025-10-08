 bird(penguin) :- cannot_fly. 
bird(eagle) :- can_fly. 
cannot_fly. 
can_fly :- has_wings. 
has_wings.  
infer(X) :- bird(X).