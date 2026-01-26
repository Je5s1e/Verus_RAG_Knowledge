<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Type Alias <span class="type">SpecString</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#210"
class="src">Source</a> </span>

</div>

``` rust
pub type SpecString = Seq<char>;
```

Expand description

<div class="docblock">

We use this special alias to tell the `exec_spec` macro to compile
[`Seq<char>`](../../seq/struct.Seq.html "struct vstd::seq::Seq") to
[`String`](https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html "struct alloc::string::String")
instead of
[`Vec<char>`](https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html "struct alloc::vec::Vec").

</div>

## Aliased Type<a href="#aliased-type" class="anchor">§</a>

``` rust
pub struct SpecString { /* private fields */ }
```

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-ExecSpecType-for-Seq%3Cchar%3E" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#212-216"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-Seq%3Cchar%3E" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="type.SpecString.html" class="type"
title="type vstd::contrib::exec_spec::SpecString">SpecString</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#213"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType" class="anchor">§</a>

#### type <a href="trait.ExecSpecType.html#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="docblock">

Owned version of the exec type.

</div>

<div id="associatedtype.ExecRefType"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#215"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType" class="anchor">§</a>

#### type <a href="trait.ExecSpecType.html#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="docblock">

Reference version of the exec type.

</div>

</div>

</div>

</div>

</div>
