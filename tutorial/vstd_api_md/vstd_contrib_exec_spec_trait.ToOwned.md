<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">ToOwned</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#19-24"
class="src">Source</a> </span>

</div>

``` rust
pub trait ToOwned<T: Sized + DeepView>: Sized + DeepView<V = T::V> {
    // Required method
    fn get_owned(self) -> T;
}
```

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.get_owned" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#20-23"
class="src rightside">Source</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> T

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

<div id="impl-ToOwned%3Cbool%3E-for-bool" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cbool%3E-for-bool" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="method.get_owned" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-ToOwned%3Cchar%3E-for-char" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cchar%3E-for-char" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="method.get_owned-1" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-1" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

</div>

<div id="impl-ToOwned%3Ci8%3E-for-i8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Ci8%3E-for-i8" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="method.get_owned-2" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-2" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

</div>

<div id="impl-ToOwned%3Ci16%3E-for-i16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Ci16%3E-for-i16" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="method.get_owned-3" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-3" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

</div>

<div id="impl-ToOwned%3Ci32%3E-for-i32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Ci32%3E-for-i32" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="method.get_owned-4" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-4" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

</div>

<div id="impl-ToOwned%3Ci64%3E-for-i64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Ci64%3E-for-i64" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="method.get_owned-5" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-5" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

</div>

<div id="impl-ToOwned%3Ci128%3E-for-i128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Ci128%3E-for-i128" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="method.get_owned-6" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-6" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

</div>

<div id="impl-ToOwned%3Cisize%3E-for-isize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cisize%3E-for-isize" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="method.get_owned-7" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-7" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

</div>

<div id="impl-ToOwned%3Cu8%3E-for-u8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cu8%3E-for-u8" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="method.get_owned-8" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-8" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

</div>

<div id="impl-ToOwned%3Cu16%3E-for-u16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cu16%3E-for-u16" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="method.get_owned-9" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-9" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

</div>

<div id="impl-ToOwned%3Cu32%3E-for-u32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cu32%3E-for-u32" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="method.get_owned-10" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-10" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

</div>

<div id="impl-ToOwned%3Cu64%3E-for-u64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cu64%3E-for-u64" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="method.get_owned-11" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-11" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

</div>

<div id="impl-ToOwned%3Cu128%3E-for-u128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cu128%3E-for-u128" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="method.get_owned-12" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-12" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

</div>

<div id="impl-ToOwned%3Cusize%3E-for-usize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-ToOwned%3Cusize%3E-for-usize" class="anchor">§</a>

### impl <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="method.get_owned-13" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.get_owned-13" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

<div id="impl-ToOwned%3CString%3E-for-%26str" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#225-231"
class="src rightside">Source</a><a href="#impl-ToOwned%3CString%3E-for-%26str" class="anchor">§</a>

### impl\<'a\> <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="method.get_owned-14" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#228-230"
class="src rightside">Source</a><a href="#method.get_owned-14" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

</div>

<div id="impl-ToOwned%3C(T1,+T2)%3E-for-%26(T1,+T2)"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#179-187"
class="src rightside">Source</a><a href="#impl-ToOwned%3C(T1,+T2)%3E-for-%26(T1,+T2)"
class="anchor">§</a>

### impl\<'a, T1: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a> + <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>, T2: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a> + <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>\> <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

</div>

<div class="impl-items">

<div id="method.get_owned-15" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#184-186"
class="src rightside">Source</a><a href="#method.get_owned-15" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

</div>

</div>

<div id="impl-ToOwned%3COption%3CT%3E%3E-for-%26Option%3CT%3E"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#141-146"
class="src rightside">Source</a><a href="#impl-ToOwned%3COption%3CT%3E%3E-for-%26Option%3CT%3E"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a> + <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>\> <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="method.get_owned-16" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#143-145"
class="src rightside">Source</a><a href="#method.get_owned-16" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

</div>

<div id="impl-ToOwned%3CVec%3CT%3E%3E-for-%26%5BT%5D"
class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#292-299"
class="src rightside">Source</a><a href="#impl-ToOwned%3CVec%3CT%3E%3E-for-%26%5BT%5D"
class="anchor">§</a>

### impl\<'a, T: <a href="../../view/trait.DeepView.html" class="trait"
title="trait vstd::view::DeepView">DeepView</a> + <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>\> <a href="trait.ToOwned.html" class="trait"
title="trait vstd::contrib::exec_spec::ToOwned">ToOwned</a>\<<a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>\> for &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

</div>

<div class="impl-items">

<div id="method.get_owned-17" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#296-298"
class="src rightside">Source</a><a href="#method.get_owned-17" class="anchor">§</a>

#### fn <a href="#tymethod.get_owned" class="fn">get_owned</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

</div>

<div class="docblock">

TODO: verify this

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
