<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](index.html)

</div>

# Enum <span class="enum">BinOp</span> Copy item path

<span class="sub-heading"><a href="../src/verus_syn/op.rs.html#1-74" class="src">Source</a>
</span>

</div>

``` rust
#[non_exhaustive]pub enum BinOp {
Show 37 variants    Add(Plus),
    Sub(Minus),
    Mul(Star),
    Div(Slash),
    Rem(Percent),
    And(AndAnd),
    Or(OrOr),
    BitXor(Caret),
    BitAnd(And),
    BitOr(Or),
    Shl(Shl),
    Shr(Shr),
    Eq(EqEq),
    Lt(Lt),
    Le(Le),
    Ne(Ne),
    Ge(Ge),
    Gt(Gt),
    AddAssign(PlusEq),
    SubAssign(MinusEq),
    MulAssign(StarEq),
    DivAssign(SlashEq),
    RemAssign(PercentEq),
    BitXorAssign(CaretEq),
    BitAndAssign(AndEq),
    BitOrAssign(OrEq),
    ShlAssign(ShlEq),
    ShrAssign(ShrEq),
    Equiv(Equiv),
    Imply(Imply),
    Exply(Exply),
    BigEq(EqEqEq),
    BigNe(NeEq),
    ExtEq(TildeEq),
    ExtNe(TildeNe),
    ExtDeepEq(TildeTildeEq),
    ExtDeepNe(TildeTildeNe),
}
```

Expand description

<div class="docblock">

A binary operator: `+`, `+=`, `&`.

</div>

## Variants (Non-exhaustive)<a href="#variants" class="anchor">§</a>

This enum is marked as non-exhaustive

<div class="docblock">

Non-exhaustive enums could have additional variants added in future.
Therefore, when matching against variants of non-exhaustive enums, an
extra wildcard arm must be added to account for any future variants.

</div>

<div class="variants">

<div id="variant.Add" class="section variant">

<a href="#variant.Add" class="anchor">§</a>

### Add(<a href="token/struct.Plus.html" class="struct"
title="struct verus_syn::token::Plus">Plus</a>)

</div>

<div class="docblock">

The `+` operator (addition)

</div>

<div id="variant.Sub" class="section variant">

<a href="#variant.Sub" class="anchor">§</a>

### Sub(<a href="token/struct.Minus.html" class="struct"
title="struct verus_syn::token::Minus">Minus</a>)

</div>

<div class="docblock">

The `-` operator (subtraction)

</div>

<div id="variant.Mul" class="section variant">

<a href="#variant.Mul" class="anchor">§</a>

### Mul(<a href="token/struct.Star.html" class="struct"
title="struct verus_syn::token::Star">Star</a>)

</div>

<div class="docblock">

The `*` operator (multiplication)

</div>

<div id="variant.Div" class="section variant">

<a href="#variant.Div" class="anchor">§</a>

### Div(<a href="token/struct.Slash.html" class="struct"
title="struct verus_syn::token::Slash">Slash</a>)

</div>

<div class="docblock">

The `/` operator (division)

</div>

<div id="variant.Rem" class="section variant">

<a href="#variant.Rem" class="anchor">§</a>

### Rem(<a href="token/struct.Percent.html" class="struct"
title="struct verus_syn::token::Percent">Percent</a>)

</div>

<div class="docblock">

The `%` operator (modulus)

</div>

<div id="variant.And" class="section variant">

<a href="#variant.And" class="anchor">§</a>

### And(<a href="token/struct.AndAnd.html" class="struct"
title="struct verus_syn::token::AndAnd">AndAnd</a>)

</div>

<div class="docblock">

The `&&` operator (logical and)

</div>

<div id="variant.Or" class="section variant">

<a href="#variant.Or" class="anchor">§</a>

### Or(<a href="token/struct.OrOr.html" class="struct"
title="struct verus_syn::token::OrOr">OrOr</a>)

</div>

<div class="docblock">

The `||` operator (logical or)

</div>

<div id="variant.BitXor" class="section variant">

<a href="#variant.BitXor" class="anchor">§</a>

### BitXor(<a href="token/struct.Caret.html" class="struct"
title="struct verus_syn::token::Caret">Caret</a>)

</div>

<div class="docblock">

The `^` operator (bitwise xor)

</div>

<div id="variant.BitAnd" class="section variant">

<a href="#variant.BitAnd" class="anchor">§</a>

### BitAnd(<a href="token/struct.And.html" class="struct"
title="struct verus_syn::token::And">And</a>)

</div>

<div class="docblock">

The `&` operator (bitwise and)

</div>

<div id="variant.BitOr" class="section variant">

<a href="#variant.BitOr" class="anchor">§</a>

