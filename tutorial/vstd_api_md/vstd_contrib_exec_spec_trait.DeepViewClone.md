<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../../index.html)::[contrib](../index.html)::[exec_spec](index.html)

</div>

# Trait <span class="trait">DeepViewClone</span> Copy item path

<span class="sub-heading"><a href="../../../src/vstd/contrib/exec_spec.rs.html#27-32"
class="src">Source</a> </span>

</div>

``` rust
pub trait DeepViewClone: Sized + DeepView {
    // Required method
    fn deep_clone(&self) -> Self;
}
```

Expand description

<div class="docblock">

Cloned objects have the same deep view

</div>

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.deep_clone" class="section method">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#28-31"
class="src rightside">Source</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

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

<div id="impl-DeepViewClone-for-bool" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-bool" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="method.deep_clone" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-char" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-char" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-1" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-1" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-i8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-i8" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-2" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-2" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-i16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-i16" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-3" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-3" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-i32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-i32" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-4" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-4" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-i64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-i64" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-5" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-5" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-i128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-i128" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-6" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-6" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-isize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-isize" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-7" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-7" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-u8" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-u8" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-8" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-8" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-u16" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-u16" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-9" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-9" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-u32" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-u32" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-10" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-10" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-u64" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-u64" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-11" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-11" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-u128" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-u128" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-12" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-12" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-usize" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-usize" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-13" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#128-132"
class="src rightside">Source</a><a href="#method.deep_clone-13" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-String" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#233-238"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-String" class="anchor">§</a>

### impl <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-14" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#235-237"
class="src rightside">Source</a><a href="#method.deep_clone-14" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-(T1,+T2)" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#189-194"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-(T1,+T2)" class="anchor">§</a>

### impl\<T1: <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>, T2: <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>\> <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(T1, T2)</a>

</div>

<div class="impl-items">

<div id="method.deep_clone-15" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#191-193"
class="src rightside">Source</a><a href="#method.deep_clone-15" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-Option%3CT%3E" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#148-156"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-Option%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>\> <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="method.deep_clone-16" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#150-155"
class="src rightside">Source</a><a href="#method.deep_clone-16" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

</div>

</div>

<div id="impl-DeepViewClone-for-Vec%3CT%3E" class="section impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#301-308"
class="src rightside">Source</a><a href="#impl-DeepViewClone-for-Vec%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a>\> <a href="trait.DeepViewClone.html" class="trait"
title="trait vstd::contrib::exec_spec::DeepViewClone">DeepViewClone</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

</div>

<div class="impl-items">

<div id="method.deep_clone-17" class="section method trait-impl">

<a href="../../../src/vstd/contrib/exec_spec.rs.html#305-307"
class="src rightside">Source</a><a href="#method.deep_clone-17" class="anchor">§</a>

#### fn <a href="#tymethod.deep_clone" class="fn">deep_clone</a>(&self) -\> Self

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
