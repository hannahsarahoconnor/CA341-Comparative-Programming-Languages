%nil represents an empty tree (empty list)
binary_tree(nil).
binary_tree(node(_, Left, Right)):- binary_tree(Left), binary_tree(Right).

search(X,node(X,_,_).
search(X,node(Y,_,Right):- 
  X < Y, search(Y,Left).
search(X,node(Y,Left,_):- 
  X > Y, search(Y,Right).

% root,left subtree, right subtree
preorder(node(X,L,R),[X|XS]) :- preorder(L,LS), preorder(R,RS), append(LS,RS,XS).
%if only 1 node
preorder(node(X,nil,nil),[X]). 
preorder(nil,[]). 

%Left subtree,Root, then Right subtree

inorder(node(X,nil,nil),[X]).
%append the root to the right list 
inorder(node(X,L,R), XS) :- inorder(L,LS), inorder(R,RS), append(LS,[X|RS], XS).
inorder(nil,[]).

%Left subtree, Right subtree then Root

postorder(nil,[]).
%nil if the left and right subtree doesnt exist

postorder(node(X,nil,nil),[X]).
%append the root to the end of right subtree list, which gives RSS, then append the left subtree with it.
postorder(node(X,L,R),XS) :- postorder(L,LS), postorder(R,RS), append(RS,[X],RSS), append(LS,RSS,XS).                  
                
%If tree is empty, make it the root 
insert(nil, i, node(i, nil, nil)).
insert(node(X, L, R), i, node(X, LS, R)) :-
   i =< X, insert(L, i, LS).
insert(node(X, L, R), i, node(X, L, RS)) :- 
  i > X, insert(R, i, RS).
