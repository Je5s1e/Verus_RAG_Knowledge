<div class="width-limiter">

<div id="main-content" class="section content">

<div class="main-heading">

<div class="rustdoc-breadcrumbs">

[proc_macro2](index.html)

</div>

# Struct <span class="struct">Literal</span> Copy item path

<span class="sub-heading"><a href="../src/proc_macro2/lib.rs.html#1102-1105"
class="src">Source</a> </span>

</div>

``` rust
pub struct Literal { /* private fields */ }
```

Expand description

<div class="docblock">

A literal string (`"hello"`), byte string (`b"hello"`), character
(`'a'`), byte character (`b'a'`), an integer or floating point number
with or without a suffix (`1`, `1u8`, `2.3`, `2.3f32`).

Boolean literals like `true` and `false` do not belong here, they are
`Ident`s.

</div>

## Implementations<a href="#implementations" class="anchor">§</a>

<div id="implementations-list">

<div id="impl-Literal" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1147-1424"
class="src rightside">Source</a><a href="#impl-Literal" class="anchor">§</a>

### impl <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.u8_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.u8_suffixed" class="fn">u8_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u16_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.u16_suffixed" class="fn">u16_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u32_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.u32_suffixed" class="fn">u32_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u64_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.u64_suffixed" class="fn">u64_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u128_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.u128_suffixed" class="fn">u128_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.usize_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.usize_suffixed" class="fn">usize_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i8_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.i8_suffixed" class="fn">i8_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i16_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.i16_suffixed" class="fn">i16_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i32_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.i32_suffixed" class="fn">i32_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i64_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.i64_suffixed" class="fn">i64_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i128_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.i128_suffixed" class="fn">i128_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.isize_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1162-1175"
class="src rightside">Source</a>

#### pub fn <a href="#method.isize_suffixed" class="fn">isize_suffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed integer literal with the specified value.

This function will create an integer like `1u32` where the integer value
specified is the first part of the token and the integral is also
suffixed at the end. Literals created from negative numbers may not
survive roundtrips through `TokenStream` or strings and may be broken
into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u8_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.u8_unsuffixed" class="fn">u8_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u16_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.u16_unsuffixed" class="fn">u16_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u16.html"
class="primitive">u16</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u32_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.u32_unsuffixed" class="fn">u32_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u32.html"
class="primitive">u32</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u64_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.u64_unsuffixed" class="fn">u64_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u64.html"
class="primitive">u64</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.u128_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.u128_unsuffixed" class="fn">u128_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u128.html"
class="primitive">u128</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.usize_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.usize_unsuffixed" class="fn">usize_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i8_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.i8_unsuffixed" class="fn">i8_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i8.html"
class="primitive">i8</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i16_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.i16_unsuffixed" class="fn">i16_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i16.html"
class="primitive">i16</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i32_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.i32_unsuffixed" class="fn">i32_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i32.html"
class="primitive">i32</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i64_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.i64_unsuffixed" class="fn">i64_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i64.html"
class="primitive">i64</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.i128_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.i128_unsuffixed" class="fn">i128_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.i128.html"
class="primitive">i128</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.isize_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1177-1190"
class="src rightside">Source</a>

#### pub fn <a href="#method.isize_unsuffixed" class="fn">isize_unsuffixed</a>(n: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.isize.html"
class="primitive">isize</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed integer literal with the specified value.

This function will create an integer like `1` where the integer value
specified is the first part of the token. No suffix is specified on this
token, meaning that invocations like `Literal::i8_unsuffixed(1)` are
equivalent to `Literal::u32_unsuffixed(1)`. Literals created from
negative numbers may not survive roundtrips through `TokenStream` or
strings and may be broken into two tokens (`-` and positive literal).

Literals created through this method have the `Span::call_site()` span
by default, which can be configured with the `set_span` method below.

</div>

<div id="method.f64_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1205-1208"
class="src rightside">Source</a>

#### pub fn <a href="#method.f64_unsuffixed" class="fn">f64_unsuffixed</a>(f: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f64.html"
class="primitive">f64</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed floating-point literal.

This constructor is similar to those like `Literal::i8_unsuffixed` where
the float’s value is emitted directly into the token but no suffix is
used, so it may be inferred to be a `f64` later in the compiler.
Literals created from negative numbers may not survive round-trips
through `TokenStream` or strings and may be broken into two tokens (`-`
and positive literal).

##### <a href="#panics" class="doc-anchor">§</a>Panics

This function requires that the specified float is finite, for example
if it is infinity or NaN this function will panic.

</div>

<div id="method.f64_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1223-1226"
class="src rightside">Source</a>

#### pub fn <a href="#method.f64_suffixed" class="fn">f64_suffixed</a>(f: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f64.html"
class="primitive">f64</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed floating-point literal.

