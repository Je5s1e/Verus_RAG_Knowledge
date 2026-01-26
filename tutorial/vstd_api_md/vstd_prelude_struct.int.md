<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[prelude](index.html)

</div>

# Struct <span class="struct">int</span> Copy item path

<span class="sub-heading"><a href="../../src/verus_builtin/lib.rs.html#580" class="src">Source</a>
</span>

</div>

``` rust
pub struct int;
```

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Add-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#584"
class="src rightside">Source</a><a href="#impl-Add-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Add.html"
class="trait" title="trait core::ops::arith::Add">Add</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#585"
class="src rightside">Source</a><a href="#associatedtype.Output" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Add.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

The resulting type after applying the `+` operator.

</div>

<div id="method.add" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#586"
class="src rightside">Source</a><a href="#method.add" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Add.html#tymethod.add"
class="fn">add</a>(self, \_other: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> \<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> as <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Add.html"
class="trait" title="trait core::ops::arith::Add">Add</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Add.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Add::Output">Output</a>

</div>

<div class="docblock">

Performs the `+` operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Add.html#tymethod.add)

</div>

</div>

<div id="impl-Clone-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#579"
class="src rightside">Source</a><a href="#impl-Clone-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#579"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

Returns a duplicate of the value. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone)

</div>

<div id="method.clone_from" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#245-247"
class="src">Source</a></span><a href="#method.clone_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from"
class="fn">clone_from</a>(&mut self, source: &Self)

</div>

<div class="docblock">

Performs copy-assignment from `source`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#method.clone_from)

</div>

</div>

<div id="impl-Div-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#605"
class="src rightside">Source</a><a href="#impl-Div-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Div.html"
class="trait" title="trait core::ops::arith::Div">Div</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-3"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#606"
class="src rightside">Source</a><a href="#associatedtype.Output-3" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Div.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

The resulting type after applying the `/` operator.

</div>

