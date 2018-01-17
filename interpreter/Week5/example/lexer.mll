(* ������ϴ�������ؤ�����:��������ե�����.mll *)
{
open Parser
}

(* ����ɽ��(right)��̾��(left)�դ� *)
let digit = ['0'-'9']
let space = ' ' | '\t' | '\r' | '\n'
let alpha = ['a'-'z' 'A'-'Z' '_' ] 
let ident = alpha (alpha | digit)*
(* <- ����ɽ��(right)�˼�ʬ����������ѿ�(left)��Ȥ��� *) 

(* ������ϵ�§����� *)
(* main : ����ȥ�ݥ����̾ *)
(* ����ɽ��n {�ȡ�����n} *)

rule token = parse
| space+       { token lexbuf }	(* ���Ф��Ƽ��� *)
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