This constructor will create a literal like `1.0f64` where the value
specified is the preceding part of the token and `f64` is the suffix of
the token. This token will always be inferred to be an `f64` in the
compiler. Literals created from negative numbers may not survive
round-trips through `TokenStream` or strings and may be broken into two
tokens (`-` and positive literal).

##### <a href="#panics-1" class="doc-anchor">§</a>Panics

This function requires that the specified float is finite, for example
if it is infinity or NaN this function will panic.

</div>

<div id="method.f32_unsuffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1241-1244"
class="src rightside">Source</a>

#### pub fn <a href="#method.f32_unsuffixed" class="fn">f32_unsuffixed</a>(f: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f32.html"
class="primitive">f32</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new unsuffixed floating-point literal.

This constructor is similar to those like `Literal::i8_unsuffixed` where
the float’s value is emitted directly into the token but no suffix is
used, so it may be inferred to be a `f64` later in the compiler.
Literals created from negative numbers may not survive round-trips
through `TokenStream` or strings and may be broken into two tokens (`-`
and positive literal).

##### <a href="#panics-2" class="doc-anchor">§</a>Panics

This function requires that the specified float is finite, for example
if it is infinity or NaN this function will panic.

</div>

<div id="method.f32_suffixed" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1259-1262"
class="src rightside">Source</a>

#### pub fn <a href="#method.f32_suffixed" class="fn">f32_suffixed</a>(f: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.f32.html"
class="primitive">f32</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Creates a new suffixed floating-point literal.

This constructor will create a literal like `1.0f32` where the value
specified is the preceding part of the token and `f32` is the suffix of
the token. This token will always be inferred to be an `f32` in the
compiler. Literals created from negative numbers may not survive
round-trips through `TokenStream` or strings and may be broken into two
tokens (`-` and positive literal).

##### <a href="#panics-3" class="doc-anchor">§</a>Panics

This function requires that the specified float is finite, for example
if it is infinity or NaN this function will panic.

</div>

<div id="method.string" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1265-1267"
class="src rightside">Source</a>

#### pub fn <a href="#method.string" class="fn">string</a>(string: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

String literal.

</div>

<div id="method.character" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1270-1272"
class="src rightside">Source</a>

#### pub fn <a href="#method.character" class="fn">character</a>(ch: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.char.html"
class="primitive">char</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Character literal.

</div>

<div id="method.byte_character" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1275-1277"
class="src rightside">Source</a>

#### pub fn <a href="#method.byte_character" class="fn">byte_character</a>(byte: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Byte character literal.

</div>

<div id="method.byte_string" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1280-1282"
class="src rightside">Source</a>

#### pub fn <a href="#method.byte_string" class="fn">byte_string</a>(bytes: &\[<a href="https://doc.rust-lang.org/1.92.0/std/primitive.u8.html"
class="primitive">u8</a>\]) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

Byte string literal.

</div>

<div id="method.c_string" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1285-1287"
class="src rightside">Source</a>

#### pub fn <a href="#method.c_string" class="fn">c_string</a>(string: &<a
href="https://doc.rust-lang.org/1.92.0/core/ffi/c_str/struct.CStr.html"
class="struct" title="struct core::ffi::c_str::CStr">CStr</a>) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="docblock">

C string literal.

</div>

<div id="method.span" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1290-1292"
class="src rightside">Source</a>

#### pub fn <a href="#method.span" class="fn">span</a>(&self) -\> <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>

</div>

<div class="docblock">

Returns the span encompassing this literal.

</div>

<div id="method.set_span" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1295-1297"
class="src rightside">Source</a>

#### pub fn <a href="#method.set_span" class="fn">set_span</a>(&mut self, span: <a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>)

</div>

<div class="docblock">

Configures the span associated for this literal.

</div>

<div id="method.subspan" class="section method">

<a href="../src/proc_macro2/lib.rs.html#1306-1308"
class="src rightside">Source</a>

#### pub fn <a href="#method.subspan" class="fn">subspan</a>\<R: <a
href="https://doc.rust-lang.org/1.92.0/core/ops/range/trait.RangeBounds.html"
class="trait"
title="trait core::ops::range::RangeBounds">RangeBounds</a>\<<a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>\>\>(&self, range: R) -\> <a href="https://doc.rust-lang.org/1.92.0/core/option/enum.Option.html"
class="enum" title="enum core::option::Option">Option</a>\<<a href="struct.Span.html" class="struct"
title="struct proc_macro2::Span">Span</a>\>

</div>

<div class="docblock">

Returns a `Span` that is a subset of `self.span()` containing only the
source bytes in range `range`. Returns `None` if the would-be trimmed
span is outside the bounds of `self`.

