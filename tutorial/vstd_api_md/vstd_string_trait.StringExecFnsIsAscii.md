<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[string](index.html)

</div>

# Trait <span class="trait">StringExecFnsIsAscii</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/string.rs.html#297-299" class="src">Source</a>
</span>

</div>

``` rust
pub trait StringExecFnsIsAscii: Sized {
    // Required method
    fn is_ascii(&self) -> bool;
}
```

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.is_ascii" class="section method">

<a href="../../src/vstd/string.rs.html#298"
class="src rightside">Source</a>

#### fn <a href="#tymethod.is_ascii" class="fn">is_ascii</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

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

<div id="impl-StringExecFnsIsAscii-for-String" class="section impl">

<a href="../../src/vstd/string.rs.html#303-308"
class="src rightside">Source</a><a href="#impl-StringExecFnsIsAscii-for-String" class="anchor">§</a>

### impl <a href="trait.StringExecFnsIsAscii.html" class="trait"
title="trait vstd::string::StringExecFnsIsAscii">StringExecFnsIsAscii</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="method.is_ascii" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#305-307"
class="src rightside">Source</a><a href="#method.is_ascii" class="anchor">§</a>

#### fn <a href="#tymethod.is_ascii" class="fn">is_ascii</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
