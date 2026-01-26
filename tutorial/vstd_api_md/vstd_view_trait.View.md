<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[view](index.html)

</div>

# Trait <span class="trait">View</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/view.rs.html#10-14" class="src">Source</a>
</span>

</div>

``` rust
pub trait View {
    type V;
}
```

Expand description

<div class="docblock">

Types used in executable code can implement View to provide a
mathematical abstraction of the type. For example, Vec implements a view
method that returns a Seq. For base types like bool and u8, the view V
of the type is the type itself. Types only used in ghost code, such as
int, nat, and Seq, do not need to implement View.

</div>

## Required Associated Types<a href="#required-associated-types" class="anchor">§</a>

<div class="methods">

<div id="associatedtype.V" class="section method">

<a href="../../src/vstd/view.rs.html#11"
class="src rightside">Source</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a>

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-View-for-bool" class="section impl">

<a href="../../src/vstd/view.rs.html#188"
class="src rightside">Source</a><a href="#impl-View-for-bool" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-1" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#188"
class="src rightside">Source</a><a href="#associatedtype.V-1" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.bool.html"
class="primitive">bool</a>

</div>

</div>

<div id="impl-View-for-char" class="section impl">

<a href="../../src/vstd/view.rs.html#214"
class="src rightside">Source</a><a href="#impl-View-for-char" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-2" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#214"
class="src rightside">Source</a><a href="#associatedtype.V-2" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

</div>

<div id="impl-View-for-i8" class="section impl">

<a href="../../src/vstd/view.rs.html#202"
class="src rightside">Source</a><a href="#impl-View-for-i8" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-3" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#202"
class="src rightside">Source</a><a href="#associatedtype.V-3" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>

</div>

</div>

<div id="impl-View-for-i16" class="section impl">

<a href="../../src/vstd/view.rs.html#204"
class="src rightside">Source</a><a href="#impl-View-for-i16" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-4" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#204"
class="src rightside">Source</a><a href="#associatedtype.V-4" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>

</div>

</div>

<div id="impl-View-for-i32" class="section impl">

<a href="../../src/vstd/view.rs.html#206"
class="src rightside">Source</a><a href="#impl-View-for-i32" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-5" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#206"
class="src rightside">Source</a><a href="#associatedtype.V-5" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>

</div>

</div>

<div id="impl-View-for-i64" class="section impl">

<a href="../../src/vstd/view.rs.html#208"
class="src rightside">Source</a><a href="#impl-View-for-i64" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-6" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#208"
class="src rightside">Source</a><a href="#associatedtype.V-6" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>

</div>

</div>

<div id="impl-View-for-i128" class="section impl">

<a href="../../src/vstd/view.rs.html#210"
class="src rightside">Source</a><a href="#impl-View-for-i128" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-7" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#210"
class="src rightside">Source</a><a href="#associatedtype.V-7" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>

</div>

</div>

<div id="impl-View-for-isize" class="section impl">

<a href="../../src/vstd/view.rs.html#212"
class="src rightside">Source</a><a href="#impl-View-for-isize" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-8" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#212"
class="src rightside">Source</a><a href="#associatedtype.V-8" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>

</div>

</div>

<div id="impl-View-for-str" class="section impl">

<a href="../../src/vstd/string.rs.html#17-21"
class="src rightside">Source</a><a href="#impl-View-for-str" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-9" class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#18"
class="src rightside">Source</a><a href="#associatedtype.V-9" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>

</div>

</div>

<div id="impl-View-for-u8" class="section impl">

<a href="../../src/vstd/view.rs.html#190"
class="src rightside">Source</a><a href="#impl-View-for-u8" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-10" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#190"
class="src rightside">Source</a><a href="#associatedtype.V-10" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

</div>

<div id="impl-View-for-u16" class="section impl">

<a href="../../src/vstd/view.rs.html#192"
class="src rightside">Source</a><a href="#impl-View-for-u16" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-11" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#192"
class="src rightside">Source</a><a href="#associatedtype.V-11" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>

</div>

</div>

<div id="impl-View-for-u32" class="section impl">

<a href="../../src/vstd/view.rs.html#194"
class="src rightside">Source</a><a href="#impl-View-for-u32" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-12" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#194"
class="src rightside">Source</a><a href="#associatedtype.V-12" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>

