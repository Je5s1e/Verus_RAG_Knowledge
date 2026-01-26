<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[indexmap](index.html)

</div>

# Trait <span class="trait">Equivalent</span> Copy item path

<span class="sub-heading"><a href="../src/indexmap/equivalent.rs.html#13-16"
class="src">Source</a> </span>

</div>

``` rust
pub trait Equivalent<K: ?Sized> {
    // Required method
    fn equivalent(&self, key: &K) -> bool;
}
```

Expand description

<div class="docblock">

Key equivalence trait.

This trait allows hash table lookup to be customized. It has one blanket
implementation that uses the regular `Borrow` solution, just like
`HashMap` and `BTreeMap` do, so that you can pass `&str` to lookup into
a map with `String` keys and so on.

## <a href="#contract" class="doc-anchor">§</a>Contract

The implementor **must** hash like `K`, if it is hashable.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.equivalent" class="section method">

<a href="../src/indexmap/equivalent.rs.html#15"
class="src rightside">Source</a>

#### fn <a href="#tymethod.equivalent" class="fn">equivalent</a>(&self, key: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;K</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Compare self to `key` and return `true` if they are equal.

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Equivalent%3CK%3E-for-Q" class="section impl">

<a href="../src/indexmap/equivalent.rs.html#18-27"
class="src rightside">Source</a><a href="#impl-Equivalent%3CK%3E-for-Q" class="anchor">§</a>

### impl\<Q, K\> <a href="trait.Equivalent.html" class="trait"
title="trait indexmap::Equivalent">Equivalent</a>\<K\> for Q

<div class="where">

where Q:
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>, K:
<a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<Q\> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

</div>

</div>

</div>