Warning: the underlying
[`proc_macro::Literal::subspan`](https://doc.rust-lang.org/1.92.0/proc_macro/struct.Literal.html#method.subspan "method proc_macro::Literal::subspan")
method is nightly-only. When called from within a procedural macro not
using a nightly compiler, this method will always return `None`.

</div>

</div>

</div>

## Trait Implementations<a href="#trait-implementations" class="anchor">§</a>

<div id="trait-implementations-list">

<div id="impl-Clone-for-Literal" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1101"
class="src rightside">Source</a><a href="#impl-Clone-for-Literal" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html"
class="trait" title="trait core::clone::Clone">Clone</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.clone" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1101"
class="src rightside">Source</a><a href="#method.clone" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/clone/trait.Clone.html#tymethod.clone"
class="fn">clone</a>(&self) -\> <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

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

<div id="impl-Debug-for-Literal" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1440-1444"
class="src rightside">Source</a><a href="#impl-Debug-for-Literal" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html"
class="trait" title="trait core::fmt::Debug">Debug</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.fmt" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1441-1443"
class="src rightside">Source</a><a href="#method.fmt" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Debug.html#tymethod.fmt)

</div>

</div>

<div id="impl-Display-for-Literal" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1446-1450"
class="src rightside">Source</a><a href="#impl-Display-for-Literal" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="method.fmt-1" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1447-1449"
class="src rightside">Source</a><a href="#method.fmt-1" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt"
class="fn">fmt</a>(&self, f: &mut <a
href="https://doc.rust-lang.org/1.92.0/core/fmt/struct.Formatter.html"
class="struct" title="struct core::fmt::Formatter">Formatter</a>\<'\_\>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/fmt/type.Result.html"
class="type" title="type core::fmt::Result">Result</a>

</div>

<div class="docblock">

Formats the value using the given formatter. [Read
more](https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html#tymethod.fmt)

</div>

</div>

<div id="impl-Extend%3CLiteral%3E-for-TokenStream" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#331-336"
class="src rightside">Source</a><a href="#impl-Extend%3CLiteral%3E-for-TokenStream" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html"
class="trait"
title="trait core::iter::traits::collect::Extend">Extend</a>\<<a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>\> for <a href="struct.TokenStream.html" class="struct"
title="struct proc_macro2::TokenStream">TokenStream</a>

</div>

<div class="impl-items">

<div id="method.extend" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#332-335"
class="src rightside">Source</a><a href="#method.extend" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend"
class="fn">extend</a>\<I: <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.IntoIterator.html"
class="trait"
title="trait core::iter::traits::collect::IntoIterator">IntoIterator</a>\<Item = <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>\>\>(&mut self, tokens: I)

</div>

<div class="docblock">

Extends a collection with the contents of an iterator. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#tymethod.extend)

</div>

<div id="method.extend_one" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#417"
class="src rightside">Source</a><a href="#method.extend_one" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_one"
class="fn">extend_one</a>(&mut self, item: A)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Extends a collection with exactly one element.

</div>

<div id="method.extend_reserve" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/iter/traits/collect.rs.html#425"
class="src rightside">Source</a><a href="#method.extend_reserve" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve"
class="fn">extend_reserve</a>(&mut self, additional: <a href="https://doc.rust-lang.org/1.92.0/std/primitive.usize.html"
class="primitive">usize</a>)

</div>

<span class="item-info"></span>

<div class="stab unstable">

🔬This is a nightly-only experimental API. (`extend_one`)

</div>

<div class="docblock">

Reserves capacity in a collection for the given number of additional
elements. [Read
more](https://doc.rust-lang.org/1.92.0/core/iter/traits/collect/trait.Extend.html#method.extend_reserve)

</div>

</div>

<div id="impl-From%3CLiteral%3E-for-TokenTree" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#634-638"
class="src rightside">Source</a><a href="#impl-From%3CLiteral%3E-for-TokenTree" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html"
class="trait" title="trait core::convert::From">From</a>\<<a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>\> for <a href="enum.TokenTree.html" class="enum"
title="enum proc_macro2::TokenTree">TokenTree</a>

</div>

<div class="impl-items">

<div id="method.from" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#635-637"
class="src rightside">Source</a><a href="#method.from" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/convert/trait.From.html#tymethod.from"
class="fn">from</a>(g: <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>) -\> Self

</div>

<div class="docblock">

Converts to this type from the input type.

</div>

</div>

<div id="impl-FromStr-for-Literal" class="section impl">

<a href="../src/proc_macro2/lib.rs.html#1426-1438"
class="src rightside">Source</a><a href="#impl-FromStr-for-Literal" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/str/traits/trait.FromStr.html"
class="trait" title="trait core::str::traits::FromStr">FromStr</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div class="impl-items">

<div id="associatedtype.Err" class="section associatedtype trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1427"
class="src rightside">Source</a><a href="#associatedtype.Err" class="anchor">§</a>

#### type <a
href="https://doc.rust-lang.org/1.92.0/core/str/traits/trait.FromStr.html#associatedtype.Err"
class="associatedtype">Err</a> = <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>

</div>

<div class="docblock">

The associated error which can be returned from parsing.

</div>

<div id="method.from_str" class="section method trait-impl">

<a href="../src/proc_macro2/lib.rs.html#1429-1437"
class="src rightside">Source</a><a href="#method.from_str" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/core/str/traits/trait.FromStr.html#tymethod.from_str"
class="fn">from_str</a>(repr: &<a href="https://doc.rust-lang.org/1.92.0/std/primitive.str.html"
class="primitive">str</a>) -\> <a href="https://doc.rust-lang.org/1.92.0/core/result/enum.Result.html"
class="enum" title="enum core::result::Result">Result</a>\<Self, <a href="struct.LexError.html" class="struct"
title="struct proc_macro2::LexError">LexError</a>\>

</div>

<div class="docblock">

Parses a string `s` to return a value of this type. [Read
more](https://doc.rust-lang.org/1.92.0/core/str/traits/trait.FromStr.html#tymethod.from_str)

</div>

</div>

</div>

## Auto Trait Implementations<a href="#synthetic-implementations" class="anchor">§</a>

<div id="synthetic-implementations-list">

<div id="impl-Freeze-for-Literal" class="section impl">

<a href="#impl-Freeze-for-Literal" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Freeze.html"
class="trait" title="trait core::marker::Freeze">Freeze</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div id="impl-RefUnwindSafe-for-Literal" class="section impl">

<a href="#impl-RefUnwindSafe-for-Literal" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.RefUnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::RefUnwindSafe">RefUnwindSafe</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div id="impl-Send-for-Literal" class="section impl">

<a href="#impl-Send-for-Literal" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Send.html"
class="trait" title="trait core::marker::Send">Send</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div id="impl-Sync-for-Literal" class="section impl">

<a href="#impl-Sync-for-Literal" class="anchor">§</a>

### impl \!<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sync.html"
class="trait" title="trait core::marker::Sync">Sync</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div id="impl-Unpin-for-Literal" class="section impl">

<a href="#impl-Unpin-for-Literal" class="anchor">§</a>

### impl <a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Unpin.html"
class="trait" title="trait core::marker::Unpin">Unpin</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

</div>

<div id="impl-UnwindSafe-for-Literal" class="section impl">

<a href="#impl-UnwindSafe-for-Literal" class="anchor">§</a>

### impl <a
href="https://doc.rust-lang.org/1.92.0/core/panic/unwind_safe/trait.UnwindSafe.html"
class="trait"
title="trait core::panic::unwind_safe::UnwindSafe">UnwindSafe</a> for <a href="struct.Literal.html" class="struct"
title="struct proc_macro2::Literal">Literal</a>

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

<div id="method.from-1" class="section method trait-impl">

<a
href="https://doc.rust-lang.org/1.92.0/src/core/convert/mod.rs.html#788"
class="src rightside">Source</a><a href="#method.from-1" class="anchor">§</a>

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

<div id="impl-ToString-for-T" class="section impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/string.rs.html#2866"
class="src rightside">Source</a><a href="#impl-ToString-for-T" class="anchor">§</a>

### impl\<T\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html"
class="trait" title="trait alloc::string::ToString">ToString</a> for T

<div class="where">

where T:
<a href="https://doc.rust-lang.org/1.92.0/core/fmt/trait.Display.html"
class="trait" title="trait core::fmt::Display">Display</a> +
?<a href="https://doc.rust-lang.org/1.92.0/core/marker/trait.Sized.html"
class="trait" title="trait core::marker::Sized">Sized</a>,

</div>

</div>

<div class="impl-items">

<div id="method.to_string" class="section method trait-impl">

<a href="https://doc.rust-lang.org/1.92.0/src/alloc/string.rs.html#2868"
class="src rightside">Source</a><a href="#method.to_string" class="anchor">§</a>

#### fn <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html#tymethod.to_string"
class="fn">to_string</a>(&self) -\> <a
href="https://doc.rust-lang.org/1.92.0/alloc/string/struct.String.html"
class="struct" title="struct alloc::string::String">String</a>

</div>

<div class="docblock">

Converts the given value to a `String`. [Read
more](https://doc.rust-lang.org/1.92.0/alloc/string/trait.ToString.html#tymethod.to_string)

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

</div>

</div>

</div>
