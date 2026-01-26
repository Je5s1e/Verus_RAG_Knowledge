<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">ExecSpecType</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#37-46"
class="src">Source</a> </span>

</div>

``` rust
pub trait ExecSpecTypewhere
    for<'a> &'a Self::ExecOwnedType: ToRef<Self::ExecRefType<'a>>,
    for<'a> Self::ExecRefType<'a>: ToOwned<Self::ExecOwnedType>,{
    type ExecOwnedType: DeepView<V = Self>;
    type ExecRefType<'a>: DeepView<V = Self>;
}
```

Expand description

<div class="docblock">

Any spec types used in
[`exec_spec`](macro.exec_spec.html "macro vstd::contrib::exec_spec::exec_spec")
macro must implement this trait to indicate the corresponding exec type
(owned and borrowed versions).

</div>

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.ExecOwnedType" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#42"
class="src rightside">Source</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a>: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\<V = Self\>

</div>

<div class="docblock">

Owned version of the exec type.

</div>

<div id="associatedtype.ExecRefType" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#45"
class="src rightside">Source</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\>: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a>\<V = Self\>

</div>

<div class="docblock">

Reference version of the exec type.

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

<div id="impl-ExecSpecType-for-bool" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-bool" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-1"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-1" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div id="associatedtype.ExecRefType-1"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-1" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ExecSpecType-for-char" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-char" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-2"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-2" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div id="associatedtype.ExecRefType-2"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-2" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

</div>

<div id="impl-ExecSpecType-for-i8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-i8" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-3"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-3" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div id="associatedtype.ExecRefType-3"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-3" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

</div>

<div id="impl-ExecSpecType-for-i16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-i16" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-4"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-4" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div id="associatedtype.ExecRefType-4"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-4" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

</div>

<div id="impl-ExecSpecType-for-i32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-i32" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-5"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-5" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div id="associatedtype.ExecRefType-5"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-5" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

</div>

<div id="impl-ExecSpecType-for-i64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-i64" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-6"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-6" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div id="associatedtype.ExecRefType-6"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-6" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

</div>

<div id="impl-ExecSpecType-for-i128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-i128" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-7"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-7" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div id="associatedtype.ExecRefType-7"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-7" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

</div>

<div id="impl-ExecSpecType-for-isize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-isize" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-8"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-8" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div id="associatedtype.ExecRefType-8"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-8" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

</div>

<div id="impl-ExecSpecType-for-u8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-u8" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-9"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-9" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div id="associatedtype.ExecRefType-9"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-9" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

</div>

<div id="impl-ExecSpecType-for-u16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-u16" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-10"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-10" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div id="associatedtype.ExecRefType-10"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-10" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

</div>

<div id="impl-ExecSpecType-for-u32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-u32" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-11"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-11" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div id="associatedtype.ExecRefType-11"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-11" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

</div>

<div id="impl-ExecSpecType-for-u64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-u64" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-12"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-12" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div id="associatedtype.ExecRefType-12"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-12" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

</div>

<div id="impl-ExecSpecType-for-u128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-u128" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-13"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-13" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div id="associatedtype.ExecRefType-13"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-13" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

</div>

<div id="impl-ExecSpecType-for-usize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-usize" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-14"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-14" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div id="associatedtype.ExecRefType-14"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-14" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-ExecSpecType-for-Seq%3Cchar%3E" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#212-216"
class="src rightside">Source</a><a href="#impl-ExecSpecType-for-Seq%3Cchar%3E" class="anchor">§</a>

### impl <a href="trait.ExecSpecType.html" class="trait"
title="trait vstd::contrib::exec_spec::ExecSpecType">ExecSpecType</a> for <a href="type.SpecString.html" class="type"
title="type vstd::contrib::exec_spec::SpecString">SpecString</a>

</div>

<div class="impl-items">

<div id="associatedtype.ExecOwnedType-15"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#213"
class="src rightside">Source</a><a href="#associatedtype.ExecOwnedType-15" class="anchor">§</a>

#### type <a href="#associatedtype.ExecOwnedType"
class="associatedtype">ExecOwnedType</a> = <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div id="associatedtype.ExecRefType-15"
class="section associatedtype trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#215"
class="src rightside">Source</a><a href="#associatedtype.ExecRefType-15" class="anchor">§</a>

#### type <a href="#associatedtype.ExecRefType"
class="associatedtype">ExecRefType</a>\<'a\> = &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

</div>

</div>

</div>

</div>