<div id="method.div" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#607"
class="src rightside">Source</a><a href="#method.div" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Div.html#tymethod.div"
class="fn">div</a>(self, \_other: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> \<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> as <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Div.html"
class="trait" title="trait core::ops::arith::Div">Div</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Div.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Div::Output">Output</a>

</div>

<div class="docblock">

Performs the `/` operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Div.html#tymethod.div)

</div>

</div>

<div id="impl-Integer-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#914"
class="src rightside">Source</a><a href="#impl-Integer-for-int" class="anchor">§</a>

### impl <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedconstant.CONST_DEFAULT"
class="section associatedconstant trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#916"
class="src rightside">Source</a><a href="#associatedconstant.CONST_DEFAULT" class="anchor">§</a>

#### const <a href="trait.Integer.html#associatedconstant.CONST_DEFAULT"
class="constant">CONST_DEFAULT</a>: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> = int

</div>

</div>

<div id="impl-Mul-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#598"
class="src rightside">Source</a><a href="#impl-Mul-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Mul.html"
class="trait" title="trait core::ops::arith::Mul">Mul</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-2"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#599"
class="src rightside">Source</a><a href="#associatedtype.Output-2" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Mul.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

The resulting type after applying the `*` operator.

</div>

<div id="method.mul" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#600"
class="src rightside">Source</a><a href="#method.mul" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Mul.html#tymethod.mul"
class="fn">mul</a>(self, \_other: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> \<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> as <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Mul.html"
class="trait" title="trait core::ops::arith::Mul">Mul</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Mul.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Mul::Output">Output</a>

</div>

<div class="docblock">

Performs the `*` operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Mul.html#tymethod.mul)

</div>

</div>

<div id="impl-Neg-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#619"
class="src rightside">Source</a><a href="#impl-Neg-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Neg.html"
class="trait" title="trait core::ops::arith::Neg">Neg</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-5"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#620"
class="src rightside">Source</a><a href="#associatedtype.Output-5" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Neg.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

The resulting type after applying the `-` operator.

</div>

<div id="method.neg" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#621"
class="src rightside">Source</a><a href="#method.neg" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Neg.html#tymethod.neg"
class="fn">neg</a>(self) -\> \<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> as <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Neg.html"
class="trait" title="trait core::ops::arith::Neg">Neg</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Neg.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Neg::Output">Output</a>

</div>

<div class="docblock">

Performs the unary `-` operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Neg.html#tymethod.neg)

</div>

</div>

<div id="impl-Ord-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#640"
class="src rightside">Source</a><a href="#impl-Ord-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html"
class="trait" title="trait core::cmp::Ord">Ord</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="method.cmp" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#641"
class="src rightside">Source</a><a href="#method.cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#tymethod.cmp"
class="fn">cmp</a>(&self, \_other: &<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>

</div>

<div class="docblock">

This method returns an
[`Ordering`](https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html "enum core::cmp::Ordering")
between `self` and `other`. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#tymethod.cmp)

</div>

<div id="method.max" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.21.0">1.21.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1021-1023"
class="src">Source</a></span><a href="#method.max" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.max"
class="fn">max</a>(self, other: Self) -\> Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Compares and returns the maximum of two values. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.max)

</div>

<div id="method.min" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.21.0">1.21.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1060-1062"
class="src">Source</a></span><a href="#method.min" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.min"
class="fn">min</a>(self, other: Self) -\> Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Compares and returns the minimum of two values. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.min)

</div>

<div id="method.clamp" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.50.0">1.50.0</span> · <a
href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1086-1088"
class="src">Source</a></span><a href="#method.clamp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.clamp"
class="fn">clamp</a>(self, min: Self, max: Self) -\> Self

<div class="where">

where Self:
<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="docblock">

Restrict a value to a certain interval. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.Ord.html#method.clamp)

</div>

</div>

<div id="impl-PartialEq-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#626"
class="src rightside">Source</a><a href="#impl-PartialEq-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html"
class="trait" title="trait core::cmp::PartialEq">PartialEq</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="method.eq" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#627"
class="src rightside">Source</a><a href="#method.eq" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#tymethod.eq"
class="fn">eq</a>(&self, \_other: &<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `self` and `other` values to be equal, and is used by `==`.

</div>

<div id="method.ne" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#264"
class="src">Source</a></span><a href="#method.ne" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialEq.html#method.ne"
class="fn">ne</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests for `!=`. The default implementation is almost always sufficient,
and should not be overridden without very good reason.

</div>

</div>

<div id="impl-PartialOrd-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#634"
class="src rightside">Source</a><a href="#impl-PartialOrd-for-int" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html"
class="trait" title="trait core::cmp::PartialOrd">PartialOrd</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="method.partial_cmp" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#635"
class="src rightside">Source</a><a href="#method.partial_cmp" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#tymethod.partial_cmp"
class="fn">partial_cmp</a>(&self, \_other: &<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="https://doc.rust-lang.org/1.92.0/core/cmp/enum.Ordering.html"
class="enum" title="enum core::cmp::Ordering">Ordering</a>\>

</div>

<div class="docblock">

This method returns an ordering between `self` and `other` values if one
exists. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#tymethod.partial_cmp)

</div>

<div id="method.lt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1398"
class="src">Source</a></span><a href="#method.lt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.lt"
class="fn">lt</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests less than (for `self` and `other`) and is used by the `<`
operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.lt)

</div>

<div id="method.le" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1416"
class="src">Source</a></span><a href="#method.le" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.le"
class="fn">le</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests less than or equal to (for `self` and `other`) and is used by the
`<=` operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.le)

</div>

<div id="method.gt" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1434"
class="src">Source</a></span><a href="#method.gt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.gt"
class="fn">gt</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests greater than (for `self` and `other`) and is used by the `>`
operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.gt)

</div>

<div id="method.ge" class="section method trait-impl">

