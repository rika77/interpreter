(* 字句解析器生成器への入力:字句定義ファイル.mll *)
{
open Parser
}

(* 正規表現(right)に名前(left)付け *)
let digit = ['0'-'9']
let space = ' ' | '\t' | '\r' | '\n'
let alpha = ['a'-'z' 'A'-'Z' '_' ] 
let ident = alpha (alpha | digit)*
(* <- 正規表現(right)に自分で定義した変数(left)を使える *) 

(* 字句解析規則の定義 *)
(* main : エントリポイント名 *)
(* 正規表現n {トークンn} *)

rule token = parse
| space+       { token lexbuf }	(* 飛ばして次へ *)
| "+"          { PLUS }
| "="          { EQ }
| "<"          { LT }
| "if"         { IF }
| "then"       { THEN }
| "else"       { ELSE }
| "true"       { BOOL (true) }
| "false"      { BOOL (false) }
| "("          { LPAR }
| ")"          { RPAR }
| ";;"         { SEMISEMI }
| digit+ { INT (int_of_string (Lexing.lexeme lexbuf)) }
| ident  as id { ID id }
| _            { failwith ("Unknown Token: " ^ Lexing.lexeme lexbuf)}