</div>

</div>

<div id="impl-View-for-u64" class="section impl">

<a href="../../src/vstd/view.rs.html#196"
class="src rightside">Source</a><a href="#impl-View-for-u64" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-13" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#196"
class="src rightside">Source</a><a href="#associatedtype.V-13" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>

</div>

</div>

<div id="impl-View-for-u128" class="section impl">

<a href="../../src/vstd/view.rs.html#198"
class="src rightside">Source</a><a href="#impl-View-for-u128" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-14" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#198"
class="src rightside">Source</a><a href="#associatedtype.V-14" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>

</div>

</div>

<div id="impl-View-for-()" class="section impl">

<a href="../../src/vstd/view.rs.html#186"
class="src rightside">Source</a><a href="#impl-View-for-()" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-15" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#186"
class="src rightside">Source</a><a href="#associatedtype.V-15" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.unit.html"
class="primitive">()</a>

</div>

</div>

<div id="impl-View-for-usize" class="section impl">

<a href="../../src/vstd/view.rs.html#200"
class="src rightside">Source</a><a href="#impl-View-for-usize" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-16" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#200"
class="src rightside">Source</a><a href="#associatedtype.V-16" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

</div>

<div id="impl-View-for-String" class="section impl">

<a href="../../src/vstd/string.rs.html#224-228"
class="src rightside">Source</a><a href="#impl-View-for-String" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-17" class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#225"
class="src rightside">Source</a><a href="#associatedtype.V-17" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>

</div>

</div>

<div id="impl-View-for-Chars%3C'a%3E" class="section impl">

<a href="../../src/vstd/string.rs.html#368-372"
class="src rightside">Source</a><a href="#impl-View-for-Chars%3C&#39;a%3E" class="anchor">§</a>

### impl\<'a\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a
href="https://doc.rust-lang.org/1.92.0/core/str/iter/struct.Chars.html"
class="struct" title="struct core::str::iter::Chars">Chars</a>\<'a\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-18" class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#369"
class="src rightside">Source</a><a href="#associatedtype.V-18" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = (<a href="../prelude/struct.int.html" class="struct"
title="struct vstd::prelude::int">int</a>, <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>)

</div>

</div>

<div id="impl-View-for-(A0,)" class="section impl">

<a href="../../src/vstd/view.rs.html#243"
class="src rightside">Source</a><a href="#impl-View-for-(A0,)" class="anchor">§</a>

### impl\<A0: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(A0,)</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-19" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#243"
class="src rightside">Source</a><a href="#associatedtype.V-19" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = (\<A0 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>,)

</div>

</div>

<div id="impl-View-for-(A0,+A1)" class="section impl">

<a href="../../src/vstd/view.rs.html#245"
class="src rightside">Source</a><a href="#impl-View-for-(A0,+A1)" class="anchor">§</a>

### impl\<A0: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>, A1: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(A0, A1)</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-20" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#245"
class="src rightside">Source</a><a href="#associatedtype.V-20" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = (\<A0 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, \<A1 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>)

</div>

</div>

<div id="impl-View-for-(A0,+A1,+A2)" class="section impl">

<a href="../../src/vstd/view.rs.html#247"
class="src rightside">Source</a><a href="#impl-View-for-(A0,+A1,+A2)" class="anchor">§</a>

### impl\<A0: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>, A1: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>, A2: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(A0, A1, A2)</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-21" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#247"
class="src rightside">Source</a><a href="#associatedtype.V-21" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = (\<A0 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, \<A1 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, \<A2 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>)

</div>

</div>

<div id="impl-View-for-(A0,+A1,+A2,+A3)" class="section impl">

<a href="../../src/vstd/view.rs.html#249"
class="src rightside">Source</a><a href="#impl-View-for-(A0,+A1,+A2,+A3)" class="anchor">§</a>

### impl\<A0: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>, A1: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>, A2: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>, A3: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.tuple.html"
class="primitive">(A0, A1, A2, A3)</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-22" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#249"
class="src rightside">Source</a><a href="#associatedtype.V-22" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = (\<A0 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, \<A1 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, \<A2 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, \<A3 as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>)

</div>

</div>

<div id="impl-View-for-%26A" class="section impl">