### BitOr(<a href="token/struct.Or.html" class="struct"
title="struct verus_syn::token::Or">Or</a>)

</div>

<div class="docblock">

The `|` operator (bitwise or)

</div>

<div id="variant.Shl" class="section variant">

<a href="#variant.Shl" class="anchor">§</a>

### Shl(<a href="token/struct.Shl.html" class="struct"
title="struct verus_syn::token::Shl">Shl</a>)

</div>

<div class="docblock">

The `<<` operator (shift left)

</div>

<div id="variant.Shr" class="section variant">

<a href="#variant.Shr" class="anchor">§</a>

### Shr(<a href="token/struct.Shr.html" class="struct"
title="struct verus_syn::token::Shr">Shr</a>)

</div>

<div class="docblock">

The `>>` operator (shift right)

</div>

<div id="variant.Eq" class="section variant">

<a href="#variant.Eq" class="anchor">§</a>

### Eq(<a href="token/struct.EqEq.html" class="struct"
title="struct verus_syn::token::EqEq">EqEq</a>)

</div>

<div class="docblock">

The `==` operator (equality)

</div>

<div id="variant.Lt" class="section variant">

<a href="#variant.Lt" class="anchor">§</a>

### Lt(<a href="token/struct.Lt.html" class="struct"
title="struct verus_syn::token::Lt">Lt</a>)

</div>

<div class="docblock">

The `<` operator (less than)

</div>

<div id="variant.Le" class="section variant">

<a href="#variant.Le" class="anchor">§</a>

### Le(<a href="token/struct.Le.html" class="struct"
title="struct verus_syn::token::Le">Le</a>)

</div>

<div class="docblock">

The `<=` operator (less than or equal to)

</div>

<div id="variant.Ne" class="section variant">

<a href="#variant.Ne" class="anchor">§</a>

### Ne(<a href="token/struct.Ne.html" class="struct"
title="struct verus_syn::token::Ne">Ne</a>)

</div>

<div class="docblock">

The `!=` operator (not equal to)

</div>

<div id="variant.Ge" class="section variant">

<a href="#variant.Ge" class="anchor">§</a>

### Ge(<a href="token/struct.Ge.html" class="struct"
title="struct verus_syn::token::Ge">Ge</a>)

</div>

<div class="docblock">

The `>=` operator (greater than or equal to)

</div>

<div id="variant.Gt" class="section variant">

<a href="#variant.Gt" class="anchor">§</a>

### Gt(<a href="token/struct.Gt.html" class="struct"
title="struct verus_syn::token::Gt">Gt</a>)

</div>

<div class="docblock">

The `>` operator (greater than)

</div>

<div id="variant.AddAssign" class="section variant">

<a href="#variant.AddAssign" class="anchor">§</a>

### AddAssign(<a href="token/struct.PlusEq.html" class="struct"
title="struct verus_syn::token::PlusEq">PlusEq</a>)

</div>

<div class="docblock">

The `+=` operator

</div>

<div id="variant.SubAssign" class="section variant">

<a href="#variant.SubAssign" class="anchor">§</a>

### SubAssign(<a href="token/struct.MinusEq.html" class="struct"
title="struct verus_syn::token::MinusEq">MinusEq</a>)

</div>

<div class="docblock">

The `-=` operator

</div>

<div id="variant.MulAssign" class="section variant">

<a href="#variant.MulAssign" class="anchor">§</a>

### MulAssign(<a href="token/struct.StarEq.html" class="struct"
title="struct verus_syn::token::StarEq">StarEq</a>)

</div>

<div class="docblock">

The `*=` operator

</div>

<div id="variant.DivAssign" class="section variant">

<a href="#variant.DivAssign" class="anchor">§</a>

### DivAssign(<a href="token/struct.SlashEq.html" class="struct"
title="struct verus_syn::token::SlashEq">SlashEq</a>)

</div>

<div class="docblock">

The `/=` operator

</div>

<div id="variant.RemAssign" class="section variant">

<a href="#variant.RemAssign" class="anchor">§</a>

### RemAssign(<a href="token/struct.PercentEq.html" class="struct"
title="struct verus_syn::token::PercentEq">PercentEq</a>)

</div>

<div class="docblock">

The `%=` operator

</div>

<div id="variant.BitXorAssign" class="section variant">

<a href="#variant.BitXorAssign" class="anchor">§</a>

### BitXorAssign(<a href="token/struct.CaretEq.html" class="struct"
title="struct verus_syn::token::CaretEq">CaretEq</a>)

</div>

<div class="docblock">

The `^=` operator

</div>

<div id="variant.BitAndAssign" class="section variant">

<a href="#variant.BitAndAssign" class="anchor">§</a>

