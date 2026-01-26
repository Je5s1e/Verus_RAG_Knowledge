<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[string](index.html)

</div>

# Trait <span class="trait">StringExecFns</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/string.rs.html#312-318" class="src">Source</a>
</span>

</div>

``` rust
pub trait StringExecFns: Sized {
    // Required methods
    fn from_str<'a>(s: &'a str) -> String;
    fn append<'a, 'b>(&'a mut self, other: &'b str);
    fn concat<'b>(self, other: &'b str) -> String;
}
```

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.from_str" class="section method">

<a href="../../src/vstd/string.rs.html#313"
class="src rightside">Source</a>

#### fn <a href="#tymethod.from_str" class="fn">from_str</a>\<'a\>(s: &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div id="tymethod.append" class="section method">

<a href="../../src/vstd/string.rs.html#315"
class="src rightside">Source</a>

#### fn <a href="#tymethod.append" class="fn">append</a>\<'a, 'b\>(&'a mut self, other: &'b <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>)

</div>

<div id="tymethod.concat" class="section method">

<a href="../../src/vstd/string.rs.html#317"
class="src rightside">Source</a>

#### fn <a href="#tymethod.concat" class="fn">concat</a>\<'b\>(self, other: &'b <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

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

<div id="impl-StringExecFns-for-String" class="section impl">

<a href="../../src/vstd/string.rs.html#321-348"
class="src rightside">Source</a><a href="#impl-StringExecFns-for-String" class="anchor">§</a>

### impl <a href="trait.StringExecFns.html" class="trait"
title="trait vstd::string::StringExecFns">StringExecFns</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="method.from_str" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#323-329"
class="src rightside">Source</a><a href="#method.from_str" class="anchor">§</a>

#### fn <a href="#tymethod.from_str" class="fn">from_str</a>\<'a\>(s: &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div id="method.append" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#332-338"
class="src rightside">Source</a><a href="#method.append" class="anchor">§</a>

#### fn <a href="#tymethod.append" class="fn">append</a>\<'a, 'b\>(&'a mut self, other: &'b <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>)

</div>

<div id="method.concat" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#341-347"
class="src rightside">Source</a><a href="#method.concat" class="anchor">§</a>

#### fn <a href="#tymethod.concat" class="fn">concat</a>\<'b\>(self, other: &'b <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
