<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[punctuated](index.html)

</div>

# Enum <span class="enum">Pair</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/punctuated.rs.html#958-961"
class="src">Source</a> </span>

</div>

``` rust
pub enum Pair<T, P> {
    Punctuated(T, P),
    End(T),
}
```

Expand description

<div class="docblock">

A single syntax tree node of type `T` followed by its trailing
punctuation of type `P` if any.

Refer to the [module
documentation](index.html "mod verus_syn::punctuated") for details about
punctuated sequences.

</div>

## Variants<a href="#variants" class="anchor">§</a>

<div class="variants">

<div id="variant.Punctuated" class="section variant">

<a href="#variant.Punctuated" class="anchor">§</a>

### Punctuated(T, P)

</div>

<div id="variant.End" class="section variant">

<a href="#variant.End" class="anchor">§</a>

### End(T)

</div>

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Pair%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#963-1037"
class="src rightside">Source</a><a href="#impl-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

</div>

<div class="impl-items">

<div id="method.into_value" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#966-970"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_value" class="fn">into_value</a>(self) -\> T

</div>

<div class="docblock">

Extracts the syntax tree node from this punctuated pair, discarding the
following punctuation.

</div>

<div id="method.value" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#973-977"
class="src rightside">Source</a>

#### pub fn <a href="#method.value" class="fn">value</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Borrows the syntax tree node from this punctuated pair.

</div>

<div id="method.value_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#980-984"
class="src rightside">Source</a>

#### pub fn <a href="#method.value_mut" class="fn">value_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows the syntax tree node from this punctuated pair.

</div>

<div id="method.punct" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#988-993"
class="src rightside">Source</a>

#### pub fn <a href="#method.punct" class="fn">punct</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;P</a>\>

</div>

<div class="docblock">

Borrows the punctuation from this punctuated pair, unless this pair is
the final one and there is no trailing punctuation.

</div>

<div id="method.punct_mut" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#1013-1018"
class="src rightside">Source</a>

#### pub fn <a href="#method.punct_mut" class="fn">punct_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut P</a>\>

</div>

<div class="docblock">

Mutably borrows the punctuation from this punctuated pair, unless the
pair is the final one and there is no trailing punctuation.

##### <a href="#example" class="doc-anchor">§</a>Example

<div class="example-wrap">

``` rust
punctuated.insert(0, parse_quote!('lifetime));
if let Some(punct) = punctuated.pairs_mut().next().unwrap().punct_mut() {
    punct.span = span;
}
```

</div>

</div>

<div id="method.new" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#1022-1027"
class="src rightside">Source</a>

#### pub fn <a href="#method.new" class="fn">new</a>(t: T, p: <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<P\>) -\> Self

</div>

<div class="docblock">

Creates a punctuated pair out of a syntax tree node and an optional
following punctuation.

</div>

<div id="method.into_tuple" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#1031-1036"
class="src rightside">Source</a>

#### pub fn <a href="#method.into_tuple" class="fn">into_tuple</a>(self) -\> (T, <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<P\>)

</div>

<div class="docblock">

Produces this punctuated pair as a tuple of syntax tree node and
optional following punctuation.

</div>

</div>

<div id="impl-Pair%3C%26T,+%26P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1041-1052"
class="src rightside">Source</a><a href="#impl-Pair%3C%26T,+%26P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>, <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;P</a>\>

</div>

<div class="impl-items">

<div id="method.cloned" class="section method">

<a href="../../src/verus_syn/punctuated.rs.html#1042-1051"
class="src rightside">Source</a>

#### pub fn <a href="#method.cloned" class="fn">cloned</a>(self) -\> <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Pair%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1056-1067"
class="src rightside">Source</a><a href="#impl-Clone-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `clone-impls`** only.

</div>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#1061-1066"
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

<div id="impl-Extend%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#487-497"
class="src rightside">Source</a><a href="#impl-Extend%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

<div class="where">

where P: <a
href="https://doc.rust-lang.org/1.92.0/core/default/trait.Default.html"
class="trait" title="trait core::default::Default">Default</a>,

</div>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#491-496"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\>\>(&mut self, i: I)

</div>

<div class="docblock">

Extends a collection with the contents of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend)

</div>

<div id="method.extend_one" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_one"
class="fn">extend_one</a>(&mut self, item: A)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Extends a collection with exactly one element.

</div>

<div id="method.extend_reserve" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve"
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Reserves capacity in a collection for the given number of additional
elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve)

</div>

</div>