### BitAndAssign(<a href="token/struct.AndEq.html" class="struct"
title="struct verus_syn::token::AndEq">AndEq</a>)

</div>

<div class="docblock">

The `&=` operator

</div>

<div id="variant.BitOrAssign" class="section variant">

<a href="#variant.BitOrAssign" class="anchor">§</a>

### BitOrAssign(<a href="token/struct.OrEq.html" class="struct"
title="struct verus_syn::token::OrEq">OrEq</a>)

</div>

<div class="docblock">

The `|=` operator

</div>

<div id="variant.ShlAssign" class="section variant">

<a href="#variant.ShlAssign" class="anchor">§</a>

### ShlAssign(<a href="token/struct.ShlEq.html" class="struct"
title="struct verus_syn::token::ShlEq">ShlEq</a>)

</div>

<div class="docblock">

The `<<=` operator

</div>

<div id="variant.ShrAssign" class="section variant">

<a href="#variant.ShrAssign" class="anchor">§</a>

### ShrAssign(<a href="token/struct.ShrEq.html" class="struct"
title="struct verus_syn::token::ShrEq">ShrEq</a>)

</div>

<div class="docblock">

The `>>=` operator

</div>

<div id="variant.Equiv" class="section variant">

<a href="#variant.Equiv" class="anchor">§</a>

### Equiv(<a href="token/struct.Equiv.html" class="struct"
title="struct verus_syn::token::Equiv">Equiv</a>)

</div>

<div id="variant.Imply" class="section variant">

<a href="#variant.Imply" class="anchor">§</a>

### Imply(<a href="token/struct.Imply.html" class="struct"
title="struct verus_syn::token::Imply">Imply</a>)

</div>

<div id="variant.Exply" class="section variant">

<a href="#variant.Exply" class="anchor">§</a>

### Exply(<a href="token/struct.Exply.html" class="struct"
title="struct verus_syn::token::Exply">Exply</a>)

</div>

<div id="variant.BigEq" class="section variant">

<a href="#variant.BigEq" class="anchor">§</a>

### BigEq(<a href="token/struct.EqEqEq.html" class="struct"
title="struct verus_syn::token::EqEqEq">EqEqEq</a>)

</div>

<div id="variant.BigNe" class="section variant">

<a href="#variant.BigNe" class="anchor">§</a>

### BigNe(<a href="token/struct.NeEq.html" class="struct"
title="struct verus_syn::token::NeEq">NeEq</a>)

</div>

<div id="variant.ExtEq" class="section variant">

<a href="#variant.ExtEq" class="anchor">§</a>

### ExtEq(<a href="token/struct.TildeEq.html" class="struct"
title="struct verus_syn::token::TildeEq">TildeEq</a>)

</div>

<div id="variant.ExtNe" class="section variant">

<a href="#variant.ExtNe" class="anchor">§</a>

### ExtNe(<a href="token/struct.TildeNe.html" class="struct"
title="struct verus_syn::token::TildeNe">TildeNe</a>)

</div>

<div id="variant.ExtDeepEq" class="section variant">

<a href="#variant.ExtDeepEq" class="anchor">§</a>

### ExtDeepEq(<a href="token/struct.TildeTildeEq.html" class="struct"
title="struct verus_syn::token::TildeTildeEq">TildeTildeEq</a>)

</div>

<div id="variant.ExtDeepNe" class="section variant">

<a href="#variant.ExtDeepNe" class="anchor">§</a>

### ExtDeepNe(<a href="token/struct.TildeTildeNe.html" class="struct"
title="struct verus_syn::token::TildeTildeNe">TildeTildeNe</a>)

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-BinOp" class="section impl">

<a href="../src/verus_syn/gen/clone.rs.html#215-219"
class="src rightside">Source</a><a href="#impl-Clone-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/verus_syn/gen/clone.rs.html#216-218"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> Self

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#245-247"
class="src">Source</a></span><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Debug-for-BinOp" class="section impl">

<a href="../src/verus_syn/gen/debug.rs.html#224-415"
class="src rightside">Source</a><a href="#impl-Debug-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/verus_syn/gen/debug.rs.html#225-414"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, formatter: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Hash-for-BinOp" class="section impl">

<a href="../src/verus_syn/gen/hash.rs.html#214-333"
class="src rightside">Source</a><a href="#impl-Hash-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.hash" class="section method trait-impl">