<a href="../../src/vstd/view.rs.html#22-29"
class="src rightside">Source</a><a href="#impl-View-for-%26A" class="anchor">§</a>

### impl\<A: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> + ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.reference.html"
class="primitive">&amp;A</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-23" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#23"
class="src rightside">Source</a><a href="#associatedtype.V-23" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = \<A as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>

</div>

</div>

<div id="impl-View-for-Box%3CA%3E" class="section impl">

<a href="../../src/vstd/view.rs.html#41-48"
class="src rightside">Source</a><a href="#impl-View-for-Box%3CA%3E" class="anchor">§</a>

### impl\<A: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> + ?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/boxed/struct.Box.html"
class="struct" title="struct alloc::boxed::Box">Box</a>\<A\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-24" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#42"
class="src rightside">Source</a><a href="#associatedtype.V-24" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = \<A as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>

</div>

</div>

<div id="impl-View-for-Rc%3CA%3E" class="section impl">

<a href="../../src/vstd/view.rs.html#61-68"
class="src rightside">Source</a><a href="#impl-View-for-Rc%3CA%3E" class="anchor">§</a>

### impl\<A: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/rc/struct.Rc.html"
class="struct" title="struct alloc::rc::Rc">Rc</a>\<A\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-25" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#62"
class="src rightside">Source</a><a href="#associatedtype.V-25" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = \<A as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>

</div>

</div>

<div id="impl-View-for-Arc%3CA%3E" class="section impl">

<a href="../../src/vstd/view.rs.html#81-88"
class="src rightside">Source</a><a href="#impl-View-for-Arc%3CA%3E" class="anchor">§</a>

### impl\<A: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/sync/struct.Arc.html"
class="struct" title="struct alloc::sync::Arc">Arc</a>\<A\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-26" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#82"
class="src rightside">Source</a><a href="#associatedtype.V-26" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = \<A as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>

</div>

</div>

<div id="impl-View-for-Option%3CT%3E" class="section impl">

<a href="../../src/vstd/view.rs.html#137-143"
class="src rightside">Source</a><a href="#impl-View-for-Option%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

<div class="impl-items">

<div id="associatedtype.V-27" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#138"
class="src rightside">Source</a><a href="#associatedtype.V-27" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<T\>

</div>

</div>

<div id="impl-View-for-%5BT%5D" class="section impl">

<a href="../../src/vstd/slice.rs.html#12-16"
class="src rightside">Source</a><a href="#impl-View-for-%5BT%5D" class="anchor">§</a>

### impl\<T\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.slice.html"
class="primitive">[T]</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-28" class="section associatedtype trait-impl">

<a href="../../src/vstd/slice.rs.html#13"
class="src rightside">Source</a><a href="#associatedtype.V-28" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<T\>

</div>

</div>

<div id="impl-View-for-Vec%3CT%3E" class="section impl">

<a href="../../src/vstd/view.rs.html#121-125"
class="src rightside">Source</a><a href="#impl-View-for-Vec%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<T\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc` and non-`verus_keep_ghost` and
non-crate feature `allocator`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-29" class="section associatedtype trait-impl">

<a href="../../src/vstd/view.rs.html#122"
class="src rightside">Source</a><a href="#associatedtype.V-29" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<T\>

</div>

</div>

<div id="impl-View-for-%5BT;+N%5D" class="section impl">

<a href="../../src/vstd/array.rs.html#13-19"
class="src rightside">Source</a><a href="#impl-View-for-%5BT;+N%5D" class="anchor">§</a>

### impl\<T, const N: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.array.html"
class="primitive">[T; N]</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-30" class="section associatedtype trait-impl">

<a href="../../src/vstd/array.rs.html#14"
class="src rightside">Source</a><a href="#associatedtype.V-30" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<T\>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

<div id="impl-View-for-CheckedU8" class="section impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#302"
class="src rightside">Source</a><a href="#impl-View-for-CheckedU8" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../arithmetic/overflow/struct.CheckedU8.html" class="struct"
title="struct vstd::arithmetic::overflow::CheckedU8">CheckedU8</a>

<div class="docblock">

The view of an `$cty` instance is the true value of the instance.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-31" class="section associatedtype trait-impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#302"
class="src rightside">Source</a><a href="#associatedtype.V-31" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