<div id="impl-FromIterator%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#479-485"
class="src rightside">Source</a><a
href="#impl-FromIterator%3CPair%3CT,+P%3E%3E-for-Punctuated%3CT,+P%3E"
class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html"
class="trait"
title="trait core::iter::traits::collect::FromIterator">FromIterator</a>\<<a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\> for <a href="struct.Punctuated.html" class="struct"
title="struct verus_syn::punctuated::Punctuated">Punctuated</a>\<T, P\>

</div>

<div class="impl-items">

<div id="method.from_iter" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#480-484"
class="src rightside">Source</a><a href="#method.from_iter" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter"
class="fn">from_iter</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>\>\>(i: I) -\> Self

</div>

<div class="docblock">

Creates a value from an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.FromIterator.html#tymethod.from_iter)

</div>

</div>

<div id="impl-ToTokens-for-Pair%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1154-1168"
class="src rightside">Source</a><a href="#impl-ToTokens-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="../../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="../../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>, P:
<a href="../../quote/to_tokens/trait.ToTokens.html" class="trait"
title="trait quote::to_tokens::ToTokens">ToTokens</a>,

</div>

</div>

<div class="impl-items">

<div id="method.to_tokens" class="section method trait-impl">

<a href="../../src/verus_syn/punctuated.rs.html#1159-1167"
class="src rightside">Source</a><a href="#method.to_tokens" class="anchor">§</a>

#### fn <a href="../../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens"
class="fn">to_tokens</a>(&self, tokens: &mut <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>)

</div>

<div class="docblock">

Write `self` to the given `TokenStream`. [Read
more](../../quote/to_tokens/trait.ToTokens.html#tymethod.to_tokens)

</div>

<div id="method.to_token_stream" class="section method trait-impl">

<a href="../../src/quote/to_tokens.rs.html#59"
class="src rightside">Source</a><a href="#method.to_token_stream" class="anchor">§</a>

#### fn <a
href="../../quote/to_tokens/trait.ToTokens.html#method.to_token_stream"
class="fn">to_token_stream</a>(&self) -\> <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../../quote/to_tokens/trait.ToTokens.html#method.to_token_stream)

</div>

<div id="method.into_token_stream" class="section method trait-impl">

<a href="../../src/quote/to_tokens.rs.html#69-71"
class="src rightside">Source</a><a href="#method.into_token_stream" class="anchor">§</a>

#### fn <a
href="../../quote/to_tokens/trait.ToTokens.html#method.into_token_stream"
class="fn">into_token_stream</a>(self) -\> <a href="../../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Convert `self` directly into a `TokenStream` object. [Read
more](../../quote/to_tokens/trait.ToTokens.html#method.into_token_stream)

</div>

</div>

<div id="impl-Copy-for-Pair%3CT,+P%3E" class="section impl">

<a href="../../src/verus_syn/punctuated.rs.html#1071-1076"
class="src rightside">Source</a><a href="#impl-Copy-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a>,

</div>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `clone-impls`** only.

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Pair%3CT,+P%3E" class="section impl">

<a href="#impl-Freeze-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a>,

</div>

</div>

<div id="impl-RefUnwindSafe-for-Pair%3CT,+P%3E" class="section impl">

<a href="#impl-RefUnwindSafe-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,
P: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a>,

</div>

</div>

<div id="impl-Send-for-Pair%3CT,+P%3E" class="section impl">

<a href="#impl-Send-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a>,

</div>

</div>

<div id="impl-Sync-for-Pair%3CT,+P%3E" class="section impl">

<a href="#impl-Sync-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a>,

</div>

</div>

<div id="impl-Unpin-for-Pair%3CT,+P%3E" class="section impl">

<a href="#impl-Unpin-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>, P:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a>,

</div>

</div>

<div id="impl-UnwindSafe-for-Pair%3CT,+P%3E" class="section impl">

<a href="#impl-UnwindSafe-for-Pair%3CT,+P%3E" class="anchor">§</a>

### impl\<T, P\> <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="enum.Pair.html" class="enum"
title="enum verus_syn::punctuated::Pair">Pair</a>\<T, P\>

<div class="where">

where T: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>, P: <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a>,

</div>

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

<a href="../../src/verus_syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T\> <a href="../spanned/trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for T

<div class="where">

where T: Spanned +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.span" class="section method trait-impl">

<a href="../../src/verus_syn/spanned.rs.html#105-107"
class="src rightside">Source</a><a href="#method.span" class="anchor">§</a>

#### fn <a href="../spanned/trait.Spanned.html#tymethod.span"
class="fn">span</a>(&self) -\> <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
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