<a href="../src/verus_syn/gen/hash.rs.html#215-332"
class="src rightside">Source</a><a href="#method.hash" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash"
class="fn">hash</a>\<H\>(&self, state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>,

</div>

</div>

<div class="docblock">

Feeds this value into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#tymethod.hash)

</div>

<div id="method.hash_slice" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.3.0">1.3.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/hash/mod.rs.html#235-237"
class="src">Source</a></span><a href="#method.hash_slice" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice"
class="fn">hash_slice</a>\<H\>(data: &\[Self\], state: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut H</a>)

<div class="where">

where H:
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html"
class="trait" title="trait core::hash::Hasher">Hasher</a>, Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Feeds a slice of this type into the given
[`Hasher`](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hasher.html "trait core::hash::Hasher").
[Read
more](https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html#method.hash_slice)

</div>

</div>

<div id="impl-Parse-for-BinOp" class="section impl">

<a href="../src/verus_syn/op.rs.html#103-183"
class="src rightside">Source</a><a href="#impl-Parse-for-BinOp" class="anchor">§</a>

### impl <a href="parse/trait.Parse.html" class="trait"
title="trait verus_syn::parse::Parse">Parse</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div class="impl-items">

<div id="method.parse" class="section method trait-impl">

<a href="../src/verus_syn/op.rs.html#104-182"
class="src rightside">Source</a><a href="#method.parse" class="anchor">§</a>

#### fn <a href="parse/trait.Parse.html#tymethod.parse" class="fn">parse</a>(input: <a href="parse/type.ParseStream.html" class="type"
title="type verus_syn::parse::ParseStream">ParseStream</a>\<'\_\>) -\> <a href="type.Result.html" class="type"
title="type verus_syn::Result">Result</a>\<Self\>

</div>

</div>

<div id="impl-PartialEq-for-BinOp" class="section impl">

<a href="../src/verus_syn/gen/eq.rs.html#183-226"
class="src rightside">Source</a><a href="#impl-PartialEq-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../src/verus_syn/gen/eq.rs.html#184-225"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, other: &Self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-ToTokens-for-BinOp" class="section impl">

<a href="../src/verus_syn/op.rs.html#217-261"
class="src rightside">Source</a><a href="#impl-ToTokens-for-BinOp" class="anchor">§</a>

### impl <a href="../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../src/verus_syn/op.rs.html#218-260"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens"
class="fn">to_tokens</a>(&self, tokens: &mut <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`. [Read
more](../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens)

</div>

<div id="method.to_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#59"
class="src rightside">Source</a><a href="#method.to_token_stream" class="anchor">§</a>

#### fn <a href="../quote/to_tokens/trait.ToTokens.html#method.to_token_stream"
class="fn">to_token_stream</a>(&self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.to_token_stream)

</div>

<div id="method.into_token_stream" class="section method trait-impl">

<a href="../src/quote/to_tokens.rs.html#69-71"
class="src rightside">Source</a><a href="#method.into_token_stream" class="anchor">§</a>

#### fn <a
href="../quote/to_tokens/trait.ToTokens.html#method.into_token_stream"
class="fn">into_token_stream</a>(self) -\> <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../quote/to_tokens/trait.ToTokens.html#method.into_token_stream)

</div>

</div>

<div id="impl-Copy-for-BinOp" class="section impl">

<a href="../src/verus_syn/gen/clone.rs.html#212"
class="src rightside">Source</a><a href="#impl-Copy-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

<div id="impl-Eq-for-BinOp" class="section impl">

<a href="../src/verus_syn/gen/eq.rs.html#180"
class="src rightside">Source</a><a href="#impl-Eq-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate features `derive` or `full`** only.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-BinOp" class="section impl">

<a href="#impl-Freeze-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div id="impl-RefUnwindSafe-for-BinOp" class="section impl">

<a href="#impl-RefUnwindSafe-for-BinOp" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div id="impl-Send-for-BinOp" class="section impl">

<a href="#impl-Send-for-BinOp" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div id="impl-Sync-for-BinOp" class="section impl">

<a href="#impl-Sync-for-BinOp" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div id="impl-Unpin-for-BinOp" class="section impl">

<a href="#impl-Unpin-for-BinOp" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

<div id="impl-UnwindSafe-for-BinOp" class="section impl">

<a href="#impl-UnwindSafe-for-BinOp" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="enum.BinOp.html" class="enum"
title="enum verus_syn::BinOp">BinOp</a>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-Spanned-for-T" class="section impl">

<a href="../src/verus_syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T\> <a href="spanned/trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for T

<div class="where">

where T: Spanned +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span" class="section method trait-impl">

<a href="../src/verus_syn/spanned.rs.html#105-107"
class="src rightside">Source</a><a href="#method.span" class="anchor">§</a>

#### fn <a href="spanned/trait.Spanned.html#tymethod.span" class="fn">span</a>(&self) -\> <a href="../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
if this node is empty.

</div>

</div>

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

</div>

</div>

</div>