</div>

<div id="impl-View-for-CheckedU16" class="section impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#303"
class="src rightside">Source</a><a href="#impl-View-for-CheckedU16" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../arithmetic/overflow/struct.CheckedU16.html" class="struct"
title="struct vstd::arithmetic::overflow::CheckedU16">CheckedU16</a>

<div class="docblock">

The view of an `$cty` instance is the true value of the instance.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-32" class="section associatedtype trait-impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#303"
class="src rightside">Source</a><a href="#associatedtype.V-32" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

</div>

<div id="impl-View-for-CheckedU32" class="section impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#304"
class="src rightside">Source</a><a href="#impl-View-for-CheckedU32" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../arithmetic/overflow/struct.CheckedU32.html" class="struct"
title="struct vstd::arithmetic::overflow::CheckedU32">CheckedU32</a>

<div class="docblock">

The view of an `$cty` instance is the true value of the instance.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-33" class="section associatedtype trait-impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#304"
class="src rightside">Source</a><a href="#associatedtype.V-33" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

</div>

<div id="impl-View-for-CheckedU64" class="section impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#305"
class="src rightside">Source</a><a href="#impl-View-for-CheckedU64" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../arithmetic/overflow/struct.CheckedU64.html" class="struct"
title="struct vstd::arithmetic::overflow::CheckedU64">CheckedU64</a>

<div class="docblock">

The view of an `$cty` instance is the true value of the instance.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-34" class="section associatedtype trait-impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#305"
class="src rightside">Source</a><a href="#associatedtype.V-34" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

</div>

<div id="impl-View-for-CheckedU128" class="section impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#306"
class="src rightside">Source</a><a href="#impl-View-for-CheckedU128" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../arithmetic/overflow/struct.CheckedU128.html" class="struct"
title="struct vstd::arithmetic::overflow::CheckedU128">CheckedU128</a>

<div class="docblock">

The view of an `$cty` instance is the true value of the instance.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-35" class="section associatedtype trait-impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#306"
class="src rightside">Source</a><a href="#associatedtype.V-35" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

</div>

<div id="impl-View-for-CheckedUsize" class="section impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#307"
class="src rightside">Source</a><a href="#impl-View-for-CheckedUsize" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../arithmetic/overflow/struct.CheckedUsize.html" class="struct"
title="struct vstd::arithmetic::overflow::CheckedUsize">CheckedUsize</a>

<div class="docblock">

The view of an `$cty` instance is the true value of the instance.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-36" class="section associatedtype trait-impl">

<a href="../../src/vstd/arithmetic/overflow.rs.html#307"
class="src rightside">Source</a><a href="#associatedtype.V-36" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../prelude/struct.nat.html" class="struct"
title="struct vstd::prelude::nat">nat</a>

</div>

</div>

<div id="impl-View-for-StringHashSet" class="section impl">

<a href="../../src/vstd/hash_set.rs.html#184-188"
class="src rightside">Source</a><a href="#impl-View-for-StringHashSet" class="anchor">§</a>

### impl <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../hash_set/struct.StringHashSet.html" class="struct"
title="struct vstd::hash_set::StringHashSet">StringHashSet</a>

</div>

<div class="impl-items">

<div id="associatedtype.V-37" class="section associatedtype trait-impl">

<a href="../../src/vstd/hash_set.rs.html#185"
class="src rightside">Source</a><a href="#associatedtype.V-37" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../set/struct.Set.html" class="struct"
title="struct vstd::set::Set">Set</a>\<<a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>\>

</div>

</div>

<div id="impl-View-for-CharsGhostIterator%3C'a%3E" class="section impl">

<a href="../../src/vstd/string.rs.html#463-469"
class="src rightside">Source</a><a href="#impl-View-for-CharsGhostIterator%3C&#39;a%3E"
class="anchor">§</a>

### impl\<'a\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../string/struct.CharsGhostIterator.html" class="struct"
title="struct vstd::string::CharsGhostIterator">CharsGhostIterator</a>\<'a\>

<span class="item-info"></span>

<div class="stab portability">

Available on **crate feature `alloc`** only.

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-38" class="section associatedtype trait-impl">

