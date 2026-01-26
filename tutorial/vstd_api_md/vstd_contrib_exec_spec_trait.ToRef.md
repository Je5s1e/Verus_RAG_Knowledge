<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">ToRef</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#12-17"
class="src">Source</a> </span>

</div>

``` rust
pub trait ToRef<T: Sized + DeepView>: Sized + DeepView<V = T::V> {
    // Required method
    fn get_ref(self) -> T;
}
```

Expand description

<div class="docblock">

[`ToRef`](trait.ToRef.html "trait vstd::contrib::exec_spec::ToRef") and
[`ToOwned`](trait.ToOwned.html "trait vstd::contrib::exec_spec::ToOwned")
are almost the same trait but separated to avoid type inference
ambiguities.

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.get_ref" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#13-16"
class="src rightside">Source</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> T

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

<div id="impl-ToRef%3C%26str%3E-for-%26String" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#218-223"
class="src rightside">Source</a><a href="#impl-ToRef%3C%26str%3E-for-%26String" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<&'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>\> for &'a <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="impl-items">

<div id="method.get_ref" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#220-222"
class="src rightside">Source</a><a href="#method.get_ref" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

</div>

<div id="impl-ToRef%3Cbool%3E-for-%26bool" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cbool%3E-for-%26bool" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="method.get_ref-1" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-1" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ToRef%3Cchar%3E-for-%26char" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cchar%3E-for-%26char" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="method.get_ref-2" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-2" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

</div>

<div id="impl-ToRef%3Ci8%3E-for-%26i8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Ci8%3E-for-%26i8" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="method.get_ref-3" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-3" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

</div>

<div id="impl-ToRef%3Ci16%3E-for-%26i16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Ci16%3E-for-%26i16" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="method.get_ref-4" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-4" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

</div>

<div id="impl-ToRef%3Ci32%3E-for-%26i32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Ci32%3E-for-%26i32" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="method.get_ref-5" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-5" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

</div>

<div id="impl-ToRef%3Ci64%3E-for-%26i64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Ci64%3E-for-%26i64" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="method.get_ref-6" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-6" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

</div>

<div id="impl-ToRef%3Ci128%3E-for-%26i128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Ci128%3E-for-%26i128" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="method.get_ref-7" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-7" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

</div>

<div id="impl-ToRef%3Cisize%3E-for-%26isize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cisize%3E-for-%26isize" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="method.get_ref-8" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-8" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

</div>

<div id="impl-ToRef%3Cu8%3E-for-%26u8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cu8%3E-for-%26u8" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="method.get_ref-9" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-9" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

</div>

<div id="impl-ToRef%3Cu16%3E-for-%26u16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cu16%3E-for-%26u16" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="method.get_ref-10" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-10" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

</div>

<div id="impl-ToRef%3Cu32%3E-for-%26u32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cu32%3E-for-%26u32" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="method.get_ref-11" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-11" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

</div>

<div id="impl-ToRef%3Cu64%3E-for-%26u64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cu64%3E-for-%26u64" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="method.get_ref-12" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-12" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

</div>

<div id="impl-ToRef%3Cu128%3E-for-%26u128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cu128%3E-for-%26u128" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="method.get_ref-13" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-13" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

</div>

<div id="impl-ToRef%3Cusize%3E-for-%26usize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToRef%3Cusize%3E-for-%26usize" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="method.get_ref-14" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_ref-14" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

<div id="impl-ToRef%3C%26(T1,+T2)%3E-for-%26(T1,+T2)"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#172-177"
class="src rightside">Source</a><a href="#impl-ToRef%3C%26(T1,+T2)%3E-for-%26(T1,+T2)"
class="anchor">§</a>

### impl\<'a, T1: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>, T2: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<&'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

<div class="docblock">

TODO: generalize to more tuple types

</div>

</div>

<div class="impl-items">

<div id="method.get_ref-15" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#174-176"
class="src rightside">Source</a><a href="#method.get_ref-15" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

</div>

</div>

<div id="impl-ToRef%3C%26%5BT%5D%3E-for-%26Vec%3CT%3E"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#285-290"
class="src rightside">Source</a><a href="#impl-ToRef%3C%26%5BT%5D%3E-for-%26Vec%3CT%3E"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<&'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

<div class="docblock">

NOTE: can’t implement
[`ExecSpecType`](trait.ExecSpecType.html "trait vstd::contrib::exec_spec::ExecSpecType")
for [`Seq<T>`](../../seq/struct.Seq.html "struct vstd::seq::Seq") since
it conflicts with
[`SpecString`](type.SpecString.html "type vstd::contrib::exec_spec::SpecString")
(i.e.,
[`Seq<char>`](../../seq/struct.Seq.html "struct vstd::seq::Seq")).

</div>

</div>

<div class="impl-items">

<div id="method.get_ref-16" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#287-289"
class="src rightside">Source</a><a href="#method.get_ref-16" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

</div>

</div>

<div id="impl-ToRef%3C%26Option%3CT%3E%3E-for-%26Option%3CT%3E"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#134-139"
class="src rightside">Source</a><a href="#impl-ToRef%3C%26Option%3CT%3E%3E-for-%26Option%3CT%3E"
class="anchor">§</a>

### impl\<'a, T: <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a> + <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\> <a href="trait.ToRef.html" class="trait"
title="trait vstd::contrib::exec_spec::ToRef">ToRef</a>\<&'a <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="method.get_ref-17" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#136-138"
class="src rightside">Source</a><a href="#method.get_ref-17" class="anchor">§</a>

#### fn <a href="#tymethod.get_ref" class="fn">get_ref</a>(self) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
