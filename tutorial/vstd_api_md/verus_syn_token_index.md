<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)

</div>

# Module token Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/token.rs.html#1-1219"
class="src">Source</a> </span>

</div>

Expand description

<div class="docblock">

Tokens representing Rust punctuation, keywords, and delimiters.

The type names in this module can be difficult to keep straight, so we
prefer to use the
[`Token!`](../macro.Token.html "macro verus_syn::Token") macro instead.
This is a type-macro that expands to the token type of the given token.

## <a href="#example" class="doc-anchor">§</a>Example

The
[`ItemStatic`](../struct.ItemStatic.html "struct verus_syn::ItemStatic")
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
[`ParseStream::parse`](../parse/struct.ParseBuffer.html#method.parse "method verus_syn::parse::ParseBuffer::parse")
method. Delimiter tokens are parsed using the
[`parenthesized!`](../macro.parenthesized.html "macro verus_syn::parenthesized"),
[`bracketed!`](../macro.bracketed.html "macro verus_syn::bracketed") and
[`braced!`](../macro.braced.html "macro verus_syn::braced") macros.

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

- [Peeking](../parse/struct.ParseBuffer.html#method.peek "method verus_syn::parse::ParseBuffer::peek")
  — `input.peek(Token![...])`

- [Parsing](../parse/struct.ParseBuffer.html#method.parse "method verus_syn::parse::ParseBuffer::parse")
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
title="struct verus_syn::token::Abstract">Abstract</a>  
`abstract`

<a href="struct.And.html" class="struct"
title="struct verus_syn::token::And">And</a>  
`&`

<a href="struct.AndAnd.html" class="struct"
title="struct verus_syn::token::AndAnd">AndAnd</a>  
`&&`

<a href="struct.AndEq.html" class="struct"
title="struct verus_syn::token::AndEq">AndEq</a>  
`&=`

<a href="struct.As.html" class="struct"
title="struct verus_syn::token::As">As</a>  
`as`

<a href="struct.Assert.html" class="struct"
title="struct verus_syn::token::Assert">Assert</a>  
`assert`

<a href="struct.Assume.html" class="struct"
title="struct verus_syn::token::Assume">Assume</a>  
`assume`

<a href="struct.AssumeSpecification.html" class="struct"
title="struct verus_syn::token::AssumeSpecification">AssumeSpecification</a>  
`assume_specification`

<a href="struct.Async.html" class="struct"
title="struct verus_syn::token::Async">Async</a>  
`async`

<a href="struct.At.html" class="struct"
title="struct verus_syn::token::At">At</a>  
`@`

<a href="struct.Auto.html" class="struct"
title="struct verus_syn::token::Auto">Auto</a>  
`auto`

<a href="struct.Await.html" class="struct"
title="struct verus_syn::token::Await">Await</a>  
`await`

<a href="struct.Axiom.html" class="struct"
title="struct verus_syn::token::Axiom">Axiom</a>  
`axiom`

<a href="struct.Become.html" class="struct"
title="struct verus_syn::token::Become">Become</a>  
`become`

<a href="struct.BigAnd.html" class="struct"
title="struct verus_syn::token::BigAnd">BigAnd</a>  
`&&&`

<a href="struct.BigOr.html" class="struct"
title="struct verus_syn::token::BigOr">BigOr</a>  
`|||`

<a href="struct.Box.html" class="struct"
title="struct verus_syn::token::Box">Box</a>  
`box`

<a href="struct.Brace.html" class="struct"
title="struct verus_syn::token::Brace">Brace</a>  
`{`…`}`

<a href="struct.Bracket.html" class="struct"
title="struct verus_syn::token::Bracket">Bracket</a>  
`[`…`]`

<a href="struct.Break.html" class="struct"
title="struct verus_syn::token::Break">Break</a>  
`break`

<a href="struct.Broadcast.html" class="struct"
title="struct verus_syn::token::Broadcast">Broadcast</a>  
`broadcast`

<a href="struct.BroadcastGroup.html" class="struct"
title="struct verus_syn::token::BroadcastGroup">BroadcastGroup</a>  
`group`

<a href="struct.By.html" class="struct"
title="struct verus_syn::token::By">By</a>  
`by`

<a href="struct.Caret.html" class="struct"
title="struct verus_syn::token::Caret">Caret</a>  
`^`

<a href="struct.CaretEq.html" class="struct"
title="struct verus_syn::token::CaretEq">CaretEq</a>  
`^=`

<a href="struct.Choose.html" class="struct"
title="struct verus_syn::token::Choose">Choose</a>  
`choose`

<a href="struct.Closed.html" class="struct"
title="struct verus_syn::token::Closed">Closed</a>  
`closed`

<a href="struct.Colon.html" class="struct"
title="struct verus_syn::token::Colon">Colon</a>  
`:`

<a href="struct.Comma.html" class="struct"
title="struct verus_syn::token::Comma">Comma</a>  
`,`

<a href="struct.Const.html" class="struct"
title="struct verus_syn::token::Const">Const</a>  
`const`

<a href="struct.Continue.html" class="struct"
title="struct verus_syn::token::Continue">Continue</a>  
`continue`

<a href="struct.Crate.html" class="struct"
title="struct verus_syn::token::Crate">Crate</a>  
`crate`

<a href="struct.Decreases.html" class="struct"
title="struct verus_syn::token::Decreases">Decreases</a>  
`decreases`

<a href="struct.Default.html" class="struct"
title="struct verus_syn::token::Default">Default</a>  
`default`

<a href="struct.DefaultEnsures.html" class="struct"
title="struct verus_syn::token::DefaultEnsures">DefaultEnsures</a>  
`default_ensures`

<a href="struct.Do.html" class="struct"
title="struct verus_syn::token::Do">Do</a>  
`do`

<a href="struct.Dollar.html" class="struct"
title="struct verus_syn::token::Dollar">Dollar</a>  
`$`

<a href="struct.Dot.html" class="struct"
title="struct verus_syn::token::Dot">Dot</a>  
`.`

<a href="struct.DotDot.html" class="struct"
title="struct verus_syn::token::DotDot">DotDot</a>  
`..`

<a href="struct.DotDotDot.html" class="struct"
title="struct verus_syn::token::DotDotDot">DotDotDot</a>  
`...`

<a href="struct.DotDotEq.html" class="struct"
title="struct verus_syn::token::DotDotEq">DotDotEq</a>  
`..=`

<a href="struct.Dyn.html" class="struct"
title="struct verus_syn::token::Dyn">Dyn</a>  
`dyn`

<a href="struct.Else.html" class="struct"
title="struct verus_syn::token::Else">Else</a>  
`else`

<a href="struct.Ensures.html" class="struct"
title="struct verus_syn::token::Ensures">Ensures</a>  
`ensures`

<a href="struct.Enum.html" class="struct"
title="struct verus_syn::token::Enum">Enum</a>  
`enum`

<a href="struct.Eq.html" class="struct"
title="struct verus_syn::token::Eq">Eq</a>  
`=`

<a href="struct.EqEq.html" class="struct"
title="struct verus_syn::token::EqEq">EqEq</a>  
`==`

<a href="struct.EqEqEq.html" class="struct"
title="struct verus_syn::token::EqEqEq">EqEqEq</a>  
`===`

<a href="struct.Equiv.html" class="struct"
title="struct verus_syn::token::Equiv">Equiv</a>  
`<==>`

<a href="struct.Exec.html" class="struct"
title="struct verus_syn::token::Exec">Exec</a>  
`exec`

<a href="struct.Exists.html" class="struct"
title="struct verus_syn::token::Exists">Exists</a>  
`exists`

<a href="struct.Exply.html" class="struct"
title="struct verus_syn::token::Exply">Exply</a>  
`<==`

<a href="struct.Extern.html" class="struct"
title="struct verus_syn::token::Extern">Extern</a>  
`extern`

<a href="struct.FatArrow.html" class="struct"
title="struct verus_syn::token::FatArrow">FatArrow</a>  
`=>`

<a href="struct.Final.html" class="struct"
title="struct verus_syn::token::Final">Final</a>  
`final`

<a href="struct.Fn.html" class="struct"
title="struct verus_syn::token::Fn">Fn</a>  
`fn`

<a href="struct.FnSpec.html" class="struct"
title="struct verus_syn::token::FnSpec">FnSpec</a>  
`FnSpec`

<a href="struct.For.html" class="struct"
title="struct verus_syn::token::For">For</a>  
`for`

<a href="struct.Forall.html" class="struct"
title="struct verus_syn::token::Forall">Forall</a>  
`forall`

<a href="struct.Ge.html" class="struct"
title="struct verus_syn::token::Ge">Ge</a>  
`>=`

<a href="struct.Ghost.html" class="struct"
title="struct verus_syn::token::Ghost">Ghost</a>  
`ghost`

<a href="struct.Global.html" class="struct"
title="struct verus_syn::token::Global">Global</a>  
`global`

<a href="struct.Group.html" class="struct"
title="struct verus_syn::token::Group">Group</a>  
None-delimited group

<a href="struct.Gt.html" class="struct"
title="struct verus_syn::token::Gt">Gt</a>  
`>`

<a href="struct.Has.html" class="struct"
title="struct verus_syn::token::Has">Has</a>  
`has`

<a href="struct.HasNot.html" class="struct"
title="struct verus_syn::token::HasNot">HasNot</a>  
`hasnt`

<a href="struct.Hide.html" class="struct"
title="struct verus_syn::token::Hide">Hide</a>  
`hide`

<a href="struct.If.html" class="struct"
title="struct verus_syn::token::If">If</a>  
`if`

<a href="struct.Impl.html" class="struct"
title="struct verus_syn::token::Impl">Impl</a>  
`impl`

<a href="struct.Implies.html" class="struct"
title="struct verus_syn::token::Implies">Implies</a>  
`implies`

<a href="struct.Imply.html" class="struct"
title="struct verus_syn::token::Imply">Imply</a>  
`==>`

<a href="struct.In.html" class="struct"
title="struct verus_syn::token::In">In</a>  
`in`

<a href="struct.InvAny.html" class="struct"
title="struct verus_syn::token::InvAny">InvAny</a>  
`any`

<a href="struct.InvNone.html" class="struct"
title="struct verus_syn::token::InvNone">InvNone</a>  
`none`

<a href="struct.Invariant.html" class="struct"
title="struct verus_syn::token::Invariant">Invariant</a>  
`invariant`

<a href="struct.InvariantEnsures.html" class="struct"
title="struct verus_syn::token::InvariantEnsures">InvariantEnsures</a>  
`invariant_ensures`

<a href="struct.InvariantExceptBreak.html" class="struct"
title="struct verus_syn::token::InvariantExceptBreak">InvariantExceptBreak</a>  
`invariant_except_break`

<a href="struct.Is.html" class="struct"
title="struct verus_syn::token::Is">Is</a>  
`is`

<a href="struct.IsNot.html" class="struct"
title="struct verus_syn::token::IsNot">IsNot</a>  
`isnt`

<a href="struct.LArrow.html" class="struct"
title="struct verus_syn::token::LArrow">LArrow</a>  
`<-`

<a href="struct.Layout.html" class="struct"
title="struct verus_syn::token::Layout">Layout</a>  
`layout`

<a href="struct.Le.html" class="struct"
title="struct verus_syn::token::Le">Le</a>  
`<=`

<a href="struct.Let.html" class="struct"
title="struct verus_syn::token::Let">Let</a>  
`let`

<a href="struct.Loop.html" class="struct"
title="struct verus_syn::token::Loop">Loop</a>  
`loop`

<a href="struct.Lt.html" class="struct"
title="struct verus_syn::token::Lt">Lt</a>  
`<`

<a href="struct.Macro.html" class="struct"
title="struct verus_syn::token::Macro">Macro</a>  
`macro`

<a href="struct.Match.html" class="struct"
title="struct verus_syn::token::Match">Match</a>  
`match`

<a href="struct.Matches.html" class="struct"
title="struct verus_syn::token::Matches">Matches</a>  
`matches`

<a href="struct.Minus.html" class="struct"
title="struct verus_syn::token::Minus">Minus</a>  
`-`

<a href="struct.MinusEq.html" class="struct"
title="struct verus_syn::token::MinusEq">MinusEq</a>  
`-=`

<a href="struct.Mod.html" class="struct"
title="struct verus_syn::token::Mod">Mod</a>  
`mod`

<a href="struct.Move.html" class="struct"
title="struct verus_syn::token::Move">Move</a>  
`move`

<a href="struct.Mut.html" class="struct"
title="struct verus_syn::token::Mut">Mut</a>  
`mut`

<a href="struct.Ne.html" class="struct"
title="struct verus_syn::token::Ne">Ne</a>  
`!=`

<a href="struct.NeEq.html" class="struct"
title="struct verus_syn::token::NeEq">NeEq</a>  
`!==`

<a href="struct.NoUnwind.html" class="struct"
title="struct verus_syn::token::NoUnwind">NoUnwind</a>  
`no_unwind`

<a href="struct.Not.html" class="struct"
title="struct verus_syn::token::Not">Not</a>  
`!`

<a href="struct.Open.html" class="struct"
title="struct verus_syn::token::Open">Open</a>  
`open`

<a href="struct.OpensInvariants.html" class="struct"
title="struct verus_syn::token::OpensInvariants">OpensInvariants</a>  
`opens_invariants`

<a href="struct.Or.html" class="struct"
title="struct verus_syn::token::Or">Or</a>  
`|`

<a href="struct.OrEq.html" class="struct"
title="struct verus_syn::token::OrEq">OrEq</a>  
`|=`

<a href="struct.OrOr.html" class="struct"
title="struct verus_syn::token::OrOr">OrOr</a>  
`||`

<a href="struct.Override.html" class="struct"
title="struct verus_syn::token::Override">Override</a>  
`override`

<a href="struct.Paren.html" class="struct"
title="struct verus_syn::token::Paren">Paren</a>  
`(`…`)`

<a href="struct.PathSep.html" class="struct"
title="struct verus_syn::token::PathSep">PathSep</a>  
`::`

<a href="struct.Percent.html" class="struct"
title="struct verus_syn::token::Percent">Percent</a>  
`%`

<a href="struct.PercentEq.html" class="struct"
title="struct verus_syn::token::PercentEq">PercentEq</a>  
`%=`

<a href="struct.Plus.html" class="struct"
title="struct verus_syn::token::Plus">Plus</a>  
`+`

<a href="struct.PlusEq.html" class="struct"
title="struct verus_syn::token::PlusEq">PlusEq</a>  
`+=`

<a href="struct.Pound.html" class="struct"
title="struct verus_syn::token::Pound">Pound</a>  
`#`

<a href="struct.Priv.html" class="struct"
title="struct verus_syn::token::Priv">Priv</a>  
`priv`

<a href="struct.Proof.html" class="struct"
title="struct verus_syn::token::Proof">Proof</a>  
`proof`

<a href="struct.ProofFn.html" class="struct"
title="struct verus_syn::token::ProofFn">ProofFn</a>  
`proof_fn`

<a href="struct.Pub.html" class="struct"
title="struct verus_syn::token::Pub">Pub</a>  
`pub`

<a href="struct.Question.html" class="struct"
title="struct verus_syn::token::Question">Question</a>  
`?`

<a href="struct.RArrow.html" class="struct"
title="struct verus_syn::token::RArrow">RArrow</a>  
`->`

<a href="struct.Raw.html" class="struct"
title="struct verus_syn::token::Raw">Raw</a>  
`raw`

<a href="struct.Recommends.html" class="struct"
title="struct verus_syn::token::Recommends">Recommends</a>  
`recommends`

<a href="struct.Ref.html" class="struct"
title="struct verus_syn::token::Ref">Ref</a>  
`ref`

<a href="struct.Requires.html" class="struct"
title="struct verus_syn::token::Requires">Requires</a>  
`requires`

<a href="struct.Return.html" class="struct"
title="struct verus_syn::token::Return">Return</a>  
`return`

<a href="struct.Returns.html" class="struct"
title="struct verus_syn::token::Returns">Returns</a>  
`returns`

<a href="struct.Reveal.html" class="struct"
title="struct verus_syn::token::Reveal">Reveal</a>  
`reveal`

<a href="struct.RevealWithFuel.html" class="struct"
title="struct verus_syn::token::RevealWithFuel">RevealWithFuel</a>  
`reveal_with_fuel`

<a href="struct.SelfType.html" class="struct"
title="struct verus_syn::token::SelfType">SelfType</a>  
`Self`

<a href="struct.SelfValue.html" class="struct"
title="struct verus_syn::token::SelfValue">SelfValue</a>  
`self`

<a href="struct.Semi.html" class="struct"
title="struct verus_syn::token::Semi">Semi</a>  
`;`

<a href="struct.Shl.html" class="struct"
title="struct verus_syn::token::Shl">Shl</a>  
`<<`

<a href="struct.ShlEq.html" class="struct"
title="struct verus_syn::token::ShlEq">ShlEq</a>  
`<<=`

<a href="struct.Shr.html" class="struct"
title="struct verus_syn::token::Shr">Shr</a>  
`>>`

<a href="struct.ShrEq.html" class="struct"
title="struct verus_syn::token::ShrEq">ShrEq</a>  
`>>=`

<a href="struct.SizeOf.html" class="struct"
title="struct verus_syn::token::SizeOf">SizeOf</a>  
`size_of`

<a href="struct.Slash.html" class="struct"
title="struct verus_syn::token::Slash">Slash</a>  
`/`

<a href="struct.SlashEq.html" class="struct"
title="struct verus_syn::token::SlashEq">SlashEq</a>  
`/=`

<a href="struct.Spec.html" class="struct"
title="struct verus_syn::token::Spec">Spec</a>  
`spec`

<a href="struct.SpecFn.html" class="struct"
title="struct verus_syn::token::SpecFn">SpecFn</a>  
`spec_fn`

<a href="struct.Star.html" class="struct"
title="struct verus_syn::token::Star">Star</a>  
`*`

<a href="struct.StarEq.html" class="struct"
title="struct verus_syn::token::StarEq">StarEq</a>  
`*=`

<a href="struct.Static.html" class="struct"
title="struct verus_syn::token::Static">Static</a>  
`static`

<a href="struct.Struct.html" class="struct"
title="struct verus_syn::token::Struct">Struct</a>  
`struct`

<a href="struct.Super.html" class="struct"
title="struct verus_syn::token::Super">Super</a>  
`super`

<a href="struct.Tilde.html" class="struct"
title="struct verus_syn::token::Tilde">Tilde</a>  
`~`

<a href="struct.TildeEq.html" class="struct"
title="struct verus_syn::token::TildeEq">TildeEq</a>  
`=~=`

<a href="struct.TildeNe.html" class="struct"
title="struct verus_syn::token::TildeNe">TildeNe</a>  
`!~=`

<a href="struct.TildeTildeEq.html" class="struct"
title="struct verus_syn::token::TildeTildeEq">TildeTildeEq</a>  
`=~~=`

<a href="struct.TildeTildeNe.html" class="struct"
title="struct verus_syn::token::TildeTildeNe">TildeTildeNe</a>  
`!~~=`

<a href="struct.Tracked.html" class="struct"
title="struct verus_syn::token::Tracked">Tracked</a>  
`tracked`

<a href="struct.Trait.html" class="struct"
title="struct verus_syn::token::Trait">Trait</a>  
`trait`

<a href="struct.Try.html" class="struct"
title="struct verus_syn::token::Try">Try</a>  
`try`

<a href="struct.Type.html" class="struct"
title="struct verus_syn::token::Type">Type</a>  
`type`

<a href="struct.Typeof.html" class="struct"
title="struct verus_syn::token::Typeof">Typeof</a>  
`typeof`

<a href="struct.Underscore.html" class="struct"
title="struct verus_syn::token::Underscore">Underscore</a>  
`_`

<a href="struct.Uninterp.html" class="struct"
title="struct verus_syn::token::Uninterp">Uninterp</a>  
`uninterp`

<a href="struct.Union.html" class="struct"
title="struct verus_syn::token::Union">Union</a>  
`union`

<a href="struct.Unsafe.html" class="struct"
title="struct verus_syn::token::Unsafe">Unsafe</a>  
`unsafe`

<a href="struct.Unsized.html" class="struct"
title="struct verus_syn::token::Unsized">Unsized</a>  
`unsized`

<a href="struct.Use.html" class="struct"
title="struct verus_syn::token::Use">Use</a>  
`use`

<a href="struct.Via.html" class="struct"
title="struct verus_syn::token::Via">Via</a>  
`via`

<a href="struct.Virtual.html" class="struct"
title="struct verus_syn::token::Virtual">Virtual</a>  
`virtual`

<a href="struct.When.html" class="struct"
title="struct verus_syn::token::When">When</a>  
`when`

<a href="struct.Where.html" class="struct"
title="struct verus_syn::token::Where">Where</a>  
`where`

<a href="struct.While.html" class="struct"
title="struct verus_syn::token::While">While</a>  
`while`

<a href="struct.With.html" class="struct"
title="struct verus_syn::token::With">With</a>  
`with`

<a href="struct.Yield.html" class="struct"
title="struct verus_syn::token::Yield">Yield</a>  
`yield`

## Traits<a href="#traits" class="anchor">§</a>

<a href="trait.Token.html" class="trait"
title="trait verus_syn::token::Token">Token</a>  
Marker trait for types that represent single tokens.

</div>

</div>
