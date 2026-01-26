<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[quote](index.html)

</div>

# Trait <span class="trait">TokenStreamExt</span> Copy item path

<span class="sub-heading"><a href="../src/quote/ext.rs.html#8-57" class="src">Source</a>
</span>

</div>

``` rust
pub trait TokenStreamExt: Sealed {
    // Required methods
    fn append<U>(&mut self, token: U)
       where U: Into<TokenTree>;
    fn append_all<I>(&mut self, iter: I)
       where I: IntoIterator,
             I::Item: ToTokens;
    fn append_separated<I, U>(&mut self, iter: I, op: U)
       where I: IntoIterator,
             I::Item: ToTokens,
             U: ToTokens;
    fn append_terminated<I, U>(&mut self, iter: I, term: U)
       where I: IntoIterator,
             I::Item: ToTokens,
             U: ToTokens;
}
```

Expand description

<div class="docblock">

TokenStream extension trait with methods for appending tokens.

This trait is sealed and cannot be implemented outside of the `quote`
crate.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.append" class="section method">

<a href="../src/quote/ext.rs.html#12-14"
class="src rightside">Source</a>

#### fn <a href="#tymethod.append" class="fn">append</a>\<U\>(&mut self, token: U)

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<<a href="../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>\>,

</div>

</div>

<div class="docblock">

For use by `ToTokens` implementations.

Appends the token specified to this list of tokens.

</div>

<div id="tymethod.append_all" class="section method">

<a href="../src/quote/ext.rs.html#33-36"
class="src rightside">Source</a>

#### fn <a href="#tymethod.append_all" class="fn">append_all</a>\<I\>(&mut self, iter: I)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
I::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

For use by `ToTokens` implementations.

<div class="example-wrap">

``` rust
struct X;

impl ToTokens for X {
    fn to_tokens(&self, tokens: &mut TokenStream) {
        tokens.append_all(&[true, false]);
    }
}

let tokens = quote!(#X);
assert_eq!(tokens.to_string(), "true false");
```

</div>

</div>

<div id="tymethod.append_separated" class="section method">

<a href="../src/quote/ext.rs.html#42-46"
class="src rightside">Source</a>

#### fn <a href="#tymethod.append_separated" class="fn">append_separated</a>\<I, U\>(&mut self, iter: I, op: U)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
I::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>, U:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

For use by `ToTokens` implementations.

Appends all of the items in the iterator `I`, separated by the tokens
`U`.

</div>

<div id="tymethod.append_terminated" class="section method">

<a href="../src/quote/ext.rs.html#52-56"
class="src rightside">Source</a>

#### fn <a href="#tymethod.append_terminated" class="fn">append_terminated</a>\<I, U\>(&mut self, iter: I, term: U)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
I::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>, U:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>,

</div>

</div>

<div class="docblock">

For use by `ToTokens` implementations.

Appends all tokens in the iterator `I`, appending `U` after each
element, including after the last element of the iterator.

</div>

</div>

## Dyn Compatibility<a href="#dyn-compatibility" class="anchor">§</a>

<div class="dyn-compatibility-info">

This trait is **not** [dyn
compatible](https://doc.rust-lang.org/1.92.0/reference/items/traits.html#dyn-compatibility).

*In older versions of Rust, dyn compatibility was called "object
safety", so this trait is not object safe.*

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-TokenStreamExt-for-TokenStream" class="section impl">

<a href="../src/quote/ext.rs.html#59-130"
class="src rightside">Source</a><a href="#impl-TokenStreamExt-for-TokenStream" class="anchor">§</a>

### impl <a href="trait.TokenStreamExt.html" class="trait"
title="trait quote::TokenStreamExt">TokenStreamExt</a> for <a href="../proc_macro2/struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.append" class="section method trait-impl">

<a href="../src/quote/ext.rs.html#60-65"
class="src rightside">Source</a><a href="#method.append" class="anchor">§</a>

#### fn <a href="#tymethod.append" class="fn">append</a>\<U\>(&mut self, token: U)

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<<a href="../proc_macro2/enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>\>,

</div>

</div>

<div id="method.append_all" class="section method trait-impl">

<a href="../src/quote/ext.rs.html#67-83"
class="src rightside">Source</a><a href="#method.append_all" class="anchor">§</a>

#### fn <a href="#tymethod.append_all" class="fn">append_all</a>\<I\>(&mut self, iter: I)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
I::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>,

</div>

</div>

<div id="method.append_separated" class="section method trait-impl">

<a href="../src/quote/ext.rs.html#85-108"
class="src rightside">Source</a><a href="#method.append_separated" class="anchor">§</a>

#### fn <a href="#tymethod.append_separated" class="fn">append_separated</a>\<I, U\>(&mut self, iter: I, op: U)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
I::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>, U:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>,

</div>

</div>

<div id="method.append_terminated" class="section method trait-impl">

<a href="../src/quote/ext.rs.html#110-129"
class="src rightside">Source</a><a href="#method.append_terminated" class="anchor">§</a>

#### fn <a href="#tymethod.append_terminated" class="fn">append_terminated</a>\<I, U\>(&mut self, iter: I, term: U)

<div class="where">

where I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>,
I::<a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html#associatedtype.Item"
class="associatedtype"
title="type core::iter::traits::collect::IntoIterator::Item">Item</a>:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>, U:
<a href="trait.ToTokens.html" class="trait"
title="trait quote::ToTokens">ToTokens</a>,

</div>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