<span class="rightside"><span class="since"
title="Stable since Rust version 1.0.0">1.0.0</span> ·
<a href="https://doc.rust-lang.org/1.92.0/src/core/cmp.rs.html#1452"
class="src">Source</a></span><a href="#method.ge" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.ge"
class="fn">ge</a>(&self, other: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;Rhs</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="docblock">

Tests greater than or equal to (for `self` and `other`) and is used by
the `>=` operator. [Read
more](https://doc.rust-lang.org/1.92.0/core/cmp/trait.PartialOrd.html#method.ge)

</div>

</div>

<div id="impl-Rem-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#612"
class="src rightside">Source</a><a href="#impl-Rem-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Rem.html"
class="trait" title="trait core::ops::arith::Rem">Rem</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-4"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#613"
class="src rightside">Source</a><a href="#associatedtype.Output-4" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Rem.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

The resulting type after applying the `%` operator.

</div>

<div id="method.rem" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#614"
class="src rightside">Source</a><a href="#method.rem" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Rem.html#tymethod.rem"
class="fn">rem</a>(self, \_other: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> \<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> as <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Rem.html"
class="trait" title="trait core::ops::arith::Rem">Rem</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Rem.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Rem::Output">Output</a>

</div>

<div class="docblock">

Performs the `%` operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Rem.html#tymethod.rem)

</div>

</div>

<div id="impl-SpecAdd%3CRhs%3E-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1367-1371"
class="src rightside">Source</a><a href="#impl-SpecAdd%3CRhs%3E-for-int" class="anchor">§</a>

### impl\<Rhs\> <a href="trait.SpecAdd.html" class="trait"
title="trait vstd::prelude::SpecAdd">SpecAdd</a>\<Rhs\> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

<div class="where">

where Rhs: <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Output-7"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1367-1371"
class="src rightside">Source</a><a href="#associatedtype.Output-7" class="anchor">§</a>

#### type <a href="trait.SpecAdd.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecAdd%3Cint%3E-for-nat" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1375-1379"
class="src rightside">Source</a><a href="#impl-SpecAdd%3Cint%3E-for-nat" class="anchor">§</a>

### impl <a href="trait.SpecAdd.html" class="trait"
title="trait vstd::prelude::SpecAdd">SpecAdd</a>\<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>\> for <a href="struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-8"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1375-1379"
class="src rightside">Source</a><a href="#associatedtype.Output-8" class="anchor">§</a>

#### type <a href="trait.SpecAdd.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecEuclideanMod-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1410-1414"
class="src rightside">Source</a><a href="#impl-SpecEuclideanMod-for-int" class="anchor">§</a>

### impl <a href="trait.SpecEuclideanMod.html" class="trait"
title="trait vstd::prelude::SpecEuclideanMod">SpecEuclideanMod</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-13"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1410-1414"
class="src rightside">Source</a><a href="#associatedtype.Output-13" class="anchor">§</a>

#### type <a href="trait.SpecEuclideanMod.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecEuclideanOrRealDiv-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1401-1404"
class="src rightside">Source</a><a href="#impl-SpecEuclideanOrRealDiv-for-int" class="anchor">§</a>

### impl <a href="trait.SpecEuclideanOrRealDiv.html" class="trait"
title="trait vstd::prelude::SpecEuclideanOrRealDiv">SpecEuclideanOrRealDiv</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-12"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1401-1404"
class="src rightside">Source</a><a href="#associatedtype.Output-12" class="anchor">§</a>

#### type <a href="trait.SpecEuclideanOrRealDiv.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecMul%3CRhs%3E-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1387-1391"
class="src rightside">Source</a><a href="#impl-SpecMul%3CRhs%3E-for-int" class="anchor">§</a>

### impl\<Rhs\> <a href="trait.SpecMul.html" class="trait"
title="trait vstd::prelude::SpecMul">SpecMul</a>\<Rhs\> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

<div class="where">

where Rhs: <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Output-10"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1387-1391"
class="src rightside">Source</a><a href="#associatedtype.Output-10" class="anchor">§</a>

#### type <a href="trait.SpecMul.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecMul%3Cint%3E-for-nat" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1395-1399"
class="src rightside">Source</a><a href="#impl-SpecMul%3Cint%3E-for-nat" class="anchor">§</a>

### impl <a href="trait.SpecMul.html" class="trait"
title="trait vstd::prelude::SpecMul">SpecMul</a>\<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>\> for <a href="struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-11"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1395-1399"
class="src rightside">Source</a><a href="#associatedtype.Output-11" class="anchor">§</a>

#### type <a href="trait.SpecMul.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecNeg-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1359-1363"
class="src rightside">Source</a><a href="#impl-SpecNeg-for-int" class="anchor">§</a>

### impl <a href="trait.SpecNeg.html" class="trait"
title="trait vstd::prelude::SpecNeg">SpecNeg</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-6"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1359-1363"
class="src rightside">Source</a><a href="#associatedtype.Output-6" class="anchor">§</a>

#### type <a href="trait.SpecNeg.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-SpecSub%3CRhs%3E-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1381-1385"
class="src rightside">Source</a><a href="#impl-SpecSub%3CRhs%3E-for-int" class="anchor">§</a>

### impl\<Rhs\> <a href="trait.SpecSub.html" class="trait"
title="trait vstd::prelude::SpecSub">SpecSub</a>\<Rhs\> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

<div class="where">

where Rhs: <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Output-9"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#1381-1385"
class="src rightside">Source</a><a href="#associatedtype.Output-9" class="anchor">§</a>

#### type <a href="trait.SpecSub.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

<div id="impl-Sub-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#591"
class="src rightside">Source</a><a href="#impl-Sub-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html"
class="trait" title="trait core::ops::arith::Sub">Sub</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="impl-items">

<div id="associatedtype.Output-1"
class="section associatedtype trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#592"
class="src rightside">Source</a><a href="#associatedtype.Output-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#associatedtype.Output"
class="associatedtype">Output</a> = <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div class="docblock">

The resulting type after applying the `-` operator.

</div>

<div id="method.sub" class="section method trait-impl">

<a href="../../src/verus_builtin/lib.rs.html#593"
class="src rightside">Source</a><a href="#method.sub" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#tymethod.sub"
class="fn">sub</a>(self, \_other: <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>) -\> \<<a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a> as <a href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html"
class="trait" title="trait core::ops::arith::Sub">Sub</a>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#associatedtype.Output"
class="associatedtype"
title="type core::ops::arith::Sub::Output">Output</a>

</div>

<div class="docblock">

Performs the `-` operation. [Read
more](https://doc.rust-lang.org/1.92.0/core/ops/arith/trait.Sub.html#tymethod.sub)

</div>

</div>

<div id="impl-Copy-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#579"
class="src rightside">Source</a><a href="#impl-Copy-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Copy.html"
class="trait" title="trait core::marker::Copy">Copy</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-Eq-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#632"
class="src rightside">Source</a><a href="#impl-Eq-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-SpecOrd%3CRhs%3E-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#1350-1355"
class="src rightside">Source</a><a href="#impl-SpecOrd%3CRhs%3E-for-int" class="anchor">§</a>

### impl\<Rhs\> <a href="trait.SpecOrd.html" class="trait"
title="trait vstd::prelude::SpecOrd">SpecOrd</a>\<Rhs\> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

<div class="where">

where Rhs: <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a>,

</div>

</div>

<div id="impl-Structural-for-int" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#756-762"
class="src rightside">Source</a><a href="#impl-Structural-for-int" class="anchor">§</a>

### impl <a href="trait.Structural.html" class="trait"
title="trait vstd::prelude::Structural">Structural</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-int" class="section impl">

<a href="#impl-Freeze-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-RefUnwindSafe-for-int" class="section impl">

<a href="#impl-RefUnwindSafe-for-int" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-Send-for-int" class="section impl">

<a href="#impl-Send-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-Sync-for-int" class="section impl">

<a href="#impl-Sync-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-Unpin-for-int" class="section impl">

<a href="#impl-Unpin-for-int" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

<div id="impl-UnwindSafe-for-int" class="section impl">

<a href="#impl-UnwindSafe-for-int" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>

</div>

</div>

## Blanket Implementations<a href="#blanket-implementations" class="anchor">§</a>

<div id="blanket-implementations-list">

<div id="impl-Any-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#138"
class="src rightside">Source</a><a href="#impl-Any-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html"
class="trait" title="trait core::any::Any">Any</a> for T

<div class="where">

where T: 'static +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.type_id" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/any.rs.html#139"
class="src rightside">Source</a><a href="#method.type_id" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id"
class="fn">type_id</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/any/struct.TypeId.html"
class="struct" title="struct core::any::TypeId">TypeId</a>

</div>

<div class="docblock">

Gets the `TypeId` of `self`. [Read
more](https://doc.rust-lang.org/1.92.0/core/any/trait.Any.html#tymethod.type_id)

</div>

</div>

<div id="impl-Borrow%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#212"
class="src rightside">Source</a><a href="#impl-Borrow%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html"
class="trait" title="trait core::borrow::Borrow">Borrow</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#214"
class="src rightside">Source</a><a href="#method.borrow" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow"
class="fn">borrow</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;T</a>

</div>

<div class="docblock">

Immutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.Borrow.html#tymethod.borrow)

</div>

</div>

<div id="impl-BorrowMut%3CT%3E-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#221"
class="src rightside">Source</a><a href="#impl-BorrowMut%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html"
class="trait" title="trait core::borrow::BorrowMut">BorrowMut</a>\<T\> for T

<div class="where">

where T:
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.borrow_mut" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/borrow.rs.html#222"
class="src rightside">Source</a><a href="#method.borrow_mut" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut"
class="fn">borrow_mut</a>(&mut self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>

</div>

<div class="docblock">

Mutably borrows from an owned value. [Read
more](https://doc.rust-lang.org/1.92.0/core/borrow/trait.BorrowMut.html#tymethod.borrow_mut)

</div>

</div>

<div id="impl-CloneToUninit-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#515"
class="src rightside">Source</a><a href="#impl-CloneToUninit-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html"
class="trait" title="trait core::clone::CloneToUninit">CloneToUninit</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="method.clone_to_uninit" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/core/clone.rs.html#517"
class="src rightside">Source</a><a href="#method.clone_to_uninit" class="anchor">§</a>

#### unsafe fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit"
class="fn">clone_to_uninit</a>(&self, dest: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.pointer.html"
class="primitive">*mut</a> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`clone_to_uninit`)

</div>

<div class="docblock">

Performs copy-assignment from `self` to `dest`. [Read
more](https://doc.rust-lang.org/1.92.0/core/clone/trait.CloneToUninit.html#tymethod.clone_to_uninit)

</div>

</div>

<div id="impl-From%3CT%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#785"
class="src rightside">Source</a><a href="#impl-From%3CT%3E-for-T" class="anchor">§</a>

### impl\<T\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\> for T

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(t: T) -\> T

</div>

<div class="docblock">

Returns the argument unchanged.

</div>

</div>

<div id="impl-Into%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#767-769"
class="src rightside">Source</a><a href="#impl-Into%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="method.into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#777"
class="src rightside">Source</a><a href="#method.into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html#tymethod.into"
class="fn">into</a>(self) -\> U

</div>

<div class="docblock">

Calls `U::from(self)`.

That is, this conversion is whatever the implementation of
[`From`](https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html "trait core::convert::From")`<T> for U`
chooses to do.

</div>

</div>

<div id="impl-ToOwned-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#85-87"
class="src rightside">Source</a><a href="#impl-ToOwned-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html"
class="trait" title="trait alloc::borrow::ToOwned">ToOwned</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Owned"
class="section associatedtype trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#89"
class="src rightside">Source</a><a href="#associatedtype.Owned" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#associatedtype.Owned"
class="associatedtype">Owned</a> = T

</div>

<div class="docblock">

The resulting type after obtaining ownership.

</div>

<div id="method.to_owned" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#90"
class="src rightside">Source</a><a href="#method.to_owned" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned"
class="fn">to_owned</a>(&self) -\> T

</div>

<div class="docblock">

Creates owned data from borrowed data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#tymethod.to_owned)

</div>

<div id="method.clone_into" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/borrow.rs.html#94"
class="src rightside">Source</a><a href="#method.clone_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into"
class="fn">clone_into</a>(&self, target: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;mut T</a>)

</div>

<div class="docblock">

Uses borrowed data to replace owned data, usually by cloning. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/borrow/trait.ToOwned.html#method.clone_into)

</div>

</div>

<div id="impl-TryFrom%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#827-829"
class="src rightside">Source</a><a href="#impl-TryFrom%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\> for T

<div class="where">

where U:
<a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.Into.html"
class="trait" title="trait core::convert::Into">Into</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error-1"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#831"
class="src rightside">Source</a><a href="#associatedtype.Error-1" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype">Error</a> = <a
href="https://doc.rust-lang.org/1.92.0/core/convert/enum.Infallible.html"
class="enum" title="enum core::convert::Infallible">Infallible</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_from" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#834"
class="src rightside">Source</a><a href="#method.try_from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#tymethod.try_from"
class="fn">try_from</a>(value: U) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<T, \<T as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<U\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-TryInto%3CU%3E-for-T" class="section impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#811-813"
class="src rightside">Source</a><a href="#impl-TryInto%3CU%3E-for-T" class="anchor">§</a>

### impl\<T, U\> <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html"
class="trait" title="trait core::convert::TryInto">TryInto</a>\<U\> for T

<div class="where">

where U: <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.Error"
class="section associatedtype trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#815"
class="src rightside">Source</a><a href="#associatedtype.Error" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#associatedtype.Error"
class="associatedtype">Error</a> = \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>

</div>

<div class="docblock">

The type returned in the event of a conversion error.

</div>

<div id="method.try_into" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#818"
class="src rightside">Source</a><a href="#method.try_into" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryInto.html#tymethod.try_into"
class="fn">try_into</a>(self) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<U, \<U as <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html"
class="trait" title="trait core::convert::TryFrom">TryFrom</a>\<T\>\>::<a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.TryFrom.html#associatedtype.Error"
class="associatedtype"
title="type core::convert::TryFrom::Error">Error</a>\>

</div>

<div class="docblock">

Performs the conversion.

</div>

</div>

<div id="impl-Chainable-for-T" class="section impl">

<a href="../../src/verus_builtin/lib.rs.html#954"
class="src rightside">Source</a><a href="#impl-Chainable-for-T" class="anchor">§</a>

### impl\<T\> <a href="trait.Chainable.html" class="trait"
title="trait vstd::prelude::Chainable">Chainable</a> for T

<div class="where">

where T: <a href="trait.Integer.html" class="trait"
title="trait vstd::prelude::Integer">Integer</a>,

</div>

</div>

</div>

</div>

</div>