<a href="../../src/vstd/string.rs.html#464"
class="src rightside">Source</a><a href="#associatedtype.V-38" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>

</div>

</div>

<div id="impl-View-for-HashSetWithView%3CKey%3E" class="section impl">

<a href="../../src/vstd/hash_set.rs.html#31-35"
class="src rightside">Source</a><a href="#impl-View-for-HashSetWithView%3CKey%3E" class="anchor">§</a>

### impl\<Key\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../hash_set/struct.HashSetWithView.html" class="struct"
title="struct vstd::hash_set::HashSetWithView">HashSetWithView</a>\<Key\>

<div class="where">

where Key: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-39" class="section associatedtype trait-impl">

<a href="../../src/vstd/hash_set.rs.html#32"
class="src rightside">Source</a><a href="#associatedtype.V-39" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../set/struct.Set.html" class="struct"
title="struct vstd::set::Set">Set</a>\<\<Key as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>\>

</div>

</div>

<div id="impl-View-for-HashMapWithView%3CKey,+Value%3E"
class="section impl">

<a href="../../src/vstd/hash_map.rs.html#30-34"
class="src rightside">Source</a><a href="#impl-View-for-HashMapWithView%3CKey,+Value%3E"
class="anchor">§</a>

### impl\<Key, Value\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../hash_map/struct.HashMapWithView.html" class="struct"
title="struct vstd::hash_map::HashMapWithView">HashMapWithView</a>\<Key, Value\>

<div class="where">

where Key: <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/cmp/trait.Eq.html"
class="trait" title="trait core::cmp::Eq">Eq</a> +
<a href="https://doc.rust-lang.org/1.92.0/core/hash/trait.Hash.html"
class="trait" title="trait core::hash::Hash">Hash</a>,

</div>

</div>

<div class="impl-items">

<div id="associatedtype.V-40" class="section associatedtype trait-impl">

<a href="../../src/vstd/hash_map.rs.html#31"
class="src rightside">Source</a><a href="#associatedtype.V-40" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../map/struct.Map.html" class="struct"
title="struct vstd::map::Map">Map</a>\<\<Key as <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a>\>::<a href="trait.View.html#associatedtype.V" class="associatedtype"
title="type vstd::view::View::V">V</a>, Value\>

</div>

</div>

<div id="impl-View-for-PointsTo%3CT%3E" class="section impl">

<a href="../../src/vstd/raw_ptr.rs.html#192-196"
class="src rightside">Source</a><a href="#impl-View-for-PointsTo%3CT%3E" class="anchor">§</a>

### impl\<T\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../raw_ptr/struct.PointsTo.html" class="struct"
title="struct vstd::raw_ptr::PointsTo">PointsTo</a>\<T\>

</div>

<div class="impl-items">

<div id="associatedtype.V-41" class="section associatedtype trait-impl">

<a href="../../src/vstd/raw_ptr.rs.html#193"
class="src rightside">Source</a><a href="#associatedtype.V-41" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../raw_ptr/struct.PointsToData.html" class="struct"
title="struct vstd::raw_ptr::PointsToData">PointsToData</a>\<T\>

</div>

</div>

<div id="impl-View-for-StringHashMap%3CValue%3E" class="section impl">

<a href="../../src/vstd/hash_map.rs.html#193-197"
class="src rightside">Source</a><a href="#impl-View-for-StringHashMap%3CValue%3E" class="anchor">§</a>

### impl\<Value\> <a href="trait.View.html" class="trait"
title="trait vstd::view::View">View</a> for <a href="../hash_map/struct.StringHashMap.html" class="struct"
title="struct vstd::hash_map::StringHashMap">StringHashMap</a>\<Value\>

</div>

<div class="impl-items">

<div id="associatedtype.V-42" class="section associatedtype trait-impl">

<a href="../../src/vstd/hash_map.rs.html#194"
class="src rightside">Source</a><a href="#associatedtype.V-42" class="anchor">§</a>

#### type <a href="#associatedtype.V" class="associatedtype">V</a> = <a href="../map/struct.Map.html" class="struct"
title="struct vstd::map::Map">Map</a>\<<a href="../seq/struct.Seq.html" class="struct"
title="struct vstd::seq::Seq">Seq</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>\>, Value\>

</div>

</div>

</div>

</div>

</div>
