<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">ExecSpecEq</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#49-56"
class="src">Source</a> </span>

</div>

``` rust
pub trait ExecSpecEq<'a>: DeepView + Sized {
    type Other: DeepView<V = Self::V>;

    // Required method
    fn exec_eq(this: Self, other: Self::Other) -> bool;
}
```

Expand description

<div class="docblock">

Spec for the executable version of equality.

</div>

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.Other" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#50"
class="src rightside">Source</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a>: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\<V = Self::<a href="../../view/trait.DeepView.html#associatedtype.V"
class="associatedtype" title="type vstd::view::DeepView::V">V</a>\>

</div>

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.exec_eq" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#52-55"
class="src rightside">Source</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
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

<div id="impl-ExecSpecEq%3C'a%3E-for-%26bool" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26bool" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-1"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-1" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div id="method.exec_eq" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26char" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26char" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-2"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-2" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div id="method.exec_eq-1" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-1" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26i8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26i8" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-3"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-3" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div id="method.exec_eq-2" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-2" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26i16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26i16" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-4"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-4" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div id="method.exec_eq-3" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-3" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26i32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26i32" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-5"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-5" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div id="method.exec_eq-4" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-4" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26i64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26i64" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-6"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-6" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div id="method.exec_eq-5" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-5" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26i128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26i128" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-7"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-7" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div id="method.exec_eq-6" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-6" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26isize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26isize" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-8"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-8" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div id="method.exec_eq-7" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-7" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26str" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#240-248"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26str" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-9"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#241"
class="src rightside">Source</a><a href="#associatedtype.Other-9" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div id="method.exec_eq-8" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#245-247"
class="src rightside">Source</a><a href="#method.exec_eq-8" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26u8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26u8" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-10"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-10" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div id="method.exec_eq-9" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-9" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26u16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26u16" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-11"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-11" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div id="method.exec_eq-10" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-10" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26u32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26u32" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-12"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-12" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div id="method.exec_eq-11" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-11" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26u64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26u64" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-13"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-13" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div id="method.exec_eq-12" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-12" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26u128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26u128" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-14"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-14" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div id="method.exec_eq-13" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-13" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26usize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26usize" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-15"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-15" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div id="method.exec_eq-14" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-14" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26String" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#251-259"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26String"
class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

<div class="docblock">

Required for comparing, e.g.,
[`Vec<String>`](https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html "struct alloc::vec::Vec")s.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Other-16"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#252"
class="src rightside">Source</a><a href="#associatedtype.Other-16" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div id="method.exec_eq-15" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#256-258"
class="src rightside">Source</a><a href="#method.exec_eq-15" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-bool" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-bool" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-17"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-17" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div id="method.exec_eq-16" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-16" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-char" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-char" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-18"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-18" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div id="method.exec_eq-17" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-17" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-i8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-i8" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-19"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-19" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div id="method.exec_eq-18" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-18" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-i16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-i16" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-20"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-20" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div id="method.exec_eq-19" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-19" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-i32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-i32" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-21"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-21" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div id="method.exec_eq-20" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-20" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-i64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-i64" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-22"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-22" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div id="method.exec_eq-21" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-21" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-i128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-i128" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-23"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-23" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div id="method.exec_eq-22" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-22" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-isize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-isize" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-24"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-24" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div id="method.exec_eq-23" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-23" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-u8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-u8" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-25"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-25" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div id="method.exec_eq-24" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-24" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-u16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-u16" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-26"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-26" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div id="method.exec_eq-25" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-25" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-u32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-u32" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-27"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-27" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div id="method.exec_eq-26" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-26" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-u64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-u64" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-28"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-28" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div id="method.exec_eq-27" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-27" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-u128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-u128" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-29"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-29" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div id="method.exec_eq-28" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-28" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-usize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-usize" class="anchor">§</a>

### impl\<'a\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="associatedtype.Other-30"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.Other-30" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div id="method.exec_eq-29" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.exec_eq-29" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26(T1,+T2)" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#196-206"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26(T1,+T2)"
class="anchor">§</a>

### impl\<'a, T1: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>, T2: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

<div class="where">

where
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T1</a>:
<a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a,
Other =
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T1</a>\>,
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T2</a>:
<a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a,
Other =
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T2</a>\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Other-31"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#200"
class="src rightside">Source</a><a href="#associatedtype.Other-31" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

</div>

<div id="method.exec_eq-30" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#203-205"
class="src rightside">Source</a><a href="#method.exec_eq-30" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26Option%3CT%3E"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#158-169"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26Option%3CT%3E"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

<div class="where">

where
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>:
<a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a,
Other =
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Other-32"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#159"
class="src rightside">Source</a><a href="#associatedtype.Other-32" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div id="method.exec_eq-31" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#162-168"
class="src rightside">Source</a><a href="#method.exec_eq-31" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26%5BT%5D" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#310-320"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26%5BT%5D"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

<div class="where">

where
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>:
<a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a,
Other =
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Other-33"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#311"
class="src rightside">Source</a><a href="#associatedtype.Other-33" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

</div>

<div id="method.exec_eq-32" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#315-319"
class="src rightside">Source</a><a href="#method.exec_eq-32" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecEq%3C'a%3E-for-%26Vec%3CT%3E"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#322-332"
class="src rightside">Source</a><a href="#impl-ExecSpecEq%3C&#39;a%3E-for-%26Vec%3CT%3E"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a\> for &'a <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

<div class="where">

where
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>:
<a href="trait.ExecSpecEq.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecEq">ExecSpecEq</a>\<'a,
Other =
<a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;'a T</a>\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Other-34"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#323"
class="src rightside">Source</a><a href="#associatedtype.Other-34" class="anchor">§</a>

#### type <a href="#associatedtype.Other" class="associatedtype">Other</a> = &'a <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

</div>

<div id="method.exec_eq-33" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#327-331"
class="src rightside">Source</a><a href="#method.exec_eq-33" class="anchor">§</a>

#### fn <a href="#tymethod.exec_eq" class="fn">exec_eq</a>(this: Self, other: Self::<a href="trait.ExecSpecEq.html#associatedtype.Other"
class="associatedtype"
title="type vstd::contrib::exec_spec::ExecSpecEq::Other">Other</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
