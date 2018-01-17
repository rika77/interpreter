(* parser.mly : token *)
type token = INT of int | BOOL of bool

(* syntex.ml : type t *)
type t =
	| Int of int  
	| Add of t * t
	| Sub of t * t
	| Bool of bool
	| Eq of t * t
	| Le of t * t
	| If of t * t * t

