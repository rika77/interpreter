(* 字句解析器生成器への入力:字句定義ファイル.mll *)

(* 正規表現(right)に名前(left)付け *)
let digit = ['0'-'9']
let space = ' ' | '\t' | '\r' | '\n'
let alpha = ['a'-'z' 'A'-'Z' '_' ] 
let ident = alpha (alpha | digit)*
(* <- 正規表現(right)に自分で定義した変数(left)を使える *) 

(* 字句解析規則の定義 *)
(* main : エントリポイント名 *)
(* 正規表現n {トークンn} *)

rule main = parse
| space+       { main lexbuf }	(* 飛ばして次へ *)
| "+"          { Parser.PLUS }
| "="          { Parser.EQ }
| "<"          { Parser.LT }
| "if"         { Parser.IF }
| "then"       { Parser.THEN }
| "else"       { Parser.ELSE }
| "true"       { Parser.BOOL (true) }
| "false"      { Parser.BOOL (false) }
| "("          { Parser.LPAR }
| ")"          { Parser.RPAR }
| ";;"         { Parser.SEMISEMI }
| digit+ as n  { Parser.INT (int_of_string n) }
| ident  as id { Parser.ID id }
| _            { failwith ("Unknown Token: " ^ Lexing.lexeme lexbuf)}
