<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[prelude](index.html)

</div>

# Trait <span class="trait">Integer</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin/lib.rs.html#863" class="src">Source</a>
</span>

</div>

``` rust
pub unsafe trait Integer: Copy {
    const CONST_DEFAULT: Self;
}
```

## Required Associated Constants<a href="#required-associated-consts" class="anchor">§</a>

<div class="methods">

<div id="associatedconstant.CONST_DEFAULT" class="section method">

<a href="../../src/verus_builtin/lib.rs.html#864"
class="src rightside">Source</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: Self

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

<div id="impl-Integer-for-char" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#922"
class="src rightside">Source</a><a href="#impl-Integer-for-char" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-1"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#924"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-1" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a> = ' '

</div>

</div>

<div id="impl-Integer-for-i8" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#890"
class="src rightside">Source</a><a href="#impl-Integer-for-i8" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-2"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#892"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-2" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a> = 0i8

</div>

</div>

<div id="impl-Integer-for-i16" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#894"
class="src rightside">Source</a><a href="#impl-Integer-for-i16" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-3"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#896"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-3" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a> = 0i16

</div>

</div>

<div id="impl-Integer-for-i32" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#898"
class="src rightside">Source</a><a href="#impl-Integer-for-i32" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-4"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#900"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-4" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a> = 0i32

</div>

</div>

<div id="impl-Integer-for-i64" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#902"
class="src rightside">Source</a><a href="#impl-Integer-for-i64" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-5"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#904"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-5" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a> = 0i64

</div>

</div>

<div id="impl-Integer-for-i128" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#906"
class="src rightside">Source</a><a href="#impl-Integer-for-i128" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-6"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#908"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-6" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a> = 0i128

</div>

</div>

<div id="impl-Integer-for-isize" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#910"
class="src rightside">Source</a><a href="#impl-Integer-for-isize" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-7"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#912"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-7" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a> = 0isize

</div>

</div>

<div id="impl-Integer-for-u8" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#866"
class="src rightside">Source</a><a href="#impl-Integer-for-u8" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-8"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#868"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-8" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a> = 0u8

</div>

</div>

<div id="impl-Integer-for-u16" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#870"
class="src rightside">Source</a><a href="#impl-Integer-for-u16" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-9"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#872"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-9" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a> = 0u16

</div>

</div>

<div id="impl-Integer-for-u32" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#874"
class="src rightside">Source</a><a href="#impl-Integer-for-u32" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-10"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#876"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-10" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a> = 0u32

</div>

</div>

<div id="impl-Integer-for-u64" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#878"
class="src rightside">Source</a><a href="#impl-Integer-for-u64" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-11"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#880"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-11" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a> = 0u64

</div>

</div>

<div id="impl-Integer-for-u128" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#882"
class="src rightside">Source</a><a href="#impl-Integer-for-u128" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-12"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#884"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-12" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a> = 0u128

</div>

</div>

<div id="impl-Integer-for-usize" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#886"
class="src rightside">Source</a><a href="#impl-Integer-for-usize" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-13"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#888"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-13" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a> = 0usize

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Integer-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#914"
class="src rightside">Source</a><a href="#impl-Integer-for-int" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-14"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#916"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-14" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> = int

</div>

</div>

<div id="impl-Integer-for-nat" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#918"
class="src rightside">Source</a><a href="#impl-Integer-for-nat" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-15"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#920"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-15" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a> = nat

</div>

</div>

</div>

</div>

</div>
