<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">ExecSpecIndex</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#64-71"
class="src">Source</a> </span>

</div>

``` rust
pub trait ExecSpecIndex<'a>: Sized + DeepView<V = Seq<<Self::Elem as DeepView>::V>> {
    type Elem: DeepView;

    // Required method
    fn exec_index(self, index: usize) -> Self::Elem;
}
```

Expand description

<div class="docblock">

Spec for executable version of
[`Seq`](../../seq/struct.Seq.html "struct vstd::seq::Seq") indexing.

</div>

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.Elem" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#65"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Elem" class="associatedtype">Elem</a>: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>

</div>

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.exec_index" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#67-70"
class="src rightside">Source</a>

#### fn <a href="#tymethod.exec_index" class="fn">exec_index</a>(self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self::<a href="trait.ExecSpecIndex.html#associatedtype.Elem"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecIndex::Elem">Elem</a>

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

<div id="impl-ExecSpecIndex%3C'a%3E-for-%26str" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#271-281"
class="src rightside">Source</a><a href="#impl-ExecSpecIndex%3C&#39;a%3E-for-%26str"
class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecIndex.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecIndex">ExecSpecIndex</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="associatedtype.Elem-1"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#272"
class="src rightside">Source</a><a href="#associatedtype.Elem-1" class="anchor">§</a>

#### type <a href="#associatedtype.Elem" class="associatedtype">Elem</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div id="method.exec_index" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#275-280"
class="src rightside">Source</a><a href="#method.exec_index" class="anchor">§</a>

#### fn <a href="#tymethod.exec_index" class="fn">exec_index</a>(self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self::<a href="trait.ExecSpecIndex.html#associatedtype.Elem"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecIndex::Elem">Elem</a>

</div>

</div>

<div id="impl-ExecSpecIndex%3C'a%3E-for-%26%5BT%5D"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#345-356"
class="src rightside">Source</a><a href="#impl-ExecSpecIndex%3C&#39;a%3E-for-%26%5BT%5D"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ExecSpecIndex.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecIndex">ExecSpecIndex</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

</div>

<div class="impl-items">

<div id="associatedtype.Elem-2"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#346"
class="src rightside">Source</a><a href="#associatedtype.Elem-2" class="anchor">§</a>

#### type <a href="#associatedtype.Elem" class="associatedtype">Elem</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>

</div>

<div id="method.exec_index-1" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#350-355"
class="src rightside">Source</a><a href="#method.exec_index-1" class="anchor">§</a>

#### fn <a href="#tymethod.exec_index" class="fn">exec_index</a>(self, index: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> Self::<a href="trait.ExecSpecIndex.html#associatedtype.Elem"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecIndex::Elem">Elem</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
