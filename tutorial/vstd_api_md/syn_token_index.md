<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[syn](../index.html)

</div>

# Module token Copy item path

<span class="sub-heading"><a href="../../src/syn/token.rs.html#1-1094" class="src">Source</a>
</span>

</div>

Expand description

<div class="docblock">

Tokens representing Rust punctuation, keywords, and delimiters.

The type names in this module can be difficult to keep straight, so we
prefer to use the [`Token!`](../macro.Token.html "macro syn::Token")
macro instead. This is a type-macro that expands to the token type of
the given token.

## <a href="#example" class="doc-anchor">§</a>Example

The [`ItemStatic`](../struct.ItemStatic.html "struct syn::ItemStatic")
syntax tree node is defined like this.

<div class="example-wrap">

``` rust
pub struct ItemStatic {
    pub attrs: Vec<Attribute>,
    pub vis: Visibility,
    pub static_token: Token![static],
    pub mutability: Option<Token![mut]>,
    pub ident: Ident,
    pub colon_token: Token![:],
    pub ty: Box<Type>,
    pub eq_token: Token![=],
    pub expr: Box<Expr>,
    pub semi_token: Token![;],
}
```

</div>

## <a href="#parsing" class="doc-anchor">§</a>Parsing

Keywords and punctuation can be parsed through the
[`ParseStream::parse`](../parse/struct.ParseBuffer.html#method.parse "method syn::parse::ParseBuffer::parse")
method. Delimiter tokens are parsed using the
[`parenthesized!`](../macro.parenthesized.html "macro syn::parenthesized"),
[`bracketed!`](../macro.bracketed.html "macro syn::bracketed") and
[`braced!`](../macro.braced.html "macro syn::braced") macros.

<div class="example-wrap">

``` rust
use syn::{Attribute, Result};
use syn::parse::{Parse, ParseStream};

// Parse the ItemStatic struct shown above.
impl Parse for ItemStatic {
    fn parse(input: ParseStream) -> Result<Self> {
        Ok(ItemStatic {
            attrs: input.call(Attribute::parse_outer)?,
            vis: input.parse()?,
            static_token: input.parse()?,
            mutability: input.parse()?,
            ident: input.parse()?,
            colon_token: input.parse()?,
            ty: input.parse()?,
            eq_token: input.parse()?,
            expr: input.parse()?,
            semi_token: input.parse()?,
        })
    }
}
```

</div>

## <a href="#other-operations" class="doc-anchor">§</a>Other operations

Every keyword and punctuation token supports the following operations.

- [Peeking](../parse/struct.ParseBuffer.html#method.peek "method syn::parse::ParseBuffer::peek")
  — `input.peek(Token![...])`

- [Parsing](../parse/struct.ParseBuffer.html#method.parse "method syn::parse::ParseBuffer::parse")
  — `input.parse::<Token![...]>()?`

- [Printing](https://docs.rs/quote/1.0/quote/trait.ToTokens.html) —
  `quote!( ... #the_token ... )`

- Construction from a
  [`Span`](https://docs.rs/proc-macro2/1.0/proc_macro2/struct.Span.html)
  — `let the_token = Token![...](sp)`

- Field access to its span — `let sp = the_token.span`

</div>

## Structs<a href="#structs" class="anchor">§</a>

<a href="struct.Abstract.html" class="struct"
title="struct syn::token::Abstract">Abstract</a>  
`abstract`

<a href="struct.And.html" class="struct"
title="struct syn::token::And">And</a>  
`&`

<a href="struct.AndAnd.html" class="struct"
title="struct syn::token::AndAnd">AndAnd</a>  
`&&`

<a href="struct.AndEq.html" class="struct"
title="struct syn::token::AndEq">AndEq</a>  
`&=`

<a href="struct.As.html" class="struct"
title="struct syn::token::As">As</a>  
`as`

<a href="struct.Async.html" class="struct"
title="struct syn::token::Async">Async</a>  
`async`

<a href="struct.At.html" class="struct"
title="struct syn::token::At">At</a>  
`@`

<a href="struct.Auto.html" class="struct"
title="struct syn::token::Auto">Auto</a>  
`auto`

<a href="struct.Await.html" class="struct"
title="struct syn::token::Await">Await</a>  
`await`

<a href="struct.Become.html" class="struct"
title="struct syn::token::Become">Become</a>  
`become`

<a href="struct.Box.html" class="struct"
title="struct syn::token::Box">Box</a>  
`box`

<a href="struct.Brace.html" class="struct"
title="struct syn::token::Brace">Brace</a>  
`{`…`}`

<a href="struct.Bracket.html" class="struct"
title="struct syn::token::Bracket">Bracket</a>  
`[`…`]`

<a href="struct.Break.html" class="struct"
title="struct syn::token::Break">Break</a>  
`break`

<a href="struct.Caret.html" class="struct"
title="struct syn::token::Caret">Caret</a>  
`^`

<a href="struct.CaretEq.html" class="struct"
title="struct syn::token::CaretEq">CaretEq</a>  
`^=`

<a href="struct.Colon.html" class="struct"
title="struct syn::token::Colon">Colon</a>  
`:`

<a href="struct.Comma.html" class="struct"
title="struct syn::token::Comma">Comma</a>  
`,`

<a href="struct.Const.html" class="struct"
title="struct syn::token::Const">Const</a>  
`const`

<a href="struct.Continue.html" class="struct"
title="struct syn::token::Continue">Continue</a>  
`continue`

<a href="struct.Crate.html" class="struct"
title="struct syn::token::Crate">Crate</a>  
`crate`

<a href="struct.Default.html" class="struct"
title="struct syn::token::Default">Default</a>  
`default`

<a href="struct.Do.html" class="struct"
title="struct syn::token::Do">Do</a>  
`do`

<a href="struct.Dollar.html" class="struct"
title="struct syn::token::Dollar">Dollar</a>  
`$`

<a href="struct.Dot.html" class="struct"
title="struct syn::token::Dot">Dot</a>  
`.`

<a href="struct.DotDot.html" class="struct"
title="struct syn::token::DotDot">DotDot</a>  
`..`

<a href="struct.DotDotDot.html" class="struct"
title="struct syn::token::DotDotDot">DotDotDot</a>  
`...`

<a href="struct.DotDotEq.html" class="struct"
title="struct syn::token::DotDotEq">DotDotEq</a>  
`..=`

<a href="struct.Dyn.html" class="struct"
title="struct syn::token::Dyn">Dyn</a>  
`dyn`

<a href="struct.Else.html" class="struct"
title="struct syn::token::Else">Else</a>  
`else`

<a href="struct.Enum.html" class="struct"
title="struct syn::token::Enum">Enum</a>  
`enum`

<a href="struct.Eq.html" class="struct"
title="struct syn::token::Eq">Eq</a>  
`=`

<a href="struct.EqEq.html" class="struct"
title="struct syn::token::EqEq">EqEq</a>  
`==`

<a href="struct.Extern.html" class="struct"
title="struct syn::token::Extern">Extern</a>  
`extern`

<a href="struct.FatArrow.html" class="struct"
title="struct syn::token::FatArrow">FatArrow</a>  
`=>`

<a href="struct.Final.html" class="struct"
title="struct syn::token::Final">Final</a>  
`final`

<a href="struct.Fn.html" class="struct"
title="struct syn::token::Fn">Fn</a>  
`fn`

<a href="struct.For.html" class="struct"
title="struct syn::token::For">For</a>  
`for`

<a href="struct.Ge.html" class="struct"
title="struct syn::token::Ge">Ge</a>  
`>=`

<a href="struct.Group.html" class="struct"
title="struct syn::token::Group">Group</a>  
None-delimited group

<a href="struct.Gt.html" class="struct"
title="struct syn::token::Gt">Gt</a>  
`>`

<a href="struct.If.html" class="struct"
title="struct syn::token::If">If</a>  
`if`

<a href="struct.Impl.html" class="struct"
title="struct syn::token::Impl">Impl</a>  
`impl`

<a href="struct.In.html" class="struct"
title="struct syn::token::In">In</a>  
`in`

<a href="struct.LArrow.html" class="struct"
title="struct syn::token::LArrow">LArrow</a>  
`<-`

<a href="struct.Le.html" class="struct"
title="struct syn::token::Le">Le</a>  
`<=`

<a href="struct.Let.html" class="struct"
title="struct syn::token::Let">Let</a>  
`let`

<a href="struct.Loop.html" class="struct"
title="struct syn::token::Loop">Loop</a>  
`loop`

<a href="struct.Lt.html" class="struct"
title="struct syn::token::Lt">Lt</a>  
`<`

<a href="struct.Macro.html" class="struct"
title="struct syn::token::Macro">Macro</a>  
`macro`

<a href="struct.Match.html" class="struct"
title="struct syn::token::Match">Match</a>  
`match`

<a href="struct.Minus.html" class="struct"
title="struct syn::token::Minus">Minus</a>  
`-`

<a href="struct.MinusEq.html" class="struct"
title="struct syn::token::MinusEq">MinusEq</a>  
`-=`

<a href="struct.Mod.html" class="struct"
title="struct syn::token::Mod">Mod</a>  
`mod`

<a href="struct.Move.html" class="struct"
title="struct syn::token::Move">Move</a>  
`move`

<a href="struct.Mut.html" class="struct"
title="struct syn::token::Mut">Mut</a>  
`mut`

<a href="struct.Ne.html" class="struct"
title="struct syn::token::Ne">Ne</a>  
`!=`

<a href="struct.Not.html" class="struct"
title="struct syn::token::Not">Not</a>  
`!`

<a href="struct.Or.html" class="struct"
title="struct syn::token::Or">Or</a>  
`|`

<a href="struct.OrEq.html" class="struct"
title="struct syn::token::OrEq">OrEq</a>  
`|=`

<a href="struct.OrOr.html" class="struct"
title="struct syn::token::OrOr">OrOr</a>  
`||`

<a href="struct.Override.html" class="struct"
title="struct syn::token::Override">Override</a>  
`override`

<a href="struct.Paren.html" class="struct"
title="struct syn::token::Paren">Paren</a>  
`(`…`)`

<a href="struct.PathSep.html" class="struct"
title="struct syn::token::PathSep">PathSep</a>  
`::`

<a href="struct.Percent.html" class="struct"
title="struct syn::token::Percent">Percent</a>  
`%`

<a href="struct.PercentEq.html" class="struct"
title="struct syn::token::PercentEq">PercentEq</a>  
`%=`

<a href="struct.Plus.html" class="struct"
title="struct syn::token::Plus">Plus</a>  
`+`

<a href="struct.PlusEq.html" class="struct"
title="struct syn::token::PlusEq">PlusEq</a>  
`+=`

<a href="struct.Pound.html" class="struct"
title="struct syn::token::Pound">Pound</a>  
`#`

<a href="struct.Priv.html" class="struct"
title="struct syn::token::Priv">Priv</a>  
`priv`

<a href="struct.Pub.html" class="struct"
title="struct syn::token::Pub">Pub</a>  
`pub`

<a href="struct.Question.html" class="struct"
title="struct syn::token::Question">Question</a>  
`?`

<a href="struct.RArrow.html" class="struct"
title="struct syn::token::RArrow">RArrow</a>  
`->`

<a href="struct.Raw.html" class="struct"
title="struct syn::token::Raw">Raw</a>  
`raw`

<a href="struct.Ref.html" class="struct"
title="struct syn::token::Ref">Ref</a>  
`ref`

<a href="struct.Return.html" class="struct"
title="struct syn::token::Return">Return</a>  
`return`

<a href="struct.SelfType.html" class="struct"
title="struct syn::token::SelfType">SelfType</a>  
`Self`

<a href="struct.SelfValue.html" class="struct"
title="struct syn::token::SelfValue">SelfValue</a>  
`self`

<a href="struct.Semi.html" class="struct"
title="struct syn::token::Semi">Semi</a>  
`;`

<a href="struct.Shl.html" class="struct"
title="struct syn::token::Shl">Shl</a>  
`<<`

<a href="struct.ShlEq.html" class="struct"
title="struct syn::token::ShlEq">ShlEq</a>  
`<<=`

<a href="struct.Shr.html" class="struct"
title="struct syn::token::Shr">Shr</a>  
`>>`

<a href="struct.ShrEq.html" class="struct"
title="struct syn::token::ShrEq">ShrEq</a>  
`>>=`

<a href="struct.Slash.html" class="struct"
title="struct syn::token::Slash">Slash</a>  
`/`

<a href="struct.SlashEq.html" class="struct"
title="struct syn::token::SlashEq">SlashEq</a>  
`/=`

<a href="struct.Star.html" class="struct"
title="struct syn::token::Star">Star</a>  
`*`

<a href="struct.StarEq.html" class="struct"
title="struct syn::token::StarEq">StarEq</a>  
`*=`

<a href="struct.Static.html" class="struct"
title="struct syn::token::Static">Static</a>  
`static`

<a href="struct.Struct.html" class="struct"
title="struct syn::token::Struct">Struct</a>  
`struct`

<a href="struct.Super.html" class="struct"
title="struct syn::token::Super">Super</a>  
`super`

<a href="struct.Tilde.html" class="struct"
title="struct syn::token::Tilde">Tilde</a>  
`~`

<a href="struct.Trait.html" class="struct"
title="struct syn::token::Trait">Trait</a>  
`trait`

<a href="struct.Try.html" class="struct"
title="struct syn::token::Try">Try</a>  
`try`

<a href="struct.Type.html" class="struct"
title="struct syn::token::Type">Type</a>  
`type`

<a href="struct.Typeof.html" class="struct"
title="struct syn::token::Typeof">Typeof</a>  
`typeof`

<a href="struct.Underscore.html" class="struct"
title="struct syn::token::Underscore">Underscore</a>  
`_`

<a href="struct.Union.html" class="struct"
title="struct syn::token::Union">Union</a>  
`union`

<a href="struct.Unsafe.html" class="struct"
title="struct syn::token::Unsafe">Unsafe</a>  
`unsafe`

<a href="struct.Unsized.html" class="struct"
title="struct syn::token::Unsized">Unsized</a>  
`unsized`

<a href="struct.Use.html" class="struct"
title="struct syn::token::Use">Use</a>  
`use`

<a href="struct.Virtual.html" class="struct"
title="struct syn::token::Virtual">Virtual</a>  
`virtual`

<a href="struct.Where.html" class="struct"
title="struct syn::token::Where">Where</a>  
`where`

<a href="struct.While.html" class="struct"
title="struct syn::token::While">While</a>  
`while`

<a href="struct.Yield.html" class="struct"
title="struct syn::token::Yield">Yield</a>  
`yield`

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Token.html" class="trait"
title="trait syn::token::Token">Token</a>  
Marker trait for types that represent single tokens.

</div>

</div>
