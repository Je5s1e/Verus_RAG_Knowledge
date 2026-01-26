<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_syn](../index.html)::[spanned](index.html)

</div>

# Trait <span class="trait">Spanned</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_syn/spanned.rs.html#96-102"
class="src">Source</a> </span>

</div>

``` rust
pub trait Spanned: Sealed {
    // Required method
    fn span(&self) -> Span;
}
```

Expand description

<div class="docblock">

A trait that can provide the `Span` of the complete contents of a syntax
tree node.

This trait is automatically implemented for all types that implement
[`ToTokens`](../../quote/to_tokens/trait.ToTokens.html "trait quote::to_tokens::ToTokens")
from the `quote` crate, as well as for `Span` itself.

See the [module documentation](index.html "mod verus_syn::spanned") for
an example.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.span" class="section method">

<a href="../../src/verus_syn/spanned.rs.html#101"
class="src rightside">Source</a>

#### fn <a href="#tymethod.span" class="fn">span</a>(&self) -\> <a href="../../proc_macro2/struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns a `Span` covering the complete contents of this syntax tree
node, or
[`Span::call_site()`](../../proc_macro2/struct.Span.html#method.call_site "associated function proc_macro2::Span::call_site")
if this node is empty.

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Spanned-for-QSelf" class="section impl">

<a href="../../src/verus_syn/path.rs.html#952-965"
class="src rightside">Source</a><a href="#impl-Spanned-for-QSelf" class="anchor">§</a>

### impl <a href="trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for <a href="../struct.QSelf.html" class="struct"
title="struct verus_syn::QSelf">QSelf</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `parsing`** only.

</div>

</div>

<div id="impl-Spanned-for-T" class="section impl">

<a href="../../src/verus_syn/spanned.rs.html#104-108"
class="src rightside">Source</a><a href="#impl-Spanned-for-T" class="anchor">§</a>

### impl\<T: ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + ToTokens\> <a href="trait.Spanned.html" class="trait"
title="trait verus_syn::spanned::Spanned">Spanned</a> for T

</div>

</div>

</div>

</div>
