<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[vstd](../index.html)::[string](index.html)

</div>

# Trait <span class="trait">StrSliceExecFns</span> Copy item path

<span class="sub-heading"><a href="../../src/vstd/string.rs.html#77-90" class="src">Source</a>
</span>

</div>

``` rust
pub trait StrSliceExecFns {
    // Required methods
    fn unicode_len(&self) -> usize;
    fn get_char(&self, i: usize) -> char;
    fn substring_ascii<'a>(&'a self, from: usize, to: usize) -> &'a str;
    fn substring_char<'a>(&'a self, from: usize, to: usize) -> &'a str;
    fn get_ascii(&self, i: usize) -> u8;
    fn as_bytes_vec(&self) -> Vec<u8> ⓘ;
}
```

## Required Methods<a href="#required-methods" class="anchor">§</a>

<div class="methods">

<div id="tymethod.unicode_len" class="section method">

<a href="../../src/vstd/string.rs.html#78"
class="src rightside">Source</a>

#### fn <a href="#tymethod.unicode_len" class="fn">unicode_len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div id="tymethod.get_char" class="section method">

<a href="../../src/vstd/string.rs.html#80"
class="src rightside">Source</a>

#### fn <a href="#tymethod.get_char" class="fn">get_char</a>(&self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div id="tymethod.substring_ascii" class="section method">

<a href="../../src/vstd/string.rs.html#82"
class="src rightside">Source</a>

#### fn <a href="#tymethod.substring_ascii" class="fn">substring_ascii</a>\<'a\>(&'a self, from: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, to: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div id="tymethod.substring_char" class="section method">

<a href="../../src/vstd/string.rs.html#84"
class="src rightside">Source</a>

#### fn <a href="#tymethod.substring_char" class="fn">substring_char</a>\<'a\>(&'a self, from: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, to: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div id="tymethod.get_ascii" class="section method">

<a href="../../src/vstd/string.rs.html#86"
class="src rightside">Source</a>

#### fn <a href="#tymethod.get_ascii" class="fn">get_ascii</a>(&self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div id="tymethod.as_bytes_vec" class="section method">

<a href="../../src/vstd/string.rs.html#89"
class="src rightside">Source</a>

#### fn <a href="#tymethod.as_bytes_vec" class="fn">as_bytes_vec</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>\> <a href="#" class="tooltip" data-notable-ty="Vec&lt;u8&gt;">ⓘ</a>

</div>

</div>

## Implementations on Foreign Types<a href="#foreign-impls" class="anchor">§</a>

<div id="impl-StrSliceExecFns-for-str" class="section impl">

<a href="../../src/vstd/string.rs.html#92-191"
class="src rightside">Source</a><a href="#impl-StrSliceExecFns-for-str" class="anchor">§</a>

### impl <a href="trait.StrSliceExecFns.html" class="trait"
title="trait vstd::string::StrSliceExecFns">StrSliceExecFns</a> for <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div class="impl-items">

<div id="method.unicode_len" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#98-103"
class="src rightside">Source</a><a href="#method.unicode_len" class="anchor">§</a>

#### fn <a href="#tymethod.unicode_len" class="fn">unicode_len</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>

</div>

<div class="docblock">

The len() function in rust returns the byte length. It is more useful to
talk about the length of characters and therefore this function was
added. Please note that this function counts the unicode variation
selectors as characters. Warning: O(n)

</div>

<div id="method.get_char" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#107-115"
class="src rightside">Source</a><a href="#method.get_char" class="anchor">§</a>

#### fn <a href="#tymethod.get_char" class="fn">get_char</a>(&self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>

</div>

<div class="docblock">

Warning: O(n) not O(1) due to unicode decoding needed

</div>

<div id="method.substring_ascii" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#118-128"
class="src rightside">Source</a><a href="#method.substring_ascii" class="anchor">§</a>

#### fn <a href="#tymethod.substring_ascii" class="fn">substring_ascii</a>\<'a\>(&'a self, from: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, to: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div id="method.substring_char" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#131-162"
class="src rightside">Source</a><a href="#method.substring_char" class="anchor">§</a>

#### fn <a href="#tymethod.substring_char" class="fn">substring_char</a>\<'a\>(&'a self, from: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>, to: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> &'a <a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>

</div>

<div id="method.get_ascii" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#165-172"
class="src rightside">Source</a><a href="#method.get_ascii" class="anchor">§</a>

#### fn <a href="#tymethod.get_ascii" class="fn">get_ascii</a>(&self, i: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>

</div>

<div id="method.as_bytes_vec" class="section method trait-impl">

<a href="../../src/vstd/string.rs.html#179-190"
class="src rightside">Source</a><a href="#method.as_bytes_vec" class="anchor">§</a>

#### fn <a href="#tymethod.as_bytes_vec" class="fn">as_bytes_vec</a>(&self) -\> <a href="https://doc.rust-lang.org/1.92.0/alloc/vec/struct.Vec.html"
class="struct" title="struct alloc::vec::Vec">Vec</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>\> <a href="#" class="tooltip" data-notable-ty="Vec&lt;u8&gt;">ⓘ</a>

</div>

</div>

## Implementors<a href="#implementors" class="anchor">§</a>

<div id="implementors-list">

</div>

</div>

</div>
