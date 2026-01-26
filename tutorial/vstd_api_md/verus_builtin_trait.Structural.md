<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[verus_builtin](index.html)

</div>

# Trait <span class="trait">Structural</span> Copy item path

<span class="sub-heading"><a href="../src/verus_builtin/lib.rs.html#731-734"
class="src">Source</a> </span>

</div>

``` rust
pub unsafe trait Structural { }
```

Expand description

<div class="docblock">

derive(Structural) means that exec-mode == and ghost == always yield the
same result. derive(Structural) is only allowed when all the fields of a
type are also Structural. derive(StructuralEq) means derive(Structural)
and also implement PartialEqSpec, setting eq_spec to == and
obeys_eq_spec to true.

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-Structural-for-bool" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-bool" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.bool.html"
class="primitive">bool</a>

</div>

<div id="impl-Structural-for-char" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-char" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.char.html"
class="primitive">char</a>

</div>

<div id="impl-Structural-for-i8" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-i8" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.i8.html"
class="primitive">i8</a>

</div>

<div id="impl-Structural-for-i16" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-i16" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.i16.html"
class="primitive">i16</a>

</div>

<div id="impl-Structural-for-i32" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-i32" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.i32.html"
class="primitive">i32</a>

</div>

<div id="impl-Structural-for-i64" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-i64" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.i64.html"
class="primitive">i64</a>

</div>

<div id="impl-Structural-for-i128" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-i128" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.i128.html"
class="primitive">i128</a>

</div>

<div id="impl-Structural-for-isize" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-isize" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.isize.html"
class="primitive">isize</a>

</div>

<div id="impl-Structural-for-u8" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-u8" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u8.html"
class="primitive">u8</a>

</div>

<div id="impl-Structural-for-u16" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-u16" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u16.html"
class="primitive">u16</a>

</div>

<div id="impl-Structural-for-u32" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-u32" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u32.html"
class="primitive">u32</a>

</div>

<div id="impl-Structural-for-u64" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-u64" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u64.html"
class="primitive">u64</a>

</div>

<div id="impl-Structural-for-u128" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-u128" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.u128.html"
class="primitive">u128</a>

</div>

<div id="impl-Structural-for-usize" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-usize" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.usize.html"
class="primitive">usize</a>

</div>

<div id="impl-Structural-for-%26S" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#736-741"
class="src rightside">Source</a><a href="#impl-Structural-for-%26S" class="anchor">§</a>

### impl\<S: <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> + ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>\> <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/primitive.reference.html"
class="primitive">&amp;S</a>

</div>

<div id="impl-Structural-for-Option%3CT%3E" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#764"
class="src rightside">Source</a><a href="#impl-Structural-for-Option%3CT%3E" class="anchor">§</a>

### impl\<T: <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a>\> <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Structural-for-int" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-int" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="struct.int.html" class="struct"
title="struct verus_builtin::int">int</a>

</div>

<div id="impl-Structural-for-nat" class="section impl">

<a href="../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-nat" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait verus_builtin::Structural">Structural</a> for <a href="struct.nat.html" class="struct"
title="struct verus_builtin::nat">nat</a>

</div>

</div>

</div>

</div>
