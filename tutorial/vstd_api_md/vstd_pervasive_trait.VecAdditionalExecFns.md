<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[pervasive](index.html)

</div>

# Trait <span class="trait">VecAdditionalExecFns</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/pervasive.rs.html#380-384"
class="src">Source</a> </span>

</div>

``` rust
pub trait VecAdditionalExecFns<T> {
    // Required methods
    fn set(&mut self, i: usize, value: T);
    fn set_and_swap(&mut self, i: usize, value: &mut T);
}
```

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.set" class="section method">

<a href="../../src/vstd/pervasive.rs.html#381"
class="src rightside">Source</a>

#### fn <a href="#tymethod.set" class="fn">set</a>(&mut self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, value: T)

</div>

<div id="tymethod.set_and_swap" class="section method">

<a href="../../src/vstd/pervasive.rs.html#383"
class="src rightside">Source</a>

#### fn <a href="#tymethod.set_and_swap" class="fn">set_and_swap</a>(&mut self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-VecAdditionalExecFns%3CT%3E-for-Vec%3CT%3E"
class="section impl">

<a href="../../src/vstd/pervasive.rs.html#387-410"
class="src rightside">Source</a><a href="#impl-VecAdditionalExecFns%3CT%3E-for-Vec%3CT%3E"
class="anchor">§</a>

### impl\<T\> <a href="trait.VecAdditionalExecFns.html" class="trait"
title="trait vstd::pervasive::VecAdditionalExecFns">VecAdditionalExecFns</a>\<T\> for <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="method.set" class="section method trait-impl">

<a href="../../src/vstd/pervasive.rs.html#390-397"
class="src rightside">Source</a><a href="#method.set" class="anchor">§</a>

#### fn <a href="#tymethod.set" class="fn">set</a>(&mut self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, value: T)

</div>

<div class="docblock">

Replacement for `self[i] = value;` (which Verus does not support for
technical reasons)

</div>

<div id="method.set_and_swap" class="section method trait-impl">

<a href="../../src/vstd/pervasive.rs.html#401-409"
class="src rightside">Source</a><a href="#method.set_and_swap" class="anchor">§</a>

#### fn <a href="#tymethod.set_and_swap" class="fn">set_and_swap</a>(&mut self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, value: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Replacement for `swap(&mut self[i], &mut value)` (which Verus does not
support for technical reasons)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
