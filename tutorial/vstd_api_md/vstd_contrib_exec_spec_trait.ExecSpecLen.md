<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">ExecSpecLen</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#59-61"
class="src">Source</a> </span>

</div>

``` rust
pub trait ExecSpecLen {
    // Required method
    fn exec_len(&self) -> usize;
}
```

Expand description

<div class="docblock">

Spec for executable version of \[`Seq::len`\].

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.exec_len" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#60"
class="src rightside">Source</a>

#### fn <a href="#tymethod.exec_len" class="fn">exec_len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-ExecSpecLen-for-%26str" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#261-269"
class="src rightside">Source</a><a href="#impl-ExecSpecLen-for-%26str" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecLen.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecLen">ExecSpecLen</a> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="method.exec_len" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#263-268"
class="src rightside">Source</a><a href="#method.exec_len" class="anchor">§</a>

#### fn <a href="#tymethod.exec_len" class="fn">exec_len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

<div id="impl-ExecSpecLen-for-%26%5BT%5D" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#334-343"
class="src rightside">Source</a><a href="#impl-ExecSpecLen-for-%26%5BT%5D" class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ExecSpecLen.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecLen">ExecSpecLen</a> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

</div>

<div class="impl-items">

<div id="method.exec_len-1" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#337-342"
class="src rightside">Source</a><a href="#method.exec_len-1" class="anchor">§</a>

#### fn <a href="#tymethod.exec_len" class="fn">exec_len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
