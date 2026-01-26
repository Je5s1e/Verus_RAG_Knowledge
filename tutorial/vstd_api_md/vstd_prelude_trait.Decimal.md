<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[prelude](index.html)

</div>

# Trait <span class="trait">Decimal</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin/lib.rs.html#935" class="src">Source</a>
</span>

</div>

``` rust
pub unsafe trait Decimal: Copy {
    const CONST_DEFAULT: Self;
}
```

## Required Associated Constants<a href="#required-associated-consts" class="anchor">§</a>

<div class="methods">

<div id="associatedconstant.CONST_DEFAULT" class="section method">

<a href="../../src/verus_builtin/lib.rs.html#936"
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

<div id="impl-Decimal-for-f32" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#942"
class="src rightside">Source</a><a href="#impl-Decimal-for-f32" class="anchor">§</a>

### impl <a href="trait.Decimal.html" class="trait"
title="trait vstd::prelude::Decimal">Decimal</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f32.html"
class="primitive">f32</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-1"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#944"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-1" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f32.html"
class="primitive">f32</a> = 0f32

</div>

</div>

<div id="impl-Decimal-for-f64" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#946"
class="src rightside">Source</a><a href="#impl-Decimal-for-f64" class="anchor">§</a>

### impl <a href="trait.Decimal.html" class="trait"
title="trait vstd::prelude::Decimal">Decimal</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f64.html"
class="primitive">f64</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-2"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#948"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-2" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f64.html"
class="primitive">f64</a> = 0f64

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-Decimal-for-real" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#938"
class="src rightside">Source</a><a href="#impl-Decimal-for-real" class="anchor">§</a>

### impl <a href="trait.Decimal.html" class="trait"
title="trait vstd::prelude::Decimal">Decimal</a> for <a href="struct.real.html" class="struct"
title="struct vstd::prelude::real">real</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT-3"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#940"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT-3" class="anchor">§</a>

#### const <a href="#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="struct.real.html" class="struct"
title="struct vstd::prelude::real">real</a> = real

</div>

</div>

</div>

</div>

</div>
