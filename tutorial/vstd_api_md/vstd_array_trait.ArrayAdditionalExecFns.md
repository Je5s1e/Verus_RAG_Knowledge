<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[array](index.html)

</div>

# Trait <span class="trait">ArrayAdditionalExecFns</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/array.rs.html#38-40" class="src">Source</a>
</span>

</div>

``` rust
pub trait ArrayAdditionalExecFns<T> {
    // Required method
    fn set(&mut self, idx: usize, t: T);
}
```

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.set" class="section method">

<a href="../../src/vstd/array.rs.html#39"
class="src rightside">Source</a>

#### fn <a href="#tymethod.set" class="fn">set</a>(&mut self, idx: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, t: T)

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-ArrayAdditionalExecFns%3CT%3E-for-%5BT;+N%5D"
class="section impl">

<a href="../../src/vstd/array.rs.html#59-69"
class="src rightside">Source</a><a href="#impl-ArrayAdditionalExecFns%3CT%3E-for-%5BT;+N%5D"
class="anchor">§</a>

### impl\<T, const N: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> <a href="trait.ArrayAdditionalExecFns.html" class="trait"
title="trait vstd::array::ArrayAdditionalExecFns">ArrayAdditionalExecFns</a>\<T\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.array.html"
class="primitive">[T; N]</a>

</div>

<div class="impl-items">

<div id="method.set" class="section method trait-impl">

<a href="../../src/vstd/array.rs.html#61-68"
class="src rightside">Source</a><a href="#method.set" class="anchor">§</a>

#### fn <a href="#tymethod.set" class="fn">set</a>(&mut self, idx: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, t: T)

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
